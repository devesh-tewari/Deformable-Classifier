import numpy as np
import pandas as pd

metadata = pd.read_csv('gtsrb-german-traffic-sign/Train.csv')
# print(metadata.head())

f = open('annotate.txt', 'w')

for index, row in metadata.iterrows():
    line = 'gtsrb-german-traffic-sign/' + str(row['Path']) + ',' + str(row['Roi.X1']) + ',' + str(row['Roi.Y1']) + ',' + str(row['Roi.X2']) + ',' + str(row['Roi.Y2']) + ',' + str(row['ClassId']) + '\n'
    f.write(line)

f.close()
