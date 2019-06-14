# -*- coding: utf-8 -*-
from graphics import *
from time import sleep
from primitivas import *


class aviao:
    '''
    def __init__(self, x, x2, x3, y, y2, y3, win, cor):
        self.x = x
        self.x2 = x2
        self.x3 = x3
        self.y = y
        self.y2 = y2
        self.y3 = y3
        self.win = win
        self.cor = cor
    '''

    # distancia = do avião até a torre. Calculo retirado das variáveis x,y,z.
    def __init__(self, temporizador, status, voo, distancia, velocidade, x, y, z):
        self.temporizador = temporizador
        self.status = status
        self.voo = voo
        self.distancia = distancia
        self.velocidade = velocidade
        self.x = x
        self.y = y
        self.z = z
        #self.cor = cor(status)

    def getTemporizador(self):
        return self.temporizador

    def getStatus(self):
        return self.status

    def getVoo(self):
        return self.voo

    def getDistancia(self):
        return self.distancia

    def getVelocidade(self):
        return self.velocidade

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    ''' Definir a cor do avião.
    def cor(self, status):
        if self.status == 'D':
            #cor do avião será verde.
        else:
            #P
            #cor do avião será vermelho
    '''

    def posicao(self, posicao):
        if posicao == 'direita':
            # reta OA
            reta(self.x, self.x2, self.y, self.y2, self.win, self.cor)
            # reta AB
            reta(self.x2, self.x3, self.y2, self.y3, self.win, self.cor)
            # reta BO
            reta(self.x3, self.x, self.y3, self.y, self.win, self.cor)
        elif posicao == 'esquerda':
            # <-   self.x2 + 20     self.x3 + 20
            # reta OA
            reta(self.x, self.x2, self.y, self.y2, self.win, self.cor)
            # reta AB
            reta(self.x2, self.x3, self.y2, self.y3, self.win, self.cor)
            # reta BO
            reta(self.x3, self.x, self.y3, self.y, self.win, self.cor)
        elif posicao == 'cima':
            # reta OA
            reta(self.x, self.x2, self.y, self.y2, self.win, self.cor)
            # reta AB
            reta(self.x2, self.x3, self.y2, self.y3, self.win, self.cor)
            # reta BO
            reta(self.x3, self.x, self.y3, self.y, self.win, self.cor)
        elif posicao == 'baixo':
            # self.x + 10       self.x2 - 10    self.x3 - 10
            # reta OA
            reta(self.x, self.x2, self.y, self.y2, self.win, self.cor)
            # reta AB
            reta(self.x2, self.x3, self.y2, self.y3, self.win, self.cor)
            # reta BO
            reta(self.x3, self.x, self.y3, self.y, self.win, self.cor)
        else:
            print
            'Escolha um das opções!\n'
            # print('')
