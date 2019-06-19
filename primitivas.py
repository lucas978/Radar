#!/usr/bin/env Python
# -*- coding: utf-8 -*-
from graphics import *
import math

'''
Nome: Ponto 
Função: O método irá desenhar um ponto de uma determinada cor na tela.
x: Posição X do Ponto
y: Posição Y do Ponto
color: Cor do Ponto
win: Janela(Radar) passada para o metodo desenhar nela(win).
'''
def ponto(x, y, color, win):
    pt = Point(x, y) # Definir Ponto com as coordenadas passadas
    pt.setOutline(color) # Definir Cor do Ponto com o parametro passado
    pt.draw(win) # Metodo para desenhar o ponto na tela passada!


'''
RETA
Função: Desenhar uma reta nos 8 octetos utilizando o algortimo de Bresshan
x1: Coordenada X do ponto inicial
x2: Coordenada X do ponto final
y1: Coordenada Y do ponto Inicial
y2: Coordenada Y do ponto final
window: Janela passada como parametro para desenhar a reta nela(window)
cor: Cor utilizada!
'''
def reta(x1, x2, y1, y2, window, cor):
    x = x1
    y = y1
    c = 1
    m = 1
    p = 0
    d_x = x2 - x1
    d_y = y2 - y1
    incx = 1
    incy = 1
    if d_x < 0:
        incx = -1
        d_x = - d_x
    if d_y < 0:
        incy = -1
        d_y = - d_y
    if d_y <= d_x:
        p = d_x / 2
        while x != x2:
            pt = Point(x, y)
            pt.setOutline(cor)
            pt.draw(window)
            p = p - d_y
            if p < 0:
                y = y + incy
                p = p + d_x
            x = x + incx
    else:
        p = d_y / 2
        while y != y2:
            pt = Point(x, y)
            pt.setOutline(cor)
            pt.draw(window)
            p = p - d_x
            if p < 0:
                x = x + incx
                p = p + d_y
            y = y + incy
        pt = Point(x, y)
        pt.setOutline(cor)
        pt.draw(window)

'''
PLOTAGEM CIRCULO 
Função: Metodo utilizado para desenhar o circulo utilizando pontos
x: coordenada para desenhar o ponto
y: coordenada para desenhar o ponto
'''
def plotagem_circulo(x, y, color, win):
    ponto(x, y, color, win)
    ponto(y, x, color, win)
    ponto(y, -x, color, win)
    ponto(-x, y, color, win)
    ponto(-x, -y, color, win)
    ponto(-y, -x, color, win)
    ponto(-y, x, color, win)
    ponto(x, -y, color, win)

'''
CIRCULO
Função: Algortimo utilizado para desenhar o circulo
x: Coordenada x para desenhar no ponto
y: Coordenada y para desenhar no ponto
p: Variavel utilizado para definir a curvatura
cor
win: janela utilizada para desenhar o circulo
'''
def circulo(x, y, p, color, win):
    plotagem_circulo(x, y, color, win)
    while x < y:
        x = x + 1
        if p < 0:
            p = p + (2 * x) + 1
        else:
            y = y - 1
            p = p + (2 * x) + 1 - (2 * y)
        plotagem_circulo(x, y, color, win)

'''
TRIANGULO ISCOSCELES
Função: Desenhar o formato do avião na tela
x: Coordenada utilizada para desenhar o avião utilizando o metodo de RETA
y: Coordenada utilizada para desenhar o avião utilizando o metodo de RETA
'''
def triangulo_isosceles(x,y,cor,win):
    # Aviao sera desenhado direcionado à direita
    reta(x, x-10, y, y+10, win, cor)
    reta(x, x-10, y, y-10, win, cor)
    reta(x-10, x-10, y+10, y-10, win, cor)


  

