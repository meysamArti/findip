import requests

ip_request = requests.get('https://get.geojs.io/v1/ip.json')
my_ip = ip_request.json()['ip']
print ("ip =>",my_ip)
url = 'https://get.geojs.io/v1/ip/geo/'+ my_ip +'.json'

geo_request = requests.get(url)
geo_result =geo_request.json()
print(geo_result)
