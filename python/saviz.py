# -*- coding: utf-8 -*-

"""
Module. Visualization tools.
"""

import numpy as np
from matplotlib import pyplot as plt
import matplotlib.gridspec

import itertools


def plot_circles(circles, ax, gfxLine='g-',gfxCentr='gx'):
    """
    Plots line circles on axes.
    :circles: n x [x, y, r] array

    """
    # -1 -> adjust for matlab indexing

    ax.plot(circles[:,1] -1, circles[:,0]-1, gfxCentr, ms=5, mew=2)
    rt = np.linspace(0, 2*np.pi)
    for c in xrange(circles.shape[0]):
        ax.plot(circles[c,2]*np.sin(rt) + circles[c,1]-1, circles[c,2]*np.cos(rt) + circles[c,0]-1, gfxLine, linewidth=2)

def custom_imshow(dataSet, ax):
    ax.imshow(dataSet, interpolation='none', cmap=plt.cm.gray, origin='lower')

# for printing

def plot_all_circles(resCirclesList, targetCircles, onlyCenters=True, wiggle=4):
    """
    Plot all results in res vs true target
    """
    f, ax = plt.subplots(figsize=(6,4))
    plot_circles(targetCircles, ax, gfxLine='g--')
    cm = plt.get_cmap('Blues')
    colorGrad = [cm(c) for c in np.linspace(0,1,len(resCirclesList))]
    if onlyCenters:
        for circles, c in zip(resCirclesList, colorGrad):
            ax.plot(circles[:,1] + wiggle*(np.random.rand()-0.5),
                    circles[:,0] + wiggle*(np.random.rand()-0.5),
                    'x', color=c, ms=5, mew=2)
    else:
        print "not implemented"

    ax.set_xbound(0, 50)
    ax.set_ybound(0, 50)
    ax.set_aspect('equal', adjustable='box')
    f.tight_layout()
    return f, ax


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

def plot_dataset(dataSet):
    """
    Plots one noisy data pic

    """
    f, ax = plt.subplots(1,1, figsize=(6,6))
    custom_imshow(dataSet, ax)
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

def plot_kdatasets_results(dataSetsList, descriptors,dataResultCircs, targetCirclesList, k):
    """
    k datasets in a list
    2xk: First row data + found, second target + found line gfx
    """
    if k > 1:
        f, ax = plt.subplots(2,k, figsize=(3*k,6))
    else:
        f, ax = plt.subplots(1,2, figsize=(6,3))
    for i in np.arange(k):
        if k > 1:
            ax0 = ax[0,i]
            ax1 = ax[1,i]
        else:
            ax0 = ax[0]
            ax1 = ax[1]
        custom_imshow(dataSetsList[i], ax0)
        plot_circles(dataResultCircs[i], ax0, gfxLine='r-', gfxCentr='rx')
        ax0.set_xbound(0, 50)
        ax0.set_ybound(0, 50)
        ax0.set_title("Kiekkoja: " +str(descriptors[i][0]))

        plot_circles(dataResultCircs[i], ax1, gfxLine='r-', gfxCentr='rx')
        plot_circles(targetCirclesList[i], ax1, gfxLine='g--')
        ax1.set_xbound(0, 50)
        ax1.set_ybound(0, 50)
        ax1.set_aspect('equal', adjustable='box')

    f.tight_layout()
    return f, ax

def best_final_energy_walkers(enDatas, descriptors=None):
    """
    Plot the best final energy as seen function of walkers
    k datasets in a list
    1 x k plot of evolution of best final energy
    """
    k = len(enDatas)
    f, ax = plt.subplots(1,k, sharey=True, figsize=(3*k,4))
    for i in np.arange(k):
        if k > 1:
            axi = ax[i]
        else:
            axi = ax
        finalEnergies = np.array([e[0,-1] for e in enDatas[i].energies])
        bestSFE = np.empty(finalEnergies.shape[0])
        bestSFE[0] = finalEnergies[0]
        for e in np.arange(finalEnergies.shape[0] - 1) + 1:
            bestSFE[e] = min(bestSFE[e-1], finalEnergies[e])

        axi.plot(finalEnergies, 'k-', linewidth=1)
        axi.plot(bestSFE, 'b-', linewidth=2)
        axi.set_xlabel('kulkija')
        axi.set_ylabel('E', labelpad=8, rotation=0)
        if descriptors:
            axi.set_title(descriptors[i])
        axi.grid(True)
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

    ax[0].set_ylabel('n', labelpad=8, rotation=0)
    f.tight_layout()
    return f, ax

def final_energies_histo(enData, descriptors=None):
    """
    Histogram of final energies of walkers in a set
    histo3 but just 'histo1'
    """
    f, ax = plt.subplots(1,1, figsize=(4,4))
    finalEnergies = np.array([e[0,-1] for e in enData.energies])
    n, bins, patches = ax.hist(finalEnergies, bins=20, range=(np.min(finalEnergies)-1, np.max(finalEnergies)+1), color='green')
    fem = np.max(finalEnergies) - np.min(finalEnergies)
    rou = min(-1, 1 - len(str(int(fem/5))))
    pr = round(fem/5, rou)
    ticks =np.arange(round(np.min(finalEnergies)+pr, rou), np.max(finalEnergies)+(pr/4), pr)
    if np.min(finalEnergies) < ticks[0] - pr:
        ticks = np.insert(ticks,0, ticks[0] - pr)
    if np.max(finalEnergies) > ticks[-1] + pr:
        ticks = np.append(ticks,ticks[-1] + pr)
    ax.set_xticks(ticks)
    ax.set_xlabel('E')
    ax.grid(True)

    ax.set_ylabel('n', labelpad=8, rotation=0)
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
        ax[i].hist(finalEnergies1, bins=bins, alpha=0.5, color='blue')
        ax[i].hist(finalEnergies2, bins=bins, alpha=0.5, color='green')

        ax[i].set_xlabel('E')
        ax[i].grid(True)
    ax[0].set_ylabel('n', labelpad=8, rotation=0)
    ax[k-1].legend(descriptors, loc='best')

    f.tight_layout()
    return f, ax

