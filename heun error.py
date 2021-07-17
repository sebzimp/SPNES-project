# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 20:49:24 2021

@author: sebzi
"""

import numpy as np
import matplotlib.pyplot as plt



Sem = []

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
        
        YS = N0 * np.exp((r) * t + gamma * B) 
        Y = N0
        Ytild = N0
        Heun = []
        

        for i in range(time):
            
            Ytild = Y + r*Y*dt + gamma*Y*dB[i] # for normal
  #          Ytild =  Y + r*Y*dt + gamma*Y*dB[i] + 0.5*gamma**2 * Y * (dB[i] ** 2 - dt) #for milstein
#            Y += 0.5*r*(Y+Ytild)*dt + 0.5*gamma*(Y+Ytild)*dB[i] #heun
            Y += 0.5*r*(Y+Ytild)*dt + 0.5*gamma*(Y+Ytild)*dB[i] + 0.25*gamma**2*(Y+Ytild)*(dB[i] ** 2 - dt)
            Heun.append(Y)
        Eem  += abs(YS - Heun)

        
    Sem.append(max(Eem / 10000))
      
        
plt.figure(dpi=200)
plt.xscale("log")
plt.yscale("log")
plt.xlabel("$\Delta t$")        
plt.ylabel("Strong error")
plt.plot(deltT, Sem, label = "Heun approximation")
      
plt.legend()       