import sys
import numpy
import random
import time

st = time.time()
def int_line(f):
    line_Text = f.readline()
    line_Text_no_Leading_zeroes = line_Text.lstrip('0')
    if(len(line_Text_no_Leading_zeroes)==1):
        line_Text_no_Leading_zeroes = "0\n"
    line_Text_int = int(line_Text_no_Leading_zeroes)
    return line_Text_int

desired_Bucket_Size =3
file_Name = sys.argv[1]
pivot_Count = int(sys.argv[2])


desired_Bucket_Size = max(desired_Bucket_Size,pivot_Count)

f = open(file_Name,'r+')
line_1_int = int_line(f)
f.close()

for i in range (0,pivot_Count+1):
    bucket_File_Name = "temp_Bucket_" + str(i) + ".txt"
    temp_Bucket_File = open(bucket_File_Name,"w")
    temp_Bucket_File.close()

def bin_Search(bucket_List,value):
    start = 0
    end = len(bucket_List)
    end = end - 1
    while(start < end):
        mid = (start + end)//2
        if((bucket_List[mid] <=value) and (bucket_List[mid+1] > value)):
            return mid
        elif(bucket_List[mid] <= value):
            start = mid + 1
        else:
            end = mid
    return start


def samplesort(start, end ,f):
    start_Char_Pos = int(11 + 7*(start-1))
    f.seek(start_Char_Pos)
    if((end-start) <= desired_Bucket_Size):
        temp_array = []
        for index in range(start, end):
            line_Text_int = int_line(f)
            temp_array.append(line_Text_int)
        temp_array.sort()
        f.seek(start_Char_Pos)
        for index in range(start, end):
            f.write(str(temp_array[index-start]).zfill(6) + "\n")
    else:
        

        for index in range(0,pivot_Count+1):
            bucket_File_Name = "temp_Bucket_" + str(index) + ".txt"
            temp_Bucket_File = open(bucket_File_Name,"r+")
            temp_Bucket_File.seek(0) 
            temp_Bucket_File.truncate()


        temp_index = random.sample(range(start, end), pivot_Count)
        temp_index.sort()
#        print(temp_index)
        temp_value = []
        for index in range(0,pivot_Count):
            pos = int(11 + 7*(temp_index[index]-1))
            f.seek(pos)
            line_Text_int = int_line(f)
            temp_value.append(line_Text_int)
        temp_value.sort()
#        print(temp_value)
        

        temp_Bucket_Boundary = []
        temp_Bucket_Boundary.append(0)
        for index in range(0,pivot_Count):
            temp_Bucket_Boundary.append(temp_value[index])
        temp_Bucket_Boundary.append(1000001)
#        print(temp_Bucket_Boundary)

        
        pointer_1 = 0
        
        f.seek(start_Char_Pos)
        for index in range(start, end):
            line_Text_int = int_line(f)
            if(pointer_1<pivot_Count):
                if(index == temp_index[pointer_1]):
                    pointer_1+=1
                    continue
            bucket_No = bin_Search(temp_Bucket_Boundary,line_Text_int)
#            print(line_Text_int,bucket_No)
            bucket_File_Name = "temp_Bucket_" + str(bucket_No) + ".txt"
            temp_Bucket_File = open(bucket_File_Name,"a")
            temp_Bucket_File.write(str(line_Text_int).zfill(6) + "\n")
            temp_Bucket_File.close()

        pivot_Index = []
        pointer_2 = start-1
        pivot_Index.append(pointer_2)
        
        f.seek(start_Char_Pos)
        for index in range(0,pivot_Count+1):
            bucket_File_Name = "temp_Bucket_" + str(index) + ".txt"
            temp_Bucket_File = open(bucket_File_Name,"r")

            for line in temp_Bucket_File:
                f.write(line)
                pointer_2+=1
            
            temp_Bucket_File.close()
            if(index+1<=pivot_Count):
                f.write(str(temp_Bucket_Boundary[index+1]).zfill(6) + "\n")
                pointer_2+=1
                pivot_Index.append(pointer_2)

        pivot_Index.append(end)
        for index in range(0,pivot_Count+1):
            samplesort(pivot_Index[index]+1,pivot_Index[index+1],f)


f1 = open(file_Name, "r+")
samplesort(1,line_1_int+1,f1)
f1.close()


et = time.time()
print(et-st)