# buscador.pyw - Este programa esta destinado a la busqueda de X contenido que desee el usuario en X carpeta
#                la direccion de la X carpeta estara guardada en el portapapeles
#
#          python buscador.pyw <PALABRA>

import os, sys, pyperclip


#TODO: BUSQUEDA DE LA X PALABRA

def busqueda(arg):
    for i in os.listdir():
        if i[-3:] == 'txt':
            with open(i) as myfile:
                for num, line in enumerate(myfile, 1):
                    if arg in line:
                        print('Termino "', arg, '" encontrado en la linea:', num)
                        print('Del fichero:', i)

#TODO: INICIO DEL PROGRAMA
try:
    ruta = pyperclip.paste()  #   C:\Users\JoeyRatt\Desktop\Nueva carpeta
    os.chdir(os.path.join(ruta))
    print('\nRuta utilizada:', ruta,'\n')
    print('--------------------------------------------------------------')
    busqueda(sys.argv[1])
except:
    print('La ruta que has copiado [',ruta,'] no es valida')
    sys.exit(0)