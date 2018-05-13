import pandas as pd
import random

for x in range (1,101,1):
    dataSet = pd.read_csv("..\\database\\ptr.water.csv",  sep=',',  comment='#', header=None).values
    file = '..\\database\\dataSet60_'+str(x)+'.csv'
    print (file)
    dataSet60 = open(file, 'w')

    rows = len(dataSet[:, 1])
    columns = len(dataSet[1, :])

    numData = rows*columns
    data60 = round((40*numData)/100)
    print(data60, rows, columns)

    cont = 1
    i = 0
    j = 0

    while i < rows:
        while j < columns:
            if (i==0 and j<columns-1) or (j==0 and j<columns-1):
                dataSet60.write(str(dataSet[i, j])+',')
                #print('test', i, rows - 1, j, columns - 1)
            elif (i==rows-1 and j<columns-1):
                dataSet60.write(str(dataSet[i, j])+',')
                #print ('test', i, rows-1, j, columns-1)
            elif (j==columns-1):
                dataSet60.write(str(dataSet[i, j]))
                #print ('test', i, rows-1, j, columns-1)
            else:
                if (cont < data60): rnd = random.randint(0,1) # 0 elimina
                else: rnd=1

                if rnd == 0:
                    dataSet60.write('2,')
                    cont+=1
                else:
                    if j==columns-1:
                        dataSet60.write(str(dataSet[i,j]))
                    else:
                        dataSet60.write(str(dataSet[i,j])+',')
                #print(i, j, cont, data60, (((cont*100)/numData)),'%')
            j+=1 #contador
        j=0
        if i < rows-1: dataSet60.write('\n') #salto
        i+=1