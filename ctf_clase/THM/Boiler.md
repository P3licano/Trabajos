

Hacemos un nmap a la ip de la máquina en búsqueda de sus puertos abiertos

```bash
nmap -sCV -p- --open -n -Pn -vvv IP_victima -oN resultado.txt
```

![](../../Imágenes/Pasted%20image%2020251213004624.png)


Al ver que tiene login "anonymous" fui directo a ver qué encontraba

![](../../Imágenes/Pasted%20image%2020251213005059.png)

Al listar directorios y no encontrar nada listé tambien los ocultos

![](../../Imágenes/Pasted%20image%2020251213005308.png)


Encontramos un info.txt oculto, nos lo descargamos

```bash
get nom_archivo
```


![](../../Imágenes/Pasted%20image%2020251213005441.png)

Vemos que el archivo está encriptado, lo llevamos a la página: https://www.dcode.fr/cipher-identifier

![](../../Imágenes/Pasted%20image%2020251213005716.png)

Nos dice que está encriptado en ROT-13

![](../../Imágenes/Pasted%20image%2020251213011350.png)


Una vez decodificado, no vemos nada de interés salvo la "pista" de que la clave es la enumeración

![](../../Imágenes/Pasted%20image%2020251213011402.png)


Como tenemos una web accedemos a ella

![](../../Imágenes/Pasted%20image%2020251213012106.png)


Al encontrar una web de apache por defecto sin nada interesante, procedemos a hacer fuzzing de directorios

```bash
feroxbuster --url http://url -w ruta_diccionario
```

![](../../Imágenes/Pasted%20image%2020251213022409.png)


Vemos que hay un directorio de robots.txt al cual accederemos

![](../../Imágenes/Pasted%20image%2020251213012122.png)


Vemos otro archivo codificado con el que seguiremos el mismo proceso que el anterior, pero repitiéndolo unas veces más

![](../../Imágenes/Pasted%20image%2020251213015205.png)



![](../../Imágenes/Pasted%20image%2020251213015218.png)


![](../../Imágenes/Pasted%20image%2020251213015303.png)


En éste paso la página que usábamos no reconocía el tipo de encriptado, por lo que lo pasamos a otra página para asegurarnos: https://toolbox.itsec.tamu.edu/

![](../../Imágenes/Pasted%20image%2020251213015333.png)


Al final el texto encriptado no era más que una "trampa" para perder el tiempo

![](../../Imágenes/Pasted%20image%2020251213015445.png)


Ya que no encontramos nada en robots, accedí  al directorio /joomla que me llamó mucho la atención

![](../../Imágenes/Pasted%20image%2020251213020527.png)


Al tener un joomla de por medio no dudé de usar joomscan para hacer un reconocimiento

![](../../Imágenes/Pasted%20image%2020251213021337.png)


![](../../Imágenes/Pasted%20image%2020251213022156.png)


Al haber encontrado directorios que no se pueden acceder si no eres administrador, y otro que no hay nada interesante, procedemos a hacer otro fuzzing, esta vez al directorio de /joomla

```bash
feroxbuster --url http://url -w ruta_diccionario
```

![](../../Imágenes/Pasted%20image%2020251213022546.png)


Vemos de primeras varios directorios: *_nombre_directorio*, en los cuales nos encontramos varios textos codificados sin información interesante

![](../../Imágenes/Pasted%20image%2020251213021150.png)


![](../../Imágenes/Pasted%20image%2020251213021210.png)


![](../../Imágenes/Pasted%20image%2020251213022811.png)



![](../../Imágenes/Pasted%20image%2020251213022759.png)


Entre esos directorios encontramos un /*_test* en el cual tiene una url un tanto sospechosa, de todas formas miramos qué es eso de "sar2html"

![](../../Imágenes/Pasted%20image%2020251213022901.png)


Al buscarlo, la segunda página me sugería un RCE muy simple modificando la url que tanta sospecha nos había levantado

![](../../Imágenes/Pasted%20image%2020251213024135.png)


Probamos a hacer un whoami para ver si nos devuelve el usuario

![](../../Imágenes/Pasted%20image%2020251213024147.png)


Como vemos que nos devuelve el usuario, procedemos a ejecutar una rev shell

![](../../Imágenes/Pasted%20image%2020251213024602.png)


Una vez se haya establecido conexión, podemos ejecutar comandos

![](../../Imágenes/Pasted%20image%2020251213024618.png)


Buscando la flag de usuario me encontré con un log.txt, en el que se encuentra un nuevo usuario con contraseña

![](../../Imágenes/Pasted%20image%2020251213025850.png)


Accedemos por ssh con esas credenciales, en búsqueda de la flag de usuario

![](../../Imágenes/Pasted%20image%2020251213025828.png)

Lo único que encontramos es un script de backup el cual me llamó la atención por si tenía algún dato guardado, o pudieramos sacar alguno.

Encontramos un nuevo usuario con contraseña

![](../../Imágenes/Pasted%20image%2020251213025941.png)


Entramos como ese usuario por ssh

![](../../Imágenes/Pasted%20image%2020251213030325.png)


Buscamos la user flag y la logramos encontrar

![](../../Imágenes/Pasted%20image%2020251213030357.png)


Miramos si tenemos algún tipo de permisos (el que tenemos no vale para nada ya que no existe)

![](../../Imágenes/Pasted%20image%2020251213030516.png)


Busqué los binarios SUID para ver si podía explotar alguno

![](../../Imágenes/Pasted%20image%2020251213031034.png)


Encontré el binario find el cual podía usar para escalar privilegios

![](../../Imágenes/Pasted%20image%2020251213031126.png)

![](../../Imágenes/Pasted%20image%2020251213031135.png)


Una vez escalado privilegios, comprobamos que somos root

![](../../Imágenes/Pasted%20image%2020251213031159.png)


Y vemos la flag

![](../../Imágenes/Pasted%20image%2020251213031505.png)