

Editamos el archivo hosts con la IP de la máquina

![](../../Imágenes/Pasted%20image%2020251215172739.png)




Hacemos un nmap a la máquina en la que encontramos dos puertos abiertos, 22 y 80 (ssh y http respectivamente)

```bash
nmap -sCV -p- --open -n -Pn -vvv IP_víctima -oN nom_resultado.txt
```

![](../../Imágenes/Pasted%20image%2020251215172834.png)


Al no tener un inicio de sesión anónima por ssh, procedemos a visitar la página web

![](../../Imágenes/Pasted%20image%2020251215173044.png)


Al encontrarnos con la página por defecto de Apache, procedemos a la enumeración de directorios

```bash
feroxbuster --url http://IP_víctima -w /ruta_diccionario
```

![](../../Imágenes/Pasted%20image%2020251215173242.png)


```bash
gobuster dir -u http://IP_víctima -w /ruta_diccionario
```

![](../../Imágenes/Pasted%20image%2020251215173454.png)


Se intentó bypassear el login pero no se pudo, ya que parece que sólo se puede acceder de forma local por ssh

![](../../Imágenes/Pasted%20image%2020251215173616.png)

![](../../Imágenes/Pasted%20image%2020251215173726.png)


Viendo el código fuente podemos ver la v ersión del PHPMyAdmin en la que se encontró una vulnerabilidad (CVE-2017-18264) en la que pasando la contraseña por un array en vez de una cadena se puede bypassear el iniciar sesión sin contraseña, en caso de que hubiera un usuario sin contraseña

![](../../Imágenes/Pasted%20image%2020251215174036.png)


Entramos a la página de wordpress que vimos previamente con el fuzzing

![](../../Imágenes/Pasted%20image%2020251215181609.png)


Enumeramos la página con wpscan

```bash
wpscan --url http://IP_víctima/wordpress
```

![](../../Imágenes/Pasted%20image%2020251215181905.png)

Enumeramos tambien los usuarios

```bash
wpscan --url http://IP_víctima/wordpress --enumerate u
```

![](../../Imágenes/Pasted%20image%2020251215182145.png)


Al tener xmlrpc activado, intentamos hacer fuerza bruta al usuario admin encontrado

```bash
wpscan --url http://IP_víctima/wordpress -U admin -P /ruta_diccionario
```

![](../../Imágenes/Pasted%20image%2020251215182630.png)



![](../../Imágenes/Pasted%20image%2020251215183121.png)


Con la sesión iniciada como admin, iremos a los temas del wordpress

![](../../Imágenes/Pasted%20image%2020251215183419.png)



![](../../Imágenes/Pasted%20image%2020251215184227.png)


Editaremos la plantilla 404 en la que pondremos nuestra reverse shell

![](../../Imágenes/Pasted%20image%2020251215184315.png)



![](../../Imágenes/Pasted%20image%2020251215184525.png)


Entramos a la dirección donde está dicha plantilla que hemos modificado

![](../../Imágenes/Pasted%20image%2020251215184919.png)


Y ya tenemos nuestra reverse shell

![](../../Imágenes/Pasted%20image%2020251215184932.png)



Investigando la máquina en búsqueda de la flag de usuario, encontramos en /opt un archivo en el que tenemos unas credenciales

![](../../Imágenes/Pasted%20image%2020251215185300.png)


Intentamos logarnos con ese usuario pero no podemos ya que tenemos que hacerlo desde la terminal

![](../../Imágenes/Pasted%20image%2020251215185517.png)


![](../../Imágenes/Pasted%20image%2020251215185706.png)


Una vez tengamos nuestra terminal podemos ver la flag de usuario

![](../../Imágenes/Pasted%20image%2020251215185750.png)


Dentro del usuario, también encontramos un txt que nos dice que hay un servicio con Jenkins corriendo en la red interna en el puerto 8080

![](../../Imágenes/Pasted%20image%2020251215185812.png)


Comprobamos y es cierto que hay un servicio por ese puerto

![](../../Imágenes/Pasted%20image%2020251215185846.png)

Para continuar habrá que hacer un port forwarding del 8080 a nuestro equipo