def aviao(aviao_lista, linha, win):
    # aviao_lista: Lista das informacoes do aviao que serão passadas para plotagem
    # Linha: Linha utilizada para resgatar valores do aviao em um determinado tempo
    F = 20000
    f = 50

    tempo = aviao_lista[linha][0]
    status = aviao_lista[linha][1]
    voo = aviao_lista[linha][2]
    distancia = aviao_lista[linha][3]
    velocidade = aviao_lista[linha][4]
    x = math.trunc(aviao_lista[linha][5])
    y = math.trunc(aviao_lista[linha][6])
    z = math.trunc(aviao_lista[linha][7])

    x_p = x * f / (F - z)
    y_p = y * f / (F - z)
    
    x_p = math.trunc(x_p)
    y_p = math.trunc(y_p)

    print("X Plano Projetivo: ",x_p)
    print("Y Plano Projetivo: ",y_p)

    if status == "D":
        print("Tempo: {0}\nStatus: {1}\nVoo: {2}\nDist: {3}\nVel: {4}\nX: {5}\nY: {6}\nZ: {7}\n\n".format(tempo,status,voo,distancia,velocidade,x,y,z))
        print("============================================================")
        triangulo_isosceles(x_p,y_p,"green2",win)
        texto = Text(Point(x_p,y_p+50),  "{0}\nDist: {1}\nVel: {2}\nX: {3}\nY: {4}\nZ: {5}\n".format(voo,distancia,velocidade,x_p,y_p,z))
        texto.setSize(7)
        texto.setTextColor("green2")
        texto.draw(win)
    if status == "P":
        print("Tempo: {0}\nStatus: {1}\nVoo: {2}\nDist: {3}\nVel: {4}\nX: {5}\nY: {6}\nZ: {7}\n\n".format(tempo,status,voo,distancia,velocidade,x,y,z))
        print("============================================================")
        triangulo_isosceles(x_p,y_p,"yellow",win)
        texto = Text(Point(x_p,y_p+50),  "{0}\nDist: {1}\nVel: {2}\nX: {3}\nY: {4}\nZ: {5}\n".format(voo,distancia,velocidade,x_p,y_p,z))
        texto.setSize(7)
        texto.setTextColor("yellow")
        texto.draw(win)

    if status == "P" and linha == 0:
        print("Tempo: {0}\nStatus: {1}\nVoo: {2}\nDist: {3}\nVel: {4}\nX: {5}\nY: {6}\nZ: {7}\n\n".format(tempo,status,voo,distancia,velocidade,x,y,z))
        print("============================================================")
        triangulo_isosceles(x_p,y_p,"snow",win)
        texto = Text(Point(x_p,y_p+50),  "{0}\nDist: {1}\nVel: {2}\nX: {3}\nY: {4}\nZ: {5}\n".format(voo,distancia,velocidade,x_p,y_p,z))
        texto.setSize(7)
        texto.setTextColor("snow")
        texto.draw(win)

    if status == "P" and linha == 1:
        print("Tempo: {0}\nStatus: {1}\nVoo: {2}\nDist: {3}\nVel: {4}\nX: {5}\nY: {6}\nZ: {7}\n\n".format(tempo,status,voo,distancia,velocidade,x,y,z))
        print("============================================================")
        triangulo_isosceles(x_p,y_p,"snow",win)
        texto = Text(Point(x_p,y_p+50),  "{0}\nDist: {1}\nVel: {2}\nX: {3}\nY: {4}\nZ: {5}\n".format(voo,distancia,velocidade,x_p,y_p,z))
        texto.setSize(7)
        texto.setTextColor("snow")
        texto.draw(win)

    if status == "D" and linha == 13 and voo == "LA 2203":
        print("Tempo: {0}\nStatus: {1}\nVoo: {2}\nDist: {3}\nVel: {4}\nX: {5}\nY: {6}\nZ: {7}\n\n".format(tempo,status,voo,distancia,velocidade,x,y,z))
        print("============================================================")
        triangulo_isosceles(x_p,y_p,"snow",win)
        texto = Text(Point(x_p,y_p+50),  "{0}\nDist: {1}\nVel: {2}\nX: {3}\nY: {4}\nZ: {5}\n".format(voo,distancia,velocidade,x_p,y_p,z))
        texto.setSize(7)
        texto.setTextColor("snow")
        texto.draw(win)

    if status == "D" and linha == 14:
        print("Tempo: {0}\nStatus: {1}\nVoo: {2}\nDist: {3}\nVel: {4}\nX: {5}\nY: {6}\nZ: {7}\n\n".format(tempo,status,voo,distancia,velocidade,x,y,z))
        print("============================================================")
        triangulo_isosceles(x_p,y_p,"snow",win)
        texto = Text(Point(x_p,y_p+50),  "{0}\nDist: {1}\nVel: {2}\nX: {3}\nY: {4}\nZ: {5}\n".format(voo,distancia,velocidade,x_p,y_p,z))
        texto.setSize(7)
        texto.setTextColor("snow")
        texto.draw(win)

    if status == "D" and linha == 15:
        print("Tempo: {0}\nStatus: {1}\nVoo: {2}\nDist: {3}\nVel: {4}\nX: {5}\nY: {6}\nZ: {7}\n\n".format(tempo,status,voo,distancia,velocidade,x,y,z))
        print("============================================================")
        triangulo_isosceles(x_p,y_p,"snow",win)
        texto = Text(Point(x_p,y_p+50),  "{0}\nDist: {1}\nVel: {2}\nX: {3}\nY: {4}\nZ: {5}\n".format(voo,distancia,velocidade,x_p,y_p,z))
        texto.setSize(7)
        texto.setTextColor("snow")
        texto.draw(win)

   
'''
    DESENHAR LINHAS
    Função: Metodo utilizado para Desenhar as Linhas para formar o Radar utilizando o metodo RETA
'''

def desenhar_linhas(win):
    # vertical
    reta(0, 0, -500, 500, win, "green")
    # horizontal
    reta(-500, 500, 0, 0, win, "green")
    # diagonal(esquerda | direita)
    reta(-500, 500, -500, 500, win, "green")
    # diagonal(direita | esquerda)
    reta(500, -500, -500, 500, win, "green")
    # pista de voo
    #reta(-50,50,-25,25,win,"red")
    #Pista
    #reta(-50, 50, -20, 20, win, "white")


'''
DESENHAR CIRCULO
Função: Metodo utilizado para desenhar os circulos na tela e formar o Radar utilizando o metodo CIRCULO e PLOTAGEM CIRCULO
'''
def desenhar_circulo(win):
    circulo(0, 450, 449, color_rgb(0, 128, 0), win)
    circulo(0, 100, 99, color_rgb(0, 128, 0), win)
    circulo(0, 200, 199, color_rgb(0, 128, 0), win)
    circulo(0, 330, 329, color_rgb(0, 128, 0), win)
