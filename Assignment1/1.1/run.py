import os
import matplotlib.pyplot as plt
import numpy as np


if os.path.isfile('data.txt'):
    os.remove("data.txt")
cmd = os.popen('bash checkhosts.sh')

arr = [16,128,8192,131072,524288]
l = len(arr)
for i in range(l):
    for j in range(5):
        string='mpiexec -np 2 -ppn 1 -f hosts ./main.out '+str(arr[i])
        cmd=os.popen(string)
        print(cmd.read())
        cmd.close()


#os.system('python3 plot.py')