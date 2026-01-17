

Realizamos un *nmap* para ver los puertos abiertos y ver qué están corriendo

```bash
nmap -sCV -p- --open -n -Pn -vvv IP_víctima -oN nom_resultado.txt
```

Encontramos 4 puertos abiertos:
### 22 SSH

### 23 CUPS

### 80 HTTP

### 3306 MYSQL

![](../../Imágenes/Pasted%20image%2020260112021857.png)


Entramos a la web del puerto 80

![](../../Imágenes/Pasted%20image%2020260112021942.png)


Al no encontrar nada, miramos el código fuente para solamente encontrar que está "bajo construcción"

![](../../Imágenes/Pasted%20image%2020260112021951.png)


Miramos las tecnologías de la web en busca de información

![](../../Imágenes/Pasted%20image%2020260112022003.png)


Realizamos un *fuzzing* a los directorios de la web

```bash
feroxbuster --url $IP_victima -w diccionario
```

![](../../Imágenes/Pasted%20image%2020260112022359.png)


![](../../Imágenes/Pasted%20image%2020260112022427.png)


Encontramos una directorio llamado "test" donde vemos qué servicio está usando (*ZenPHOTO*)

![](../../Imágenes/Pasted%20image%2020260112022437.png)


Dentro del código fuente, vemos que está corriendo la versión del servicio

![](../../Imágenes/Pasted%20image%2020260112022821.png)


En el *feroxbuster* encontramos el directorio de "/robots" en el cual encontramos unos directorios interesantes

![](../../Imágenes/Pasted%20image%2020260112022913.png)


Encontramos un panel de inicio de sesión el cual intentaremos entrar con credenciales por defecto

![](../../Imágenes/Pasted%20image%2020260112023100.png)


![](../../Imágenes/Pasted%20image%2020260112023117.png)


Probando entre los distintos directorios, encontramos uno "/zp-data" en el que podemos encontrar varios archivos entre los cuales vemos un "security_log.txt" en el cual por obvios motivos no podremos acceder

![](../../Imágenes/Pasted%20image%2020260112023003.png)

![](../../Imágenes/Pasted%20image%2020260112023021.png)


Sin más que hacer, miramos en *searchsploit* en búsqueda de algún *exploit*

```bah
searchsploit servicio
```

![](../../Imágenes/Pasted%20image%2020260112023233.png)


Encontramos uno que nos permite ejecutar comandos poniendo la *IP* del objetivo y la ruta del *ZenPHOTO*

![](../../Imágenes/Pasted%20image%2020260112024808.png)



![](../../Imágenes/Pasted%20image%2020260112024752.png)


