import requests
username = "CupOfNoodle"
url = "https://api.mojang.com/users/profiles/minecraft/" + username
r = requests.get(url)
uuid = r.json()['id']

url2 = "https://api.mojang.com/user/profiles/" + uuid + "/names"
r2 = requests.get(url2)
numNames = len(r2.json())
yah = ""
while(numNames > 0):
	yah += (r2.json()[numNames - 1]['name']) + "\n"
	numNames -= 1
print(yah)
