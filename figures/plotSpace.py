#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import collections  as mc

font = {'family' : 'DejaVu Sans',
        'weight' : 'normal',
        'size'   : 16}

matplotlib.rc('font', **font)
# Fixing random state for reproducibility
np.random.seed(19680801)


def get_correlated_dataset(n, dependency, mu, scale):
    latent = np.random.randn(n, 2)
    dependent = latent.dot(dependency)
    scaled = dependent * scale
    scaled_with_offset = scaled + mu
    # return x and y of the new, correlated dataset
    return scaled_with_offset[:, 0], scaled_with_offset[:, 1]
def newline(p1, p2):
    ax = plt.gca()
    xmin, xmax = ax.get_xbound()

    if(p2[0] == p1[0]):
        xmin = xmax = p1[0]
        ymin, ymax = ax.get_ybound()
    else:
        ymax = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmax-p1[0])
        ymin = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmin-p1[0])

    l = mlines.Line2D([xmin,xmax], [ymin,ymax])
    ax.add_line(l)
    return l


smX, smY = [0], [0]
x1, y1 = [0.6], [0.2]
x3, y3 = [0.2], [0.8]
x2, y2 = [0.8], [0.8]

plt.clf()
fontsize = 20
fig, ax = plt.subplots()
plt.title("Theory parameter space")
plt.plot(x1, y1, 'r', markersize=20, marker='s')
plt.text(0.65, 0.1, "pMSSM1", color='r', size=22)
plt.plot(x2, y2, 'b', markersize=20, marker='P')
plt.text(0.6, 0.65, "pMSSM2", color='b', size=22)
plt.plot(x3, y3, 'g', markersize=20, marker='v')
plt.text(0.15, 0.65, "pMSSM3", color='g', size=22)
plt.plot(smX, smY, 'ko', markersize=40)
plt.text(0.05, 0.05, "SM", color='black', size=22)
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_xlabel("theory parameter 1", fontsize=fontsize)
ax.set_ylabel("theory parameter 2", fontsize=fontsize)
plt.tight_layout(pad=0.0)
plt.margins(0,0)
plt.savefig('theorySpace.pdf',bbox_inches='tight', pad_inches=0)
plt.savefig('theorySpace.svg',bbox_inches='tight', pad_inches=0)
plt.savefig('theorySpace.png',bbox_inches='tight', pad_inches=0)


params = [[[0.85, 0.35],
           [0.85, -0.65]],

          [[0.8, -0.4],
           [0.3, -0.6]],
          [[1, 0],
           [0, 1]],
]
mu = 2, 4
scale = 3, 5
n = 200
x1, y1 = get_correlated_dataset(n, params[1], 0.2, .1)
x1 +=0.1
y1 +=0.6
x2, y2 = get_correlated_dataset(n, params[0], 0.75, .15)
y2+=-0.5
x3, y3 = get_correlated_dataset(n, params[2], 0.2, .1)
y3 += 0.6

latent = np.random.randn(n, 2)
scale = 0.1
smX, smY = latent[:,0]*scale+0.2, latent[:,1]*scale+.1

plt.clf()
fig, ax = plt.subplots()
plt.title("Observable space")
plt.scatter(x1, y1, color='r', marker='s')
plt.text(0.46, 0.8, "pMSSM1", color='r', size=22)
plt.scatter(x2, y2, color='b', marker='P')
plt.text(0.65, 0.55, "pMSSM2", color='b', size=22)
plt.scatter(x3, y3, color='g', marker='v')
plt.text(0.01, 0.5, "pMSSM3", color='g', size=22)
plt.scatter(smX, smY, color='black')
plt.text(0.05, 0.32, "SM", color='black', size=22)
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_xlabel("$\Delta R (b_1,b_2)$", fontsize=fontsize)
ax.set_ylabel("$\mathcal{S}$", fontsize=fontsize)
plt.tight_layout(pad=0.0)
plt.margins(0,0)
plt.savefig('expSpace.pdf',bbox_inches='tight', pad_inches=0)
plt.savefig('expSpace.svg',bbox_inches='tight', pad_inches=0)
plt.savefig('expSpace.png',bbox_inches='tight', pad_inches=0)

