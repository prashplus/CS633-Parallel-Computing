import os

if os.path.isfile('data.txt'):
    os.remove("data.txt")
cmd = os.popen('bash checkhosts.sh')
arr = [128,8192,32768,131072]
l = len(arr)
for i in range(l):
    for j in range(5):
        string='mpiexec -np 8 -ppn 4 -f hosts ./main.out '+str(arr[i])
        cmd=os.popen(string)
        print(cmd.read())
        cmd.close()

for i in range(l):
    for j in range(5):
        string='mpiexec -np 16 -ppn 4 -f hosts ./main.out '+str(arr[i])
        cmd=os.popen(string)
        print(cmd.read())
        cmd.close()

for i in range(l):
    for j in range(5):
        string='mpiexec -np 32 -ppn 4 -f hosts ./main.out '+str(arr[i])
        cmd=os.popen(string)
        print(cmd.read())
        cmd.close()

#os.system('python3 plot.py')