#!/usr/bin/env Python
# *- coding: utf-8 -*-
from graphics import *
from aviao import *
from primitivas import *
import math
#from planilha import *
from time import *

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
def direita(ponto, win):
    #pt = Point(x,y)
    pt = Point(ponto.getX(), ponto.getY())
    pt.setOutline("black")
    pt.draw(win)
        
    for x in [0,1]:
        for y in [0,0]:
            #pt = Point(50,50)
            #pt.draw(win)
            pt.setOutline("red")

        
        for _ in range(250):
            #x += 1
            #y += 0
            pt.move(x, y)
            sleep(0.025)

    pt.setOutline("black")
    return (pt)

def cima(ponto, win):

    #pt = Point(x,y)
    pt = Point(ponto.getX(), ponto.getY())
    pt.setOutline("black")
    pt.draw(win)
        
    for x in [0,0]:
        for y in [0,1]:
            #pt = Point(50,50)
            #pt.draw(win)
            pt.setOutline("red")

        
        for _ in range(250):
            #x += 1
            #y += 0
            pt.move(x, y)
            sleep(0.025)

    return (pt)

def aviao(x,y,cor,win):
    reta(x, x-10, y, y+10, win, cor)
    reta(x, x-10, y, y-10, win, cor)
    reta(x-10, x-10, y+10, y-10, win, cor)

    '''
    reta(x1, x2, y1, y2, win, cor)
    reta(x1, x3, y1, y3, win, cor)
    reta(x2, x3, y2, y3, win, cor)

    '''
def tela(win):
    desenhar_linhas(win)
    desenhar_circulo(win)


def main():

    try:
        win = GraphWin("", 1000, 1000)
        win.setCoords(-500, -500, 500, 500)
        win.setBackground(color_rgb(0, 0, 0))
        # Desenhando  linhas e circulos
        tela(win)

        ''' 
        Mostrar informação acima do avião
        x = -200
        y = 200
        angulo = 45
        txt = Text(Point(x,y+20), "TESTE")
        txt.setSize(5)
        txt.setTextColor("red")
        txt.draw(win)
        aviao(x,y,"red",win)
        '''


        '''   
        # PLOTAGEM DO AVIAO
        a = 0
        x = -200
        y = 200
        while a <=10:    
            aviao(x,y,"red",win)
            x+=70
            y+=0
            a+=1
            sleep(2)
            win.close()
            if win.isClosed():
                win = GraphWin("", 1000, 1000)
                win.setCoords(-500, -500, 500, 500)
                win.setBackground(color_rgb(0, 0, 0))
                # Desenhando  linhas e circulos
                tela(win)        
        '''
        # FIM DA PLOTAGEM 


        win.getMouse()
        win.close()
        # Fechando Janela/Radar
    except:
        print("Fechando Janela")



main()

