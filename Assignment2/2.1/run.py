import os
import threading


with open('hosts') as f:
    lines = f.readlines()
    z = [line.split()[0] for line in lines]
#Data sizes
arr = [8192,65536,262144]

# Data size 1
def func1():
    for i in range(10):
        string='mpiexec -np 30 -ppn 1 -f hosts ./main.out '+str(arr[0]) + ' 1'
        cmd=os.popen(string)
        print(cmd.read())
        cmd.close()

# Data size 2
def func2():
    for i in range(10):
        string='mpiexec -np 30 -ppn 1 -f hosts ./main.out '+str(arr[1]) + ' 2'
        cmd=os.popen(string)
        print(cmd.read())
        cmd.close()

# Data size 3
def func3():
    for i in range(10):
        string='mpiexec -np 30 -ppn 1 -f hosts ./main.out '+str(arr[2]) + ' 3'
        cmd=os.popen(string)
        print(cmd.read())
        cmd.close()

if __name__ == "__main__":
    #Checks for the data files
    #Remove them is already present before the run
    if os.path.isfile('data1.txt'):
        os.remove("data1.txt")
    if os.path.isfile('data2.txt'):
        os.remove("data2.txt")
    if os.path.isfile('data3.txt'):
        os.remove("data3.txt")
    # Script to check all the available hosts
    cmd = os.popen('bash checkhosts.sh')
    print(cmd.read())
    cmd.close()

    # creating threads
    t1 = threading.Thread(target=func1)
    t2 = threading.Thread(target=func2)
    t3 = threading.Thread(target=func3)

    # set the value of range as per your requirements
    for i in range(1):
        t1.start()
        t2.start()
        t3.start()

    # both threads completely executed
    print("Done!")

#os.system('python3 plot.py')