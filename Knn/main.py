import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

lista = []
for x in range (1,101,1):
    print('Archivo ', x)
    file = '..\\database\\dataSet60_' + str(x) + '.csv'
    data = np.array(np.loadtxt(file, delimiter=','))
    dataOld = np.array(pd.read_csv('..\\database\\ptr.water.csv', delimiter=',', header=None))
    dataInt = open('..\\database\\dataSetInterpolated.csv', 'w')

    valor = 0
    suma = 0
    kk = 4 #1 a 7
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
                    if valor == 2:#dataOld[][]
                        a1 = dataOld[i-1][j-1]
                        a2 = dataOld[i-1][j]
                        a3 = dataOld[i-1][j+1]
                        a4 = dataOld[i][j-1]
                        a5 = dataOld[i][j]
                        a6 = dataOld[i][j+1]
                        a7 = dataOld[i+1][j-1]
                        a8 = dataOld[i+1][j]
                        a9 = dataOld[i+1][j+1]

                        #cálculo de distancias mínimas entrre todos los datos
                        listaDM = []
                        a5a1 = ((((a5 - a1) / 2) ** 2) ** (1 / 2))
                        listaDM.append(a5a1)
                        a5a2 = ((((a5 - a2) / 2) ** 2) ** (1 / 2))
                        listaDM.append(a5a2)
                        a5a3 = ((((a5 - a3) / 2) ** 2) ** (1 / 2))
                        listaDM.append(a5a3)
                        a5a4 = ((((a5 - a4) / 2) ** 2) ** (1 / 2))
                        listaDM.append(a5a4)
                        a5a6 = ((((a5 - a6) / 2) ** 2) ** (1 / 2))
                        listaDM.append(a5a6)
                        a5a7 = ((((a5 - a7) / 2) ** 2) ** (1 / 2))
                        listaDM.append(a5a7)
                        a5a8 = ((((a5 - a8) / 2) ** 2) ** (1 / 2))
                        listaDM.append(a5a8)
                        a5a9 = ((((a5 - a9) / 2) ** 2) ** (1 / 2))
                        listaDM.append(a5a9)

                        listaDM = sorted(listaDM)
                        newData = 0
                        if kk == 1:
                            newData = listaDM[0]
                        else:
                            for knn in range (0,kk,1): # valores mínimos
                                newData = ((newData+listaDM[knn])/2)
                        suma += round((newData - valor)**2,4)

                        #print (newData, '  -   ', valorOld,'   ',suma)
                    else:
                        dataInt.write(str(valor)+',')
            dataInt.write('\n')
        lista.append((suma/(144*73))**(1/2))
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
plt.title("Knn")
plt.ylabel("Error")
plt.xlabel("Media: "+str(round(s,3)))
plt.plot(t,lista,t,media)
plt.show()