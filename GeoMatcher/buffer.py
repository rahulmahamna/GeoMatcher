from pyproj import CRS, Transformer
from shapely.geometry import Point
from shapely.ops import transform
import json

def geodesic_point_buffer(lat, lon, km):
    # Azimuthal equidistant projection
    aeqd_proj = CRS.from_proj4(
        f"+proj=aeqd +lat_0={lat} +lon_0={lon} +x_0=0 +y_0=0")
    tfmr = Transformer.from_proj(aeqd_proj, aeqd_proj.geodetic_crs)
    buf = Point(0, 0).buffer(km * 1000)  # distance in metres
    transformer = transform(tfmr.transform, buf).exterior.coords[:]
    return {"type": "Feature", "properties": {},  "geometry": { "type": "Polygon", "coordinates": [[list(coords) for coords in transformer]]}}