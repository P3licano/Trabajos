
  
## 1. Preparación del Sistema

  
### Actualizamos el sistema


```bash
sudo apt update && sudo apt upgrade -y
```


### Instalación de las dependencias necesarias


```bash
sudo apt install apt-transport-https curl gnupg2 -y
```


### Importar la clave GPG de Elastic


```bash
curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo gpg --dearmor -o /usr/share/keyrings/elastic-keyring.gpg
```


### Agregar el repositorio de Elastic

```bash
echo "deb [signed-by=/usr/share/keyrings/elastic-keyring.gpg] https://artifacts.elastic.co/packages/8.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-8.x.list
```


### Actualizar la lista de paquetes

```bash
sudo apt update
```



## 2. Instalación de Elasticsearch



### Instalar Elasticsearch

```bash
sudo apt install elasticsearch -y
```


*Durante la instalación, se generará automáticamente una contraseña para el usuario **elastic***

```
--------------------- Security autoconfiguration information ----------------------

Authentication and authorization are enabled.

TLS for the transport and HTTP layers is enabled and configured.

  

The generated password for the elastic built-in superuser is : CONTRASEÑA
```


### Configurar Elasticsearch



Edita el archivo de configuración:

```bash
sudo nano /etc/elasticsearch/elasticsearch.yml
```


Configura los siguientes parámetros *`Descomenta (quita el "#") de TODO lo que modifiques`*:

```yaml
# ---------------------------------- Cluster -----------------------------------
cluster.name: elk-cluster #--> nombre del cluster (identifica tu cluster de Elastic)

# ------------------------------------ Node ------------------------------------
node.name: node-1 #--> nombre del nodo (identifica éste servidor)

# ----------------------------------- Network ----------------------------------
network.host: localhost #--> quién se puede conectar (localhost = el propio servidor. 0.0.0.0 = acepta conexiones de cualquier red)

http.port: 9200 #--> es el puerto por defecto de elastic (se puede dejar por defecto)

# --------------------------------- Discovery ----------------------------------
discovery.type: single-node #--> si solo vamos a tener un nodo (has de añadir todo el parámetro ENTERO sin comentar en el apartado "Discovery")

xpack.security.enabled: true #--> debería de venir con el valor "true" por defecto

xpack.security.enrollment.enabled: true # al igual que el anterior, debería de venir con el valor "true" por defecto
```


### Iniciar y habilitar Elasticsearch

```bash
sudo systemctl daemon-reload

sudo systemctl enable elasticsearch

sudo systemctl start elasticsearch
```


### Verificar estado

```bash
sudo systemctl status elasticsearch
```


### Probar la conexión (espera 30-60 segundos después de iniciar)

```bash
curl --cacert /etc/elasticsearch/certs/http_ca.crt -u elastic:TU_CONTRASEÑA https://localhost:9200
```
  
Si se te olvida o pierdes la contraseña la puedes resetear

```bash
sudo /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic
```



## 3. Instalación de Kibana


### Instalar Kibana

```bash
sudo apt install kibana -y
```


### Generar token de inscripción para Kibana

```bash
sudo /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana
```


**Guarda el token generado para configurar Kibana**.


### Configurar Kibana
  

Edita el archivo de configuración:

```bash
sudo nano /etc/kibana/kibana.yml
```


Configura los siguientes parámetros:

```yaml
server.port: 5601

server.host: "0.0.0.0"

server.name: "kibana-server"

elasticsearch.hosts: ["https://localhost:9200"]
```


### Iniciar y habilitar Kibana

```bash
sudo systemctl daemon-reload

sudo systemctl enable kibana

sudo systemctl start kibana
```


### Verificar el estado

```bash
sudo systemctl status kibana
```


### Configurar Kibana desde el navegador


1. Abre tu navegador y accede a: `http://IP_DE_TU_SERVIDOR:5601`

2. Pega el token de inscripción que generaste anteriormente

3. Obtén el código de verificación con el siguiente comando:

```bash
sudo /usr/share/kibana/bin/kibana-verification-code
```

4. Ingresa el código en la interfaz web

5. Inicia sesión con el usuario `elastic` y la contraseña generada durante la instalación de Elasticsearch



## 4. Instalar Elastic Agent con Fleet Server


### Paso 1 Creamos y configuramos una Agent policy

1. En Kibana, ve a **☰ Menu** → **Management** → **Fleet**

2. Seleccionamos la pestaña **Agent policies**

3. Hacemos click en **Create agent policy**

4. Creamos la policy con el nombre X

5. Clickamos en la policy que acabamos de crear

6. Daremos a la opción **Add integration** y añadiremos **Elastic Defend y System si no lo teníamos previamente**

