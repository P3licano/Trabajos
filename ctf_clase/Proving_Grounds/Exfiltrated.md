

Realizamos un *nmap* para ver los puertos abiertos y ver qué están corriendo

```bash
nmap -sCV -p- --open -n -Pn -vvv IP_víctima -oN nom_resultado.txt
```

![](../../Imágenes/Pasted%20image%2020260109184910.png)


Encontramos 2 puertos abiertos:
### 22 SSH
### 80 HTTP

![](../../Imágenes/Pasted%20image%2020260109184924.png)


Entramos a la página web

![](../../Imágenes/Pasted%20image%2020260109185214.png)


Observamos qué tecnologías está usando la página

![](../../Imágenes/Pasted%20image%2020260109185229.png)


![](../../Imágenes/Pasted%20image%2020260109190544.png)


admin:admin

![](../../Imágenes/Pasted%20image%2020260109190603.png)


![](../../Imágenes/Pasted%20image%2020260109201836.png)


Teniendo el servicio y la versión buscamos algún exploit

```bash
searchsploit servicio
```

![](../../Imágenes/Pasted%20image%2020260109191500.png)


Una vez tenemos nuestro exploit, miramos las instrucciones

![](../../Imágenes/Pasted%20image%2020260109201728.png)


Sabiendo ya las instrucciones, configuramos el *exploit* a nuestras necesidades

![](../../Imágenes/Pasted%20image%2020260109201951.png)


Obtenemos una *shell* con la que ejecutar comandos

![](../../Imágenes/Pasted%20image%2020260109202051.png)



![](../../Imágenes/Pasted%20image%2020260109202100.png)


