import random
import tqdm
f = open("input_2.txt",'w+')
f.write("1000\n")
temp_index = random.sample(range(0, 1000001), 1000)
for index in temp_index:
    f.write(str(index).zfill(6)+"\n")