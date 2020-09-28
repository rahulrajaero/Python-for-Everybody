import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'http://python-data.dr-chuck.net/geojson'
address = input('Enter location: ')
url = serviceurl + '?' + urllib.parse.urlencode({'sensor':'false', 'address':  address})
data = urllib.request.urlopen(url).read().decode()
info = json.loads(data)
#print(info)
info = info['results']
print ('Retrieving', url, '\nRetrieved', len(data), 'caracters')
for item in info:
    key = item['place_id']
#    print(key)
print ('Place id:', key)