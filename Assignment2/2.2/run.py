import os
# Cleaning up data files
if os.path.isfile('data1.txt'):
    os.remove("data1.txt")
if os.path.isfile('data2.txt'):
    os.remove("data2.txt")
if os.path.isfile('data3.txt'):
    os.remove("data3.txt")

# finding all the available hosts
cmd = os.popen('bash checkhosts.sh')
print(cmd.read())
cmd.close()

# data sizes
arr = [8192,32768,65536,262144,524288]
l = len(arr)
#P = 8
for i in range(l):
    for j in range(10):
        string='mpiexec -np 8 -ppn 2 -f hosts ./main.out '+str(arr[i]) + ' 1'
        cmd=os.popen(string)
        print(cmd.read())
        cmd.close()

for i in range(l):
    for j in range(10):
        string='mpiexec -np 8 -ppn 4 -f hosts ./main.out '+str(arr[i]) + ' 1'
        cmd=os.popen(string)
        print(cmd.read())
        cmd.close()

for i in range(l):
    for j in range(10):
        string='mpiexec -np 8 -ppn 8 -f hosts ./main.out '+str(arr[i]) + ' 1'
        cmd=os.popen(string)
        print(cmd.read())
        cmd.close()

#P = 16
for i in range(l):
    for j in range(10):
        string='mpiexec -np 16 -ppn 2 -f hosts ./main.out '+str(arr[i]) + ' 2'
        cmd=os.popen(string)
        print(cmd.read())
        cmd.close()

for i in range(l):
    for j in range(10):
        string='mpiexec -np 16 -ppn 4 -f hosts ./main.out '+str(arr[i]) + ' 2'
        cmd=os.popen(string)
        print(cmd.read())
        cmd.close()

for i in range(l):
    for j in range(10):
        string='mpiexec -np 16 -ppn 8 -f hosts ./main.out '+str(arr[i]) + ' 2'
        cmd=os.popen(string)
        print(cmd.read())
        cmd.close()

#P = 32
for i in range(l):
    for j in range(10):
        string='mpiexec -np 32 -ppn 2 -f hosts ./main.out '+str(arr[i]) + ' 3'
        cmd=os.popen(string)
        print(cmd.read())
        cmd.close()

for i in range(l):
    for j in range(10):
        string='mpiexec -np 32 -ppn 4 -f hosts ./main.out '+str(arr[i]) + ' 3'
        cmd=os.popen(string)
        print(cmd.read())
        cmd.close()

for i in range(l):
    for j in range(10):
        string='mpiexec -np 32 -ppn 8 -f hosts ./main.out '+str(arr[i]) + ' 3'
        cmd=os.popen(string)
        print(cmd.read())
        cmd.close()


#uncommnent the below part if matplot lib and all other libs are installed
#os.system('python3 plot.py')