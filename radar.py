#!/usr/bin/env Python
# unicode: utf-8
from graphics import *
from time import sleep


def ponto(x,y,z=0,color="black"):
	pt = Point(x,y)
	pt.setFill(color)


# reta octeto bressham
def reta(x1,x2,y1,y2,window,cor):
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
		d_x =  - d_x
	if d_y < 0:
		incy = -1
		d_y = - d_y
	if d_y <= d_x:
		p = d_x / 2
		while x != x2:
			pt = Point(x,y)
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
			pt = Point(x,y)
			pt.setOutline(cor)
			pt.draw(window)
			p = p - d_x
			if p < 0:
				x = x + incx
				p = p + d_y
			y = y + incy
		pt = Point(x,y)
		pt.setOutline(cor)
		pt.draw(window)



def plotagem_circulo(x, y, color):
  ponto(x, y, color)
  ponto(y, x, color)
  ponto(y, -x, color)
  ponto(-x, y, color)
  ponto(-x, -y, color)
  ponto(-y, -x, color)
  ponto(-y, x, color)
  ponto(x, -y, color)

def circulo(x, y, p, color):
   plotagem_circulo(x, y, color)
   while x < y:
       x = x + 1
       if p < 0:
           p = p + (2 * x) + 1
       else:
           y = y - 1
           p = p + (2 * x) + 1 - (2 * y)
       plotagem_circulo(x, y, color)


def aviao(x,x2,x3,y,y2,y3,win,cor):
	#reta OA
	reta(x,x2,y,y2,win,cor)
	#reta AB
	reta(x2,x3,y2,y3,win,cor)
	#reta BO
	reta(x3,x,y3,y,win,cor)



def animacao(win):
	points = []
	# padrao  x -> [-1, 1]
	# padrao  y -> [-1, 1]
	# padrao desce!
	# se inverter o padrao, a bolinha sobe na direcao oposta
	for x in [-5, 5]:
    		for y in [-5, 5]:
        		pt = Point(250,250)
			pt.draw(win)
			pt.setOutline("red")
			points.append(pt)		

	for _ in range(250):
    		for pt in points:
        		pt.move(x,y)
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

def cruz(win):
	reta(500,500,0,1000,win,"green")
        reta(0,1000,500,500,win,"green")



def main():
	# Configurando Window
	win = GraphWin("GG",1000,1000)
	win.setBackground(color_rgb(0,0,0))
	# Desenhando cruz
	cruz(win)	
	aviao(145,140,150,160,130,130,win,"red")


	# Fechando Janela/Radar
	win.getMouse()
	win.close()
	

main()