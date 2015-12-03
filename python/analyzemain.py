#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script. Analyze and plot all
"""

import saiotools

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

def error_rates(circleSetData, targetData, measure):
    """
    Returns error rate evolution for walker in scenario.
    """
    #base = measure(dataCircles, trueCircles)
    # TODO
    pass

def error_rates_final(circleSetResultData, targetData, measure):
    """
    Returns error rates of final state of each walker.
    """
    #TODO
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

def analyze_all(scenario_list, basedirname):
    """
    Handles all scenarios:
        - load scenario
        - analyze
        - save results
        (- handle stuff that uses all data gathered on previous rounds?)
    """

    # original targets for each circle set in dataset
    target_data = satools.load_set2_target()

    # scenario: same annealing schedule and other related settings
    # scenario includes multiple circleDatas
    data = dict()
    for s in scenario_list:
        for circleSet in ['c1-', 'c2-', 'c3-', 'c4-', 'c5-']:
            circleSetData = saiotools.load_set2_full(basedirname + s + circleSet)
            meta = saiotools.parse_meta(s)
            numCircles = int(circleSet[1])
            meta['numCircles'] = numCircles
            analyze_circleSet(circleSetData, targetData[numCircles], meta)

if __name__ == "__main__":
    scenario_list = ['t99-n1000',
                     't98-n800',
                     't96-n600',
                     't94-n600',
                     't90-n600']

    basedirname = 'testdata-annealingset2b-50x50-'
    analyze_all(scenario_list, basedirname)
