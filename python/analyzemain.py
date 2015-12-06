#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script. Analyze and plot all
"""

import saiotools
import sadistance
import numpy as np
import copy

# selected: reserved globals

selectedTargetSetsA = [(2,8),
                       (4,1),
                       (5,2)]
selectedTarget2 = [(2,13)]
selectedTarget3 = [(3,1),
                   (3,3)]
selectedTargetSets =copy.deepcopy(selectedTargetSetsA)
selectedTargetSets.extend(selectedTarget2)
selectedTargetSets.extend(selectedTarget3)

selectedBasedirname = '../testdata-annealingset2b-50x50-'
selectedDataResultsA_slow = 't99-n1000'
selectedDataResultsA_fast = 't90-n600'

def pick_selected_target_ims(targetData, sList=selectedTargetSets):
    selected = []
    selectedCirc = []
    for c, p in sList:
        selected.append(targetData[c].dataSets[p-1])
        selectedCirc.append(targetData[c].targets[p-1])
    return selected, selectedCirc, selectedTargetSets

def pick_nload_selected_all_results(sTargetList=selectedTargetSetsA, sDataResults=selectedDataResultsA_slow):
    res = []
    for c, p in sTargetList:
        dirStr = selectedBasedirname + sDataResults + '-c' + str(c) + '-/'
        enData, resData = saiotools.load_set2_full(dirStr)
        res.append((enData[p], resData[p]))
    return res

def pick_best_energy_results_A(s):
    """:s: res above"""
    bestEnergies =[]
    bestEnergyInds =[]
    bestEnergyCircles =[]

    for enData, resData in s:
        energies = np.array([e[0,-1] for e in enData.energies])
        bestEnergies.append(np.min(energies))
        bestInd = np.argmin(energies)
        bestEnergyInds.append(bestInd)
        bestEnergyCircles.append(resData.circles[bestInd])

    return bestEnergies, bestEnergyInds, bestEnergyCircles

def get_best_enery_error_rates(bestEnergyCircles, targets, measure=sadistance.naive_dist):
    """
    'helpful' almost oneliner

    :bestEnergyCircles:list
    :targets: corresponding targets
    :returns: list of measure output for circ, target pairs
    """

    return [measure(circs,ts) for circs, ts in zip(bestEnergyCircles, targets)]


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
    Very slow, very stupid, do not use.
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
    #

if __name__ == "__main__":
    scenario_list = ['t99-n1000',
                     't98-n1000',
                     't96-n600',
                     't94-n600',
                     't90-n600']

    basedirname = '../testdata-annealingset2b-50x50-'
    #analyze_all(scenario_list, basedirname)
    #analyze_particular('')
