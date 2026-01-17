

Realizamos un *nmap* para ver los puertos abiertos y ver qué están corriendo

```bash
nmap -sCV -p- --open -n -Pn -vvv IP_víctima -oN nom_resultado.txt
```


Encontramos 3 puertos abiertos:
### 22 SSH
### 80 HTTP

### 8338 HTTP

![](../../Imágenes/Pasted%20image%2020260112030335.png)


Entramos en la página del puerto 80 en el que encontramos una página por defecto de *Apache*

![](../../Imágenes/Pasted%20image%2020260112030309.png)


Al no encontrar nada en la página previa, miramos a ver qué tiene la que está en el puerto:**8338**

Nos encontramos un panel de inicio de sesión en el que como siempre probamos credenciales de acceso por defecto como admin:admin

![](../../Imágenes/Pasted%20image%2020260112030417.png)


Al no tener suerte con las credenciales por defecto, vemos en la página el servicio que está corriendo la web, así como la versión

![](../../Imágenes/Pasted%20image%2020260112030454.png)


Encontramos un *exploit* con el que simplemente con indicarle `nuestra IP nuestro puerto, y la IP del objetivo`, obtenemos una *shell* con la que poder ejecutar comandos de manera remota

![](../../Imágenes/Pasted%20image%2020260112033421.png)


![](../../Imágenes/Pasted%20image%2020260112033434.png)