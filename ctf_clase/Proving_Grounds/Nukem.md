
Realizamos un *nmap* para ver los puertos abiertos y ver qué están corriendo

```bash
nmap -sCV -p- --open -n -Pn -vvv IP_víctima -oN nom_resultado.txt
```


Encontramos 6 puertos abiertos:
### 22 SSH

### 80 HTTP

### 3306 MYSQL

### 5000 HTTP

### 13000 HTTP

### 36445 SMBD

![](../../Imágenes/Pasted%20image%2020260112164058.png)


Entramos a la página alojada en el puerto 80 y nos encontramos con lo siguiente

![](../../Imágenes/Pasted%20image%2020260112164220.png)


En la página, se nos indica que está usando un *Wordpress* por lo que procedemos a su enumeración con la herramienta de *wpscan*

```bash
wpscan --url http://$IP_victima
```

![](../../Imágenes/Pasted%20image%2020260112170120.png)


Vemos que tiene *XML-RPC* activado

![](../../Imágenes/Pasted%20image%2020260112170128.png)


Vemos los temas que tiene en uso (desactualizados por cierto)

![](../../Imágenes/Pasted%20image%2020260112170144.png)


Así como los *plugins* en uso (desactualizados tambien)

![](../../Imágenes/Pasted%20image%2020260112170157.png)


Buscamos por algún usuario al que podamos realizarle fuerza bruta

![](../../Imágenes/Pasted%20image%2020260112170209.png)


Encontramos un usuario administrador

![](../../Imágenes/Pasted%20image%2020260112170221.png)

**Intentamos hacer fuerza bruta al *login* sin resultado**


Buscamos *exploits* en los temas sin resultado

![](../../Imágenes/Pasted%20image%2020260112193012.png)


Buscamos *exploits* en los plugins y encontramos uno que nos permite *RCE*

![](../../Imágenes/Pasted%20image%2020260112193019.png)


Ejecutamos el exploit, que nos devulelve la *url* donde se ha subido el fichero del programa

![](../../Imágenes/Pasted%20image%2020260112193044.png)


Entramos en la *url* con burpsuite y modificamos el parámetro POST

![](../../Imágenes/Pasted%20image%2020260112193106.png)


Le ponemos el parámetro de "password" que nos dio previamente, en el que podemos poner comandos

![](../../Imágenes/Pasted%20image%2020260112193146.png)


Como vemos se ejecutan

![](../../Imágenes/Pasted%20image%2020260112193158.png)


Ponemos una *shell* por el puerto que tenemos a la escucha

![](../../Imágenes/Pasted%20image%2020260112193255.png)


Adquirimos la *shell*

![](../../Imágenes/Pasted%20image%2020260112193307.png)


