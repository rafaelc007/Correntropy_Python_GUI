# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 08:32:19 2018

@author: rafael

Projeto de doutorado - trabalho 01: entendendo ITL
"""

import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
from mpl_toolkits.mplot3d import axes3d

mpl.rcParams['legend.fontsize'] = 10

## generating the model

## input
x_size = 1000
n_samples = 0.1
x = np.linspace(0, 10, x_size)

## desired parameters
A = 2
B = 1

## varible parameter
y_A = 1
y_B = 0

## desired model
d = A*x+B

## model output
y = y_A*x+y_B

## determinate error
samples = np.random.choice(range(x_size), size = int(n_samples*x_size))
d_samp = d[samples]
y_samp = y[samples]


###############################################################################
## plotting interface

fig, ax = plt.subplots(1,2, figsize=(12, 6))
plt.subplots_adjust(left=0.05, bottom=0.02, top = 0.95)

## subplots
ax1 = plt.subplot(221)
ax1.grid(1)
ax1.plot(x,d, label = 'desired')
l1, = ax1.plot(x,y, label = 'obtained')
l3, = ax1.plot(x[samples], d_samp, 'ko')
plt.setp(l3, markerfacecolor= 'None', markeredgecolor='k')
ax1.set_title('models output')
ax1.set_xlabel('input')
ax1.set_ylabel('outputs')
ax1.legend(loc = 0)


## plotting the error relation
ax2 = plt.subplot(222)
ax2.grid(1)

ax2.plot(d,d, 'r-')
#ax2.scatter(d_samp, y_samp, marker = 'o', c = '#ffffff', edgecolors ='black')
l2, = ax2.plot(d_samp, y_samp, 'ko')
plt.setp(l2, markerfacecolor= 'None', markeredgecolor='k')
ax2.axis([1, 21, 1, 21])
ax2.set_title('output comparison')
ax2.set_xlabel('desired')
ax2.set_ylabel('obtained')

## plotting the distrbution graph
ax3 = plt.subplot(224, projection='3d')
ax3.plot(d, d, np.zeros(x_size), label='desired curve')
sc = ax3.scatter(d_samp, y_samp, np.zeros(len(samples)), c = 'None', marker = 'o', edgecolors = 'k')

## set limits and labels
ax3.set_xlim(1, 21)
ax3.set_ylim(1, 21)
ax3.set_zlim(0, 1)
ax3.set_xlabel('desired')
ax3.set_ylabel('obtained')
ax3.set_zlabel('probability')
ax3.set_title('distribution')

###############################################################################

## sliders colors
axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.08, 0.2, 0.35, 0.03], facecolor=axcolor)
axamp = plt.axes([0.08, 0.25, 0.35, 0.03], facecolor=axcolor)
axsamp = plt.axes([0.08, 0.3, 0.35, 0.03], facecolor=axcolor)

## sliders
sA = Slider(axfreq, 'A', -5.0, 5.0, valinit=y_A)
sB = Slider(axamp, 'B', -5.0, 5, valinit=y_B)
s_sample = Slider(axsamp, 'n samples', 0.001, 0.2, valinit=n_samples)

def update(val):
    ## reseting output data
    y_B = sB.val
    y_A = sA.val
    y = y_A*x+y_B 
    l1.set_ydata(y_A*x+y_B)

    ## reseting error
    n_sample = int(s_sample.val*x_size)
    samples = np.random.choice(range(x_size), size = n_sample)
    d_samp = d[samples]
    y_samp = y[samples]
    
    ## redraw samples
    l2.set_ydata(y_samp)
    l2.set_xdata(d_samp)
    
    ## redraw samples
    l3.set_xdata(x[samples])
    l3.set_ydata(d_samp)
    
    ## redraw 3d samples
    sc._offsets3d = (d_samp, y_samp, np.zeros(len(samples)))
    ax3.add_collection3d(sc)
    
    fig.canvas.draw_idle()
    
sA.on_changed(update)
sB.on_changed(update)
s_sample.on_changed(update)

resetax = plt.axes([0.08, 0.1, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    sA.reset()
    sB.reset()
    s_sample.reset()
button.on_clicked(reset)

#rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
#radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)


#def colorfunc(label):
#    l1.set_color(label)
#    fig.canvas.draw_idle()
#radio.on_clicked(colorfunc)
plt.show()