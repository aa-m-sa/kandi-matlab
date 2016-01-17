#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script. Produce some plots (related to landscape pics of chapter 3 but not created with octave/matlab).
"""

import scipy.io
import numpy as np

import saviz
import analyzemain

def main():
    data1 = scipy.io.loadmat('../matlab/golfholedata.mat')
    f1, ax1 = saviz.plot_dataset(data1['A_data'])
    analyzemain.fig_print_routines(f1, 'golfholedata')

    data2 = scipy.io.loadmat('../matlab/localmindata.mat')
    f2, ax2 = saviz.plot_dataset(data2['A_data'])
    analyzemain.fig_print_routines(f2, 'localmindata')

if __name__ == "__main__":
    main()
