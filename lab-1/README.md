# Laboratorio 1

## Docuemnto
Puede ver el PDF adjunto en [Laboratorio Guiado 1](Laboratorio_guiado.pdf), dentro del repositorio.

## ¿Cómo correrlo?

### Linux
Para crear el ambiente, corremos
```
docker build --rm . -t lab1-image && docker run --rm -ti -v "$(pwd)":/home lab1-image
```
```
sh buildLanguage.sh
```
Para ejecutar los programas de las actividades solo es de reemplazar ``<programa>`` por algún txt dentro de /programms.
```
./calc < <programa>
```

### Windows
Parecido a Linux, es de reemplazar ``<ruta>`` por la ruta en la que se encuentre la carpeta ``lab-1`` y agregar al path "\home" 
```
docker build --rm . -t lab1-image && docker run --rm -ti -v <ruta>\home lab1-image
```
Arreglar el script
```
sh fixBuild.sh
```
```
sh newBuildLanguage.sh
```
Para ejecutar los programas de las actividades solo es de reemplazar ``<programa>`` por algún txt dentro de /programms.
```
./calc < <programa>
```