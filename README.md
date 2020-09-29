# Dockerfiles rtsp-simple-server
    
En este trabajo se pide elegir un protocolo a nivel de capa de aplicación, junto a una combinación de software cliente/servidor que haga uso del protocolo en cuestión. De esta manera, se analizará su tráfico y posibles vulnerabilidades existentes.

Para esto, se ha decidio utilizar el software libre servidor [rtsp-simple-server](https://github.com/aler9/rtsp-simple-server) y cliente [ffmpeg](https://ffmpeg.org/releases), utilizando directamente el protocolo RTSP.

### Instalación
Para ejecutar los dockerfile, usted necesita instalar [Docker](https://www.docker.com/get-started)
Luego, para iniciar el servidor utilizando la ip 172.17.0.2

```sh
$ cd server
$ docker build -t rtsp:server . && docker run --ip 172.17.0.2 -it rtsp:server
```

Para iniciar el cliente,

```sh
$ cd client
$ docker build -t rtsp:client . && docker run -it rtsp:client
```

# Video

A continuación, se muestra cómo utilizar el software utilizado a través de un video, junto con unas pruebas del funcionamiento de protocolo RTSP como patrones de tráfico:

[![Video para tarea!](https://imgur.com/p4qQwsA)](https://youtu.be/OyYM2XeqFFI)
