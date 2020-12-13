#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Autor: Alexandre Varela Sixto
# Apodo: ||ShellDredd||
# Dato inservible: Hago pizzas artesanas en base 64.
# Licencia de este código: GPL.V3 (Para más información visite el archivo adjunto LICENSE.)
#            _  _
#           (.)(.)
#          /  ()  \
#        _ \ '--' / _
#       { '-`""""`-' }
#        `"/      \"`
#          \      /
#         _/  /\  \_
#        {   /  \   }
#         `"`    `"`
#Importación de Liberías y requerimientos:
import requests
from bs4 import BeautifulSoup
import subprocess
from subprocess import call
from tkinter import *
from tkinter import ttk
import tkinter as tk
import time

#Definición de paleta de colores:
cs_color='\033[0;m'
def charizar(skk): print("\x1b[1;91m {}\033[01m" .format(skk) + cs_color)
def bulbasur(skk): print("\x1b[1;32m {}\033[01m" .format(skk) + cs_color)
verde="\x1b[1;32m"
rojo="\x1b[1;91m"
moradito="\x1b[1;35m"

#Cabecera cargando:
print (moradito + "\/\/\/\/" + verde + "···· Cargando ····" + moradito + "\/\/\/\/\/\/")
time.sleep(1)
print (moradito + "  \/\/\/\/" + verde + "··············" + moradito + "\/\/\/\/\/\/")
time.sleep(0.5)
print (moradito + "    \/\/\/\/\/" + verde + "·······" + moradito + "\/\/\/\/\/\/\/")

#Instalación requerimientos y librerias:
call("apt install -y python3-pip apt-get && install python3-tk && pip3 install requests && pip3 install beautifulsoup4 && pip3 install pandas", shell=True)
call("clear")

#Cabecera Iniciando:
print (moradito + "\/\/\/\/" + verde + "···· Iniciando ····" + moradito + "\/\/\/\/\/\/")
time.sleep(1)
print (moradito + "  \/\/\/\/" + verde + "··············" + moradito + "\/\/\/\/\/\/\/")
time.sleep(0.5)
print (moradito + "    \/\/\/\/\/" + verde + "·······" + moradito + "\/\/\/\/\/\/\/\/")

#Variables del programa:
url_inicio = 'https://www.vulnhub.com'
page = requests.get(url_inicio)
soup = BeautifulSoup(page.content, 'html.parser', on_duplicate_attribute='delete')
time = subprocess.check_output(['date'])

# |Inicio Programa|

#Cabecera:
print("")
charizar ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
charizar ('| ~ShellDredd Society~                      |')
charizar ('|  #Lista actualizada de máquinas de VulHub.|')
charizar ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#Funciones:
print ('')
print (moradito + 'Hora y fecha de la lista: ' + cs_color + verde + str(time).split("b'")[-1].rsplit("n'")[0], sep="")
print ('')

for link in soup.find_all(class_ = 'card-title'):
    print (rojo + '          ~' + cs_color, *link.get_text('').strip(), sep = "")
    pass

print ('')
print ('')
charizar ('<<<< ·Software Libre· >>>>          <<<< ·Happy Hacking· >>>>')

#Ventana gráfica:
root = Tk()
root.title("✰ ShellDredd Society ✰")
root.geometry("600x300+300+250")
root.resizable(width=False, height=False)
root.config(bg='black')

#Textos y botones:
boton_general=Frame(root)
boton_general.pack(fill=BOTH, expand=YES)
boton_general.place(x=0, y=20)
Button(boton_general, highlightbackground="black", command=lambda:[],
         width=20, height=5, text="ShellDredd te desea\n¡Happy Hacking!\n✾", foreground='green', activeforeground='darkgreen',
          cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black",
           activebackground="black", font=("URW Chancery L", 25)).pack()

boton_cerrar=Frame(root)
boton_cerrar.pack(fill=BOTH, expand=YES)
boton_cerrar.place(x=390, y=25)
Button(boton_cerrar, highlightbackground="black", command=lambda:[exit()],
         width=2, height=1, text="➟", foreground='darkred', activeforeground='orange',
          cursor="fleur", justify="center", bd=0,  relief="raised", overrelief="sunken", background="black",
           activebackground="black", font=("URW Chancery L", 90)).pack()


root.mainloop()

#FIN...

