

Metemos la ip de la máquina en nuestro archivo etc/hosts 

![](../../Imágenes/Pasted%20image%2020251211190403.png)


Hacemos un nmap a la ip de la máquina en búsqueda de sus puertos abiertos

```bash
nmap -sCV -p- --open -n -Pn -vvv IP_victima -oN resultado.txt
```

![](../../Imágenes/Pasted%20image%2020251211184952.png)

Viendo que tiene únicamente dos puertos, (22 y 80) se comprueba el puerto 80 ya que en el 22 de momento no podemos acceder por falta de credenciales.

En la página no se encontró nada interesante, por lo que se procedió a realizar un fuzzing de directorios

```bash
feroxbuster --url http://IP_victima -w /usr/share/ruta_diccionario/diccionario
```

![](../../Imágenes/Pasted%20image%2020251211185025.png)


En el fuzzing descubrimos el directorio de robots.txt al cual accedemos, pero no logramos sacar ningún resultado ya que no tenemos permisos para acceder a los directorios que nos muestran

![](../../Imágenes/Pasted%20image%2020251211185159.png)

![](../../Imágenes/Pasted%20image%2020251211185220.png)


Ya que no obtuvimos ningún resultado con los robots, accedimos al directorio de admin, probando unas credenciales por defecto sin mucho éxito.

![](../../Imágenes/Pasted%20image%2020251211185105.png)


Al no encontrar nada más interesante


![](../../Imágenes/Pasted%20image%2020251211190846.png)



![](../../Imágenes/Pasted%20image%2020251211191225.png)


![](../../Imágenes/Pasted%20image%2020251211191549.png)



![](../../Imágenes/Pasted%20image%2020251211195121.png)


![](../../Imágenes/Pasted%20image%2020251211195524.png)

![](../../Imágenes/Pasted%20image%2020251211195732.png)



![](../../Imágenes/Pasted%20image%2020251211195949.png)


![](../../Imágenes/Pasted%20image%2020251211200250.png)


![](../../Imágenes/Pasted%20image%2020251211200941.png)


![](../../Imágenes/Pasted%20image%2020251211201356.png)