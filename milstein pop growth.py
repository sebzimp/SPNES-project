# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 17:25:29 2021

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

np.random.seed(1)
dB = np.sqrt(dt) * np.random.randn(N)
B  = np.cumsum(dB)

YI = N0 * np.exp((r - 0.5 * gamma**2) * t + gamma * B) 
Y = N0
M = []
for i in range(N):
    Y += r*Y*dt + gamma*Y*dB[i] + 0.5*gamma**2 * Y * (dB[i] ** 2 - dt)
    M.append(Y)

plt.figure(dpi=200)
plt.ylabel('Exact solution - Milstein Approximation'); plt.xlabel('t')

#plt.plot(t,YI, label ="Exact solution")
#plt.plot(t,M, label ="Ito Milstein Approximation")
plt.plot(t, YI-M)
#plt.legend()