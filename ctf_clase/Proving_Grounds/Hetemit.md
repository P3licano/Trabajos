

Realizamos un *nmap* para ver los puertos abiertos y ver qué están corriendo

```bash
nmap -sCV -p- --open -n -Pn -vvv IP_víctima -oN nom_resultado.txt
```

![](../../Imágenes/Pasted%20image%2020260112002019.png)


Encontramos 7 puertos abiertos:
### 21 FTP
### 22 SSH

### 80 HTTP

### 139 SMBD

### 445 SMBD

### 18000 HTTP

### 50000 HTTP

![](../../Imágenes/Pasted%20image%2020260112002038.png)




![](../../Imágenes/Pasted%20image%2020260112002056.png)


![](../../Imágenes/Pasted%20image%2020260112002113.png)


Entramos por el puerto 80 a la web

![](../../Imágenes/Pasted%20image%2020260112002151.png)


Al no encontrar nada de interés en la anterior página, pasamos a la del puerto **18000**

![](../../Imágenes/Pasted%20image%2020260112010028.png)


Como vemos nos deja iniciar sesión y registrarnos, intentamos crearnos una cuenta

![](../../Imágenes/Pasted%20image%2020260112010144.png)


Al no tener un código de invitación, no podemos crearnos una cuenta de usuario

![](../../Imágenes/Pasted%20image%2020260112010156.png)


Intentamos credenciales por defecto como admin:admin sin suerte 

![](../../Imágenes/Pasted%20image%2020260112010214.png)





Por último, entramos en la última web, alojada en el puerto **50000** la cual nos devolverá un "/generate" y un "/verify"

![](../../Imágenes/Pasted%20image%2020260112002306.png)


Si accedemos a la primera "opción" veremos que nos devuelve un formato de mail con el que probablemente nos pueda generar un código para crearnos una cuenta o que nos genere un mail para poder acceder

![](../../Imágenes/Pasted%20image%2020260112002845.png)


Probando un poco en *burpsuite* encontramos que con el parámetro "email"+ nmail@dominio.com podemos generar lo que parece ser un código de invitación que nos faltaba previamente

![](../../Imágenes/Pasted%20image%2020260112013410.png)


Ahora, al intentar crearnos la cuenta, no nos dará error, adicionalmente meteremos una imagen con código malicioso a ver si podemos ejecutarlo de alguna manera

![](../../Imágenes/Pasted%20image%2020260112013419.png)


Iniciamos sesión con la cuenta creada previamente

![](../../Imágenes/Pasted%20image%2020260112013440.png)


En principio no vemos que podamos acceder a la imagen creada con el código malicioso, ya que al ejecutarla, únicamente nos descarga el archivo

![](../../Imágenes/Pasted%20image%2020260112013827.png)


Ya que no pudimos ejecutar el código de antes, volvemos a la página y vamos a "/verify" donde vemos que supuestamente podemos escribir código

![](../../Imágenes/Pasted%20image%2020260112010336.png)


Intentamos ejecutar un *whoami*

![](../../Imágenes/Pasted%20image%2020260112015016.png)


Y vemos que parece que funciona

![](../../Imágenes/Pasted%20image%2020260112015025.png)


Como queremos ver el resultado, me encontré con éste post que nos explica como hacerlo --> https://stackoverflow.com/questions/3503879/assign-output-of-os-system-to-a-variable-and-prevent-it-from-being-displayed-on

```python
os.popen('whoami').read()
```




![](../../Imágenes/Pasted%20image%2020260112015243.png)


Ahora vemos que podemos ver la salida del comando

![](../../Imágenes/Pasted%20image%2020260112021307.png)


Lanzamos una shell y nos ponemos a la escucha por el mismo puerto

![](../../Imágenes/Pasted%20image%2020260112021115.png)


Ya tenemos una *shell* funcional

![](../../Imágenes/Pasted%20image%2020260112021131.png)