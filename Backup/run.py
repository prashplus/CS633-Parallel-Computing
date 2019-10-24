import os
import threading


with open('hosts') as f:
    lines = f.readlines()
    z = [line.split()[0] for line in lines]
arr = [8192,65536,262144]

def func1():
    for k in range(10):
        for i in range(30):
            for j in range(30):
                if i == j:
                    string='mpiexec -np 2 -hosts '+ z[i] + ' ./main.out '+str(arr[0])+ ' 1 ' +str(i)+ ' ' +str(j)
                else:
                    string='mpiexec -np 2 -ppn 1 -hosts '+ z[i] + ',' + z[j] + ' ./main.out '+str(arr[0])+ ' 1 ' +str(i)+ ' ' +str(j)
                cmd=os.popen(string)
                print('\n' + str(i) + ',' +str(j)+'done')
                #print(string)
                print(cmd.read())
                cmd.close()

def func2():
    for k in range(10):
        for i in range(30):
            for j in range(30):
                if i == j:
                    string='mpiexec -np 2 -hosts '+ z[i] + ' ./main.out '+str(arr[1])+ ' 2 ' +str(i)+ ' ' +str(j)
                else:
                    string='mpiexec -np 2 -ppn 1 -hosts '+ z[i] + ',' + z[j] + ' ./main.out '+str(arr[1])+ ' 2 ' +str(i)+ ' ' +str(j)
                cmd=os.popen(string)
                print('\n' + str(i) + ',' +str(j)+'done')
                #print(string)
                print(cmd.read())
                cmd.close()

def func3():
    for k in range(10):
        for i in range(30):
            for j in range(30):
                if i == j:
                    string='mpiexec -np 2 -hosts '+ z[i] + ' ./main.out '+str(arr[2])+ ' 3 ' +str(i)+ ' ' +str(j)
                else:
                    string='mpiexec -np 2 -ppn 1 -hosts '+ z[i] + ',' + z[j] + ' ./main.out '+str(arr[2])+ ' 3 ' +str(i)+ ' ' +str(j)
                cmd=os.popen(string)
                print('\n' + str(i) + ',' +str(j)+'done')
                #print(string)
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