import requests
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

url = "https://www.openstreetmap.org/api/0.6/changeset/71779142"

req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    xml_string = response.read()
root = ET.fromstring(xml_string)

child = root[0]

osm = str(child.attrib)
osm2 = osm.split()

lat = osm2[17]
lon = osm2[19]

url2 = "http://www.finds.jp/ws/rgeocode.php?" + "lat=" + lat + "&" + "lon=" + lon

req2 = urllib.request.Request(url2)

with urllib.request.urlopen(req2) as response2:
    xml_string = response2.read()
root2 = ET.fromstring(xml_string)

child2 = root2[0]

osm3 = str(child2.tag)


print(osm3)
