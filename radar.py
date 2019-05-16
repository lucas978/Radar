#!/usr/bin/env Python
# unicode: utf-8
from graphics import *
from aviao import *
from primitivas import *


def main():

    #aviao.reta()
    # Configurando Window
    win = GraphWin("", 1000, 1000)
    win.setCoords(-500, -500, 500, 500)
    win.setBackground(color_rgb(0, 0, 0))
    # Desenhando  linhas e circulos
    desenhar_linhas(win)
    desenhar_circulo(win)

    #Vinicius - chamadas dos aviões

    #Vinicius - Teste para mover o avião. Favor não mexer.
    #Masashi - Mover o win.getMouse(), win.close() para depois deste método!

    '''
    v = True
    for i in range(0, 100):
        triangulo_isosceles(10+i, 100, "blue", win)
        if v:
            triangulo_isosceles(10 + i, 100, "black", win)
            v = False
        else:
            triangulo_isosceles(10 + i, 100, "black", win)
        time.sleep(0.0000000000000000001)
    '''

    #triangulo_isosceles(100, 200, "blue", win)
    #triangulo_isosceles(400, 300, "blue", win)
    #triangulo_isosceles(300, 250, "blue", win)
    win.getMouse()
    win.close()
    # Fechando Janela/Radar




main()

