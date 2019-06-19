#!/usr/bin/env Python
# *- coding: utf-8 -*-
from graphics import *
from primitivas import *
import math
from planilha import *
from time import *


def tela(win):
    desenhar_linhas(win)
    desenhar_circulo(win)




def main():
    win = GraphWin("", 1000, 1000)
    win.setCoords(-500, -500, 500, 500)
    win.setBackground(color_rgb(0, 0, 0))
    # Desenhando  linhas e circulos
    tela(win)
    
    # Ler dados da planilha
    
    la2203 = getLA2203()
    gz0331 = getGZ0331()
    az0032 = getAZ0032()
    az0157 = getAZ0157()
    gz0667 = getGZ0667()

    for linha in range(0,len(la2203)):
        aviao(la2203,linha,win)
        aviao(gz0331,linha,win)
        aviao(az0032,linha,win)
        aviao(az0157,linha,win)
        aviao(gz0667,linha,win)
        sleep(2)
        win.close()
        if win.isClosed():
            win = GraphWin("", 1000, 1000)
            win.setCoords(-500, -500, 500, 500)
            win.setBackground(color_rgb(0, 0, 0))
            tela(win)


    win.getMouse()
    win.close()
    # Fechando Janela/Radar


main()

