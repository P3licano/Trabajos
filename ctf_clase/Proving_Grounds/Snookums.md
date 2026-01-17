

Realizamos un *nmap* para ver los puertos abiertos y ver qué están corriendo

```bash
nmap -sCV -p- --open -n -Pn -vvv IP_víctima -oN nom_resultado.txt
```

![](Pasted%20image%2020260113210442.png)


Encontramos 8 puertos abiertos:

### 21 FTP
### 22 SSH
### 80 HTTP

### 111 RPCBIN

### 139 SMBD

### 445 SMBD

### 3306 MYSQL

### 33060 MYSQLX

![](Pasted%20image%2020260113210516.png)


Entramos a la única web que tenemos por el puerto 80

![](Pasted%20image%2020260113210317.png)


Vemos que tenemos un "Simple PHP Photo Gallery" por lo que buscamos un *exploit* (al no poder hacerlo con *searchsploit* busqué en *github*) --> https://github.com/beauknowstech/SimplePHPGal-RCE.py

Poniendo la *IP* del objetivo + la nuestra + nuestro puerto a la escucha logramos una *reverse shell*

![](Pasted%20image%2020260113202110.png)


![](Pasted%20image%2020260113202037.png)



