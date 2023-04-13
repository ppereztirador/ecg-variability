import numpy as np
import csv

fileName = "ecg_16bit/verynoisy_16_bits.txt"
dataRow = 2

with open(fileName) as fh:
    fr = csv.reader(fh, delimiter='\t')
    for i in range(3):
        next(fr)
    data = []
    data8bit = []
    data0 = 0
    dataMax = 0
    for row in fr:
        try:
            data.append(int(row[dataRow]))
            hi = int(row[dataRow])//256
            lo = int(row[dataRow])%256
            if (hi<255 and lo<255): # Only append if data isn't saturated
                data8bit.append(hi)
                data8bit.append(lo)
            else:
                if (hi==0): data0+=1
                if (lo==0): data0+=1
                if (hi==255): dataMax+=1
                if (lo==255): dataMax+=1
        except Exception as ex:
            print(ex)
            continue


newLen = len(data8bit)//16
#data16 = np.reshape(data, (len(data)//16, 16))
data16_8bit = np.reshape(data8bit[0:newLen*16], (newLen, 16))

fileName_name = fileName.split('.')[0]
np.save(fileName_name+'_clean.npy', data16_8bit)
