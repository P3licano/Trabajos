

Realizamos un nmap para ver los puertos abiertos y ver qué están corriendo

```bash
nmap -sCV -p- --open -n -Pn -vvv IP_víctima -oN nom_resultado.txt
```

![](../../Imágenes/Pasted%20image%2020251215210542.png)


Entramos en la página pero no encontramos nada de interés

![](../../Imágenes/Pasted%20image%2020251215211017.png)


Hacemos un fuzzing de directorios

```bash
feroxbuster --url http://IP_víctima -w /ruta_diccionario
```

![](../../Imágenes/Pasted%20image%2020251215210919.png)

```bash
gobuster dir -u http://IP_víctima -w /ruta_diccionario
```

![](../../Imágenes/Pasted%20image%2020251215210941.png)


Encontramos el directorio /panel que nos permite subir archivos

![](../../Imágenes/Pasted%20image%2020251215211134.png)


Vemos que lenguaje usa la página con wappalyzer

![](../../Imágenes/Pasted%20image%2020251215211144.png)


Subimos nuestra reverse shell

![](../../Imágenes/Pasted%20image%2020251215211204.png)


Nos dice que los archivos con extensión .php no están permitidos

![](../../Imágenes/Pasted%20image%2020251215211229.png)


Cambiamos la extensión de php a phtml

![](../../Imágenes/Pasted%20image%2020251215211438.png)



![](../../Imágenes/Pasted%20image%2020251215211411.png)



![](../../Imágenes/Pasted%20image%2020251215211423.png)


Como parece que nos ha dejado, solo nos queda irnos al apartado de /uploads y ejecutar nuestra reverse

![](../../Imágenes/Pasted%20image%2020251215211512.png)




![](../../Imágenes/Pasted%20image%2020251215211632.png)


Aquí encontramos la flag de usuario

![](../../Imágenes/Pasted%20image%2020251215212113.png)


Vemos si podemos abusar de algún binario para escalar privilegios

![](../../Imágenes/Pasted%20image%2020251215213820.png)


Encontramos que con el binario python podemos escalar privilegios

![](../../Imágenes/Pasted%20image%2020251215213926.png)


Ahora somos root

![](../../Imágenes/Pasted%20image%2020251215213941.png)


Y podemos ver la flag de root

![](../../Imágenes/Pasted%20image%2020251215214205.png)