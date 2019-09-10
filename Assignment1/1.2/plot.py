import os
import matplotlib.pyplot as plt
import numpy as np
import statistics

with open('data.txt') as f:
    lines = f.readlines()
    z = [line.split()[0] for line in lines]

rows, cols = (24, 5) 
data_set = [[0 for i in range(cols)] for j in range(rows)]

for i in range(0,len(z)):
    if i%2 == 0:
        if i < 10:
            data_set[0].append(z[i])
        if i < 20:
            data_set[1].append(z[i])
        if i < 30:
            data_set[2].append(z[i])
        if i < 40:
            data_set[3].append(z[i])
        if i < 50:
            data_set[4].append(z[i])
        if i < 60:
            data_set[5].append(z[i])
        if i < 70:
            data_set[6].append(z[i])
        if i < 80:
            data_set[7].append(z[i])
        if i < 90:
            data_set[8].append(z[i])
        if i < 100:
            data_set[9].append(z[i])
        if i < 110:
            data_set[10].append(z[i])
        if i < 120:
            data_set[11].append(z[i])
    else:
        if i < 10:
            data_set[12].append(z[i])
        if i < 20:
            data_set[13].append(z[i])
        if i < 30:
            data_set[14].append(z[i])
        if i < 40:
            data_set[15].append(z[i])
        if i < 50:
            data_set[16].append(z[i])
        if i < 60:
            data_set[17].append(z[i])
        if i < 70:
            data_set[18].append(z[i])
        if i < 80:
            data_set[19].append(z[i])
        if i < 90:
            data_set[20].append(z[i])
        if i < 100:
            data_set[21].append(z[i])
        if i < 110:
            data_set[22].append(z[i])
        if i < 120:
            data_set[23].append(z[i])

   
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

data_a = [a0,a1,a2,a3]
data_b = [a4,a5,a6,a7]
data_c = [a8,a9,a10,a11]
data_d = [a12,a13,a14,a15]
data_e = [a16,a17,a18,a19]
data_f = [a20,a21,a22,a23]

ticks = ['A', 'B', 'C', 'D']

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

s1 = [a0,a1,a2,a3]
s11 = statistics.median(a0)
s12 = statistics.median(a1)
s13 = statistics.median(a2)
s14 = statistics.median(a3)
y = [0, 2, 4, 6]
x = [s11, s12, s13, s14]
plt.plot(y,x,linewidth=4,color='y',label='8 P (Blocking)')

s2 = [a4,a5,a6,a7]
s21 = statistics.median(a4)
s22 = statistics.median(a5)
s23 = statistics.median(a6)
s24 = statistics.median(a7)
y = [0, 2, 4, 6]
x = [s21, s22, s23, s24]
plt.plot(y,x,linewidth=4,color='r',label='16 P (Blocking)')

s3 = [a8,a9,a10,a11]
s31 = statistics.median(a8)
s32 = statistics.median(a9)
s33 = statistics.median(a10)
s34 = statistics.median(a11)
y = [0, 2, 4, 6]
x = [s31, s32, s33, s34]
plt.plot(y,x,linewidth=4,color='b',label='32 P (Blocking)')

s4 = [a12,a13,a14,a15]
s41 = statistics.median(a12)
s42 = statistics.median(a13)
s43 = statistics.median(a14)
s44 = statistics.median(a15)
y = [0, 2, 4, 6]
x = [s41, s42, s43, s44]
plt.plot(y,x,linewidth=4,color='g',label='8 P (Non Blocking)')

s5 = [a16,a17,a18,a19]
s51 = statistics.median(a16)
s52 = statistics.median(a17)
s53 = statistics.median(a18)
s54 = statistics.median(a19)
y = [0, 2, 4, 6]
x = [s51, s52, s53, s54]
plt.plot(y,x,linewidth=4,color='m',label='16 P (Non Blocking)')

s6 = [a20,a21,a22,a23]
s61 = statistics.median(a20)
s62 = statistics.median(a21)
s63 = statistics.median(a22)
s64 = statistics.median(a23)
y = [0, 2, 4, 6]
x = [s61, s62, s63, s64]
plt.plot(y,x,linewidth=4,color='c',label='32 P (Non Blocking)')
plt.xlabel('Data (Bytes)')
plt.ylabel('Bandwidth (Mbps)')
plt.xticks([0,2,4,6],['128','65536','262144','1048576'])
plt.legend()

# plt.xticks(range(0, len(ticks) * 2, 2), ticks)
# plt.xlim(-2, len(ticks)*2)
# plt.ylim(0, 8)
# plt.tight_layout()
plt.savefig('image.png')