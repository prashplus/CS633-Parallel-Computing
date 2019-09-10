import os
import matplotlib.pyplot as plt
import numpy as np

with open('data.txt') as f:
    lines = f.readlines()
    z = [line.split()[0] for line in lines]

data_set1 = []
data_set2 = []
data_set3 = []
data_set4 = []
data_set5 = []

for i in range(0,len(z)):
    if i==0 or i==1 or i==2 or i==3 or i==4:
        data_set1.append(z[i])
    if i==5 or i==6 or i==7 or i==8 or i==9:
        data_set2.append(z[i])
    if i==10 or i==11 or i==12 or i==13 or i==14:
        data_set3.append(z[i])
    if i==15 or i==16 or i==17 or i==18 or i==19:
        data_set4.append(z[i])
    if i==20 or i==21 or i==22 or i==23 or i==24:
        data_set5.append(z[i])
    
a=np.asarray(data_set1).astype(np.float)
b=np.asarray(data_set2).astype(np.float)
c=np.asarray(data_set3).astype(np.float)
d=np.asarray(data_set4).astype(np.float)
e=np.asarray(data_set5).astype(np.float)

data = [a,b,c,d,e]
print(a)
print(b)
print(c)
print(d)
print(e)
mpl_fig = plt.figure()
ax = mpl_fig.add_subplot(111)

ax.boxplot(data)
plt.xlabel('Data (Bytes)')
plt.ylabel('Bandwidth (Mbps)')
plt.ylim(0,128)
plt.xticks([1, 2, 3, 4, 5], ['128', '1024', '65536', '1048576', '4194304'])
plt.savefig('image.png')
plt.show()