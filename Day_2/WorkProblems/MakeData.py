#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 18:22:49 2019

@author: bryanchavez
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(194)

x_data = np.linspace(-10, 10, num=500)
x_data2 = np.linspace(-1000,1000, num=10000) #setup x data
y_data = 8.4 * np.sin(1.5 * x_data) + np.random.normal(size=500) #setup sin(x) random data
errors = np.zeros(len(y_data)) + 1


#plt.plot(x_data,y_data)


pd.DataFrame({'x':x_data, 'y': y_data, 'errors':errors}).to_csv("../ExampleData/sinx.csv", index=False)

y_data2 = 5.7*np.sin(np.pi*x_data) + 8.1*np.cos(1.4*x_data) +np.random.normal(size=500)
y_data3 = (5.7*np.sin(np.pi*x_data) + 8.1*np.cos(1.4*x_data))**2 +np.random.normal(size=500)
y_data4 = 5.7*np.sin(np.pi*x_data)*np.cos(1.4*x_data) +np.random.normal(size=500)
y_data5 = 80*np.tanh(4.5*x_data + 1.5) -9.4 + 10*np.random.normal(size=500)
y_data6 = 600+ 10*x_data - (9.8/2)*x_data**2  + 30*np.random.normal(size=500)
y_data7 = (5.7*np.sin(np.pi*x_data) + 8.1*np.cos(1.4*x_data))**3 + 100*np.random.normal(size=500)
y_data8 = 4.2*np.sin(np.pi*x_data) + 7.5*np.cos(1.5*x_data) + 9.5*x_data +np.random.normal(size=500)
y_data9 = 5.7*np.sin(np.pi*x_data) + 8.1*np.cos(1.4*x_data) + np.exp(0.5*x_data) +np.random.normal(size=500)
y_data10 = 4.5*np.exp(0.5*x_data) + 30.5*x_data +np.random.normal(size=500)
y_data11 = 5*np.abs(x_data) + 2.4*np.sin(1.5*x_data) + 2*np.random.normal(size=500)

#y_data12 = 5.7*np.sin(np.pi*x_data) + 8.1*np.cos(1.4*x_data) +np.random.normal(size=500)
#y_data13 = 5.7*np.sin(np.pi*x_data) + 8.1*np.cos(1.4*x_data) +np.random.normal(size=500)
#y_data14 = 5.7*np.sin(np.pi*x_data) + 8.1*np.cos(1.4*x_data) +np.random.normal(size=500)
#y_data15 = 5.7*np.sin(np.pi*x_data) + 8.1*np.cos(1.4*x_data) +np.random.normal(size=500)
#y_data16 = 5.7*np.sin(np.pi*x_data) + 8.1*np.cos(1.4*x_data) +np.random.normal(size=500)
#y_data17 = 5.7*np.sin(np.pi*x_data) + 8.1*np.cos(1.4*x_data) +np.random.normal(size=500)
#y_data18 = 5.7*np.sin(np.pi*x_data) + 8.1*np.cos(1.4*x_data) +np.random.normal(size=500)
#y_data19 = 5.7*np.sin(np.pi*x_data) + 8.1*np.cos(1.4*x_data) +np.random.normal(size=500)
#y_data20 = 5.7*np.sin(np.pi*x_data) + 8.1*np.cos(1.4*x_data) +np.random.normal(size=500)
#y_data21 = 5.7*np.sin(np.pi*x_data) + 8.1*np.cos(1.4*x_data) +np.random.normal(size=500)
#y_data22 = 5.7*np.sin(np.pi*x_data) + 8.1*np.cos(1.4*x_data) +np.random.normal(size=500)


#plt.plot(x_data,y_data2)
#plt.plot(x_data,y_data3)
#plt.plot(x_data,y_data4)
plt.scatter(x_data,y_data11)
pd.DataFrame({'x':x_data, 'y': y_data2, 'errors':errors}).to_csv("../ExampleData/sinxandcosx.csv", index=False)
pd.DataFrame({'x':x_data, 'y': y_data3, 'errors':errors}).to_csv("../ExampleData/sinxandcosx2.csv", index=False)
pd.DataFrame({'x':x_data, 'y': y_data4, 'errors':errors}).to_csv("../ExampleData/sinxcosx.csv", index=False)
pd.DataFrame({'x':x_data, 'y': y_data5, 'errors':errors}).to_csv("../ExampleData/hysteresis.csv", index=False)
pd.DataFrame({'x':x_data, 'y': y_data6, 'errors':errors}).to_csv("../ExampleData/gravity.csv", index=False)
pd.DataFrame({'x':x_data, 'y': y_data7, 'errors':errors}).to_csv("../ExampleData/sinxandcosx3.csv", index=False)
pd.DataFrame({'x':x_data, 'y': y_data8, 'errors':errors}).to_csv("../ExampleData/linesinxandcosx.csv", index=False)
pd.DataFrame({'x':x_data, 'y': y_data9, 'errors':errors}).to_csv("../ExampleData/sinxandcosxexp.csv", index=False)
pd.DataFrame({'x':x_data, 'y': y_data10, 'errors':errors}).to_csv("../ExampleData/lineexp.csv", index=False)
pd.DataFrame({'x':x_data, 'y': y_data2, 'errors':errors}).to_csv("../ExampleData/sinxandabs.csv", index=False)
