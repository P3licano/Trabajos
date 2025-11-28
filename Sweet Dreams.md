
Una vez realizado el `netdiscover`, hacemos un ping a la máquina para ver si tenemos conectividad

![[Pasted image 20251125175218.png]]

Una vez comprobamos la conectividad, hacemos un escaneo de puertos con `nmap`

```ruby
nmap -sCV -p- --open -Pn -n IP -On nresultado.txt
```

![[Pasted image 20251125175234.png]]


Añadimos la máquina en `etc/hosts`

![[Pasted image 20251125175312.png]]

Vemos la página http

![[Pasted image 20251125175338.png]]


Buscamos qué tecnologías usa la página con ***Wappalyzer***

![[Pasted image 20251125175418.png]]



Hacemos una enumeración de usuarios con ***WPScan***

```ruby
wpscan --url http://IP --enumerate u
```

![[Pasted image 20251125175536.png]]

Encontramos un usuario válido

![[Pasted image 20251125175615.png]]


Hemos encontrado un directorio de `wp-admin`

```ruby
feroxbuster --url http://IP
```

![[Pasted image 20251128174524.png]]

Hacemos un cewl a la página y con el diccionario que nos crea hacemos fuerza bruta en la página de inicio de sesión de wordpress

```ruby
cewl http://IP/
```

![[Pasted image 20251128175105.png]]

Se intenta hacer fuerza bruta pero no se logra hacer nada

```ruby
wpscan --url http://IP_maquina -U usuario -P diccionario
```

![[Pasted image 20251128175230.png]]

La página por defecto no se encuentra nada interesante por lo que procedemos a hacer un escaneo de subdominios

```ruby
ffuf -u http://ip_maquina/ -H "Host: FUZZ.IP_maquina" -w diccionario -fc cód_respuesta
```


![[Pasted image 20251128182707.png]]

Añadimos el subdominio a `/etc/hosts`

![[Pasted image 20251128180624.png]]


Al acceder al subdominio tenemos acceso denegado

![[Pasted image 20251128182959.png]]


Necesitamos bypassear el error 403, haciendo una búsqueda en google vemos que unos de los bypasses consisten en modificar la cabecera añadiendo `X-Host: 127.0.0.1`

![[Pasted image 20251128184951.png]]


Hacemos una reverse shell básica

![[Pasted image 20251128185851.png]]


La subimos pero nos da otra vez el error 403. Abrimos burpsuite y capturamos la subida del archivo, cambiando el `content-type` de `application/x-php` a `image/gif` y añadiendo de nuevo el `X-host: 127.0.0.1`

![[Pasted image 20251128193428.png]]

nos ponemos a la escucha en el puerto 4444

```bash
nc -nlvp 4444
```


![[Pasted image 20251128193623.png]]


Vamos al directorio donde se ha guardado la shell y la *clickamos* para ejecutar nuestra shell

![[Pasted image 20251128201906.png]]

Una vez hayamos ejecutado la shell veremos que el `nc` que hicimos previamente nos devuelve una shell en la que podemos ejecutar comandos

![[Pasted image 20251128202035.png]]