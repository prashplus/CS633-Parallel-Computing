import os
import threading

# Cleaning up time files
if os.path.isfile('cse/data1/time1.txt'):
    os.remove("cse/data1/time1.txt")
if os.path.isfile('cse/data2/time2.txt'):
    os.remove("cse/data2/time2.txt")

# finding all the available hosts
cmd = os.popen('bash checkhosts.sh')
print(cmd.read())
cmd.close()

#Make and make clean
cmd = os.popen('make clean')
print(cmd.read())
cmd.close()

cmd = os.popen('make')
print(cmd.read())
cmd.close()

#Main Loop
n = [17,16] #argv[1]
data = ["data/data1/file","data/data2/file"] #argv[2]
filename = ["cse/data1/output_","cse/data2/output_"] #argv[3]


for i in range(2):
    for p in range(16):
        for q in range(5):
            string = "mpiexec -ppn 4 -n " + str(p+1) + " -f hosts ./main.out " + str(n[i])+" "+str(data[i])+" "+str(filename[i])
            cmd = os.popen(string)
            output = cmd.read()
            cmd.close()
            if i == 0:
                file1 = open("cse/data1/time1.txt","a")
                file1.writelines(output)
                file1.close()
            else:
                file2 = open("cse/data2/time2.txt","a")
                file2.writelines(output)
                file2.close()
            print((i+1),(p+1),(q+1))

#uncommnent the below part if matplot lib and all other libs are installed
#os.system('python3 cseplot.py')