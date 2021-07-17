# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 14:25:12 2021

@author: sebzi
"""

import numpy as np
import matplotlib.pyplot as plt

plt.figure(dpi=200)
# Plot settings
plt.rcParams['figure.figsize'] = (9,6)
plt.rcParams['lines.linewidth'] = 3
plt.rcParams['xtick.bottom'] = False
plt.rcParams['ytick.left'] = False
#pal = ["#FBB4AE","#B3CDE3", "#CCEBC5","#CFCCC4"]
pal = ["r","b", "g", "y"]
# SDE model parameters
r, gamma, N0 = 0.5, 1, 100

# Simulation parameters
T, N = 1, 10**5
dt = 1.0 / N
t = np.arange(dt, 1 + dt, dt)  # Start at dt because Y = X0 at t = 0

# Initiate plot object
#plt.title('Sample Solution Paths for Geometric Brownian Motion')
plt.ylabel('N(t)'); plt.xlabel('t')

# Create and plot sample paths
for i in range(len(pal)):
    
    # Create Brownian Motion

    dB = np.sqrt(dt) * np.random.randn(N)
    B  = np.cumsum(dB)
    
    # Compute exact solution
#    Y = N0 * np.exp((r - 0.5 * gamma**2) * t + gamma * B) #ito
    Y = N0 * np.exp(r * t + gamma * B)    #strato
    # Add line to plot
    plt.scatter(t, Y, label = "Iteration" + str(i+1), color=pal[i],s=0.5)

# Add legend
plt.legend(loc = 2);