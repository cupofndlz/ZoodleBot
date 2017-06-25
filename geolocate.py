import requests
import json
ip = input("Enter Ip: ")
url = 'http://ip-api.com/json/' + ip
r = requests.get(url)
print("IP: " + r.json()['query'])
print("Country: " + r.json()['country'] + " (" + r.json()['countryCode'] + ")")
print("Region/State: " + r.json()['regionName'] + " (" + r.json()['region'] + ")")
print("City: " + r.json()['city'])
print("Lat, Lon: " + str(r.json()['lat']) + ", " + str(r.json()['lon']))
print("ISP: " + r.json()['isp'])
print("AS number/name: " + r.json()['as'])
