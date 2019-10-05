import os
import matplotlib.pyplot as plt
import numpy as np
import statistics

def function(name,save):
    with open(name) as f:
        lines = f.readlines()
        z = [line.split()[0] for line in lines]

    rows, cols = (30, 10) 
    data_set = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(0,len(z)):
        if i%2 == 0:
            if i < 20:
                data_set[0].append(z[i])
            if i < 40:
                data_set[1].append(z[i])
            if i < 60:
                data_set[2].append(z[i])
            if i < 80:
                data_set[3].append(z[i])
            if i < 100:
                data_set[4].append(z[i])
            if i < 120:
                data_set[5].append(z[i])
            if i < 140:
                data_set[6].append(z[i])
            if i < 160:
                data_set[7].append(z[i])
            if i < 180:
                data_set[8].append(z[i])
            if i < 200:
                data_set[9].append(z[i])
            if i < 220:
                data_set[10].append(z[i])
            if i < 240:
                data_set[11].append(z[i])
            if i < 260:
                data_set[12].append(z[i])
            if i < 280:
                data_set[13].append(z[i])
            if i < 300:
                data_set[14].append(z[i])
        else:
            if i < 20:
                data_set[15].append(z[i])
            if i < 40:
                data_set[16].append(z[i])
            if i < 60:
                data_set[17].append(z[i])
            if i < 80:
                data_set[18].append(z[i])
            if i < 100:
                data_set[19].append(z[i])
            if i < 120:
                data_set[20].append(z[i])
            if i < 140:
                data_set[21].append(z[i])
            if i < 160:
                data_set[22].append(z[i])
            if i < 180:
                data_set[23].append(z[i])
            if i < 200:
                data_set[24].append(z[i])
            if i < 220:
                data_set[25].append(z[i])
            if i < 240:
                data_set[26].append(z[i])
            if i < 260:
                data_set[27].append(z[i])
            if i < 280:
                data_set[28].append(z[i])
            if i < 300:
                data_set[29].append(z[i])

    
    a0=np.asarray(data_set[0]).astype(np.float) 
    a1=np.asarray(data_set[1]).astype(np.float)
    a2=np.asarray(data_set[2]).astype(np.float)
    a3=np.asarray(data_set[3]).astype(np.float)
    a4=np.asarray(data_set[4]).astype(np.float)
    a5=np.asarray(data_set[5]).astype(np.float)
    a6=np.asarray(data_set[6]).astype(np.float)
    a7=np.asarray(data_set[7]).astype(np.float)
    a8=np.asarray(data_set[8]).astype(np.float)
    a9=np.asarray(data_set[9]).astype(np.float)
    a10=np.asarray(data_set[10]).astype(np.float)
    a11=np.asarray(data_set[11]).astype(np.float)
    a12=np.asarray(data_set[12]).astype(np.float)
    a13=np.asarray(data_set[13]).astype(np.float)
    a14=np.asarray(data_set[14]).astype(np.float)
    a15=np.asarray(data_set[15]).astype(np.float)
    a16=np.asarray(data_set[16]).astype(np.float)
    a17=np.asarray(data_set[17]).astype(np.float)
    a18=np.asarray(data_set[18]).astype(np.float)
    a19=np.asarray(data_set[19]).astype(np.float)
    a20=np.asarray(data_set[20]).astype(np.float)
    a21=np.asarray(data_set[21]).astype(np.float)
    a22=np.asarray(data_set[22]).astype(np.float)
    a23=np.asarray(data_set[23]).astype(np.float)
    a24=np.asarray(data_set[24]).astype(np.float)
    a25=np.asarray(data_set[25]).astype(np.float)
    a26=np.asarray(data_set[26]).astype(np.float)
    a27=np.asarray(data_set[27]).astype(np.float)
    a28=np.asarray(data_set[28]).astype(np.float)
    a29=np.asarray(data_set[29]).astype(np.float)

    data_a = [a0,a1,a2,a3,a4]
    data_b = [a5,a6,a7,a8,a9]
    data_c = [a10,a11,a12,a13,a14]
    data_d = [a15,a16,a17,a18,a19]
    data_e = [a20,a21,a22,a23,a24]
    data_f = [a25,a26,a27,a28,a29]

    ticks = ['A', 'B', 'C', 'D', 'E']

    def set_box_color(bp, color):
        plt.setp(bp['boxes'], color=color)
        plt.setp(bp['whiskers'], color=color)
        plt.setp(bp['caps'], color=color)
        plt.setp(bp['medians'], color=color)

    plt.figure()

    b1 = plt.boxplot(data_a, positions=np.array(range(len(data_a)))*2.0, sym='', widths=0.6)
    b2 = plt.boxplot(data_b, positions=np.array(range(len(data_b)))*2.0, sym='', widths=0.6)
    b3 = plt.boxplot(data_c, positions=np.array(range(len(data_c)))*2.0, sym='', widths=0.6)
    b4 = plt.boxplot(data_d, positions=np.array(range(len(data_d)))*2.0, sym='', widths=0.6)
    b5 = plt.boxplot(data_e, positions=np.array(range(len(data_e)))*2.0, sym='', widths=0.6)
    b6 = plt.boxplot(data_f, positions=np.array(range(len(data_f)))*2.0, sym='', widths=0.6)

    s1 = [a0,a1,a2,a3,a4]
    s11 = statistics.median(a0)
    s12 = statistics.median(a1)
    s13 = statistics.median(a2)
    s14 = statistics.median(a3)
    s15 = statistics.median(a4)
    y = [0, 2, 4, 6, 8]
    x = [s11, s12, s13, s14, s15]
    plt.plot(y,x,linewidth=4,color='y',label='PPN 2 (OLD Bcast)')

    s2 = [a5,a6,a7,a8,a9]
    s21 = statistics.median(a5)
    s22 = statistics.median(a6)
    s23 = statistics.median(a7)
    s24 = statistics.median(a8)
    s25 = statistics.median(a9)
    y = [0, 2, 4, 6, 8]
    x = [s21, s22, s23, s24, s25]
    plt.plot(y,x,linewidth=4,color='r',label='PPN 4 (OLD Bcast)')

    s3 = [a10,a11,a12,a13,a14]
    s31 = statistics.median(a10)
    s32 = statistics.median(a11)
    s33 = statistics.median(a12)
    s34 = statistics.median(a13)
    s35 = statistics.median(a14)
    y = [0, 2, 4, 6, 8]
    x = [s31, s32, s33, s34, s35]
    plt.plot(y,x,linewidth=4,color='b',label='PPN 8 (OLD Bcast)')

    s4 = [a15,a16,a17,a18,a19]
    s41 = statistics.median(a15)
    s42 = statistics.median(a16)
    s43 = statistics.median(a17)
    s44 = statistics.median(a18)
    s45 = statistics.median(a19)
    y = [0, 2, 4, 6, 8]
    x = [s41, s42, s43, s44, s45]
    plt.plot(y,x,linewidth=4,color='g',label='PPN 2 (NEW Bcast)')

    s5 = [a20,a21,a22,a23,a24]
    s51 = statistics.median(a20)
    s52 = statistics.median(a21)
    s53 = statistics.median(a22)
    s54 = statistics.median(a23)
    s55 = statistics.median(a24)
    y = [0, 2, 4, 6, 8]
    x = [s51, s52, s53, s54, s55]
    plt.plot(y,x,linewidth=4,color='m',label='PPN 4 (NEW Bcast)')

    s6 = [a25,a26,a27,a28,a29]
    s61 = statistics.median(a25)
    s62 = statistics.median(a26)
    s63 = statistics.median(a27)
    s64 = statistics.median(a28)
    s65 = statistics.median(a29)
    y = [0, 2, 4, 6, 8]
    x = [s61, s62, s63, s64, s65]
    plt.plot(y,x,linewidth=4,color='c',label='PPN 8 (NEW Bcast)')

    plt.xlabel('Data (KB)')
    plt.ylabel('Bandwidth (Mbps)')
    plt.xticks([0,2,4,6,8],['64','256','512','2048','4096'])
    plt.legend()

    # plt.xticks(range(0, len(ticks) * 2, 2), ticks)
    # plt.xlim(-2, len(ticks)*2)
    # plt.ylim(0, 8)
    # plt.tight_layout()
    plt.savefig(save)

if __name__ == "__main__":
    function('data1.txt','plot-8.png')
    function('data2.txt','plot-16.png')
    function('data3.txt','plot-32.png')