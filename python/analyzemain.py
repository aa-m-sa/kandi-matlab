#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script. Analyze and plot all
"""

import numpy as np
import copy

import saiotools
import sadistance
import saviz


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

def find_energy_mode(enData):
    """Find mode of a binned energy histogram.
    (= Bin with most elements.)

    :enData: TODO
    :returns: energies, indices, circles
        of in the mode (bin)

    """
    energies = np.array([e[0,-1] for e in enData.energies])
    hist, edges = np.histogram(energies, bins=20)
    mbin = np.argmax(hist)
    indsInBin = [i for i,e in enumerate(enData.energies) if (e[0,-1] >= edges[mbin] and (e[0,-1] < edges[mbin + 1] or e[0,-1] == edges[-1]))]
    enerInBin = [e[0,-1] for e in enData.energies[indsInBin]]
    circInBin = [c[-1] for c in enData.circles[indsInBin]]
    return enerInBin, indsInBin, circInBin


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

def run_print_plotters():
    """
    Get data an call print routines from saviz for plotting the prints.
    """

    t = saiotools.load_set2_target()

    tImsAll, tCircsAll, tDescsAll = pick_selected_target_ims(t)
    f1, ax1 = saviz.plot_datasets_2x3(tImsAll, tDescsAll)

    tImsA, tCircsA, tDescsA = pick_selected_target_ims(t, sList=selectedTargetSetsA)

    resA_slow = pick_nload_selected_all_results(sTargetList=selectedTargetSetsA, sDataResults=selectedDataResultsA_slow)
    resA_fast = pick_nload_selected_all_results(sTargetList=selectedTargetSetsA, sDataResults=selectedDataResultsA_fast)

    bestEnergiesA_slow, bestEnergyIndsA_slow, bestEnergyCirclesA_slow = pick_best_energy_results_A(resA_slow)
    bestEnergiesA_fast, bestEnergyIndsA_fast, bestEnergyCirclesA_fast = pick_best_energy_results_A(resA_fast)

    f2, ax2 = saviz.plot_3datasets_results(tImsA, tDescsA, bestEnergyCirclesA_slow, tCircsA)
    f3, ax3 = saviz.plot_3datasets_results(tImsA, tDescsA, bestEnergyCirclesA_fast, tCircsA)

    f4, ax4 = saviz.final_energies_histo3([e for e,r in resA_slow])
    f5, ax5 = saviz.final_energies_histo3([e for e,r in resA_fast])

    f6, ax6 = saviz.final_energies_histo_k_compare([e for e,r in resA_slow],[e for e,r in resA_fast], k=3, descriptors=('Hidas', 'Nopea'))

    # plot circles in the mode bin
    modeWalkersFast = []
    for (e,r), t in zip(resA_fast, tCircsA):
        be, bi, bc = find_energy_mode(e)
        print 'min', np.min([ei[0,-1] for ei in e.energies])
        print bi, len(bc)
        print be
        bc, bi = np.array(bc), np.array(bi)
        saviz.plot_all_circles(bc[np.argsort(be)], t)
        modeWalkersFast.append(bi[np.argsort(be)[0]])

    modeWalkersSlow = []
    for (e,r), t in zip(resA_slow, tCircsA):
        be, bi, bc = find_energy_mode(e)
        print 'min', np.min([ei[0,-1] for ei in e.energies])
        print bi, len(bc)
        print be
        bc, bi = np.array(bc), np.array(bi)
        saviz.plot_all_circles(bc[np.argsort(be)], t)
        modeWalkersSlow.append(bi[np.argsort(be)[0]])
    #TODO handpick a bin
    #TODO mark bins in a histogram (vertical line?)

    sbi, smi = bestEnergyIndsA_slow[1], modeWalkersSlow[1]
    print sbi, smi
    enData_s, resData_s = resA_slow[1]
    fbi, fmi = bestEnergyIndsA_fast[1], modeWalkersFast[1]
    print fbi, fmi
    enData_f, resData_f = resA_fast[1]

    f7, ax7 = saviz.walker_temp_compare_1([enData_s.energies[sbi],enData_s.energies[smi]],
                                          [enData_s.temps[sbi], enData_s.temps[smi]],
                                          [enData_f.energies[fbi],enData_f.energies[fmi]],
                                          [enData_f.temps[fbi], enData_f.temps[fmi]])


    #print 'errors'
    #beErrors_slow = get_best_enery_error_rates(bestEnergyCirclesA_slow, tCircsA, measure=sadistance.naive_dist)
    #beErrors_fast = get_best_enery_error_rates(bestEnergyCirclesA_fast, tCircsA, measure=sadistance.naive_dist)
    #TODO latex table format





if __name__ == "__main__":
    scenario_list_all = ['t99-n1000',
                         't98-n1000',
                         't96-n600',
                         't94-n600',
                         't90-n600']

    basedirname = '../testdata-annealingset2b-50x50-'
    #analyze_all(scenario_list, basedirname)
    run_print_plotters()
