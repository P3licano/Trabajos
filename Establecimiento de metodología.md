

## Fase 1 -Planificación previa

Se planificará el reparto de tareas en caso de estar en grupo, en caso de no ser así se planificará un horario que se debería seguir en función a los requerimientos y cómo se avance en un futuro. **TODA** información recabada o que se vaya realizando durante el avance de los días deberá de estar reflejada en un documento ya sea en ***Obsidian, CherryTree, Word***..., en el que se explique de manera clara y concisa, qué se ha hecho y en caso de ser necesario por qué se ha hecho, adjuntando capturas tanto de lo realizado como del resultado, o en su defecto una breve explicación de lo que se ha realizado

## Fase 2 -Reconocimiento

La fase de reconocimiento será o debería de ser de la más duraderas (en función de los resultados)

- Probaremos el uso de ***OSINT** en busca de algún archivo, credenciales, cualquier tipo de  datos de importancia que no estén bien tratados y sean accesibles de forma pública y que no deberían serlo. Recabaremos esta información mediante:

	- ***Google Dorking*** (esto sobretodo)
	- *Reversing* de imágenes
	- ***Maltego***
	- ***TheHarvester***
	- ***Recon-ng***

- A continuación se realizará un mapeo de la infraestructura, se hará uso de las herramientas:

	- ***Nikto***
	- ***Nmap***

- Una vez tengamos un "mapa" de lo que sería la infraestructura:

	- listaremos subdominios (***sublist3r, Subfinder**)
	- listaremos contenido web (***dirbuster, feroxbuster***)
	- Enumeraremos CMS si es que tiene (***wpscan para wordpress, droopscan para drupal...***)


## FASE 3 — Análisis de vulnerabilidades

**Objetivo:** encontrar vulnerabilidades y aprovecharlas como configuraciones inseguras o versiones obsoletas. Usaremos herramientas como:

- ***Nessus, OpenVAS, Nmap*** (Escáneres de red y host)

- Para la parte Web: ***Burp Suite, OWASP ZAP, Nikto***
## Fase 4 -Explotación


El objetivo de esta fase es explotar las vulnerabilidades encontradas previamente:

- Versiones obsoletas de las que poder aprovecharse (en ***nmap*** debería de salir la versión de lo que corre en cada puerto)
- Buscar vulnerabilidades en B.B.D.D. (***sqlmap*** nos lo automatiza)
- Usar CVEs para explotar vulnerabilidades (***Metaesploit***)
- Modificar cabeceras con ***BurpSuite***
- Si necesitamos hacer *cracking* a un login *SSH* por ejemplo (***Hydra***)
- Escalada de privilegios (abusando de binarios en **gtfobins.com**, o automatizándolo con ***linpeas*** o ***winpeas***)



## Fase 4 -Post Explotación

En esta fase lo que buscamos es persistencia una vez hayamos logrado tener acceso a la máquina

- ***Metasploit/Meterpreter***
- ***Cobalt Strike***
- ***CrackMapExec para ejecución remota***


## Fase 5 -Reporte

Ésta fase es la que más peso tiene, ya que será para el cliente y habrá que hacerle ver cómo hemos realizado el *pentest* y por qué de forma clara y no muy técnica. Otro documento será más técnico y más largo que será para el equipo técnico que se encargarán de corregir los errores reportados. Para ello podemos usar ***LaTex*** o cualquier herramienta que haga ***Markdown***
