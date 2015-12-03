#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script. Analyze and plot all
"""

import saiotools
import sadistance
import numpy as np

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

def error_rate_evo(walkerCircles, walkerLen, targetCircles, measure):
    """
    Returns error rate evolution for a walker.
    """
    def wrapper(wCircle):
        measure(wCircle.squeeze().T, targetCircles)

    return np.apply_along_axis(wrapper, walkerCircles, axis=1)


def error_rates_final(circleSetResultData, targetData, measure):
    """
    Returns error rates of final state of each walker.
    """
    pass

def analyze_circleSet(circleSetData, targetData, meta):
    """
    :circleSetData: a dict of saiotools.EnsembleData objects
    :targetData: a TargetData object
    :meta: some meta information from filename
    """

    # run all hooks on data and target_data
    # what plots we need / want?

    # error rate

    # test if it works

    print '-'
    print meta['origFilename'], meta['tempConst'], meta['maxLen']

    for s in circleSetData:
        ensemble = circleSetData[s]
        for walker in xrange(ensemble.ensembleSize):
            # error rate evolution of a walker
            error_rates = error_rate_evo(ensemble.circles[walker], ensemble.iterNums[walker], targetData, sadistance.naive_dist)
            np.savetxt('error_rates' + meta['scenario'] + '_c' + meta['numCircles'] + '_' + int(walker) + '.txt', error_rates)
            # energy evolution of a walker

def analyze_all(scenario_list, basedirname):
    """
    Handles all scenarios:
        - load scenario
        - analyze
        - save results
        (- handle stuff that uses all data gathered on previous rounds?)
    """

    # original targets for each circle set in dataset
    targetData = saiotools.load_set2_target()

    # scenario: same annealing schedule and other related settings
    # scenario includes multiple circleDatas
    data = dict()
    for s in scenario_list:
        for circleSet in ['c1-', 'c2-', 'c3-', 'c4-', 'c5-']:
            circleSetData = saiotools.load_set2_full(basedirname + s + '-' + circleSet)
            meta = saiotools.parse_meta(s)
            numCircles = int(circleSet[1])
            meta['numCircles'] = numCircles
            meta['scenario'] = s
            analyze_circleSet(circleSetData, targetData[numCircles], meta)

if __name__ == "__main__":
    scenario_list = ['t99-n1000',
                     't98-n1000',
                     't96-n600',
                     't94-n600',
                     't90-n600']

    basedirname = '../testdata-annealingset2b-50x50-'
    analyze_all(scenario_list, basedirname)
