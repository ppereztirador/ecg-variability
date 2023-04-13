import numpy as np
import csv

fileName = "ecg_10bit/noisy_10bit.txt"
dataRow = 5

with open(fileName) as fh:
    fr = csv.reader(fh, delimiter='\t')
    for i in range(3):
        next(fr)
    data = []
    data8bit = []

    first = True
    rowCounter = 0
    for row in fr:
        rowCounter += 1
        try:
            dataPoint = int(row[dataRow])
            if dataPoint==255 or dataPoint==0:
                next
            if first==True:
                first=False
                dataH = dataPoint >> 2
                dataL = dataPoint - (dataH << 2)
                data.append(dataH)
                shiftLevel = 4
            else:
                dataH = dataPoint >> shiftLevel
                if shiftLevel==2:
                    data.append(dataL)
                    data.append(dataH)
                else:
                    dataHL = dataH+(dataL<<(10-shiftLevel))
                    data.append(dataHL)
                
                dataL = dataPoint - (dataH << shiftLevel)
                if shiftLevel==8:
                    shiftLevel = 2
                else:
                    shiftLevel += 2
                

        except Exception as ex:
            print(ex)
            continue

print(rowCounter)
print(len(data))

newLen = len(data)//16
data16_8bit = np.reshape(data[0:newLen*16], (newLen, 16))

fileName_name = fileName.split('.')[0]
np.save(fileName_name+'_variability.npy', data16_8bit)
