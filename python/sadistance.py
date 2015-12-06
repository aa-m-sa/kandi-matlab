# -*- coding: utf-8 -*-

"""
Module sadistance.py
Distance mearsures for circle toy SA problem results evaluation.

(data|true)Circles: set of n circles = n x 3 ndarray (x,y,r)
"""

import numpy as np
import scipy as sp
from scipy.spatial.distance import cdist

def filled_circles(circles, imSize):
    nData = circles.shape[0]
    m = np.zeros((imSize, imSize), dtype=np.bool)
    xx, yy = np.meshgrid(np.arange(imSize), np.arange(imSize))
    for c in xrange(nData):
        cx, cy, cr = circles[c,:]
        m = m + ((xx - cx)**2 + (yy - cy)**2 <= cr**2)
    return m

def symmetric_diff(dataCircles, trueCircles, imSize=50):
    """
    Symmetric difference (area) distance between two circle sets
    """
    nData = dataCircles.shape[0]
    nTrue = trueCircles.shape[0]

    dm = filled_circles(dataCircles, imSize)
    tm = filled_circles(trueCircles, imSize)

    return np.sum(dm != tm)

def naive_dist(dataCircles, trueCircles):
    """
    Sum of distances of each circle to its nearest true neighbour not already
    matched to some other data circle.  i.e.
    Calculate distances between each datacircle-truecircle pair.
    True circles are naively paired with data circles:
        each data circle is paired with a true circle with smallest distance of all un-matched true circles
    The distances so found are summed.

    Distance used is euclidean distance bw. parameters.
    """

    nData = dataCircles.shape[0]
    nTrue = trueCircles.shape[0]
    if nData != nTrue:
        # raise error
        raise TypeError('dimension mismatch ' + str(nData) + " " + str(nTrue))

    # distance matrix
    dists = cdist(dataCircles, trueCircles)
    dists_org = dists

    # naive algo implementation, no intelligent data structures
    pairs = []
    pair_ds = []
    for c in np.arange(nData):
        pair_ds.append(np.min(dists))
        flat_min = np.argmin(dists)
        dc_min, tc_min = np.unravel_index(flat_min, (nData-c, nTrue-c))
        pairs.append((dataCircles[dc_min,:], trueCircles[tc_min,:]))

        dataCircles = np.delete(dataCircles,dc_min,axis=0)
        trueCircles = np.delete(trueCircles,tc_min,axis=0)

        mask = np.ones(dists.shape, dtype=np.bool)
        mask[dc_min,:] = False
        mask[:, tc_min] = False
        dists = dists[mask].reshape(nData-c-1, nTrue-c-1)

    return np.sum(pair_ds), pairs
