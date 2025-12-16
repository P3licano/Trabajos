

Realizamos un nmap para ver los puertos abiertos y ver qué están corriendo

```bash
nmap -sCV -p- --open -n -Pn -vvv IP_víctima -oN nom_resultado.txt
```

![](../../Imágenes/Pasted%20image%2020251215192831.png)


Vemos que tenemos un Tomcat corriendo en el puerto 8080

![](../../Imágenes/Pasted%20image%2020251215192924.png)


Hacemos un fuzzing de directorios

```bash
feroxbuster --url http://IP_víctima -w /ruta_diccionario
```

![](../../Imágenes/Pasted%20image%2020251215193156.png)

```bash
gobuster dir -u http://IP_víctima -w /ruta_diccionario
```

![](../../Imágenes/Pasted%20image%2020251215193210.png)


Entramos en /docs donde podemos ver la documentación de Tomcat

![](../../Imágenes/Pasted%20image%2020251215193407.png)


Entramos en /examples donde se muestran ejemplos de Servlets, WebSockets y JSP

![](../../Imágenes/Pasted%20image%2020251215193434.png)


![](../../Imágenes/Pasted%20image%2020251215193447.png)



Al entrar en /manager nos encontramos con un panel de login del cual no tenemos credenciales

![](../../Imágenes/Pasted%20image%2020251215193511.png)


Al cancelar el login nos sale una página de ejemplo con un usuario y contraseña por defecto

![](../../Imágenes/Pasted%20image%2020251215193546.png)


(En esta lista se pueden ver los usuarios por defecto)

![](../../Imágenes/Pasted%20image%2020251215195140.png)


Parece que el usuario tomcat con contraseña s3cret ha funcionado. En la página podemos subir únicamente archivos .war

![](../../Imágenes/Pasted%20image%2020251215193619.png)


Mirando en internet como subir una reverse mediante un archivo war, vemos que se puede realizar mediante Metasploit, lo que haremos será filtrar los payloads por "java" ya que es el lenguaje que usa la aplicación

![](../../Imágenes/Pasted%20image%2020251215202711.png)


Vemos qué tenemos que configurar del payload

![](../../Imágenes/Pasted%20image%2020251215203156.png)


Ponemos nuestra IP y el puerto que tenemos a la escucha, con el formato (-f) war y que nos lo mande al output (-o) revy.war

![](../../Imágenes/Pasted%20image%2020251215203359.png)


Subimos nuestra reverse y la ejecutamos

![](../../Imágenes/Pasted%20image%2020251215203548.png)


Tenemos acceso a la máquina como usuario tomcat

![](../../Imágenes/Pasted%20image%2020251215203607.png)


Vemos la flag de usuario junto con un txt que nos devuelve el id de root

![](../../Imágenes/Pasted%20image%2020251215203647.png)


Junto a la flag vemos un script con permisos de usuario de jack, que al ejecutar id devuelve el output a un fichero llamado test.txt el cual tiene permisos del usuario root

![](../../Imágenes/Pasted%20image%2020251215204449.png)


Si modificamos el script para que nos imprima lo que hay dentro del directorio de jack

![](../../Imágenes/Pasted%20image%2020251215205024.png)


Al ejecutar el comando id y volver a consultar el fichero test.txt, podemos ver lo que hay dentro del directorio de jack

![](../../Imágenes/Pasted%20image%2020251215205133.png)


Lo mismo pasa con el directorio de root

![](../../Imágenes/Pasted%20image%2020251215205431.png)


![](../../Imágenes/Pasted%20image%2020251215205550.png)


Ahora que hemos visto la flag de root, sólo nos queda leerla

![](../../Imágenes/Pasted%20image%2020251215205624.png)


Vemos la flag de root

![](../../Imágenes/Pasted%20image%2020251215205857.png)


