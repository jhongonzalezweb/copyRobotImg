#!/usr/bin/env python
#_*_coding: utf8_*_

import os
import shutil

os.system("clear")

user = os.environ['USERNAME']
home = "/home/" + user
os.chdir(home)
dst = "/home/marcos/Imágenes/robot_images"
carpetas = os.listdir()
carpetas = [x for x in carpetas if not x.startswith(".")]

extensiones = [".img", ".jpg", ".jpeg", ".png", ".webp"]

def discover():
    file_list = open('file_list','w')
    for carpeta in carpetas:
        ruta = home+'/'+carpeta
        for extension in extensiones:
            for rutabs, directorio, archivo in os.walk(ruta):
                for file in archivo:
                    if file.endswith(extension):
                        os.chdir(rutabs)
                        try:
                            shutil.copy(file, dst)
                        except:
                            pass
                        file_list.write(os.path.join(rutabs, file)+"\n")
    file_list.close()

def main():
    discover()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()