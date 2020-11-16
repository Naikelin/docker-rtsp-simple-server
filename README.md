# Dockerfiles rtsp-simple-server

Este repositorio posee como finalidad el analisis de cliente-servdor para el protocolo RTSP.

Para esto, se ha decidio utilizar el software libre servidor [rtsp-simple-server](https://github.com/aler9/rtsp-simple-server) y cliente [ffmpeg](https://ffmpeg.org/releases).

### Instalación
Para ejecutar los dockerfile, usted necesita instalar [Docker](https://www.docker.com/get-started)
Luego, para iniciar el servidor utilizando la ip 172.17.0.2

```sh
$ cd server
$ docker build -t rtsp:server . && docker run --ip 172.17.0.2 -it rtsp:server
```

Para iniciar el cliente

```sh
$ cd client
$ docker build -t rtsp:client . && docker run -it rtsp:client
```

# Video

A continuación, se muestra cómo utilizar el software utilizado a través de un video, junto con unas pruebas del funcionamiento de protocolo RTSP como patrones de tráfico:

[![Video para tarea2!](https://i.imgur.com/p4qQwsA.png)](https://youtu.be/OyYM2XeqFFI)

Por otro lado, en el siguiente video se muestra el compormamiento del software al someterlo a modificaciones de paquetes del protocolo a través del Software [Polymorph](https://github.com/shramos/polymorph):

[![Video para tarea3!](https://i.imgur.com/jPQpITjh.jpg)](https://youtu.be/-NHELpdSMNs)

[![Video para tarea3!](https://i.imgur.com/qu3caKU.png)](https://youtu.be/uAMGyppT6sg)
