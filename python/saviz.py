# -*- coding: utf-8 -*-

"""
Module. Visualization tools.
"""

import numpy as np
from matplotlib import pyplot as plt

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

def plot_circles(circles, ax):
    """
    Plots line circles on axes.
    :circles: n x [x, y, r] array

    """
    ax.plot(circles[:,1], circles[:,0], 'gx', ms=5, mew=2)
    rt = np.linspace(0, 2*np.pi)
    for c in xrange(circles.shape[0]):
        ax.plot(circles[c,2]*np.sin(rt) + circles[c,1], circles[c,2]*np.cos(rt) + circles[c,0], 'g-', linewidth=2)

def plot_targets_1(circles, dataSet):
    """
    Plots circles of one pic,
    both the abstract circles and noisy data
    :circles: n x 3 circle ndarray
    :dataSet: corresponding noisy data pic
    :returns: TODO

    """
    f, ax = plt.subplots(1,2)
    plot_circles(circles, ax[0])

    ax[0].set_xbound(0, 50)
    ax[0].set_ybound(0, 50)
    ax[0].set_aspect('equal', adjustable='box')

    ax[1].imshow(dataSet, interpolation='none', cmap=plt.cm.gray, origin='lower')

    return f, ax
