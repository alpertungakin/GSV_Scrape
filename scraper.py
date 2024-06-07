import streetview
import matplotlib.pyplot as plt
import requests
import json
import numpy as np
from PIL import Image
import geopandas as gp
import os
from shapely.geometry import Point, LineString, Polygon

def unique(list1):
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

buildings = gp.read_file("building_konaklar.shp")
centroid = buildings.centroid
lons = list(centroid.x)
lats = list(centroid.y)
panoIds = []
#lat, lon = 40.99771765148172, 39.77149431400864
GOOGLE_MAPS_API_KEY = "AIzaSyDqottGUfvxiYc6s_G9qHQzTtNaM7dhl08"

headers = {'Content-Type': 'application/json'}
data = """{"mapType": "streetview","language": "en-US", "region": "US"}"""
response = requests.post("https://tile.googleapis.com/v1/createSession?key={}".format(GOOGLE_MAPS_API_KEY), headers=headers, data=data)
SESSION_TOKEN = response.json()['session']

for i in range(len(lats)):
    try:
        panos = streetview.panoids(lat=lats[i], lon=lons[i])
        first = panos[0]['panoid']
        panoIds.append(first)
    except: 
        IndexError

panoIds_u = unique(panoIds)


for iD in panoIds_u:
    g1 = requests.get("https://tile.googleapis.com/v1/streetview/tiles/{}/{}/{}?session={}&key={}&panoId={}".format(2,0,0,SESSION_TOKEN, GOOGLE_MAPS_API_KEY,iD))
    g2 = requests.get("https://tile.googleapis.com/v1/streetview/tiles/{}/{}/{}?session={}&key={}&panoId={}".format(2,1,0,SESSION_TOKEN, GOOGLE_MAPS_API_KEY,iD))
    g3 = requests.get("https://tile.googleapis.com/v1/streetview/tiles/{}/{}/{}?session={}&key={}&panoId={}".format(2,2,0,SESSION_TOKEN, GOOGLE_MAPS_API_KEY,iD))
    g4 = requests.get("https://tile.googleapis.com/v1/streetview/tiles/{}/{}/{}?session={}&key={}&panoId={}".format(2,3,0,SESSION_TOKEN, GOOGLE_MAPS_API_KEY,iD))
    g5 = requests.get("https://tile.googleapis.com/v1/streetview/tiles/{}/{}/{}?session={}&key={}&panoId={}".format(2,0,1,SESSION_TOKEN, GOOGLE_MAPS_API_KEY,iD))
    g6 = requests.get("https://tile.googleapis.com/v1/streetview/tiles/{}/{}/{}?session={}&key={}&panoId={}".format(2,1,1,SESSION_TOKEN, GOOGLE_MAPS_API_KEY,iD))
    g7 = requests.get("https://tile.googleapis.com/v1/streetview/tiles/{}/{}/{}?session={}&key={}&panoId={}".format(2,2,1,SESSION_TOKEN, GOOGLE_MAPS_API_KEY,iD))
    g8 = requests.get("https://tile.googleapis.com/v1/streetview/tiles/{}/{}/{}?session={}&key={}&panoId={}".format(2,3,1,SESSION_TOKEN, GOOGLE_MAPS_API_KEY,iD))



    with open("{}_{}.jpg".format(iD,0), 'wb') as f:
        f.write(g1.content)

    with open("{}_{}.jpg".format(iD,1), 'wb') as f:
        f.write(g2.content)

    with open("{}_{}.jpg".format(iD,2), 'wb') as f:
        f.write(g3.content)

    with open("{}_{}.jpg".format(iD,3), 'wb') as f:
        f.write(g4.content)

    with open("{}_{}.jpg".format(iD,4), 'wb') as f:
        f.write(g5.content)

    with open("{}_{}.jpg".format(iD,5), 'wb') as f:
        f.write(g6.content)

    with open("{}_{}.jpg".format(iD,6), 'wb') as f:
        f.write(g7.content)

    with open("{}_{}.jpg".format(iD,7), 'wb') as f:
        f.write(g8.content)

    images_r1 = [Image.open(x) for x in ["{}_{}.jpg".format(iD,0), "{}_{}.jpg".format(iD,1), "{}_{}.jpg".format(iD,2), "{}_{}.jpg".format(iD,3)]]
    images_r2 = [Image.open(x) for x in ["{}_{}.jpg".format(iD,4), "{}_{}.jpg".format(iD,5), "{}_{}.jpg".format(iD,6), "{}_{}.jpg".format(iD,7)]]
    widths, heights = zip(*(i.size for i in images_r1))
    total_width = sum(widths)
    max_height = max(heights)
    new_im_r1 = Image.new('RGB', (total_width, max_height))
    new_im_r2 = Image.new('RGB', (total_width, max_height))
    new_im = Image.new('RGB', (total_width, 2*max_height))

    x_offset1 = 0
    x_offset2 = 0

    y_offset = 0

    for im in images_r1:
        new_im_r1.paste(im, (x_offset1,0))
        x_offset1 += im.size[0]

    for im in images_r2:
        new_im_r2.paste(im, (x_offset2,0))
        x_offset2 += im.size[0]

    ims = [new_im_r1,new_im_r2]

    for img in ims:
        new_im.paste(img, (0, y_offset))

        y_offset += max_height

    new_im.save("{}.jpg".format(iD))
    print("{}.jpg".format(iD))
    os.remove("{}_{}.jpg".format(iD,0))
    os.remove("{}_{}.jpg".format(iD,1))
    os.remove("{}_{}.jpg".format(iD,2))
    os.remove("{}_{}.jpg".format(iD,3))
    os.remove("{}_{}.jpg".format(iD,4))
    os.remove("{}_{}.jpg".format(iD,5))
    os.remove("{}_{}.jpg".format(iD,6))
    os.remove("{}_{}.jpg".format(iD,7))


