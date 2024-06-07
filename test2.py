import streetview
import matplotlib.pyplot as plt
import requests
import json
import numpy as np
from PIL import Image
import geopandas as gp
import os
from shapely.geometry import Point, LineString, Polygon

GOOGLE_MAPS_API_KEY = "AIzaSyDqottGUfvxiYc6s_G9qHQzTtNaM7dhl08"

headers = {'Content-Type': 'application/json'}
data = """{"mapType": "streetview","language": "en-US", "region": "US"}"""
response = requests.post("https://tile.googleapis.com/v1/createSession?key={}".format(GOOGLE_MAPS_API_KEY), headers=headers, data=data)
SESSION_TOKEN = response.json()['session']
iD = "8OUxbc7B9WLOJBHdPfKMXQ"

meta = requests.get("https://tile.googleapis.com/v1/streetview/metadata?session={}&key={}&panoId={}".format(SESSION_TOKEN, GOOGLE_MAPS_API_KEY,iD))
print(meta.json())

#panos = streetview.panoids(lat=40.993791549894446, lon=39.77886227229716)
#for pano in panos:
#    print(pano)