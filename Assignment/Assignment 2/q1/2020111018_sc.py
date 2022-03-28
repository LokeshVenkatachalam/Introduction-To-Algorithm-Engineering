import sys
import numpy
import random
import time
st = time.time()
s1 = 47
s2 = 64

f_Name_1 = sys.argv[1]
f_Name_2 = sys.argv[2]
f_Name_3 = "2020111017_output_10.txt"



f_temp_1 = open(f_Name_1,"r")
l1_T = f_temp_1.readline()
l1_Nozero = l1_T.lstrip('0')
if(len(l1_Nozero)==1):
    l1_Nozero == "0\n"
l1_N = int(l1_Nozero)

f_temp = open(f_Name_3,"w+")
string = ""
for i in range(l1_N):
    string =  string + "0000000"
    if(i<l1_N-1):
        string = string + " "
string += "\n"
for i in range(l1_N):
    f_temp.write(string)
f_temp.close() 

# No blocking version 
#
##transposing
#
with  open(f_Name_2,'r+') as f2:
    for i in range(l1_N):
        for j in range(i):
            f2.seek(6+i*(2*l1_N)+2*j)
            x = int(f2.read(1))
            f2.seek(6+j*(2*l1_N)+2*i)
            y = int(f2.read(1))
            z = y
            y = x
            x = z
            f2.seek(6+i*(2*l1_N)+2*j)
            f2.write(str(x))
            f2.seek(6+j*(2*l1_N)+2*i)
            f2.write(str(y))

with open(f_Name_1,'r+') as f1, open(f_Name_2,'r+') as f2 , open(f_Name_3,'r+') as f3:
    for i in range(l1_N):
        f1.seek(6+i*(2*l1_N))
        a_read = f1.read(2*l1_N)
        a_num = list(map(int,a_read.split()))
        for j in range(l1_N):
            f2.seek(6+j*(2*l1_N))
            b_read = f2.read(2*l1_N)
            b_num = list(map(int,b_read.split()))
            c_num = 0 
            for k in range(l1_N):
                c_num += a_num[k]*b_num[k]
            f3.seek(i*(8*l1_N)+8*j)
            f3.write(str(c_num).zfill(7))
            if j<l1_N-1:
                f3.write(" ")
            else:
                f3.write("\n")
            
et = time.time()
print(et-st)


##1 Blocking Version
#block_1 = [[0 for i in range(s1)] for j in range(s1)]
#block_2 = [[0 for i in range(s1)] for j in range(s1)]
#block_3 = [[0 for i in range(s1)] for j in range(s1)]
#
#
#
#st = time.time()
#with open(f_Name_1,'r+') as f1, open(f_Name_2,'r+') as f2 , open(f_Name_3,'r+') as f3:
#    for i in range (0,int((l1_N-1)/s1)+1):
#        for j in range(0,int((l1_N-1)/s1)+1):
#            for k in range (0,int((l1_N-1)/s1)+1):
#                for i1 in range(s1):
#                    for j1 in range(s1):
#                        block_1[i1][j1] = 0
#                        block_2[i1][j1] = 0
#                        block_3[i1][j1] = 0
#                col_len = min(s1,l1_N-j*s1)
#                row_len = min(s1,l1_N-i*s1)
#                col_2_len = min(s1,l1_N-k*s1)
#                for i1 in range(row_len):
#                    f1.seek(6+(i*s1+i1)*(2*l1_N)+2*j*s1)
#                    line = f1.read(2*col_len)
#                    line_list = list(map(int,line.split()))
#                    for j1 in range(col_len):
#                        block_1[i1][j1] = line_list[j1]
#                for j1 in range(col_len):
#                    f2.seek(6+(j*s1+j1)*(2*l1_N)+2*k*s1)
#                    line = f2.read(2*col_2_len)
#                    line_list = list(map(int,line.split()))
#                    for k1 in range(col_2_len):
#                        block_2[j1][k1] = line_list[k1]
#
#                for i1 in range(row_len):
#                    for k1 in range(col_2_len):
#                        for index in range(col_len):
#                            block_3[i1][k1] += block_1[i1][index]*block_2[index][k1]
#                
#                for i1 in range(row_len):
#                    f3.seek((i*s1+i1)*(8*l1_N)+8*k*s1)
#                    line = f3.read(8*col_2_len)
#                    ct1 = 0
#                    if(line[8*col_2_len-1]=='\n'):
#                        ct1 = 1
#                    #print(line)
#                    line_list = line.split()
#                    #print(line_list)
#                    line_num = []
#                    line_str = ""
#                    for k1 in range(col_2_len):
#                        x = line_list[k1].lstrip('0')
#                        #print(i1,k1)
#                        if(len(x)==0):
#                            x="0\n"
#                        line_num.append(int(x))
#                        line_num[k1] =  line_num[k1] + block_3[i1][k1]
#                        line_str = line_str + str(line_num[k1]).zfill(7)
#                        if(ct1 == 0) or k1 < col_2_len-1:
#                            line_str = line_str + " "
#                        else:
#                            line_str = line_str + "\n"
#                    f3.seek((i*s1+i1)*(8*l1_N)+8*k*s1)
#                    f3.write(line_str)
#
#
#
#et = time.time()
#print(et-st)


