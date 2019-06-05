#!/usr/bin/env Python
# unicode: utf-8
from graphics import *
from aviao import *
from primitivas import *
import math

'''
MAIN
Metodo utilizado para criar a janela, setando as coordenadas, cor de fundo e o tamanho da tela
'''
def main():

    try:
        #aviao.reta()
        # Configurando Window
        win = GraphWin("", 1000, 1000)
        win.setCoords(-500, -500, 500, 500)
        win.setBackground(color_rgb(0, 0, 0))
        # Desenhando  linhas e circulos
        desenhar_linhas(win)
        desenhar_circulo(win)



        ''' Vinicius - Rotação'''
        #x = 50
        #y = 0
        '''
        pt = Point(x, y)
        pt.setOutline("red")
        pt.draw(win)


        x1 = x*math.cos(math.radians(90)) - y*math.sin(math.radians(90))
        y1 = y*math.cos(math.radians(90)) + x*math.sin(math.radians(90))

        reta(0,x,0,y,win,"blue")
        reta(0,x1,0,y1,win,"red")
        '''

        #x1 = x * math.cos(math.radians(90)) - y * math.sin(math.radians(90))
        #y1 = y * math.cos(math.radians(90)) + x * math.sin(math.radians(90))
        #triangulo



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
    except:
        print("Fechando Janela")



main()

