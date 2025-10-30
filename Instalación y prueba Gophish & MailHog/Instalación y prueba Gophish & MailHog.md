

## Instalación Gophish


Descargamos el recurso que sea correspondiente para nuestro S.O en el github oficial de [gophish](https://github.com/gophish/gophish/releases)

![Captura](<img/Pasted image 20251029224349.png>)


Creamos un directorio donde guardar el repo

```bash
mkdir nom_archivo
cd nom_archivo
```


![Captura](<img/Pasted image 20251029224832.png>)


Nos traemos el fichero el fichero al directorio actual

```bash
mv ~/ruta_del_programa/nom_programa
```

![Captura](<img/Pasted image 20251029225246.png>)


Lo extraemos en el directorio actual

```bash
unzip nom_comprimido
```

![Captura](<img/Pasted image 20251029225651.png>)


Una vez descomprimido, iniciaremos ***gophish***

```bash
nom_programa
```


![Captura](<img/Pasted image 20251029230326.png>)


Una vez dentro de la web, nos iremos al apartado ***"Sending Profiles"*** y añadiremos un nuevo profile (aquí aprovecharemos y pondremos el ***[[#Instalación MailHog|MailHog]]***)


## Configuración y prueba Gophish


Nos vamos al apartado de ***Sending Profiles***

![Captura](<img/Pasted image 20251029235528.png>)

Configuramos nuestro ***SMTP***

- **Name**: Nombre que queramos
- **SMTP From**: email de nuestro dominio
- **Host**: nuestro ***SMTP*** alojado


![Captura](<img/Pasted image 20251029235513.png>)



En el apartado ***Landing Pages***


![Captura](<img/Pasted image 20251029235359.png>)

Una vez configurado el ***Sending Profile*** procedemos a crear nuestra página de phishing

![Captura](<img/Pasted image 20251029235411.png>)



Nos vamos al apartado ***Email Templates***

![Captura](<img/Pasted image 20251030001314.png>)


Con la página de phishing creada, continuamos con un mail atractivo para la víctima


![Captura](<img/Pasted image 20251030001330.png>)


Si nos vamos al apartado ***Users & Groups***

![Captura](<img/Pasted image 20251030002231.png>)

Podemos crear grupos con una o varias personas

![Captura](<img/Pasted image 20251030002216.png>)


El apartado de ***Campaigns***

![Captura](<img/Pasted image 20251030002642.png>)

Crearemos la campaña de phising:

- **Name**: Nombre de la campaña
- **Email Template**: Nuestro mail que creamos para el phising
- **Landing Page**: La página del phising
- **URL**: Localización de nuestro GoPhising
- **Sending Profile**: Nuestro SMTP que configuramos
- **Groups**: El grupo con los nombres que creamos


![Captura](<img/Pasted image 20251030002722.png>)


Una vez lanzada la campaña veremos que se ha enviado el mail

![Captura](<img/Pasted image 20251030003502.png>)

En nuestro ***MailHog*** veremos el correo

![Captura](<img/Pasted image 20251030003534.png>)


*Correo falso para redirigir a la página falsa*

![Captura](<img/Pasted image 20251030003550.png>)

*Página falsa para robar credenciales*

![Captura](<img/Pasted image 20251030004739.png>)


*Página oficial que se muestra una vez introduces las credenciales*

![Captura](<img/Pasted image 20251030005045.png>)


Cuando la víctima abra el email, lo clicke o envíe información, se reportará en la campaña

![Captura](<img/Pasted image 20251030010859.png>)


![Captura](<img/Pasted image 20251030010918.png>)



## Instalación MailHog


Deberemos instalarlo

```bash
sudo apt-get -y install golang-go
go install github.com/mailhog/MailHog@latest
```

![Captura](<img/Pasted image 20251029231537.png]]>)

Iniciamos MailHog

```bash
~/go/bin/MailHog
```


![Captura](<img/Pasted image 20251029233922.png>)


Podemos entrar a la interfaz web aunque no la usaremos en este caso


![Captura](<img/Pasted image 20251029234612.png>)


