#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 11:30:13 2017

@author: labsim
"""

#!coenergia: um jeito de trabalhar com a corrente 

#importar biblioteca
import numpy as np
import matplotlib.pyplot as plt

#armazenamento de variaveis
i1, i2 = 0.8 , 0.3

#utilizar biblioteca
theta = np.linspace(-3, 3, 1000) #amostras de -10 a 10 com 1000 amostras

#armazenamento de variaveis
L11 = (3+np.cos(2*theta))*10e-3
L22 = 0.3*np.cos(theta)
L12 = (30 + 10*np.cos(2*theta))

W = 0.5*L11*i1**2 + L12*i1*i2 + 0.5*L22*i2**2#potencia **

#derivada_ nao pega as definiçoes, pega os valores ("derivada discreta")
T_total = np.diff(W)

W_relutancia = 0.5*L11*i1**2 + 0.5*L22*i2**2
W_mutuo = L12 * i1 * i2

T_r = np.diff(W_relutancia)
T_m = np.diff(W_mutuo)

#plotando graficos
#indexaçao: colocar o valor de elemento e ele conseguir acessar
#a derivada suga um valor, ai tem que indexar para evitar erros de dimensoes
#plt.plot(theta[0:len(theta)-1],T_total,'r')
#plt.plot(theta[0:len(theta)-1],T_r, 'g')
#plt.plot(theta[0:len(theta)-1],T_m)

#subplot
plt.figure(1, [10,7])
#subplot(linhas/colunas/celula)
plt.subplot(311)
plt.plot(theta[0:len(theta)-1],T_total,'r')
plt.title("Torque Total")
plt.ylabel("Torque [N-m]")
plt.xlabel("$\Theta$ (radianos)")
plt.grid()

plt.subplot(312)
plt.plot(theta[0:len(theta)-1],T_r,'g')
plt.title("Torque por relutancia")
plt.ylabel("Torque [N-m]")
plt.xlabel("$\Theta$ (radianos)")
plt.grid()

plt.subplot(313)
plt.plot(theta[0:len(theta)-1],T_m)
plt.title("Torque mutuo")
plt.ylabel("Torque [N-m]")
plt.xlabel("$\Theta$ (radianos)")
plt.grid()

plt.tight_layout() #garantir a nao sobreposiçao do x
plt.show()

