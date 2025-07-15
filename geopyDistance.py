import geopy.distance

coords_1 = (13.735271077942391, 100.52876524963297) # Put in latitude and longtitude
coords_2 = (13.735286515234304, 100.52950889120022) # Put in latitude and longtitude

print(geopy.distance.geodesic(coords_1, coords_2).meters)
# Output is 80.44780898525379