

Al realizar un nmap

```bash
nmap -sCV -p- --open -n -Pn -vvv IP_victima -oN resultado.txt
```

Encontramos los puertos:

21 --> ftp
22 --> ssh
80 --> http
139 --> Samba 3.X
445 --> Samba 4.9
7080 --> LiteSpeed
7601 --> http
8088 --> http

![](../../Imágenes/Pasted%20image%2020251213144047.png)


Accedemos al puerto 80, en el cual nos pedirán unas credenciales de las cuales carecemos, por lo que pasaremos al siguiente http

![](../../Imágenes/Pasted%20image%2020251213144429.png)


Éste nos carga una solamente una imagen

![](../../Imágenes/Pasted%20image%2020251213144502.png)


Miramos en el código fuente en búsqueda de algún comentario o pista

![](../../Imágenes/Pasted%20image%2020251213144513.png)


Al no encontrar nada en la página, pasamos al fuzzing con feroxbuster

```bash
feroxbuster --url http://url -w ruta_diccionario
```

![](../../Imágenes/Pasted%20image%2020251213144922.png)


Encontramos varios directorios curiosos /a, /b, /c... por lo que accederemos a ellos

![](../../Imágenes/Pasted%20image%2020251213155420.png)


Entre los directorios curiosos nos encontramos un /ckeditor, el cual al ojear rápidamente no encontramos nada interesante, pero que lo tendremos en cuenta para un posible futuro

![](../../Imágenes/Pasted%20image%2020251213160254.png)


Mirando el ferox, nos encontramos con un directorio /keys con una clave de ssh

![](../../Imágenes/Pasted%20image%2020251213160736.png)


![](../../Imágenes/Pasted%20image%2020251213160754.png)


Al no encontrar nada más interesante realicé un gobuster en búsqueda de nuevas pistas

```bash
gobuster dir -u http://IP_victima -w ruta_diccionario
```

![](../../Imágenes/Pasted%20image%2020251213161054.png)


En el gobuster encontramos un directorio llamado /secret (el directorio tambien estaba en el feroxbuster pero no me di cuenta ya que estaba muy al final) el cual nos da unas credenciales de usuario como un diccionario para la contraseña

![](../../Imágenes/Pasted%20image%2020251213161122.png)



![](../../Imágenes/Pasted%20image%2020251213161135.png)




![](../../Imágenes/Pasted%20image%2020251213161154.png)


Con las credenciales obtenidas realizamos un ataque de fuerza bruta al ssh al usuario que hemos encontrado con el diccionario

![](../../Imágenes/Pasted%20image%2020251213161421.png)


Con el usuario y contraseña encontrados, accedemos por ssh al usuario seppuku, en el cual en su directorio nos esperan tanto su flag como otra contraseña

![](../../Imágenes/Pasted%20image%2020251213161456.png)



![](../../Imágenes/Pasted%20image%2020251213161614.png)


![](../../Imágenes/Pasted%20image%2020251213161903.png)