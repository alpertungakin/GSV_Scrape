# 40.992381°N 39.776593°E goruntu
# 40.992733°N 39.776618°E orman
# 40.992412°N 39.777144°E sera
# 40.992327°N 39.775779°E elektrik
# 40.991864°N 39.776616°E d kapı

import numpy as np
import math
import pyproj

geodesic = pyproj.Geod(ellps='WGS84')

def getBearing(a,b):
    fwd_azimuth,back_azimuth,distance = geodesic.inv(A[1], A[0], B[1], B[0])
    if fwd_azimuth < 0:
        fwd_azimuth = fwd_azimuth + 360
    return fwd_azimuth

A = [40.992381, 39.776593]
B = [40.992327, 39.775779]

print(getBearing(A,B))

# (col/360)*north + bearing*(col/360)


