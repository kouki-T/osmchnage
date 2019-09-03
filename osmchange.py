import requests
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
import sqlite3

conn = sqlite3.connect("testsample.db")
cur = conn.cursor()

def changesetloop(setnumber):
    url = "https://www.openstreetmap.org/api/0.6/changeset/" + str(setnumber)
    urlnumber = url.strip("https://www.openstreetmap.org/api/0.6/changeset/")

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        xml_string = response.read()
    root = ET.fromstring(xml_string)

    child = root[0]

    osm = str(child.attrib)
    osm2 = osm.split()

    lat_p = osm2[17].strip("','")
    lon_p = osm2[19].strip("','")
    
    if 123 <= float( lon_p) <=140:
        item = (setnumber , lat_p , lon_p)
        cur.execute("INSERT INTO geolatlon VALUES (? , ? , ?)" , item)
        conn.commit()
        return print('%s is compleated.' % setnumber)
    else:
        return print('%s is not Japan.' % setnumber)
    

changesetloop(10000)
changesetloop(40000)
changesetloop(60000)
changesetloop(70127314)

cur.execute("SELECT * FROM geolatlon")
x = cur.fetchall()
print(x)
conn.close()