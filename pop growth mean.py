# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 15:36:26 2021

@author: sebzi
"""

import numpy as np
import matplotlib.pyplot as plt

plt.figure(dpi=200)


# SDE model parameters
r, gamma, N0 = 0, 1, 100

# Simulation parameters
T, N = 1, 10**4
dt = 1.0 / N
t = np.arange(dt, 1 + dt, dt)  # Start at dt because Y = X0 at t = 0

YtotI = []
YtotS = []
# Initiate plot object
#plt.title('Sample Solution Paths for Geometric Brownian Motion')
plt.ylabel('N(t)'); plt.xlabel('t')

# Create and plot sample paths
for i in range(10000):
    
    # Create Brownian Motion

    dB = np.sqrt(dt) * np.random.randn(N)
    B  = np.cumsum(dB)
    
    # Compute exact solution
    YI = N0 * np.exp((r - 0.5 * gamma**2) * t + gamma * B) #ito
    YS = N0 * np.exp(r * t + gamma * B)  #strato
    YtotI.append(YI)
    YtotS.append(YS)
    # Add line to plot
I = np.mean(YtotI,0)
S = np.mean(YtotS,0)
plt.scatter(t, I,s=0.5, label = "Mean for Ito interpretation")
plt.scatter(t, S,s=0.5, label = "Mean for Stratonovich interpretation")
# Add legend
plt.legend()