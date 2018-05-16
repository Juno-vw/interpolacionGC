from pykrige import OrdinaryKriging
import numpy as np
import pykrige.kriging_tools as kt
import matplotlib.pyplot as plt
import pandas as pd

lista = []

for x in range (1,101,1):
    print('Archivo ', x)
    file = '..\\database\\dataSet60_' + str(x) + '.csv'
    data = np.array(np.loadtxt(file, delimiter=','))
    dataOld = np.array(pd.read_csv('..\\database\\ptr.water.csv', delimiter=','))
    dataInt = open('..\\database\\dataSetInterpolatedKringing.csv', 'w')

    gridx = np.arange(0.0, 72, 0.5)
    gridy = np.arange(0.0, 37, 0.5)

    OK = OrdinaryKriging(data[:, 0], data[:, 1], data[:, 2], variogram_model='linear', verbose=False, enable_plotting=False)
    z, ss = OK.execute('grid', gridx, gridy)
    kt.write_asc_grid(gridx, gridy, z, filename="output.asc")

    valor = 0
    suma = 0
    for k in range (1,2,1):
        print('Iteracion ', k)
        for i in range (0,72,1):
            for j in range(0, 144, 1):
                valor = round(data[i][j],4)
                valorOld = round(dataOld[i][j],4)
                if (i==0 and j<143) or (j==0 and j<143):
                    dataInt.write(str(valor)+',')
                    #print('test', i, rows - 1, j, columns - 1)
                elif (i==73 and j<143):
                    dataInt.write(valor+',')
                    #print ('test', i, rows-1, j, columns-1)
                elif (j==143):
                    dataInt.write(str(valor))
                    #print ('test', i, 72, j, 143)
                else:
                    if valor == 2:
                        newData = round(((((dataOld[i][j-1]+dataOld[i][j+1])/2)+((dataOld[i-1][j]+dataOld[i+1][j])/2))/2),4)
                        dataInt.write(str(newData)+',')
                        suma += (newData - valor)**2
                        #print ('s', newData, ' - ', valorOld,suma)
                    else:
                        dataInt.write(str(valor)+',')
            dataInt.write('\n')
        lista.append((suma/(144*73))**(1/8))
        suma=0

#lista = sorted(lista)
print(lista)
s = 0
for h in range (0,len(lista),1):
    s+=lista[h]
s = s/len(lista)
print('Media: ', s)
media = []
for h in range (0,len(lista),1):
    media.append(s)

a = lista[0]
b = lista[len(lista)-1]
c = (b-a)/len(lista)

t=np.arange(a,b,c)
plt.title("Kringing")
plt.ylabel("Error")
plt.xlabel("Media: "+str(round(s,3)))
plt.plot(t,lista,t,media)
plt.show()