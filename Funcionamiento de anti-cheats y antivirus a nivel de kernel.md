
## Qué hacen y por qué


A nivel de kernel o *kernel-mode* lo que se busca es obtener una visibilidad y control que no se podría alcanzar de una forma fiable desde un *user-mode* o nivel de usuario

### ¿Qué objetivos tiene?

Los objetivos que tienen son:

- **Visibilidad:** Necesitan observar procesos, ficheros, drivers, llamadas al sistema, tráfico de red, memoria, dispositivos...

- **Prevención:** Han de bloquear la ejecución de código malicioso, detener modificaciones que no hayan sido autorizadas, impedir acceso DMA (Direct Access Memory)...

- **Integridad:** Deben comprobar que binarios, drivers y estructuras kernel no hayan sido alterados.

- **Resiliencia:** Tienen que ser robustos frente a manipulaciones por software malicioso y minimizar falsos positivos

Para poder lograr todo esto, es necesario que deban actuar a nivel de kernel debido a que de este modo tienen un mayor privilegio y por ende acceso a eventos que no podría ver si actuara a nivel usuario.

## Incidente 2024 Crowdstrike

### ¿Qué ocurrió?

El 19 de julio de 2024 la empresa de [*Crowdstrike*](https://www.crowdstrike.com/es-es/) lanzó una actualización de **Respuesta Rápida para el sensor Falcon** destinada a los hosts con un sistema operativos Windows (también conocida como la actualización  ***Channel File 291***) el cual su principal propósito era recopilar la telemetría ante nuevas amenazas detectadas por la empresa, lo que acabó provocando pantallas azules o **BSOD** (*Blue Screen of Death*), únicamente entre las horas 04:09 y las 05:27 UTC. Los equipos con sistemas operativos ajenos a Windows como Linux o Mac no se vieron afectados al igual que los equipos que estuvieron desconectados en ese intervalo de tiempo.

#### Puntos a tener en cuenta

- El fallo estuvo en la capa de interpretacion del contenido, es decir, no fue un malware o un exploit.
- Como se ha mencionado previamente, únicamente afectó a equipos Windows ya que afectaba a la funcionalidad específica llamada *named pipes* las cuales son un canal de comnicaciones entre un servidor pipe y uno o más clientes, las *named pipes* se manejan usando la API Win32 con [**funciones**](https://learn.microsoft.com/es-es/windows/win32/ipc/named-pipe-operations)).

### ¿Por qué ocurrió?

- **Pipeline de contenido centralizada:** La empresa de *Crowdstrike* tiene un sistema central el cual compila y publica contenidos como pueden ser plantillas y reglas, la introducción de una nueva plantilla sin una validación completa produjo que se hiciera una permisión y publicación del contenido con una discordancia en el número de entradas esperadas por la plantilla.

- **Falta de controles de validación:** El contenido pasó por unos controles automáticos de validación insuficientes, por ende esta disconformidad no se detecto previamente a ser publicada.

- **Despliegue global sin segmentación:** La falta de segmentación en varias empresas implicaron que se extendiera de forma masiva y esto sumado a un *rollback retardado* provocó que aunque se aplicó dicha reversión muchos hosts ya estaban en BSOD y necesitaron intervención


### Impacto del incidente

Microsoft estimó que un total de **8.5 millones de dispositivos con sistemas Windows** se vieron afectados por el incidente. El gran número de equipos afectados provocó que varias infraestructuras de **aerolíneas, hospitales, organismos públicos y grandes empresas** experimentaron interrupciones operativas, repercutiendo en accione legales contra la empresa *Crowdstrike* por daños operativos. A nivel seguridad generó varias ventanas de riesgo y aumento de intentos de ***phising*** y ***scams*** aprovechando la confusión


### Medidas de mitigación y solución

*Crowdstrike* revirtió el contenido para detener nuevas "infecciones" por la variante de canal, se publicó un parche y acordó mejoras en las validaciones del ***Sensor Content Compiler***, junto con varis pruebas y comprobaciones adicionales de límites y despliegues segmentados. La empresa de ***Microsoft*** y otras empresas cloud trabajaron junto con ***Crowdstrike*** para aislar y restaurar varios Cloud PCs, VMs... CISA (*Cybersecurity & Infraestructure Security Agency*) y autoridades emitieron alertas y guías para su remediación


## Relación incidente con anti-cheats *Kernel mode*

- **Privilegio y fragilidad**: los componentes en kernel manejan estructuras sensibles y llamadas que ante datos mal validados, pueden provocar corrupción de memoria o accesos inválidos. Esto es crítico en antivirus/anti-cheat que colocan lógica de autorización/filtrado en kernel para visibilidad y control en tiempo real. Un error lógico en el parsing de reglas o en parámetros de configuración puede escalar a fallo de sistema.

## Bibliografía

https://terralias.com/que-es-anti-cheat-a-nivel-de-kernel-y-por-que-deberia-importarle/

https://www.crowdstrike.com/wp-content/uploads/2024/07/CrowdStrike-PIR-Executive-Summary_es-ES.pdf

https://time.com/7000925/crowdstrike-microsoft-it-outage-scams-how-to-protect-yourself/?utm_source=chatgpt.com

https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/?utm_source=chatgpt.com

https://www.crowdstrike.com/wp-content/uploads/2024/08/Channel-File-291-Incident-Root-Cause-Analysis-08.06.2024.pdf?utm_source=chatgpt.com

https://www.cisa.gov/news-events/alerts/2024/07/19/widespread-it-outage-due-crowdstrike-update?utm_source=chatgpt.com

https://time.com/7000925/crowdstrike-microsoft-it-outage-scams-how-to-protect-yourself/?utm_source=chatgpt.com

https://www.xatakaon.com/services/kernel-mode-explained-this-is-how-windows-security-operates-and-how-crowdstrike-bypassed-it-to-cause-chaos

https://www.techtarget.com/whatis/feature/Explaining-the-largest-IT-outage-in-history-and-whats-next?utm_source=chatgpt.com