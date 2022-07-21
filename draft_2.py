import json
import requests
f1_data_req = requests.get("http://ergast.com/api/f1/2021/drivers.json")
print(f1_data_req)

print(f1_data_req.headers)
print(f1_data_req.content) # this gives us a list of drivers but the list is limited to 30.

s = ''.join(map(chr, f1_data_req.content))
print(s)
print(type(s))

dict = json.loads(s)
print(dict)
print(type(dict))

print(dict['MRData'])
print(dict['MRData']['DriverTable'])    #this is a list of dictionaries for each driver
print(dict['MRData']['DriverTable']['Drivers'])
print(dict['MRData']['DriverTable']['Drivers'][0]['givenName'])

driver_list = []
for i in range(len(dict['MRData']['DriverTable']['Drivers'])):
    driver_list.append({"First Name": dict['MRData']['DriverTable']['Drivers'][i]['givenName'],
                       "Last Name": dict['MRData']['DriverTable']['Drivers'][i]['familyName'],
                        "Car Number": dict['MRData']['DriverTable']['Drivers'][i]['permanentNumber']})
print(driver_list)

