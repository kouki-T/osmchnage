import requests
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json

url = "https://www.openstreetmap.org/api/0.6/changeset/71779142"

req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    xml_string = response.read()
root = ET.fromstring(xml_string)

child = root[0]

osm = str(child.attrib)
osm2 = osm.split()

lat_p = osm2[17].strip("','")
lon_p = osm2[19].strip("','")


def rgeocode(lat, lon, res_type):
    req_url = 'http://www.finds.jp/ws/rgeocode.php?lat={0}&lon={1}'.format(lat,lon)
    if res_type != None:
        req_url += '&{0}'.format(res_type)
        print(req_url)

        return requests.get(req_url)

res = rgeocode(lat_p, lon_p, 'json').text

jsonData = json.loads(res)['result']

pname = jsonData['prefecture']['pname']
mname = jsonData['municipality']['mname']
section = jsonData['local'][0]['section']

print("pname={0}, mname={1}, section={2}".format(pname, mname, section))
