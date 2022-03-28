import matplotlib.pyplot as plt
X = [250,500,750]
Y =  [6.185982942581177,42.77980065345764,140.55998587608337]
Y1 = [3.5141375064849854,22.735530376434326,98.41511559486389]
Y2 = [5.34631085395813,31.782694101333618,110.90812873840332]
Y3 = [8.10411262512207,47.71538972854614,133.18228816986084]

plt.plot(X,Y,label = "No blocking")
plt.plot(X,Y1,label="1-Blocking S~N/4")
plt.plot(X,Y2,label="1-Blocking S~N/8")
plt.plot(X,Y3,label="1-Blocking S~N/16")
plt.ylabel('Time(sec)')    
plt.xlabel('N')    
plt.show()