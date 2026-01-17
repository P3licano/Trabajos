
Realizamos un *nmap* para ver los puertos abiertos y ver qué están corriendo

```bash
nmap -sCV -p- --open -n -Pn -vvv IP_víctima -oN nom_resultado.txt
```

![](../../Imágenes/Pasted%20image%2020260114011121.png)


Encontramos 3 puertos abiertos:
### 22 SSH
### 8090 HTTP

### 8091 JAMLINK

![](../../Imágenes/Pasted%20image%2020260114011217.png)



Entramos en el puerto 8090 y vemos un panel de login

![](../../Imágenes/Pasted%20image%2020260114011305.png)


Intentamos credenciales por defecto como admin:admin

![](../../Imágenes/Pasted%20image%2020260114011326.png)


Vemos el servicio que está corriendo en la web y vemos que es "Atlassian Confluence 7.13.6"

![](../../Imágenes/Pasted%20image%2020260114011604.png)



Buscamos un exploit con searchsploit

```bash
searchsploit servicio
```

![](../../Imágenes/Pasted%20image%2020260114011545.png)


Como siempre, miramos las instrucciones del *exploit* para ver cómo usarlo

![](../../Imágenes/Pasted%20image%2020260114011712.png)


Desgraciadamente, no consigo que funcione el primer exploit, por lo que paso a uno que me encontré en github: https://github.com/jbaines-r7/through_the_wire con el que conseguimos adquirir una shell con la que ejecutar comandos

![](../../Imágenes/Pasted%20image%2020260114013042.png)