### Paso 2 Crear Fleet Server desde Kibana

1. En Kibana, ve a **☰ Menu** → **Management** → **Fleet**
2. Si es primera vez, verás el asistente de configuración
3. Click en **Add Fleet Server**

Kibana te mostrará un comando. Cópialo. y pégalo en la consola


## 5. Añadir la Integración de Elastic Defend

  

### Paso 1 integramos la nueva agent policy para Elastic Defend

1. En Kibana, ve a **Management** → **Fleet** → **Agent policies**

2. Click en **Create agent policy**

3. Nombre: `security-policy` por ejemplo

4. Descripción: `Política para agentes de seguridad con Elastic Defend` o lo que quieras



## 6. Configuración para Recopilar Datos de Seguridad del Host


### Verificar que Elastic Defend está activo


1. En Kibana, ve a **Security** →**Manage** → **Endpoints**

2. Deberías ver tu host listado con estado "Healthy"

3. Click en el host para ver detalles


### Configurar políticas de detección (este apartado es opcional porque es de pago pero si tienes el platinum tienes estas opciones)


1. Ve a **Security** → **Manage** → **Policies**

2. Selecciona la política (en este caso el nombre que le hayamos puesto al Defender)

3. Configura las protecciones según tus necesidades:


#### Malware Protection (Elastic Platinum, es de pago)

- **Mode**: Prevent (bloquea amenazas)

- **Notification**: Enabled


#### Ransomware Protection (Elastic Platinum, es de pago)

- **Mode**: Prevent

- **Notification**: Enabled


#### Memory Threat Protection (Elastic Platinum, es de pago)

- **Mode**: Prevent


#### Behavior Protection (Elastic Platinum, es de pago)

- **Mode**: Prevent

- Configura reglas personalizadas si es necesario


### Añadir integraciones adicionales para seguridad


#### System Logs

1. Ve a **Management** → **Integrations**

2. Busca **System**

3. Click en **Add System**

4. Como hemos hecho previamente; nómbralo y ponle una descripción (opcional)

5. Habilita:

   - **Collect logs from System instances**

   - **Collect logs from System instances using Journald**

   - **Collect events from the Windows event log**
  
   - **Collect metrics** (opcional)
  
  6. Asignalo a la agent-policy existente
  
  7. Click en *Save and Continue*


#### Auditd (Auditoría del sistema Linux)

1. Instala auditd en el sistema:

```bash
sudo apt install auditd -y

sudo systemctl enable auditd

sudo systemctl start auditd
```


2. En Kibana, añade la integración **Auditd**:

   - Ve a **Management** → **Integrations**

   - Busca **Auditd**

   - Click en **Add Auditd**

   - Selecciona `security-policy`

   - Configura las rutas de logs


#### Configurar reglas de auditoría personalizadas


Edita `/etc/audit/rules.d/audit.rules`:

```bash
sudo nano /etc/audit/rules.d/audit.rules
```


Añade reglas de ejemplo:

```bash
# Monitorear accesos a archivos sensibles

-w /etc/passwd -p wa -k passwd_changes

-w /etc/shadow -p wa -k shadow_changes

-w /etc/sudoers -p wa -k sudoers_changes

  

# Monitorear comandos ejecutados con sudo

-a always,exit -F arch=b64 -S execve -F euid=0 -k root_commands

  

# Monitorear cambios en la red

-w /etc/network/ -p wa -k network_changes

-w /etc/ssh/sshd_config -p wa -k sshd_config_changes

  

# Monitorear intentos de login

-w /var/log/lastlog -p wa -k logins

-w /var/run/faillock/ -p wa -k logins

  

# Monitorear modificaciones del kernel

-w /etc/sysctl.conf -p wa -k sysctl

-a always,exit -F arch=b64 -S init_module -S delete_module -k modules
```


Reinicia auditd:

```bash
sudo systemctl restart auditd
```



## 7. Visualizar Datos de Seguridad en Kibana


### Dashboard de Security


1. Ve a **Security** → **Dashboards** → **Overview**

2. Aquí verás:

   - Eventos de seguridad en tiempo real

   - Alertas generadas

   - Actividad de red

   - Comportamiento de usuarios y hosts


### Explorar eventos


1. Ve a **Security** → **Events**

2. Filtra por:

   - Tipo de evento

   - Host

   - Usuario

   - Proceso

   - Archivo


### Crear reglas de detección personalizadas


1. Ve a **Security** → **Rules**

2. Click en **Create new rule**

3. Selecciona el tipo de regla:

   - Custom query

   - Machine Learning

   - Threshold

   - Event Correlation

4. Define las condiciones

5. Configura las acciones (alertas, notificaciones)


## 8. Comandos Útiles de Mantenimiento


