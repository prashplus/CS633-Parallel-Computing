# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 20:48:21 2019

@author: Sanket
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import sys
import numpy as np

def function(name,save):
    matplotlib.rc('figure', figsize=(13, 7))

    file = open(name, "r")

    X, Y, Z = [], [], []
    A, B, C, D= [], [], [], []

    for l in file:
        row = l.split()
        A.append(float(row[0].lstrip().rstrip()))
        A.append(float(row[1].lstrip().rstrip()))
        A.append(float(row[2].lstrip().rstrip()))
        B.append(A)
        A = []

    file.close()

    for i in range(30):
        for j in range(30):
            for k in range(9000):
                if B[k][0] == i and B[k][1] == j:
                    A.append(B[k][0])
                    A.append(B[k][1])
                    A.append(B[k][2])
                    C.append(A)
                    A = []
            #D = C[C[:,2].argsort()]
            sorted(C,key=lambda x: x[2])
            X.append(C[5][0])
            Y.append(C[5][1])
            Z.append(C[5][2])
            C = []
                

    data = pd.DataFrame({'X': X, 'Y': Y, 'Z': Z})
    data_pivoted = data.pivot("Y", "X", "Z")
    #ax = sns.heatmap(data_pivoted)
    ax = sns.heatmap(data_pivoted,vmin=0,vmax=200)
    plt.savefig(save)
    plt.show()
    print("Done:"+name)

if __name__ == "__main__":
    function('data11.txt','plot-64.png')
    function('data22.txt','plot-512.png')
    function('data33.txt','plot-2048.png')