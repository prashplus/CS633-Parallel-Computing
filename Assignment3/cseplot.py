import numpy as np
import matplotlib.pyplot as plt
import statistics

#Function to read from file
def readFromFile(fileName):
    with open(fileName) as f:
        lines = f.readlines()

    lines = [x.strip() for x in lines]
    data=[]
    for strngs in lines:
        o=[]
        for t in strngs.split():
            o.append(float(t))
        data.append(o);
    preproc = [row[0] for row in data]
    cluster = [row[1] for row in data]
    total = [row[2] for row in data]

    preproc1 = []
    clstr1 = []
    total1 = []

    for i in range(16):
        preproc1.append(preproc[i * 5:(i + 1) * 5])
        clstr1.append(cluster[i * 5:(i + 1) * 5])
        total1.append(total[i * 5:(i + 1) * 5])
    return preproc1, clstr1, total1


files = ["cse/data1/time1.txt","cse/data2/time2.txt"]
images = ["cse/data1/plot.png","cse/data2/plot.png"]

for set in range(2):
    preProc, cluster, total = readFromFile(files[set])

    pmid = []
    cmid = []
    tmid = []
    for i in range(16):
        pmid.append(float(statistics.median(preProc[i])))
        cmid.append(float(statistics.median(cluster[i])))
        tmid.append(float(statistics.median(total[i])))

    fig1, ax1 = plt.subplots()
    ax1.set_title('Time Plot')
    plt.xlabel("Number of processes")
    plt.ylabel("Time(s)")
    xx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    ax1.boxplot(preProc, labels=xx)
    ax1.plot(xx, pmid, label="Average preprocessing time")
    plt.legend()

    ax1.boxplot(cluster, labels=xx)
    ax1.plot(xx, cmid, label="Average processing time")
    plt.legend()

    ax1.boxplot(total, labels=xx)
    ax1.plot(xx, tmid, label="Total time")
    plt.legend()

    plt.savefig(images[set])
    plt.show()