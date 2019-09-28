import requests
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import json
import sqlite3

## dbの作成
conn = sqlite3.connect("testsample1.db")
cur = conn.cursor()
cur.execute("create table if not exists geolatlon (lat int, lon int)")

## changesetAPIを叩いて緯度経度を取得後、農研APIで日本かどうか判別。dbへ保存。
def changesetloop(setnumber):
    url = "https://www.openstreetmap.org/api/0.6/changeset/" + str(setnumber)

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        xml_string = response.read()
    root = ET.fromstring(xml_string)

    child = root[0]

    osm = str(child.attrib)
    osm2 = osm.split()
    try:
        lat_p = osm2[17].strip("','")
        lon_p = osm2[19].strip("','")
    except IndexError:
        return print('%s is out of range type.' % setnumber)

    req_url = "http://www.finds.jp/ws/rgeocode.php?lat={0}&lon={1}&json" .format(lat_p, lon_p)

    res = requests.get(req_url).text
    jpcheck = json.loads(res)["status"]

    try:
        if not jpcheck  == 200:
            return print('%s is not Japan.' % setnumber)
        else:
            item = (lat_p ,lon_p)
            cur.execute("INSERT INTO geolatlon VALUES (? , ?)" , item)
            conn.commit()
            return print('%s is compleated.' % setnumber)
    except ValueError:
        return print('%s is unformat xml type.' % setnumber)
"""
  try:
        if 123 <= float(lon_p) <=140:
            item = (lat_p ,lon_p)
            cur.execute("INSERT INTO geolatlon VALUES (? , ?)" , item)
            conn.commit()
            return print('%s is compleated.' % setnumber)
        else:
            return print('%s is not Japan.' % setnumber)
    except ValueError:
        return print('%s is unformat xml type.' % setnumber)
"""

## 検索するchangesetの番号を指定する
searchnumber = 73775492

## 検索範囲の指定
for searchchange in range(100):
    changesetloop(searchnumber)
    searchnumber +=1

## sqlへのアクセス終了
conn.close()
