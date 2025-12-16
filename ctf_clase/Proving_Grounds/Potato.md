

Realizamos un nmap para ver los puertos abiertos y ver qué están corriendo

```bash
nmap -sCV -p- --open -n -Pn -vvv IP_víctima -oN nom_resultado.txt
```

![](../../Imágenes/Pasted%20image%2020251215220935.png)


Como tenemos login anónimo por ftp, accedemos a el primero

![](../../Imágenes/Pasted%20image%2020251215221242.png)


Encontramos dos ficheros los cuales nos los traemos a nuestra máquina

```bash
get nom_archivo
```

![](../../Imágenes/Pasted%20image%2020251215221313.png)


Vemos el contenido del fichero index.php.bak que resulta ser un script de autenticación de inicio de sesión en el que podemos ver unas credenciales

![](../../Imágenes/Pasted%20image%2020251215221438.png)


Vemos la página inicial sin nada interesante, salvo una apetecible patata

![](../../Imágenes/Pasted%20image%2020251215221608.png)


Iniciamos el fuzzing de directorios

```bash
feroxbuster --url http://IP_víctima -w /ruta_diccionario
```

![](../../Imágenes/Pasted%20image%2020251215221732.png)

```bash
gobuster dir -u http://IP_víctima -w /ruta_diccionario
```

![](../../Imágenes/Pasted%20image%2020251215221956.png)


Usamos las credenciales previamente pero no son las correctas

![](../../Imágenes/Pasted%20image%2020251215221719.png)


![](../../Imágenes/Pasted%20image%2020251215222008.png)


Me dirijo al último directorio a ver si hay algo de utilidad (no la hay)

![](../../Imágenes/Pasted%20image%2020251215222049.png)


Buscando una manera de bypassear el login, me encuentro con esta página: https://rst.hashnode.dev/bypassing-php-strcmp en la que por lo visto hay una vulnerabilidad en el parámetro strcmp, en el cual si pasábamos la contraseña por un array en vez de una cadena podíamos bypassear el login

![](../../Imágenes/Pasted%20image%2020251215223626.png)


Y así fue

![](../../Imágenes/Pasted%20image%2020251215223633.png)


Navegando un poco por el panel de admin, encontramos los siguientes campos interesantes

![](../../Imágenes/Pasted%20image%2020251215223702.png)


Encontramos al usuario admin de nuevo

![](../../Imágenes/Pasted%20image%2020251215223751.png)


Podemos visualizar 3 logs

![](../../Imágenes/Pasted%20image%2020251215223829.png)


Si capturamos el log_3.txt veremos que hay un parametro "file" del cual parece que podemos hacer un path traversal

![](../../Imágenes/Pasted%20image%2020251215225220.png)


Y vemos que poniendo ../../../../../etc/passwd logramos ver los usuarios del sistema

![](../../Imágenes/Pasted%20image%2020251215225322.png)


Cogemos todo el campo de webadmin y lo pasamos a un fichero .txt para crackear la contraseña con john the ripper

```bash
john --wordlist=ruta_diccionario.txt hash.txt
```

![](../../Imágenes/Pasted%20image%2020251215225827.png)


Con las credenciales iniciamos sesión por ssh como webadmin

![](../../Imágenes/Pasted%20image%2020251215225911.png)


Buscamos de algún binario que podamos explotar

![](../../Imágenes/Pasted%20image%2020251215230234.png)


Observamos que tenemos permiso para usar el binario nice (que se puede abusar) en /notes/ (no lo conseguí pero vamos a las muy malas se puede mirar que se puede explotar la vulnerabilidad PwnKit – CVE-2021-4034 https://github.com/ly4k/PwnKit que seguramente lo tenga)

![](../../Imágenes/Pasted%20image%2020251215230400.png)