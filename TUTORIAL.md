# Tutorial
1. Cambiar $PORT en la última línea del archivo de Dockerfile por 5220 
1. `$> docker build Dockerfile`
1. Apuntar el id del build que genere cuando lo construya
1. `$> docker run -p 5220:5220 -v .:/opt/webapp 373e724c643e`, donde `373e724c643e` es el id de ejemplo
1. Entrar a localhost:5220