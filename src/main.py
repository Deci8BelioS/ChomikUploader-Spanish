#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Author: Adam Grycner (adam_gr [at] gazeta.pl)
#
# Written: 12/11/2011
#
# Released under: GNU GENERAL PUBLIC LICENSE
#
# Ver: 0.4

import uploader   
import sys
import getopt

######################################################################################    
def usage():
    print ('Uso del programa:')
    print ('python', sys.argv[0], '[-h|--help]  [-l|--login nombre_hamster] [-p|--password contrasena hamster] [-r|--recursive directorio_en_chomikuj directorio_en_disco] [-u|--upload directorio_en_home directorio ruta_al_archivo]')
    print ('-h, --help\t\t muestra la ayuda del programa')
    print ('-r, --recursive\t\t envia el contenido del directorio (y todos los subdirectorios) al hamster al directorio especificado. Toda la estructura de subdirectorios se crea en el hamster. Ejemplo:')
    print ('python', sys.argv[0], '-r "/directorio1/directorio2/directorio3" "/home/nick/Documentos"')
    print ('-u, --upload\t\t envia el archivo en el hamster al directorio especificado. Ejemplo:')
    print ('python', sys.argv[0], '-u "/directorio1/directorio2/directorio3" "/home/nick/Documentos/documento1.txt"')
    print ('-l, --login\t\t nombre de usuario/usuario para el hamster')
    print ('-p, --password\t\t Contrasena de hamster. Ejemplo:')
    print ('python', sys.argv[0], '-l nombre_hamster -p contrasena -u "/directorio1/directorio2/directorio3" "/home/nick/Documentos/documento1.txt"')
    print ('-d, --debug\t\t mostrar mas informacion en caso de error del programa')
    print ('-t, --threads\t\t numero de hilos (cuantos archivos se cargan simultaneamente). Ejemplo:')
    print ('python', sys.argv[0], '-t 5 -r "/directorio1/directorio2/directorio3" "/home/nick/Documentos"')
    
#if __name__ == '__main__':
if True:
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hrul:p:dt:', ['help','recursive', 'upload', 'login', 'password','debug', 'threads'])
    except Exception as e:
        print ('Se ha pasado un parametro no valido')
        print (e)
        usage()
        sys.exit(2)
    
    if opts == []:
        usage()
    
    login    = None
    password = None
    threads  = 1
    debug    = False
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        elif opt in ('-l', '--login'):
            login = arg
        elif opt in ('-p', '--password'):
            password = arg
        elif opt in ('-t', '--threads'):
            threads = int(arg)
        elif opt in ('-d', '--debug'):
            debug = True
    try:
        for opt, arg in opts:
            if opt in ('-r', '--recursive'):
                chomik_path, dirpath = args
                u = uploader.Uploader(login, password, debug = debug)
                if threads > 1:
                    u.upload_multi(chomik_path, dirpath, threads)
                else:
                    u.upload_dir(chomik_path, dirpath)
            elif opt in ('-u', '--upload'):
                chomik_path, filepath = args
                u = uploader.Uploader(login, password, debug = debug)
                u.upload_file(chomik_path, filepath)
    except ValueError as e:
        print (e)
        print ("Error: Necesita especificar tanto la ruta en el hamster como en el disco. Ha dejado cualquiera de estas rutas")
