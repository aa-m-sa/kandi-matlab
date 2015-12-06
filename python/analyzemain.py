#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script. Analyze and plot all
"""

import saiotools
import sadistance
import numpy as np

selectedTargetSetsA = [(2,8),
                       (4,1),
                       (5,2)]
selectedTarget2 = [(2,13)]
selectedTarget3 = [(3,1),
                   (3,3)]
selectedTargetSets = selectedTargetSetsA
selectedTargetSets.extend(selectedTarget2)
selectedTargetSets.extend(selectedTarget3)

def create_selected_target_ims(targetData):
    selected = []
    for c, p in selectedTargetSets:
        selected.append(targetData[c].dataSets[p-1])
    return selected, selectedTargetSets

def error_rates_final(circleSetResultData, targetData, measure):
    """
    Returns error rates of final state of each walker.
    """
    pass

def analyze_circleSet(circleSetData, circleSetResultData, targetData, meta):
    """
    :circleSetData: a dict of saiotools.EnsembleData objects
    :circleSetResultData: dict of saiotools.ResultsData objects
    :targetData: a TargetData object
    :meta: some meta information from filename
    """

    print '-'
    print meta['origFilename'], meta['tempConst'], meta['maxLen']

    for s in circleSetData:
        ensemble = circleSetData[s]
        error_rates = dict()
        for walker in xrange(ensemble.ensembleSize):
            # something we want for every walker
            pass

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
            circleSetData, circleSetResultData = saiotools.load_set2_full(basedirname + s + '-' + circleSet)
            meta = saiotools.parse_meta(s)
            numCircles = int(circleSet[1])
            meta['numCircles'] = numCircles
            meta['scenario'] = s
            analyze_circleSet(circleSetData, circleSetResultData, targetData[numCircles], meta)

def analyze_particular(scenario, basedirname, circleSet):
    targetData = saiotools.load_set2_target()
    circleSetData = saiotools.load_set2_full(basedirname + s + '-' + circleSet)
    meta = saiotools.parse_meta(s)
    numCircles = int(circleSet[1])
    meta['numCircles'] = numCircles
    meta['scenario'] = s

    # alternatively
    analyze_circleSet(circleSetData, targetData[numCircles], meta)

    ## pick an ensemble
    #ensemble = 
    #walker = 

    ## pick walker
    ## error rate evolution of a walker
    #error_rates[walker] = error_rate_evo(ensemble.circles[walker], ensemble.iterNums[walker], targetData.targets[s-1], sadistance.naive_dist)
    # energy evolution of a walker

if __name__ == "__main__":
    scenario_list = ['t99-n1000',
                     't98-n1000',
                     't96-n600',
                     't94-n600',
                     't90-n600']

    basedirname = '../testdata-annealingset2b-50x50-'
    #analyze_all(scenario_list, basedirname)
    #analyze_particular('')
