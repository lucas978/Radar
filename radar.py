#!/usr/bin/env Python
# unicode: utf-8
from graphics import *
from aviao import *
from primitivas import *
import math
from graphics import *

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


    ''' Vinicius - Rotação'''
    x = 50
    y = 0

    pt = Point(x, y)
    pt.setOutline("red")
    pt.draw(win)


    x1 = x*math.cos(math.radians(90)) - y*math.sin(math.radians(90))
    y1 = y*math.cos(math.radians(90)) + x*math.sin(math.radians(90))

    '''
    x2 = x*math.cos(math.radians(180)) - y*math.sin(math.radians(180))
    y2 = y*math.cos(math.radians(180)) + x*math.sin(math.radians(180))


    x3 = x*math.cos(math.radians(270)) - y*math.sin(math.radians(270))
    y3 = y*math.cos(math.radians(270)) + x*math.sin(math.radians(270))

    pt1 = Point(x1, y1)
    pt1.setOutline("yellow")
    pt1.draw(win)

    pt2 = Point(x2, y2)
    pt2.setOutline("pink")
    pt2.draw(win)

    pt3 = Point(x3, y3)
    pt3.setOutline("brown")
    pt3.draw(win)
    
    '''
    reta(0,x,0,y,win,"blue")
    reta(0,x1,0,y1,win,"red")
    
    ''''''

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

