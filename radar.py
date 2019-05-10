#!/usr/bin/env Python
# unicode: utf-8
from graphics import *
from time import sleep

#from aviao import aviao#nome da classe


def ponto(x, y, color, win):
    pt = Point(x, y)
    pt.setOutline(color)
    pt.draw(win)


# reta octeto bressham
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


def plotagem_circulo(x, y, color, win):
    ponto(x, y, color, win)
    ponto(y, x, color, win)
    ponto(y, -x, color, win)
    ponto(-x, y, color, win)
    ponto(-x, -y, color, win)
    ponto(-y, -x, color, win)
    ponto(-y, x, color, win)
    ponto(x, -y, color, win)


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


def aviao(win):
    # Criar outro metodo de Ponto() para passar parametros
    # P/ os pontos se moverem!!!
    # 9
    ponto(300, 301, "red", win)
    ponto(300, 302, "red", win)
    ponto(300, 303, "red", win)
    ponto(300, 304, "red", win)
    ponto(300, 305, "red", win)
    ponto(300, 306, "red", win)
    ponto(300, 307, "red", win)
    ponto(300, 308, "red", win)
    ponto(300, 309, "red", win)
    # 7
    ponto(301, 302, "red", win)
    ponto(301, 303, "red", win)
    ponto(301, 304, "red", win)
    ponto(301, 305, "red", win)
    ponto(301, 306, "red", win)
    ponto(301, 307, "red", win)
    ponto(301, 308, "red", win)
    # 5
    ponto(302, 303, "red", win)
    ponto(302, 304, "red", win)
    ponto(302, 305, "red", win)
    ponto(302, 306, "red", win)
    ponto(302, 307, "red", win)
    # 3
    ponto(303, 304, "red", win)
    ponto(303, 305, "red", win)
    ponto(303, 306, "red", win)
    # 1
    ponto(304, 305, "red", win)
    # 1
    ponto(304, 305, "red", win)
    # 1
    ponto(304, 305, "red", win)
    ponto(304, 305, "red", win)
    ponto(304, 305, "red", win)
    ponto(304, 305, "red", win)
    ponto(304, 305, "red", win)
    ponto(304, 305, "red", win)
    ponto(304, 305, "red", win)
    ponto(304, 305, "red", win)
    ponto(304, 305, "red", win)


def animacao(win):
    points = []
    # padrao  x -> [-1, 1]
    # padrao  y -> [-1, 1]
    # padrao desce!
    # se inverter o padrao, a bolinha sobe na direcao oposta
    for x in [-5, 5]:
        for y in [-5, 5]:
            pt = Point(250, 250)
            pt.draw(win)
            pt.setOutline("red")
            points.append(pt)

    for _ in range(250):
        for pt in points:
            pt.move(x, y)
            sleep(0.025)


'''
def move(win):
# PODE SER USADA PARA O PREENCHIMENTO!!
# ta funcionando a animacao, no entanto,  ele vai deixando um rasto
# o rastro que ele deixa deve ser apagado!!!
	x = 250
	y = 250
	for _ in range(250):
		# o ponto se movimenta, porem, o ponto "apagado" tem que
		# ser da mesma cor que o fundo da tela!!!!!
		win.plot(x,y,"white")
		x += 1
		y += 1
		win.plot(x, y, "blue")
		sleep(0.025)	
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


def desenhar_circulo(win):
    circulo(0, 450, 449, color_rgb(0, 128, 0), win)
    circulo(0, 50, 49, color_rgb(0, 128, 0), win)
    circulo(0, 200, 199, color_rgb(0, 128, 0), win)
    circulo(0, 330, 329, color_rgb(0, 128, 0), win)

def main():
    #aviao.reta()
    # Configurando Window
    win = GraphWin("", 1000, 1000)
    win.setCoords(-500, -500, 500, 500)
    win.setBackground(color_rgb(0, 0, 0))
    # Desenhando  linhas e circulos
    desenhar_linhas(win)
    desenhar_circulo(win)
    # Aviao
    aviao(win)
    aviao(win)
    # Fechando Janela/Radar
    win.getMouse()
    win.close()


main()

