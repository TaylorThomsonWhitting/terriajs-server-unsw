import csv
import os
from os.path import isfile, join
import shutil

csv_file = open('231018 UNSW Building List_2.csv', newline='')
reader = csv.DictReader(csv_file)

data = {}
for row in reader:
    data[row['Building'].strip()] = row

# Create CZML
czml = [
    {
        "id":"document",
        "version":"1.0",
        "clock": {
            "interval": "2023-12-18T00:00:00Z/2023-12-21T00:00:00Z",
            "currentTime": "2023-12-20T00:00:00Z"
        }
    }
]

files = [f for f in os.listdir(".") if isfile(join(".", f)) and f.endswith('.glb')]

for f in files:
    building_name = f.removesuffix('.glb')
    building_name = building_name.replace('_', ' ')
    building_data = data.get(building_name)
    if building_data:
        building_ref = building_data['Ref']
        shutil.copyfile(f, f'./ids/{building_ref}.glb')
        