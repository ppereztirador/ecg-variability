import numpy as np
import csv

fileName = "ecg_16bit/good_16_bits.txt"
dataRow = 2

with open(fileName) as fh:
    fr = csv.reader(fh, delimiter='\t')
    for i in range(3):
        next(fr)
    data = []
    data8bit = []
    for row in fr:
        try:
            data.append(int(row[dataRow]))
            data8bit.append(int(row[dataRow])//256)
            data8bit.append(int(row[dataRow])%256)
        except Exception as ex:
            print(ex)
            continue


newLen = len(data8bit)//16
#data16 = np.reshape(data, (len(data)//16, 16))
data16_8bit = np.reshape(data8bit[0:newLen*16], (newLen, 16))

fileName_name = fileName.split('.')[0]
np.save(fileName_name+'.npy', data16_8bit)
