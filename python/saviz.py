# -*- coding: utf-8 -*-

"""
Module. Visualization tools.
"""

import numpy as np
from matplotlib import pyplot as plt

import itertools

def best_final_energy_walkers():
    """
    Plot the best final energy as seen function of walkers
    """
    pass

def final_energies_histo():
    """
    Histogram of final energies of walkers in a set
    """
    pass

def plot_circles(circles, ax, gfxLine='g-',gfxCentr='gx'):
    """
    Plots line circles on axes.
    :circles: n x [x, y, r] array

    """
    ax.plot(circles[:,1], circles[:,0], gfxCentr, ms=5, mew=2)
    rt = np.linspace(0, 2*np.pi)
    for c in xrange(circles.shape[0]):
        ax.plot(circles[c,2]*np.sin(rt) + circles[c,1], circles[c,2]*np.cos(rt) + circles[c,0], gfxLine, linewidth=2)

def custom_imshow(dataSet, ax):
    ax.imshow(dataSet, interpolation='none', cmap=plt.cm.gray, origin='lower')

# for printing

def plot_targets_1(circles, dataSet):
    """
    Plots circles of one pic,
    both the abstract circles and noisy data
    :circles: n x 3 circle ndarray
    :dataSet: corresponding noisy data pic
    :returns: TODO

    """
    f, ax = plt.subplots(1,2, figsize=(6,4))
    plot_circles(circles, ax[0])

    ax[0].set_xbound(0, 50)
    ax[0].set_ybound(0, 50)
    ax[0].set_aspect('equal', adjustable='box')

    custom_imshow(dataSet, ax[1])

    f.tight_layout()
    return f, ax

def plot_datasets_2x3(dataSetsList, descriptors):
    """
    Plot 2x3 target noisy pics.
    """
    f, ax = plt.subplots(2,3, figsize=(9,6))
    print descriptors
    for ai in itertools.product([0,1],[0,1,2]):
        i = ai[0]*3 + ai[1]
        print ai, i
        custom_imshow(dataSetsList[i], ax[ai[0],ai[1]])
        ax[ai[0],ai[1]].set_title("Kiekkoja: " +str(descriptors[i][0]))

    #f.subplots_adjust(0.05,0.05,0.65,0.90,0.10,0.20)
    #^ difficult to get right
    f.tight_layout()
    return f, ax

def plot_3datasets_results(dataSetsList, descriptors,dataResults, targetCirclesList):
    """
    3 datasets in a list
    2x3: First row data + found, second target + found line gfx
    """
    f, ax = plt.subplots(2,3, figsize=(9,6))
    for i in [0,1,2]:
        custom_imshow(dataSetsList[i], ax[0,i])
        plot_circles(dataResults[i], ax[0,i], gfxLine='r-', gfxCentr='rx')
        ax[0,i].set_xbound(0, 50)
        ax[0,i].set_ybound(0, 50)
        ax[0,i].set_title("Kiekkoja: " +str(descriptors[i][0]))

        plot_circles(dataResults[i], ax[1,i], gfxLine='r-', gfxCentr='rx')
        plot_circles(targetCirclesList[i], ax[1,i], gfxLine='g--')
        ax[1,i].set_xbound(0, 50)
        ax[1,i].set_ybound(0, 50)

    f.tight_layout()
    return f, ax