### Verificar el estado de todos los servicios

```bash
sudo systemctl status elasticsearch

sudo systemctl status kibana

sudo elastic-agent status
```


### Ver logs de Elasticsearch

```bash
sudo journalctl -u elasticsearch -f

sudo tail -f /var/log/elasticsearch/elk-cluster.log
```


### Ver logs de Kibana

```bash
sudo journalctl -u kibana -f

sudo tail -f /var/log/kibana/kibana.log
```


### Ver logs de Elastic Agent

```bash

sudo tail -f /opt/Elastic/Agent/data/elastic-agent-*/logs/elastic-agent-json.log

```

  

### Reiniciar servicios

```bash

sudo systemctl restart elasticsearch

sudo systemctl restart kibana

sudo systemctl restart elastic-agent

```

  

### Verificar conectividad del agente

```bash

sudo elastic-agent status

```

  

### Resetear contraseña del usuario elastic

```bash

sudo /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic

```



## 9. Exposición Segura de Kibana (OPCIONAL - Para acceso remoto)


### Opción 2: Acceso desde Red Local (Sin HTTPS)



```bash
sudo nano /etc/kibana/kibana.yml
```

  

Configura:

```yaml
server.host: "0.0.0.0"  # Permite acceso desde cualquier IP

server.port: 5601
```


Reinicia Kibana:

```bash
sudo systemctl restart kibana
```


**Configura el firewall:**

```bash
# Si usas UFW

sudo ufw allow from 192.168.1.0/24 to any port 5601  # Ajusta tu red

sudo ufw reload

  

# O si usas iptables

sudo iptables -A INPUT -p tcp -s 192.168.1.0/24 --dport 5601 -j ACCEPT
```


Ahora puedes acceder desde cualquier equipo de tu red:

```
http://IP_DEL_SERVIDOR:5601
```


### Verificación de Seguridad


Después de configurar, verifica:


#### 1. Puertos abiertos

```bash
sudo ss -tulpn | grep -E '5601|443|80'
```


#### 2. Conexión SSL

```bash
# Verificar certificado

openssl s_client -connect localhost:5601 -showcerts

  

# O con curl

curl -k https://localhost:5601
```


#### 3. Acceso desde otro equipo

```bash
# Desde otro equipo en la red

curl -k https://IP_DEL_SERVIDOR:5601/api/status
```



## 10. Problemas que me he encontrado instalándolo en Kali


1. Mira que tengas la suficiente RAM en tu equipo (si tienes menos de 8GB)

Si tienes menos de 8GB de RAM:

```bash
sudo nano /etc/elasticsearch/jvm.options.d/heap.options
```

Añade (ajusta según tu RAM):

 **Para 4GB de RAM total:**
-Xms1g
-Xmx1g

 **Para 8GB de RAM total:**
-Xms2g
-Xmx2g

2. Al iniciar el servicio de Elastic salió un error como este:

```bash
The unit elasticsearch.service has entered the 'failed' state with result 'exit-code'.
Oct 12 20:29:52 kali systemd[1]: Failed to start elasticsearch.service - Elasticsearch.
░░ Subject: A start job for unit elasticsearch.service has failed
```

Esto se debe a que en la configuración de `sudo nano /etc/elasticsearch/elasticsearch.yml` no se comentó la línea de `cluster.initial_master_nodes: ["kali"]` ya que en este caso se está usando el modo ***single-node***

3. Al verificar conectividad con curl dió un error

```bash
curl: (77) error setting certificate file: /etc/elasticsearch/certs/http_ca.crt
```

Al revisar la ruta de `/etc/elasticsearch/certs/http_ca.crt` en mi caso fue problemas de permisos por privilegios con un *sudo* se solucionó

4. El token que se genera en Kibana dura unos 30 min. aprox. por lo que si te caduca el token debes de realizar el comando a continuación de nuevo:

```bash
sudo /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana
```

5. Al integrar Elastic Defend arrojó un error el Kibana: `Error Unable to create actions client because the Encrypted Saved Objects plugin is missing encryption key. Please set xpack.encryptedSavedObjects.encryptionKey in the kibana.yml or use the bin/kibana-encryption-keys command.`

Debemos hacer uso de este comando de kibana y copiar el resultado que nos de (es un generador de claves encriptadas)

```bash
sudo /usr/share/kibana/bin/kibana-encryption-keys generate
```

Debemos modificar el fichero

```bash
sudo nano /etc/kibana/kibana.yml
```

Añadiremos lo la clave que nos ha generado

```yml
xpack.encryptedSavedObjects.encryptionKey:clave_generada
xpack.reporting.encryptionKey: clave_generada
xpack.security.encryptionKey: clave_generada
```