import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

url = "https://www.openstreetmap.org/api/0.6/changeset/20000000"

req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    xml_string = response.read()
root = ET.fromstring(xml_string)

child = root[0]

print(child.tag,child.attrib)
