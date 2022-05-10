import numpy as np
import matplotlib.pyplot as plt
def jud(data):
    num = []
    for i in data:
         num.append(i.isdigit())
    return num

def data_select(file,lat_num,lon_num,time_num):

    f = open(file, "r",encoding='utf-8')
    data = f.readlines()
    f.close()

    s= []
    for k in range(len(data)):
        num_list = jud(data[k].split())
            
        if all(num_list):
            s.append(k)

    img = []

    for value in s:
        img = img + list(map(int,data[value].split()))
    
    img = np.array(img)
    tec = img.reshape(lat_num*time_num ,lon_num)
   

    return tec
 
def plot_tec(tec_data,hour):

    lat,lon = tec_data.shape


    for i in range(hour):
        plt.imshow(tec_data[i*71:(i+1)*71,:],origin='lower')
        plt.xlabel('LON')
        plt.xticks(np.linspace(0,72,3), [r'$-180^{\circ}$', '0', r'$180^{\circ}$'])
        plt.ylabel('LAT')
        plt.yticks(np.linspace(0,70,3), [r'$-87.5^{\circ}$', '0', r'$87.5^{\circ}$'])
        plt.colorbar()
        plt.savefig('./img/tec-{}.png'.format(i))
        plt.close()
        
#main   

tec_data = data_select(file='data.txt',lat_num=71,lon_num=73,time_num=25)

plot_tec(tec_data,hour=24)

print('done')