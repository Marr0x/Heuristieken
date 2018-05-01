# load CSV
import csv
import numpy as np

filename = 'genome.csv'
raw_data = open(filename, 'rt')
data = np.loadtxt(raw_data, dtype = np.int8, delimiter = ',', usecols = range(1,26))

data_list = data.tolist()
print(data_list)