def walker_temp_compare_1(energies1, temp1, energies2, temp2,
                          desc1=['paras','tyypil.'], desc2=['paras','tyypil.'],
                          logeny=True, logenx=True):
    """
    Compare walkers of two temps on one 2x1 plot:
        first pic energies
        second pic below temps
    :energies1: list of energies to plot
    :temp1: corresponding list of temps
    :energies2: respectively but for
    :temp2:
    """
    f = plt.figure(figsize=(9,6))
    gs = matplotlib.gridspec.GridSpec(2,1, height_ratios=[2,1])
    ax1 = f.add_subplot(gs[0])
    ax2 = f.add_subplot(gs[1])

    ni = np.max([len(e.squeeze()) for e in energies1 + energies2])
    majorTicks = np.arange(0, ni, 2000)
    minorTicks = np.arange(0, ni, 500)

    for i, e in enumerate(energies1):
        label = "hidas, " + desc1[i]
        if logeny and logenx:
            ax1.loglog(e.squeeze(), label=label)
        elif logeny and not logenx:
            ax1.semilogy(e.squeeze(), label=label)
        elif not logeny and logenx:
            ax1.semilogx(e.squeeze(), label=label)
        else:
            ax1.plot(e.squeeze(), label=label)

        if not logenx:
            ax2.plot(temp1[i].squeeze(), label=label)
        else:
            ax2.semilogx(temp1[i].squeeze(), label=label)

    for i, e in enumerate(energies2):
        label = "nopea, " + desc1[i]
        if logeny and logenx:
            ax1.loglog(e.squeeze(), label=label)
        elif logeny and not logenx:
            ax1.semilogy(e.squeeze(), label=label)
        elif not logeny and logenx:
            ax1.semilogx(e.squeeze(), label=label)
        else:
            ax1.plot(e.squeeze(), label=label)

        if not logenx:
            ax2.plot(temp2[i].squeeze(), label=label)
        else:
            ax2.semilogx(temp2[i].squeeze(), label=label)

    l1 = ax1.legend(loc='best')
    #l2 = ax2.legend(loc='best')
    #for legobj in l1.legendHandles + l2.legendHandles:
    for legobj in l1.legendHandles:
        legobj.set_linewidth(2.0)


    if not logenx:
        ax1.set_xticks(majorTicks)
        ax2.set_xticks(majorTicks)
        ax1.set_xticks(minorTicks, minor=True)
        ax2.set_xticks(minorTicks, minor=True)
    ax1.grid(which='minor', alpha=0.2)
    ax1.grid(which='major', alpha=0.4)
    ax2.grid(which='minor', alpha=0.2)
    ax2.grid(which='major', alpha=0.4)

    ax1.set_ylabel('E', labelpad=8, rotation=0)
    ax2.set_ylabel('t', labelpad=8, rotation=0)
    ax2.set_xlabel('iter')

    f.tight_layout()
    return f, [ax1, ax2]


def walker_temp(energies, temp, descriptors=[],
                logeny=True, logenx=True):
    """
    Plot walkers on 2x1 plot (similar as above)
        first pic energies
        second pic below temps
    :energies: list of energies to plot
    :temp: corresponding list of temps
    :descriptors: corresponding list of labels
    """
    f = plt.figure(figsize=(9,6))
    gs = matplotlib.gridspec.GridSpec(2,1, height_ratios=[2,1])
    ax1 = f.add_subplot(gs[0])
    ax2 = f.add_subplot(gs[1])

    ni = np.max([len(e.squeeze()) for e in energies])
    majorTicks = np.arange(0, ni, 2000)
    minorTicks = np.arange(0, ni, 500)

    for i, e in enumerate(energies):
        label = descriptors[i]
        if logeny and logenx:
            ax1.loglog(e.squeeze(), label=label)
        elif logeny and not logenx:
            ax1.semilogy(e.squeeze(), label=label)
        elif not logeny and logenx:
            ax1.semilogx(e.squeeze(), label=label)
        else:
            ax1.plot(e.squeeze(), label=label)

        if not logenx:
            ax2.plot(temp[i].squeeze(), label=label)
        else:
            ax2.semilogx(temp[i].squeeze(), label=label)

    l1 = ax1.legend(loc='best')
    #l2 = ax2.legend(loc='best')
    #for legobj in l1.legendHandles + l2.legendHandles:
    for legobj in l1.legendHandles:
        legobj.set_linewidth(2.0)


    if not logenx:
        ax1.set_xticks(majorTicks)
        ax2.set_xticks(majorTicks)
        ax1.set_xticks(minorTicks, minor=True)
        ax2.set_xticks(minorTicks, minor=True)
    ax1.grid(which='minor', alpha=0.2)
    ax1.grid(which='major', alpha=0.4)
    ax2.grid(which='minor', alpha=0.2)
    ax2.grid(which='major', alpha=0.4)

    ax1.set_ylabel('E', labelpad=8, rotation=0)
    ax2.set_ylabel('t', labelpad=8, rotation=0)
    ax2.set_xlabel('iter')

    f.tight_layout()
    return f, [ax1, ax2]
