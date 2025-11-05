
### Instalación y configuración Apache


**Instalamos Apache**

```bash
sudo apt install apache2
```


**Iniciamos el servicio Apache**

```bash
systemctl start apache2 ## --> Inicia el servicio de Apache
systemctl status apache2 ## --> Miramos que el servicio se ha levantado
```


**Configuración Virtual Host para login**

```bash
sudo nano /etc/apache2/sites-available/login.n_dominio.com.conf
```

```bash
<VirtualHost *:80>
    ServerName login.n_dominio.com
    DocumentRoot /var/www/login

    <Directory /var/www/login>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/login-error.log
    CustomLog ${APACHE_LOG_DIR}/login-access.log combined
</VirtualHost>
```


**Habilitamos el sitio web virtual y creamos el directorio**


```bash
sudo mkdir -p /var/www/login #--> Creamos el directorio para el login
sudo a2ensite login.tudominio.com.conf #--> Activamos el sitio
```

A continuación se creamos el HTML de la página de  login


Configuramos ***etc/hosts***

```bash
sudo nano /etc/hosts

#Añades tu IP junto con el nombre de tu dominio --> IP     login.n_dominio.com
```

### Instalación y configuración DNS


Instalamos bind9 

```bash
sudo apt install bind9 bind9utils bind9-doc
```


Configuramos zona DNS

```bash
sudo nano /etc/bind/named.conf.local
# Agregas tu zona

zone "n_dominio.com" { type master; file "/etc/bind/zones/db.n_dominio.com"; };
```

**Creamos el archivo de la zona**

```bash
sudo mkdir /etc/bind/zones
```

**Lo editamos**

```bash
sudo nano /etc/bind/zones/db.n_dominio.com

#--------------------------------------
$TTL 604800 @ IN SOA ns1.n_dominio.com. admin.n_dominio.com. ( 3 ; Serial 604800 ; Refresh 86400 ; Retry 2419200 ; Expire 604800 ) ; Negative Cache TTL ; @ IN NS ns1.n_dominio.com. @ IN A TU_IP_SERVIDOR ns1 IN A TU_IP_SERVIDOR login IN A TU_IP_SERVIDOR www IN A TU_IP_SERVIDOR
```

Reiniciamos BIND9

```bash
sudo systemctl restart named #--> named en kali en debian es bind9
```


**Captura Wireshark**

Capturamos nuestra red y ponemos el siguiente filtro para filtrar por el dns: ***dns || http || tls*** y mandamos el login para ver la petición

Para Burpsuite debemos activar el proxy y a continuación deberemos activar el modo captura en ***Burpsuite*** y enviar el login para capturar la petición (podemos llevarlo al *repeater para modificar la petición si queremos*)