plt.clf()
fig, ax = plt.subplots()
plt.title("Clustered observable space")
plt.scatter(x1, y1, color='r', marker='s')
plt.text(0.45, 0.9, "Search Region 1", color='r', size=18)
plt.scatter(x2, y2, color='b', marker='P')
plt.text(0.58, 0.53, "Search Region 2", color='b', size=18)
plt.scatter(x3, y3, color='g', marker='v')
#plt.text(0.05, 0.45, "pMSSM3", color='g', size=22)
plt.scatter(smX, smY, color='black')
lines = [[(0, .6), (.55, .6)], [(0.4, 1), (.55, .6)], [(0.5, 0), (.5, .5)], [(0.5, .5), (1, .5)] ]
lcolors = ['r', 'r', 'b', 'b']
lc = mc.LineCollection(lines, colors=lcolors, linewidths=2)
ax.add_collection(lc)
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_xlabel("$\Delta R (b_1,b_2)$", fontsize=fontsize)
ax.set_ylabel("$\mathcal{S}$", fontsize=fontsize)
plt.tight_layout(pad=0.1)
plt.margins(0,0)
plt.savefig('searchSpace.pdf',bbox_inches='tight', pad_inches=0)
plt.savefig('searchSpace.svg',bbox_inches='tight', pad_inches=0)
plt.savefig('searchSpace.png',bbox_inches='tight', pad_inches=0)


params = [[[0.9, 0.3],
           [0.9, -0.6]],

          [[0.7, -0.5],
           [0.3, -0.5]],
          [[1, 0],
           [0, 1]],
]
mu = 2, 4
scale = 3, 5
n = 200
x1, y1 = get_correlated_dataset(n, params[1], 0.2, .1)
x1 +=0.1
y1 +=0.6
x2, y2 = get_correlated_dataset(n, params[0], 0.75, .15)
y2+=-0.5
x3, y3 = get_correlated_dataset(n, params[2], 0.2, .1)
y3 += 0.6

x4, y4 = get_correlated_dataset(n, params[1], 0.7, .7)
y4 += 0.2

latent = np.random.randn(n, 2)
scale = 0.1
smX, smY = latent[:,0]*scale+0.5, latent[:,1]*scale+.1

plt.clf()
fig, ax = plt.subplots()
x = np.arange(0,1.01,0.01)
y = 0.6-(0.7*x)**2
plt.fill_between(x, y, np.max(x), color='green', alpha=0.4)
plt.title("Observable space")
plt.scatter(x1, y1, color='r', marker='x')
plt.text(0.4, 0.8, "pMSSM1", color='r', size=18)
plt.scatter(x2, y2, color='darkred', marker='P')
plt.text(0.65, 0.5, "pMSSM2", color='darkred', size=18)
plt.scatter(x3, y3, color='brown', marker='s')
plt.text(0.01, 0.55, "pMSSM3", color='brown', size=18)
plt.scatter(x4, y4, color='orangered', marker='v')
plt.text(0.8, 0.9, "pMSSM4", color='orangered', size=18)
plt.scatter(smX, smY, color='black', marker='o')
plt.text(0.01, 0.28, "Simplified model", color='black', size=18)
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_xlabel("Observable 1", fontsize=fontsize)
ax.set_ylabel("Observable 2", fontsize=fontsize)
plt.tight_layout(pad=0.0)
plt.margins(0,0)
plt.savefig('expSpaceSimplified.pdf',bbox_inches='tight', pad_inches=0)
plt.savefig('expSpaceSimplified.svg',bbox_inches='tight', pad_inches=0)
plt.savefig('expSpaceSimplified.png',bbox_inches='tight', pad_inches=0)
