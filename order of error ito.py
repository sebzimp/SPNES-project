# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 17:35:39 2021

@author: sebzi
"""

import numpy as np
import matplotlib.pyplot as plt



Sem = []
Smil = []
# SDE model parameters
r, gamma, N0 = 0.5, 1, 100
deltT = []

for k in range(3,15):
    T, N = 1, 2**k
    dt = 1.0 / N
    deltT.append(dt)
    t = np.arange(dt, 1 + dt, dt)
    time = len(t)
    
    Eem, Emil = np.zeros(time), np.zeros(time)
    
    for j in range(10000):
        dB = np.sqrt(dt) * np.random.randn(N)
        B  = np.cumsum(dB)
        
        YI = N0 * np.exp((r - 0.5 * gamma**2) * t + gamma * B) 
        Y = N0
        M = []
        
        X =N0
        EM = []
        for i in range(time):
            #milstein
            Y += r*Y*dt + gamma*Y*dB[i] + 0.5*gamma**2 * Y * (dB[i] ** 2 - dt)
            M.append(Y)
            #maruyame
            X += r*X*dt + gamma*X*dB[i]
            EM.append(X)
        Eem  += abs(YI - EM)
        Emil += abs(YI - M)
        
    Sem.append(max(Eem / 10000))
    Smil.append(max(Emil / 10000))        
        
plt.figure(dpi=200)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("$\Delta t$")        
plt.ylabel("Strong error")
plt.plot(deltT, Sem, label = "Maruyame approximation")
plt.plot(deltT, Smil, label = "Milstein approximation")        
plt.legend()       
        
        
        
        
        
        
        
        