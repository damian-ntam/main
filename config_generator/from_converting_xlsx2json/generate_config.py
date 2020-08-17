#import excel_to_json
#import excel2json
#import xls2json
#import xlrd
from io import StringIO
#convert("LLD_sample_monitor.xlsx")
import xlrd
import json
import json as JSON
from collections import OrderedDict
import simplejson as json
# Open the workbook and select the first worksheet
wb = xlrd.open_workbook('LLD_sample_monitor.xls')
sh = wb.sheet_by_index(0)
# List to hold dictionaries
cars_list = []
# Iterate through each row in worksheet and fetch values into dict
for rownum in range(1, sh.nrows):
    cars = OrderedDict()
    row_values = sh.row_values(rownum)
    cars['Object'] = row_values[0]
    cars['Unique_ID'] = row_values[1]
    cars['Scope'] = row_values[2]
    cars['Applicable_environments'] = row_values[3]
    cars['Applicable_countries'] = row_values[4]
    cars['Blueprint/Country Specific'] = row_values[5]
    cars['Tenant'] = row_values[6]
    cars['ADC'] = row_values[7]
    cars['Ports'] = row_values[8]
    cars['Protocol'] = row_values[9]
    cars['Parent_Monitor'] = row_values[10]
    cars['Interval'] = row_values[11]
    cars['Up_Interval'] = row_values[12]
    cars['Time_Until_Up'] = row_values[13]
    cars['Timeout'] = row_values[14]
    cars['Send_String'] = row_values[15]
    cars['Receive_String'] = row_values[16]
    cars['Alias_Address'] = row_values[17]
    cars['Comments'] = row_values[18]
    cars['ODEP_Tickets'] = row_values[19]
    cars['Release'] = row_values[20]
    cars['Change_Log'] = row_values[21]
    cars_list.append(cars)

# Serialize the list of dicts to JSON string
j = json.dumps(cars_list)


print(json.dumps(j, indent=4, sort_keys=True))

#We have written a json string to below file:
with open('data.json', 'w') as f:
    f.write(json.dumps(j, indent=2, sort_keys=True))
    f.close()


with open('data.json', 'r') as f:
    #str_response = f.read().decode('utf-8')
    #read_json_var = json.loads(f.decode("utf-8"))
    read_json_var = json.loads(f)

print("'\n'")
print("Now json data is being read !!!! ")

print(read_json_var['Object'])




# Write to file
#with open('data.json', 'w') as f:
#    f.write(j)

#print(json.dumps(j, indent=4, sort_keys=True))

