

Realizamos un nmap para ver los puertos abiertos y ver qué están corriendo

```bash
nmap -sCV -p- --open -n -Pn -vvv IP_víctima -oN nom_resultado.txt
```

![](../../Imágenes/Pasted%20image%2020251215231745.png)


Vemos la web por el puerto 33414 la cual no logramos sacar nada

![](../../Imágenes/Pasted%20image%2020251215232141.png)


Y la web del puerto 40080 la cual vemos algo

![](../../Imágenes/Pasted%20image%2020251215232152.png)


Continuamos con la enumeración de directorios

```bash
feroxbuster --url http://IP_víctima -w /ruta_diccionario
```

![](../../Imágenes/Pasted%20image%2020251215232246.png)

```bash
gobuster dir -u http://IP_víctima -w /ruta_diccionario
```

![](../../Imágenes/Pasted%20image%2020251215232333.png)


Al no encontrar nada de interés, realizamos lo mismo en la página anterior

```bash
feroxbuster --url http://IP_víctima -w /ruta_diccionario
```

![](../../Imágenes/Pasted%20image%2020251215232426.png)

```bash
gobuster dir -u http://IP_víctima -w /ruta_diccionario
```

![](../../Imágenes/Pasted%20image%2020251215232445.png)


Entramos en el directorio /help en el que nos da información de que podemos listar directorios, y de que hay otro que es file-upload

![](../../Imágenes/Pasted%20image%2020251215232543.png)


En el directorio de info podemos ver un posible usuario

![](../../Imágenes/Pasted%20image%2020251215232554.png)


Como vemos podemos visualizar directorios

![](../../Imágenes/Pasted%20image%2020251215232811.png)


Vemos que el directorio de alfredo existe, por lo que validamos el usuario

![](../../Imágenes/Pasted%20image%2020251215232824.png)


Y dentro de su directorio, encontramos nuestra preciada flag de usuario y unas claves ssh bastante interesantes

![](../../Imágenes/Pasted%20image%2020251215233341.png)


Vemos como funciona la subida de archivos

(Funciona con método POST)

![](../../Imágenes/Pasted%20image%2020251215232926.png)


![](../../Imágenes/Pasted%20image%2020251215233001.png)


Vemos los archivos de las claves de alfredo, pero no podemos acceder a ellas

![](../../Imágenes/Pasted%20image%2020251215233725.png)


Probamos subir archivos no vaya a ser que no tengamos permisos o no tengamos acceso

![](../../Imágenes/Pasted%20image%2020251215234047.png)


![](../../Imágenes/Pasted%20image%2020251215234111.png)


Probamos lo mismo, pero en el directorio de alfredo


![](../../Imágenes/Pasted%20image%2020251215234359.png)


![](../../Imágenes/Pasted%20image%2020251215234347.png)


Como podemos subir archivos al directorio de alfredo, subiremos nuestras propias claves de ssh para poder autenticarnos

Generamos un par de claves

![](../../Imágenes/Pasted%20image%2020251215235533.png)


Le damos permisos de lectura y escritura para el usuario

![](../../Imágenes/Pasted%20image%2020251215235633.png)


Las subimos , pero vemos que no admite extensiones .pub por lo que deberemos de cambiarla por una de las que nos pone ahí

![](../../Imágenes/Pasted%20image%2020251215235852.png)


Una vez cambiada la extensión veremos que nos deja subir la clave

![](../../Imágenes/Pasted%20image%2020251215235942.png)


![](../../Imágenes/Pasted%20image%2020251216000056.png)


Ahora accederemos por ssh con las claves subidas

![](../../Imágenes/Pasted%20image%2020251216000037.png)


Así obtendremos nuestra flag de usuario

![](../../Imágenes/Pasted%20image%2020251216000133.png)