#!/usr/bin/env Python
# *- coding: utf-8 -*-
from graphics import *
from aviao import *
from primitivas import *
import math

''' Masashi: Rotação Metodo!

def rotacao(ang,win):
    if ang == 0:
        pt = Point(100,0)
        pt.setOutline("red")
        pt.draw(win)
        triangulo_isosceles(100,0,"red",win)
    elif ang == 45:
        pt = Point(70,70)
        pt.setOutline("red")
        pt.draw(win)
        triangulo_isosceles(70,70,"green",win)
    elif ang == 90:
        pt = Point(0,100)
        pt.setOutline("red")
        pt.draw(win)
        triangulo_isosceles(0,100,"green",win)
    elif ang ==135:
        pt = Point(-71,70)
        pt.setOutline("red")
        pt.draw(win)
        triangulo_isosceles(-71,70,"green",win)
    elif ang == 180:
        pt = Point(-100,0)
        pt.setOutline("red")
        pt.draw(win)
        triangulo_isosceles(-100,0,"green",win)
    elif ang == 225:
        pt = Point(-71,-71)
        pt.setOutline("red")
        pt.draw(win)
        triangulo_isosceles(-71,-71,"green",win)
    elif ang == 270:
        pt = Point(-1,-100)
        pt.setOutline("red")
        pt.draw(win)
        triangulo_isosceles(-1,-100,"green",win)
    elif ang == 315:
        pt = Point(70,-71)
        pt.setOutline("red")
        pt.draw(win)
        triangulo_isosceles(70,-71,"green",win)
'''
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
        
        '''
        * Masashi: Rotação
        rotacao(0,win)
        rotacao(45,win)
        rotacao(90, win)
        rotacao(135, win)
        rotacao(180, win)
        rotacao(225, win)
        rotacao(270, win)
        rotacao(315, win)
        '''


        ''' Vinicius - Rotação

        x = 50
        y = 0
        #x = 50
        #y = 0
        '''
        '''

        #x1 = x*math.cos(math.radians(90)) - y*math.sin(math.radians(90))
        #y1 = y*math.cos(math.radians(90)) + x*math.sin(math.radians(90))



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

