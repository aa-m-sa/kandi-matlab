# -*- coding: utf-8 -*-

"""
Module. Visualization tools.
"""

import numpy as np
from matplotlib import pyplot as plt

import itertools


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

def plot_3datasets_results(dataSetsList, descriptors,dataResultCircs, targetCirclesList):
    """
    3 datasets in a list
    2x3: First row data + found, second target + found line gfx
    """
    f, ax = plt.subplots(2,3, figsize=(9,6))
    for i in [0,1,2]:
        custom_imshow(dataSetsList[i], ax[0,i])
        plot_circles(dataResultCircs[i], ax[0,i], gfxLine='r-', gfxCentr='rx')
        ax[0,i].set_xbound(0, 50)
        ax[0,i].set_ybound(0, 50)
        ax[0,i].set_title("Kiekkoja: " +str(descriptors[i][0]))

        plot_circles(dataResultCircs[i], ax[1,i], gfxLine='r-', gfxCentr='rx')
        plot_circles(targetCirclesList[i], ax[1,i], gfxLine='g--')
        ax[1,i].set_xbound(0, 50)
        ax[1,i].set_ybound(0, 50)

    f.tight_layout()
    return f, ax

def best_final_energy_walkers(enDatas, descriptors):
    """
    Plot the best final energy as seen function of walkers
    3 datasets in a list
    1 x 3 plot of evolution of best final energy
    """
    f, ax = plt.subplots(1,3, figsize=(9,4))
    for i in [0, 1, 2]:
        finalEnergies = np.array([e[0,-1] for e in enDatas[i].energies])
        bestSFE = np.empty(finalEnergies.shape[0])
        bestSFE[0] = finalEnergies[0]
        for e in xrange(finalEnergies.shape[0] - 1) + 1:
            bestSFE[e] = np.min(bestSFE[e-1], finalEnergies[e])

        ax[i].plot(finalEnergies, 'k-', linewidth=1)
        ax[i].plot(bestSFE, 'b-', linewidth=2)
        ax[i].set_xlabel('kulkija')
        ax[i].set_ylabel('E')
        #ax[i].set_title('')
        ax[i].grid(True)
    f.tight_layout()
    return f, ax


def final_energies_histo3(enDatas, descriptors=None):
    """
    Histogram of final energies of walkers in a set
    3 datasets in a list
    1 x 3 histogram of final energies
    """
    f, ax = plt.subplots(1,3, sharey=True, figsize=(9,4))
    for i in [0, 1, 2]:
        finalEnergies = np.array([e[0,-1] for e in enDatas[i].energies])
        # TODO color
        n, bins, patches = ax[i].hist(finalEnergies, bins=20, range=(np.min(finalEnergies)-1, np.max(finalEnergies)+1), color='green')
        fem = np.max(finalEnergies) - np.min(finalEnergies)
        rou = min(-1, 1 - len(str(int(fem/5))))
        pr = round(fem/5, rou)
        ticks =np.arange(round(np.min(finalEnergies)+pr, rou), np.max(finalEnergies)+(pr/4), pr)
        if np.min(finalEnergies) < ticks[0] - pr:
            ticks = np.insert(ticks,0, ticks[0] - pr)
        if np.max(finalEnergies) > ticks[-1] + pr:
            ticks = np.append(ticks,ticks[-1] + pr)
        ax[i].set_xticks(ticks)
        ax[i].set_xlabel('E')
        ax[i].grid(True)

    ax[0].set_ylabel('n', rotation=0)
    f.tight_layout()
    return f, ax

def final_energies_histo_k_compare(enDatas1, enDatas2,k=1, descriptors=None):
    """
    Histogram of final energies of walkers in a set (any number of histograms to compare)
    1 x k subplots, histograms 1 vs 2
    In each subplot, compare histrogram in the first list to its pair in the second.
    """
    f, ax = plt.subplots(1,k, sharey=True, figsize=(9,4))
    finalEnergies = []
    for i in np.arange(k):
        finalEnergies1 = np.array([e[0,-1] for e in enDatas1[i].energies])
        finalEnergies2 = np.array([e[0,-1] for e in enDatas2[i].energies])
        cmax = np.ceil(max(finalEnergies1.max(), finalEnergies2.max()))
        bw = max(cmax/40, 10)
        bins = np.arange(0, cmax+bw+1, bw)
        ax[i].hist(finalEnergies1, bins=bins, alpha=0.5)
        ax[i].hist(finalEnergies2, bins=bins, alpha=0.5)

        ax[i].set_xlabel('E')
        ax[i].grid(True)
    ax[0].set_ylabel('n', rotation=0)
    ax[2].legend(descriptors, loc='best')

    f.tight_layout()
    return f, ax

