

Realizamos un *nmap* para ver los puertos abiertos y ver qué están corriendo

```bash
nmap -sCV -p- --open -n -Pn -vvv IP_víctima -oN nom_resultado.txt
```

Encontramos 4 puertos abiertos:
### 8080 HTTP
### 12445 SMBD

### 18030 HTTP

### 43022 SSH

![](../../Imágenes/Pasted%20image%2020260112200011.png)


Entramos por el puerto 8080 a la página web en la que podemos ver unos haikus

![](../../Imágenes/Pasted%20image%2020260112201323.png)


Entramos adicionalmente a la web del puerto 18030 en la que nos encontramos el juego de golpear al topo

![](../../Imágenes/Pasted%20image%2020260112201814.png)


Mirando en la página del puerto 8080 no encontramos nada interesante, pero dentro de los haikus, encontramos en el código fuente una dirección a una api que no sabíamos de su existencia

![](../../Imágenes/Pasted%20image%2020260112202246.png)


Al entrar vemos que tenemos varias opciones:

### /api

### /article

### /article/?

### /user

### /user/?

![](../../Imágenes/Pasted%20image%2020260112203822.png)


Yendo por orden, nos encontramos que en la parte de "/user", podemos encontrar datos de usuarios

![](../../Imágenes/Pasted%20image%2020260112203935.png)


Probamos iniciar sesión por *ssh* con todos, hasta encontrar que el 3º es el correcto y con el que podemos ejecutar comandos

![](../../Imágenes/Pasted%20image%2020260112204241.png)


