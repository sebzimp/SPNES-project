# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 20:31:50 2021

@author: sebzi
"""

import numpy as np
import matplotlib.pyplot as plt


# SDE model parameters
r, gamma, N0 = 0.5, 1, 100

# Simulation parameters
T, N = 1, 10**3
dt = 1.0 / N
t = np.arange(dt, 1 + dt, dt)  # Start at dt because Y = X0 at t = 0

np.random.seed(101)
dB = np.sqrt(dt) * np.random.randn(N)
B  = np.cumsum(dB)

YS = N0 * np.exp(r* t + gamma * B) 
Y = N0
Ytild = N0
Heun = []
for i in range(N):
    Ytild = Y + r*Y*dt + gamma*Y*dB[i]
#    Ytild =  Y + r*Y*dt + gamma*Y*dB[i] + 0.5*gamma**2 * Y * (dB[i] ** 2 - dt)
    Y += 0.5*r*(Y+Ytild)*dt + 0.5*gamma*(Y+Ytild)*dB[i]
 #   Y += r*Y*dt + 0.5*gamma*(Y+Ytild)*dB[i]
    Heun.append(Y)

plt.figure(dpi=200)
plt.ylabel('N(t)'); plt.xlabel('t')

plt.plot(t,YS, label ="Exact solution")
plt.plot(t,Heun, label ="Stochastic Heun approximation")
#plt.plot(t, YI-EM)
plt.legend()