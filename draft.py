import json
import requests
f1_data_req = requests.get("http://ergast.com/api/f1/drivers.json")
print(f1_data_req)

print(f1_data_req.headers)
print('here:')
print(f1_data_req.content) # this gives us a list of drivers but the list is limited to 30.

s = ''.join(map(chr, f1_data_req.content))
print(s)
print(type(s))
print(s[1])
print(json.loads(s))
print(type(json.loads(s)))

#this also gave us the another url so lets investigate.

f1_data_req_2 = requests.get("http://ergast.com/api/f1/drivers.json")
print(f1_data_req_2.content) # I have no idea what the difference between the two lists is meant to be.
print('hi')

f1_data_req_3 = requests.get("http://ergast.com/api/f1/2021/10.json?limit=50")
print(f1_data_req_3.content) # gives us a wiki link to the 2021 British Grand Prix, circuit name, data and time of practises and sprint.

#Need to try and get rid of this limit.

f1_data_req_4 = requests.get("http://ergast.com/api/f1/2021/10")
print(f1_data_req_4)

print(f1_data_req_4.json)
print(type(f1_data_req_4.json))
#print(type(f1_data_req_4.json()))


f1_data_req_5 = requests.get("http://ergast.com/api/f1/2021/10")
print(f1_data_req_5.content)
print(type(f1_data_req_5.json))

resp = f1_data_req_5.json
print(resp)















