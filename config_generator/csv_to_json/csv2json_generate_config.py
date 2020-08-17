#!/usr/bin/env python
__author__      = "Melih TEKE"

import csv, json

csvFilePath = "sample_device_table.csv"
jsonFilePath = "table.json"

#reading csv and adding data to dictionary
data = {}
with open(csvFilePath) as csvFile:
  csvReader = csv.DictReader(csvFile)
  for csvRow in csvReader:
    print(csvRow)
    hostname = csvRow["ï»¿hostname"]
    data[hostname] = csvRow
    #print(data)
    print(type(data))
    print("\n\n\n\n")
#print(data)

#write to json file:
with open("table.json", "w") as jsonFile:
  jsonFile.write(json.dumps(data, indent = 4))


