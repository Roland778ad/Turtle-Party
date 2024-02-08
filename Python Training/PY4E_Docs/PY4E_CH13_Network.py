# PY4E Document
#CHAPTER 13 XML JSON
#By Roland Udvari 2024-02-07

import json
import urllib.request, urllib.parse, urllib.error
import ssl

# input = '''[
#    { "id" : "001",
#      "x" : "atr1",
#      "name" : "Chuck"
#    },
#    { "id" : "009",
#      "x" : "atr2",
#      "name" : "Chuck"
#    }
# ]'''
#
# info = json.loads(input)
# print('User count:', len(info))
# for item in info:
#     print('Name:', item['name'])
#     print('ID:', item['id'])
#     print('Attribute:', item['x'])
#     print(item['name'], item['id'], item['x'])
# print(info[1]['name'])

import xml.etree.ElementTree as ET
# data = '''<person><name>Chuck</name><phone type="intl">+1 734 303 4456</phone><email hide="yes"/></person>'''
#
# tree = ET.fromstring(data)
# print('Name', tree.find('name'))
# print('Name', tree.find('name').text)
# print('Attribute:', tree.find('phone').get('type'))

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True :
    address = input('Enter location: ')
    if len(address) < 1 : break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retreiving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrived', len(data), 'characters')

    try :
        js = json.loads(data)
    except :
        js = None

    if not js or 'status' not in js or js['status'] != 'OK' :
        print('==== Failure to Retreive ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)