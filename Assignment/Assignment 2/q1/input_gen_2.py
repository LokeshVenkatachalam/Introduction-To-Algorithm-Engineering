import random 
f = open("./input_1_750.txt",'w+')
n = 750
f.write(str(n).zfill(5)+"\n")
for i in range(n):
    for j in range(n):
        x = random.randint(0,9)
        if(j<n-1):
            f.write(str(x)+" " )
        else:
            f.write(str(x)+"\n")
f.close()