

Realizamos un nmap para ver los puertos abiertos y ver qué están corriendo

```bash
nmap -sCV -p- --open -n -Pn -vvv IP_víctima -oN nom_resultado.txt
```


![](../../Imágenes/Pasted%20image%2020260108182826.png)


Encontramos 4 puertos abiertos:
### 22 SSH
### 25 SMTP
### 80 HTTP
### 445 SMBD

![](../../Imágenes/Pasted%20image%2020260108182845.png)


Entramos en el puerto 80 a la web

![](../../Imágenes/Pasted%20image%2020260108183036.png)



![](../../Imágenes/Pasted%20image%2020260108183050.png)


Al no encontrar nada en la web, continuamos con un *fuzzeo* de directorios a la búsqueda de algo interesante

```bash
feroxbuster --url http://$IP_victima -w ruta_diccionario
```

![](../../Imágenes/Pasted%20image%2020260108183217.png)


```bash
gobuster dir -u http://$IP_victima -w ruta_diccionario
```

![](../../Imágenes/Pasted%20image%2020260108184000.png)


Al no encontrar nada de interés en el *fuzzing*, volví a mirar todo de nuevo en búsqueda de nuevas pistas, vi en el *nmap* que me reportó que podía acceder al servicio *smb* sin autenticarme

![](../../Imágenes/Pasted%20image%2020260108184017.png)


Gracias a la página --> https://0xdf.gitlab.io/cheatsheets/smb-enum# podemos enumerar el *smb* así como alguno de sus contenidos

```bash
netexec $IP_victima -u usuario --shares #vemos los compartidos
```

![](../../Imágenes/Pasted%20image%2020260108185653.png)

o

```bash
smbclient -N -L bratarina
```

![](../../Imágenes/Pasted%20image%2020260108190142.png)


Como vemos que tenemos un archivo compartido llamado "backups" accedemos a el para ver su contenido

```bash
smbclient //$IP_victima/compartido -N
```

![](../../Imágenes/Pasted%20image%2020260108190239.png)


Encontramos un fichero "passwd.bak" 

![](../../Imágenes/Pasted%20image%2020260108190335.png)


En el que encontramos el archivo de "/etc/passwd" con un usuario llamado "neil"

![](../../Imágenes/Pasted%20image%2020260108190522.png)


Buscamos vulnerabilidades en el servicio "smb" pero no logramos encontrar nada

```bash
nmap --script smb-vuln* -p puerto/s_smb $IP_victima
```

![](../../Imágenes/Pasted%20image%2020260108190814.png)


En cambio encontramos que en el smtp podemos encontrar un usuario root -->https://nmap.org/nsedoc/scripts/smtp-enum-users.html

```bash
nmap --script smtp-enum-users.nse -p puerto/s_smtp $IP_victima
```

![](../../Imágenes/Pasted%20image%2020260108191042.png)


Encontramos una forma de validar usuarios, por lo que enumeramos el usuario "neil" encontrado en el smb previamente --> https://medium.com/@rajkumarkumawat/%EF%B8%8Fsmtp-enumeration-the-ethical-hackers-guide-to-uncovering-email-vulnerabilities-efc85ae0a563 pero no logramos validar al usuario

```bash
smtp-user-enum -M VRFY -u usuario -t $IP_victima
```

![](../../Imágenes/Pasted%20image%2020260108191801.png)


También probamos a hacer fuerza bruta al *smtp* con el usuario root, pero no podemos ya que el "login auth" está deshabilitado o no lo está usando

```bash
hydra -l usuario -P diccionario smtp://$IP_victima
```

![](../../Imágenes/Pasted%20image%2020260108193336.png)


Buscamos algún exploit a la versión de *SMTPD* en el que encontramos una manera de realizar ejecución remota de comandos

```bash
searchsploit servicio
```


![](../../Imágenes/Pasted%20image%2020260108194052.png)


Nos descargamos el exploit y lo miramos

![](../../Imágenes/Pasted%20image%2020260108194757.png)


![](../../Imágenes/Pasted%20image%2020260108194823.png)


Usamos el exploit teniendo previamente un puerto a la escucha

```python
python3 nexploit.py $IP_victima 'comando'
```

![](../../Imágenes/Pasted%20image%2020260108200410.png)


Obtenemos la shell

![](../../Imágenes/Pasted%20image%2020260108200421.png)