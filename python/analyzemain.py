#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script. Analyze and plot all
"""

import numpy as np
from matplotlib import pyplot as plt
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

selectedDataResults3_slow = 't99-n1000'
selectedDataResults3_med  = 't94-n600'
selectedDataResults3_fast = 't90-n600'

selectedDataResults2_t99 = 't99-n1000'
selectedDataResults2_t98 = 't98-n1000'
selectedDataResults2_t96 = 't96-n600'
selectedDataResults2_t94 = 't94-n600'
selectedDataResults2_t90 = 't90-n600'

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

def pick_best_energy_results(s):
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

def display_modalbin_circle_centers(res, tCircs, title=""):
    modeWalkers = []
    f_ax = []
    for (e,r), t in zip(res, tCircs):
        be, bi, bc = find_energy_mode(e)
        print 'min', np.min([ei[0,-1] for ei in e.energies])
        print bi, len(bc)
        print be
        bc, bi = np.array(bc), np.array(bi)
        f, ax = saviz.plot_all_circles(bc[np.argsort(be)], t)
        if not title == "":
            ax.set_title(title)
        f_ax.append((f, ax))
        #modeWalkers.append(bi[np.argsort(be)[0]]) #smallest element
        med = np.floor(len(be)/2)
        modeWalkers.append(bi[np.argsort(be)[med]]) #median element
    return modeWalkers, f_ax

def fig_print_routines(fig, fname):
    #pdf
    fig.savefig(fname + '.pdf', dpi=300)
    #eps
    fig.savefig(fname + '.eps', dpi=100)
    #png
    fig.savefig(fname + '.png', dpi=300)

def run_print_plotters_all_A(printfigs=False):
    """
    Get data an call print routines from saviz for plotting the prints.
    selectedTargetSetsA and selectedTargetSets (all)
    """
    plt.close('all')

    t = saiotools.load_set2_target()

    tImsAll, tCircsAll, tDescsAll = pick_selected_target_ims(t)
    f1, ax1 = saviz.plot_datasets_2x3(tImsAll, tDescsAll)
    if printfigs:
        fig_print_routines(f1, 'all_datasets')

    tImsA, tCircsA, tDescsA = pick_selected_target_ims(t, sList=selectedTargetSetsA)

    resA_slow = pick_nload_selected_all_results(sTargetList=selectedTargetSetsA, sDataResults=selectedDataResultsA_slow)
    resA_fast = pick_nload_selected_all_results(sTargetList=selectedTargetSetsA, sDataResults=selectedDataResultsA_fast)

    bestEnergiesA_slow, bestEnergyIndsA_slow, bestEnergyCirclesA_slow = pick_best_energy_results(resA_slow)
    bestEnergiesA_fast, bestEnergyIndsA_fast, bestEnergyCirclesA_fast = pick_best_energy_results(resA_fast)

    f2, ax2 = saviz.plot_kdatasets_results(tImsA, tDescsA, bestEnergyCirclesA_slow, tCircsA, k=3)
    f3, ax3 = saviz.plot_kdatasets_results(tImsA, tDescsA, bestEnergyCirclesA_fast, tCircsA, k=3)
    if printfigs:
        fig_print_routines(f2, 'A_datasets_res_slow')
        fig_print_routines(f3, 'A_datasets_res_fast')

    f4, ax4 = saviz.final_energies_histo3([e for e,r in resA_slow])
    f5, ax5 = saviz.final_energies_histo3([e for e,r in resA_fast])
    # we add stuff to ax4,ax5 later

    f6, ax6 = saviz.final_energies_histo_k_compare([e for e,r in resA_slow],[e for e,r in resA_fast], k=3, descriptors=('Hidas', 'Nopea'))

    # plot circles in the mode bin
    modeWalkersFast, f_ax_WF = display_modalbin_circle_centers(resA_fast, tCircsA, title='0.90')
    modeWalkersSlow, f_ax_WS = display_modalbin_circle_centers(resA_slow, tCircsA, title='0.99')
    if printfigs:
        for i, (f, ax) in enumerate(f_ax_WF):
            fig_print_routines(f, 'A_modalbin_cc_fast_' + str(i))
        for i, (f, ax) in enumerate(f_ax_WS):
            fig_print_routines(f, 'A_modalbin_cc_slow_' + str(i))


    #TODO handpick a bin
    #TODO mark bins in a histogram (vertical line?)

    sbi, smi = bestEnergyIndsA_slow[1], modeWalkersSlow[1]
    print sbi, smi
    enData_s, resData_s = resA_slow[1]
    fbi, fmi = bestEnergyIndsA_fast[1], modeWalkersFast[1]
    print fbi, fmi
    enData_f, resData_f = resA_fast[1]


    #ax6[1].axvline(enData_s.energies[sbi].squeeze()[-1], color='blue', linestyle='dashed')
    #ax6[1].axvline(enData_s.energies[smi].squeeze()[-1], color='blue', linestyle='dashed')
    #ax6[1].axvline(enData_f.energies[fbi].squeeze()[-1], color='green', linestyle='dashed')
    #ax6[1].axvline(enData_f.energies[fmi].squeeze()[-1], color='green', linestyle='dashed')
    if printfigs:
        fig_print_routines(f6, 'A_histo_compare_3_slow_fast')

    ax4[1].axvline(enData_s.energies[sbi].squeeze()[-1], color='blue', linestyle='dashed')
    ax4[1].axvline(enData_s.energies[smi].squeeze()[-1], color='blue', linestyle='dashed')
    ax5[1].axvline(enData_f.energies[fbi].squeeze()[-1], color='blue', linestyle='dashed')
    ax5[1].axvline(enData_f.energies[fmi].squeeze()[-1], color='blue', linestyle='dashed')

    if printfigs:
        fig_print_routines(f4, 'A_final_histo3_slow')
        fig_print_routines(f5, 'A_final_histo3_fast')

    f7, ax7 = saviz.walker_temp_compare_1([enData_s.energies[sbi],enData_s.energies[smi]],
                                          [enData_s.temps[sbi], enData_s.temps[smi]],
                                          [enData_f.energies[fbi],enData_f.energies[fmi]],
                                          [enData_f.temps[fbi], enData_f.temps[fmi]])

    if printfigs:
        fig_print_routines(f7, 'A_walker_temp_compare')

    f8, ax8 = saviz.best_final_energy_walkers([e for e,r in resA_slow])
    if printfigs:
        fig_print_routines(f8, 'A_best_final_e_walkers_slow')

    f9, ax9 = saviz.best_final_energy_walkers([e for e,r in resA_fast])

    if printfigs:
        fig_print_routines(f9, 'A_best_final_e_walkers_fast')

    #print 'errors'
    beErrors_slow = get_best_enery_error_rates(bestEnergyCirclesA_slow, tCircsA, measure=sadistance.naive_dist)
    beErrors_fast = get_best_enery_error_rates(bestEnergyCirclesA_fast, tCircsA, measure=sadistance.naive_dist)
    #TODO latex table format


    if not printfigs:
        plt.show()


def run_print_plotters_3(printfigs=False):
    """Set 3: compare two pics of three circles"""
    plt.close('all')

    t = saiotools.load_set2_target()

    tIms3, tCircs3, tDescs3 = pick_selected_target_ims(t, sList=selectedTarget3)

    res3_slow = pick_nload_selected_all_results(sTargetList=selectedTarget3, sDataResults=selectedDataResults3_slow)
    res3_med  = pick_nload_selected_all_results(sTargetList=selectedTarget3, sDataResults=selectedDataResults3_med)
    res3_fast = pick_nload_selected_all_results(sTargetList=selectedTarget3, sDataResults=selectedDataResults3_fast)

    bestEnergies3_slow, bestEnergyInds3_slow, bestEnergyCircles3_slow = pick_best_energy_results(res3_slow)
    bestEnergies3_med,  bestEnergyInds3_med,  bestEnergyCircles3_med  = pick_best_energy_results(res3_med)
    bestEnergies3_fast, bestEnergyInds3_fast, bestEnergyCircles3_fast = pick_best_energy_results(res3_fast)

    f1, ax1 = saviz.plot_kdatasets_results(tIms3, tDescs3, bestEnergyCircles3_slow, tCircs3, k=2)
    f1.suptitle('0.99', fontsize=12)
    f2, ax2 = saviz.plot_kdatasets_results(tIms3, tDescs3, bestEnergyCircles3_fast, tCircs3, k=2)
    f2.suptitle('0.94', fontsize=12)
    f3, ax3 = saviz.plot_kdatasets_results(tIms3, tDescs3, bestEnergyCircles3_med, tCircs3, k=2)
    f3.suptitle('0.90', fontsize=12)

    if printfigs:
        fig_print_routines(f1, 'set3_datasets_res_099')
        fig_print_routines(f2, 'set3_datasets_res_094')
        fig_print_routines(f3, 'set3_datasets_res_090')

    f4, ax4 = saviz.final_energies_histo_k_compare([e for e,r in res3_slow],[e for e,r in res3_fast], k=2, descriptors=('Hidas', 'Nopea'))
    if printfigs:
        fig_print_routines(f4, 'set3_histo_compare_2_099_090')

    # plot circles in the mode bin
    modeWalkersFast, f_ax_WF = display_modalbin_circle_centers(res3_fast, tCircs3, title='0.90')
    modeWalkersSlow, f_ax_WS = display_modalbin_circle_centers(res3_slow, tCircs3, title='0.99')
    if printfigs:
        for i, (f, ax) in enumerate(f_ax_WF):
            fig_print_routines(f, 'set3_modalbin_cc_090_' + str(i))
        for i, (f, ax) in enumerate(f_ax_WS):
            fig_print_routines(f, 'set3_modalbin_cc_099_' + str(i))

    #TODO (also here) mark bins in a histogram (vertical line?)

    sbi, smi = bestEnergyInds3_slow[0], modeWalkersSlow[0]
    print sbi, smi
    enData_s, resData_s = res3_slow[0]
    fbi, fmi = bestEnergyInds3_fast[0], modeWalkersFast[0]
    print fbi, fmi
    enData_f, resData_f = res3_fast[0]

    f5, ax5 = saviz.walker_temp_compare_1([enData_s.energies[sbi],enData_s.energies[smi]],
                                          [enData_s.temps[sbi], enData_s.temps[smi]],
                                          [enData_f.energies[fbi],enData_f.energies[fmi]],
                                          [enData_f.temps[fbi], enData_f.temps[fmi]])

    if printfigs:
        fig_print_routines(f5, 'set3_walker_temp_compare')

    #ax4[0].axvline(x=enData_s.energies[sbi][0,-1], color='blue', linestyle='solid')
    #ax4[0].axvline(enData_s.energies[smi].squeeze()[-1], color='blue', linestyle='dashed')
    #ax4[0].axvline(enData_f.energies[fbi].squeeze()[-1], color='green', linestyle='solid')
    #ax4[0].axvline(enData_f.energies[fmi].squeeze()[-1], color='green', linestyle='dashed')


    f6, ax6 = saviz.best_final_energy_walkers([e for e,r in res3_slow])
    f6.suptitle('0.99', fontsize=12)
    f7, ax7 = saviz.best_final_energy_walkers([e for e,r in res3_fast])
    f7.suptitle('0.90', fontsize=12)
    f8, ax8 = saviz.best_final_energy_walkers([e for e,r in res3_med])
    f8.suptitle('0.94', fontsize=12)


    if printfigs:
        fig_print_routines(f6, 'set3_best_final_e_walkers_099')
        fig_print_routines(f7, 'set3_best_final_e_walkers_090')
        fig_print_routines(f8, 'set3_best_final_e_walkers_094')

    #print 'errors'
    beErrors_slow = get_best_enery_error_rates(bestEnergyCircles3_slow, tCircs3, measure=sadistance.naive_dist)
    beErrors_med = get_best_enery_error_rates(bestEnergyCircles3_med, tCircs3, measure=sadistance.naive_dist)
    beErrors_fast = get_best_enery_error_rates(bestEnergyCircles3_fast, tCircs3, measure=sadistance.naive_dist)
    #TODO latex table format


    if not printfigs:
        plt.show()


def run_print_plotters_2(printfigs=False):
    """Set 2: one pic of 2 circles"""
    plt.close('all')

    t = saiotools.load_set2_target()

    tIms2, tCircs2, tDescs2 = pick_selected_target_ims(t, sList=selectedTarget2)

    sl = [selectedDataResults2_t99,
          selectedDataResults2_t98,
          selectedDataResults2_t96,
          selectedDataResults2_t94,
          selectedDataResults2_t90]

    res2l = []
    res2lt = ['0.99','0.98','0.96','0.94','0.90']

    for s in sl:
        res2tmp = pick_nload_selected_all_results(sTargetList=selectedTarget2, sDataResults=s)
        res2l.append(res2tmp)

    bestET = []
    for res2 in res2l:
        bestEnergies2_t, bestEnergyInds2_t, bestEnergyCircles2_t = pick_best_energy_results(res2)
        bestET.append((bestEnergies2_t, bestEnergyInds2_t, bestEnergyCircles2_t))

    ft1, axt1 = [], []
    for (bes, beis, becircles), title in zip(bestET, res2lt):
        ft, axt = saviz.plot_kdatasets_results(tIms2, tDescs2, becircles, tCircs2, k=1)
        ft.suptitle(title, fontsize=12)
        ft1.append(ft)
        axt1.append(axt)
        if printfigs:
            fig_print_routines(ft, 'set2_datasets_res_' + title[2:])

    #f4, ax4 = saviz.final_energies_histo_k_compare([e for e,r in res3_slow],[e for e,r in res3_fast], k=2, descriptors=('Hidas', 'Nopea'))
    # ^ would be too crowded (5 temps)


    ft2, axt2 = [], []
    for res2, title in zip(res2l, res2lt):
        e = res2[0][0]
        ft, axt = saviz.final_energies_histo(e)
        axt.set_title(title)
        ft2.append(ft)
        axt2.append(axt)
        if printfigs:
            fig_print_routines(ft, 'set2_final_histo_' + title[2:])

    # plot circles in the mode bin
    ft3, axt3 = [], []
    for res2, title in zip(res2l, res2lt):
        modeWalkers, f_ax_t = display_modalbin_circle_centers(res2, tCircs2, title=title)
        ft3.append(f_ax_t[0][0])
        axt3.append(f_ax_t[0][1])
        if printfigs:
            fig_print_routines(f_ax_t[0][0], 'set2_modalbin_cc_' + title[2:])


    # just plot the best, no comp
    energies_toplot = []
    temps_toplot = []
    for res2, (_, inds, _) in zip(res2l, bestET):
        enData, resData = res2[0]
        bi = inds[0]
        energies_toplot.append(enData.energies[bi])
        temps_toplot.append(enData.temps[bi])

    f4, axs4 = saviz.walker_temp(energies_toplot, temps_toplot, res2lt)
    if printfigs:
        fig_print_routines(f4, 'set2_walkers_temp')

    # just plot walkers
    #for res2, title in zip(res2l, res2lt):
    #    f, ax = saviz.best_final_energy_walkers([e for e,r in res2])
    #    f.suptitle(title, fontsize=12)
    #    ft5.append(f)
    #    axt5.append(ax)
    f5, ax5 = saviz.best_final_energy_walkers([res[0][0] for res in res2l], res2lt)
    if printfigs:
        fig_print_routines(f5, 'set2_best_final_e_walkers')


    #TODO print 'errors'


    if not printfigs:
        plt.show()


if __name__ == "__main__":
    scenario_list_all = ['t99-n1000',
                         't98-n1000',
                         't96-n600',
                         't94-n600',
                         't90-n600']

    basedirname = '../testdata-annealingset2b-50x50-'
    #analyze_all(scenario_list, basedirname)
    run_print_plotters_all_A(True)
    run_print_plotters_3(True)
    run_print_plotters_2(True)
