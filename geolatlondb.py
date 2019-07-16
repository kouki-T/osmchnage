#!/usr/bin/env python
# coding: utf-8

# In[3]:


import requests
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
import sqlite3

url = "https://www.openstreetmap.org/api/0.6/changeset/71779142"
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


conn = sqlite3.connect("changesetgeo.db")
cur = conn.cursor()
item = (urlnumber , lat_p , lon_p)
cur.execute("INSERT INTO geolatlon VALUES (? , ? , ?)" , item)
conn.commit


# In[4]:


cur.execute("SELECT * FROM geolatlon")
cur.fetchone()


# In[ ]:




