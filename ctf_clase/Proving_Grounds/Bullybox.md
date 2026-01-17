
Realizamos un nmap para ver los puertos abiertos y ver qué están corriendo

```bash
nmap -sCV -p- --open -n -Pn -vvv IP_víctima -oN nom_resultado.txt
```

Encontramos 2 puertos abiertos:
### 22 SSH
### 80 HTTP

![](../../Imágenes/Pasted%20image%2020260113033230.png)


Entramos a la página web y encontramos un "box billing" 

![](../../Imágenes/Pasted%20image%2020260113030526.png)


Encontramos un panel de login en el que intentamos unas credenciales por defecto sin éxito

![](../../Imágenes/Pasted%20image%2020260113030713.png)


probamos a crearnos una cuenta

![](../../Imágenes/Pasted%20image%2020260113030759.png)


Encontramos que en el panel de reset de la contraseña podemos validar usuarios

![](../../Imágenes/Pasted%20image%2020260113032840.png)


Buscamos algún tipo de exploit

```bash
searchsploit servicio
```

![](../../Imágenes/Pasted%20image%2020260113035722.png)


Miramos el código del exploit y vemos que necesitamos de estar autenticados como administrador

![](../../Imágenes/Pasted%20image%2020260113035735.png)


Realizamos *fuzzing* de directorios pero no encontramos nada interesante

```bash
feroxbuster --url http://$IP_victima -w ruta_diccionario
```

![](../../Imágenes/Pasted%20image%2020260113034749.png)

```bash
gobuster dir -u http://$IP_victima -w ruta_diccionario
```

![](../../Imágenes/Pasted%20image%2020260113034809.png)

no encontramos nada

Al estar sin poder hacer nada se vuelve a mirar todo de nuevo, y se encuentra un *.git* que nos reporta nuestro *nmap* decidimos *dumpearlo* con la siguiente herramienta -->https://github.com/arthaud/git-dumper

```bash
pipx intall git-dumper
```


Una vez instalado vemos cómo podemos usar dicha herramienta

```bash
git-dumper -h
```

![](../../Imágenes/Pasted%20image%2020260113035535.png)


Sabiendo cómo utilizar la herramienta, procedemos a *dumpear* el *.git*

```bash
git-dumper http://$IP/.git/ nresultado
```

![](../../Imágenes/Pasted%20image%2020260113035517.png)


Una vez haya finalizado la herramienta, se miró que resultados nos había dado

![](../../Imágenes/Pasted%20image%2020260113035843.png)


accedimos primero al archivo "bb-config.php" en el que encontramos una url y un administrador con contraseña

![](../../Imágenes/Pasted%20image%2020260113035903.png)


Si miramos el *log* del *git* encontramos un email que muy probablemente sea el usuario de administrador

```bash
git log
```

![](../../Imágenes/Pasted%20image%2020260113042238.png)


Nos dirigimos a la url --> /bullybox.local/bb-admin que nos había reportado el fichero anterior e introdujimos las credenciales que habíamos logrado adquirir

admin@bullybox.local:Playing-Unstylish7-Provided

![](../../Imágenes/Pasted%20image%2020260113040509.png)


Ya dentro del panel de administrador de "box billing" continuamos con las instrucciones del exploit

![](../../Imágenes/Pasted%20image%2020260113042902.png)


1º Introdujimos un producto con el usuario que habíamos creado previamente

![](../../Imágenes/Pasted%20image%2020260113042848.png)


2º Se probó que el POC del exploit nos funcionaba accediendo en el panel de administrador

![](../../Imágenes/Pasted%20image%2020260113044547.png)


Funciona

![](../../Imágenes/Pasted%20image%2020260113044555.png)


Accedemos al directorio donde podemos ejecutar la shell una vez subida

![](../../Imágenes/Pasted%20image%2020260113045005.png)


Modificamos el POC de antes cambiando el contenido de "data" poniendo una shell en la que podremos ejecutar comandos

![](../../Imágenes/Pasted%20image%2020260113050043.png)


Comprobamos que funciona

![](../../Imágenes/Pasted%20image%2020260113050048.png)


Logramos ver que tenemos ejecución de comandos

![](../../Imágenes/Pasted%20image%2020260113050058.png)


Nos mandamos una reverse shell para trabajar más cómodamente

![](../../Imágenes/Pasted%20image%2020260113050204.png)


![](../../Imágenes/Pasted%20image%2020260113050215.png)


