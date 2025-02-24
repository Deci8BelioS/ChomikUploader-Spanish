# Script de Chomik

Este es un script traducido al Español por `DeciBelioS` que te permite enviar archivos y directorios a Chomikuj, un servicio de alojamiento de archivos en línea. A continuación, se proporcionan instrucciones para la instalación y ejemplos de uso.

## Instalación

Antes de utilizar el script, debes asegurarte de tener Python 2.7 instalado en tu sistema. Si estás utilizando Ubuntu o Debian, puedes actualizar los repositorios e instalar Python 2.7 ejecutando los siguientes comandos en tu terminal:

```bash
sudo apt update && sudo apt install python2.7 -y
```

Una vez que tienes Python 2.7 instalado, puedes proceder a instalar el script. Ejecuta el siguiente comando con privilegios de administrador (debes de estar en el directorio ChomikUploader-Spanish):

```bash
sudo python2.7 setup.py install
```

Si no tienes derechos de administrador, aún puedes utilizar el programa sin necesidad de instalarlo. Simplemente ejecuta `main.py` desde el directorio "src".

En Windows, no es necesario instalar el script. En su lugar, en el directorio "src", puedes ejecutar el siguiente comando:

```bash
python main.py
```

## Ejemplo de uso

A continuación se presentan algunos ejemplos de cómo utilizar el script:

1. Para obtener ayuda sobre los comandos disponibles, ejecuta:

```bash
chomik -h
```

2. Para enviar todos los archivos de un directorio y sus subdirectorios al directorio de Chomikuj, utiliza el siguiente comando:

```bash
chomik -r "/directorio_en_chomik/subdirectorio" "ruta_al_directorio_en_disco"
```

Por ejemplo:

```bash
chomik -r "/directorio1/directorio2/directorio3" "/home/nick/Documentos"
```

3. Para cargar un único archivo en Chomikuj, utiliza el siguiente comando:

```bash
chomik -u "/directorio1/directorio2/directorio3" "/home/nick/Documentos/archivo.txt"
```

A continuación, se te solicitará que ingreses tu nombre de usuario y contraseña.

## Añadir el usuario y contraseña o archivos simultaneos en el comando chomik

5. Puedes añadir directamente el usuario y contraseña usando `-l` y `-p`
```bash
chomik -l usuario_chomikuj -p contraseña_chomikuj -r "/directorio1/directorio2/directorio3" "/home/nick/Documentos"
```

6. Para enviar varios archivos al mismo tiempo (por ejemplo, 4 archivos simultáneamente), utiliza la opción `-t` seguida del número de archivos que deseas enviar:

```bash
chomik -t 4 -l usuario_chomikuj -p contraseña_chomikuj -r "/directorio1/directorio2/directorio3" "/home/nick/Documentos"
```

7. Si deseas obtener información detallada sobre los errores, utiliza la opción `-d`:

```bash
chomik -d -l usuario_chomikuj -p contraseña_chomikuj -r "/directorio1/directorio2/directorio3" "/home/nick/Documentos"
```

## Ejecutar comando chomik en segundo plano y así poder cerrar la terminal o la sesión por SSH al servidor linux (o raspberry)

```bash
sudo nohup chomik -t 2 -l usuario_chomikuj -p contraseña_chomikuj -r "/directorio1/directorio2/directorio3" "/home/nick/Documentos" >/dev/null 2>&1 &
```

## Notas

- Cuando se envía un directorio (`-r`), el script crea los archivos `subido.txt` y `nosubido.txt` en el directorio donde estas ejecutando el comando chomik, por lo tanto se recomienda ejecutar el comando en el directorio predeterminado donde iniciemos sesión por SSH dado que si ejecutamos el comando en otro directorio no leera los `.txt` y sin eso no sabe que es lo que ha subido y volverá a subir lo que posiblemente esté ya subido.
- `subido.txt` contiene la lista de archivos que se han subido exitosamente. Si ya existe un archivo `subido.txt` en el directorio, el programa leerá este archivo para determinar qué archivos ya han sido subidos y los omitirá durante el proceso de carga.
- `nosubido.txt` contiene la lista de archivos que no se han podido subir debido a errores.
- Las subidas de archivos tardan un rato en arrancar.
