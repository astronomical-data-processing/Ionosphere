import numpy as np
import matplotlib.pyplot as plt
f = open("data.txt", "r",encoding='utf-8')
data = f.readlines()
f.close()

tec = [[0 for j in range(73)] for i in range(71)] 
tec = np.array(tec)

j = 0

i =4722

while True:

    s= []
    for k in range(i,i+5):    
        s = s + (list(map(int,data[k].split()))) 

    tec[j,:] = s

    i = i + 6
    j = j + 1
    
    if j == 71:
        break
    
# print(tec)
plt.imshow(tec,origin='lower')
plt.xlabel('LON')
plt.xticks(np.linspace(0,72,3), [r'$-180^{\circ}$', '0', r'$180^{\circ}$'])
plt.ylabel('LAT')
plt.yticks(np.linspace(0,70,3), [r'$-87.5^{\circ}$', '0', r'$87.5^{\circ}$'])
plt.colorbar()

plt.show()
plt.close()
