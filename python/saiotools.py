# -*- coding: utf-8 -*-

"""
Module saiotools.py

Tools for loading SA data
"""

import os
import scipy.io
import numpy as np


def createCircles(circleDataPts, circleDataR, ensembleSize):
    """Circle coordinates of all iterations of all walkers in the ensemble.
    Verraa niize format, sveethot.

    Returns: Ensemble-sized ndtype= object array, where each walker is a
    (3, iterLen, numCircles) array
    first 3 params: [x, y, r]
    """
    ensCircles = np.empty(ensembleSize, dtype=object)
    for walker in xrange(ensembleSize):
        wpts = circleDataPts[walker]
        wrs  = circleDataR[walker]
        rs = (1, wrs.shape[0], wrs.shape[1])
        ensCircles[walker] = np.concatenate([wpts.reshape((2, rs[1], rs[2])), wrs.reshape(rs)])
    return ensCircles

class EnsembleData(object):

    """Parsed ann-data. Object -> lose a bit efficiency, but a bit easier to use.

    class members are dtype=object ndarrays
    each of them is a (ensembleSize,) object ndarray consisting of numeric ndarrays
        some notes
        iterNums: number of iterations of each walker
        markovChainNos: homog. Markov chain id of each iteration of each walker
        circleDataR: radii of each iter, shape = (iterations, circles)
        circleDataPts: points, shape = (xy, iterations, circles) eg [0, 4, 3] (x of circle 3 after 4th iteration)
    """

    def __init__(self, loadedAnnData):
        """
        :loadedAnnData: output of scipy.io.loadmat
        """

        self.ensembleSize    = loadedAnnData['enDataMarkovNo'].shape[1]
        self.iterNums        = loadedAnnData['enDataLen'][0,:]
        self.markovChainNos  = loadedAnnData['enDataMarkovNo'][0,:]

        self.circleDataPts   = loadedAnnData['enDataPts'][0,:]
        self.circleDataR     = loadedAnnData['enDataR'][0,:]
        self.circles = createCircles(self.circleDataPts, self.circleDataR, self.ensembleSize)

        self.ratios          = loadedAnnData['enDataRatios'][0,:]
        self.energies        = loadedAnnData['enDataEnerg'][0,:]
        self.temps           = loadedAnnData['enDataTemps'][0,:]
        self.originalAnnData = loadedAnnData

def parse_sa_resmat(loadedResData):
    """Parse final results of each walker"""
    # TODO
    pass

def load_set2_full(dataFolder):
    """
    Loads a set2 style dataset
    (parse filenames to match data with relevant originals)

    :dataFolder: where to look at (load all format*.mat files in there)

    :returns: a dict of ndarray things (keyed by the unique part of filename = int)
    (not a list; original numbering begins with 1, don't want to mess with it
    unless necessary) """

    files = os.listdir(dataFolder)
    commonFormat = 'ann-data-pic-'

    dataSet = dict()
    for file in [f for f in files if f.startswith(commonFormat)]:
        fIdent = file[len(commonFormat):]
        if fIdent.isdigit():
            fIdent = int(fIdent)
        try:
            dataSet[fIdent] = EnsembleData(scipy.io.loadmat(dataFolder + '/' + file))
        except NotImplementedError as e:
            # new-style Matlab file not compatible
            print 'Warning: Dropping error'
            print e
            # if one has managed to creep in, implement a h5py thing here TODO

    return dataSet

class TargetData(object):

    """Similar to EnsembleData but for original testdatasets.

    targets = original circle vectors
    dataSets = noisy target images
    numSets = number of sets
    """

    def __init__(self, loadedTestFile):
        """TODO: to be defined1. """
        self.targets = loadedTestFile['picSets'][0,:]
        self.dataSets = loadedTestFile['dataSets'][0,:]
        self.nDataCircles = loadedTestFile['nDataCircles'].squeeze()
        self.numSets = loadedTestFile['numPics'].squeeze()

        self.originalTestData = loadedTestFile

def load_set2_target(dirName='../testdata-shared/', commonPart='testdata2_'):
    """
    Load set2 originals,
    format them as nice python things

    :returns: a dict of ndarray things (keyed by the unique part of filename
    after common part, usually 'c1-' etc)
    """
    # get c1-, c2-, c3-, c4-, c5-

    target = dict()
    for c in ['1','2','3','4','5']:
        target[int(c)] = TargetData(scipy.io.loadmat(dirName + commonPart + c + '.mat'))

    return target

def parse_meta(filename):
    """get meta info from filename

    :filename: TODO
    :returns: TODO

    """
    #here be rexgreppery magikcs
    return {'tempConst': t, 'maxLen': n}


