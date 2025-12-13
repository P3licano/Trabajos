

Realizamos un nmap a la ip de la máquina en búsqueda de puertos abiertos

```bash
nmap -sCV -p- --open -n -Pn -vvv IP_victima -oN nom_resultado.txt
```

![](../../Imágenes/Pasted%20image%2020251213162319.png)



Al acceder a la web y no poder ver nada en ella, realizamos un fuzzing de directorios a la página, primero un feroxbuster

```bash
feroxbuster --url http://IP_victima -w ruta_diccionario
```

Al no devolvernos nada interesante, procedemos a realizar otro fuzzing, esta vez usando gobuster

```bash
gobuster dir -u http://IP_victima -w ruta_diccionario
```

Y encontramos de primeras un directorio llamado "/rms"

![](../../Imágenes/Pasted%20image%2020251212194913.png)


Al entrar vemos una página de un restaurante, hacemos un reconocimiento rápido de la página para ver qué encontramos

![](../../Imágenes/Pasted%20image%2020251212195009.png)


![](../../Imágenes/Pasted%20image%2020251212200145.png)


Nos creamos una cuenta para ver si siendo usuarios tenemos más funcionalidades interesantes

![](../../Imágenes/Pasted%20image%2020251212195644.png)


Encontramos unas nuevas funcionalidades

![](../../Imágenes/Pasted%20image%2020251212195725.png)


Encontramos el user de admin

![](../../Imágenes/Pasted%20image%2020251212195954.png)

Al no poder encontrar nada en la página salvo un parámetro que se debería inyectar sql (eliminando un pedido que hayas hecho), continuamos para ver que es eso de "rms" (Restaurant Management System)


Haciendo una pequeña búsqueda nos encontramos con un RCE en el que no hace falta que estemos autenticados

![](../../Imágenes/Pasted%20image%2020251213000200.png)


Haciendo unos ajustes al exploit, podemos ver que sube una shell para ejecutar comandos, en la cual ya habremos modificado para que lo que nos devuelva sea una reverse shell

![](../../Imágenes/Pasted%20image%2020251213001210.png)


Escuchando por el puerto 4444 recibimos la reverse en la que podemos ejecutar comandos

![](../../Imágenes/Pasted%20image%2020251213003226.png)