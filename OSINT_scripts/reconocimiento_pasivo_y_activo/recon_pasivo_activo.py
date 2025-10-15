#!/usr/bin/env python3
# interactive_recon.py

import requests
import whois
import json
import time
import re
from urllib.parse import quote_plus
from datetime import datetime

USER_AGENT = "InteractiveRecon/1.0 (+educational)"
SECURITY_HEADERS = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "Strict-Transport-Security",
    "X-Content-Type-Options",
    "Referrer-Policy",
    "Permissions-Policy",
    "Expect-CT",
    "Feature-Policy"
]

# Try import Wappalyzer (optional)
try:
    from Wappalyzer import Wappalyzer, WebPage
    have_wappalyzer = True
except Exception:
    have_wappalyzer = False

def normalize_target(t):
    t = t.strip()
    if not t:
        return None
    if t.startswith("http://") or t.startswith("https://"):
        domain = t.split("://",1)[1].split("/")[0]
        return {"input": t, "domain": domain, "url_root": t.rstrip("/")}
    else:
        domain = t.split("/")[0]
        return {"input": t, "domain": domain, "url_root": "http://" + domain}

def whois_lookup(domain):
    try:
        return whois.whois(domain)
    except Exception as e:
        return {"error": str(e)}

def crtsh_lookup(domain):
    url = f"https://crt.sh/?q=%25.{quote_plus(domain)}&output=json"
    try:
        r = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=20)
        if r.status_code == 200:
            # sometimes crt.sh returns invalid JSON for empty results -> handle
            try:
                return r.json()
            except ValueError:
                return {"raw": r.text}
        return {"http_status": r.status_code}
    except Exception as e:
        return {"error": str(e)}

def wayback_cdx(domain, limit=50):
    url = "http://web.archive.org/cdx/search/cdx"
    params = {"url": f"*.{domain}/*", "output": "json", "limit": limit}
    try:
        r = requests.get(url, params=params, headers={"User-Agent": USER_AGENT}, timeout=20)
        if r.status_code == 200:
            try:
                return r.json()
            except ValueError:
                return {"raw": r.text}
        return {"http_status": r.status_code}
    except Exception as e:
        return {"error": str(e)}

def google_dork_suggestions(domain):
    return [
        f"site:{domain} intitle:index.of",
        f"site:{domain} inurl:admin",
        f"site:{domain} filetype:env",
        f"site:{domain} \"password\" OR \"passwd\"",
        f"site:{domain} \"login\"",
        f"site:{domain} \"sensitive\""
    ]

def active_http_probe(url):
    try:
        r = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=20, allow_redirects=True)
        title = None
        if r.text:
            m = re.search(r"<title[^>]*>(.*?)</title>", r.text, re.I|re.S)
            if m:
                title = m.group(1).strip()
        return {"status_code": r.status_code, "final_url": r.url, "title": title, "headers": dict(r.headers)}
    except Exception as e:
        return {"error": str(e)}

def extract_security_headers(headers):
    sec = {}
    for h in SECURITY_HEADERS:
        if h in headers:
            sec[h] = headers.get(h)
    return sec

def wappalyzer_detect(url):
    if not have_wappalyzer:
        return {"skipped": "python-Wappalyzer not installed"}
    try:
        w = Wappalyzer.latest()
        wp = WebPage.new_from_url(url)
        return w.analyze_with_categories(wp)
    except Exception as e:
        return {"error": str(e)}

def save_json(results, domain):
    safe = domain.replace(".", "_")
    fname = f"recon_{safe}_{datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}.json"
    with open(fname, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, default=str, ensure_ascii=False)
    return fname

def main():
    print("=== Interactive Recon (OSINT) ===")
    target = input("Introduce dominio o URL objetivo (ej: example.com ó https://example.com): ").strip()
    if not target:
        print("No se introdujo objetivo. Saliendo.")
        return

    tinfo = normalize_target(target)
    if not tinfo:
        print("Objetivo inválido.")
        return

    domain = tinfo["domain"]
    url_root = tinfo["url_root"]
    print(f"\nObjetivo detectado: dominio = {domain}, url base = {url_root}\n")

    proceed = input("¿Quieres ejecutar el OSINT completo contra este objetivo? (s/N): ").strip().lower()
    if proceed not in ("s","si","y","yes"):
        print("Operación cancelada por el usuario.")
        return

    results = {}
    results["meta"] = {"input": target, "domain": domain, "url_root": url_root, "timestamp_utc": datetime.utcnow().isoformat()+"Z"}

    print("\n[1/6] WHOIS...")
    results["whois"] = whois_lookup(domain)
    time.sleep(1)

    print("[2/6] crt.sh (certificados)...")
    results["crtsh"] = crtsh_lookup(domain)
    time.sleep(1)

    print("[3/6] Wayback (CDX) ...")
    results["wayback"] = wayback_cdx(domain, limit=50)
    time.sleep(1)

    print("[4/6] Google Dork suggestions (no automatizadas)...")
    results["google_dorks"] = google_dork_suggestions(domain)

    print("[5/6] Probe HTTP (cabeceras y título)...")
    probe = active_http_probe(url_root)
    results["http_probe"] = probe
    if isinstance(probe, dict) and "headers" in probe:
        results["security_headers"] = extract_security_headers(probe["headers"])
    else:
        results["security_headers"] = {}

    print("[6/6] Wappalyzer detection (opcional)...")
    if have_wappalyzer:
        results["wappalyzer"] = wappalyzer_detect(url_root)
    else:
        results["wappalyzer"] = {"skipped": "python-Wappalyzer no instalado (pip install python-Wappalyzer)"}

    # Guardar
    fname = save_json(results, domain)
    print(f"\nRecon completado. Resultados guardados en: {fname}")
    print("Resumen rápido:")
    print(f" - WHOIS: {'error' if isinstance(results['whois'], dict) and 'error' in results['whois'] else 'ok'}")
    print(f" - crt.sh: {'ok' if results.get('crtsh') else 'no data'}")
    hprobe = results.get("http_probe", {})
    if isinstance(hprobe, dict) and "status_code" in hprobe:
        print(f" - HTTP probe status: {hprobe.get('status_code')}  final_url: {hprobe.get('final_url')}")
        if results["security_headers"]:
            print(f" - Cabeceras de seguridad encontradas: {', '.join(results['security_headers'].keys())}")
        else:
            print(" - No se encontraron cabeceras de seguridad comunes.")
    else:
        print(" - HTTP probe falló o no disponible.")

    print("\nTen en cuenta: evita automatizar búsquedas masivas contra Google y respeta TOS y la ley.")
    print("Fin.")

if __name__ == "__main__":
    main()
