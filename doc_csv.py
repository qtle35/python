

import csv


with open("BTH2.csv") as f:
    data = list(csv.reader(f))
print(len(data))