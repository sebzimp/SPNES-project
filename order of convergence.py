# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 20:25:32 2021

@author: sebzi
"""

import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

dt_grid = np.loadtxt("Time.txt")
weak_err_em = np.loadtxt("MaruyameSE.txt")
weak_err_mil = np.loadtxt("MilsteinSE.txt")
heun = np.loadtxt("heunerrors.txt")
impHeun = np.loadtxt("heun2nd.txt")
X = sm.add_constant(np.log(dt_grid))

# Run OLS on above simulations to estimate gamma values
results = sm.OLS(np.log(weak_err_em),X).fit()
print("Weak E-M Convergence:        "+ str(results.params[1]))

results = sm.OLS(np.log(weak_err_mil),X).fit()
print("Weak Milstein Convergence:   "+ str(results.params[1]))

results = sm.OLS(np.log(impHeun),X).fit()
print("Heun Convergence:   "+ str(results.params[1]))

plt.figure(dpi=200)
plt.plot(dt_grid, heun, label = "Stong error of the Heun method")
plt.plot(dt_grid, impHeun, label = "Stong error of the imp heun method")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("$\Delta t$")
plt.ylabel("Strong Error")
plt.legend()