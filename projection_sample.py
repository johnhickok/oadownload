# sample code transform coordinates
# https://pcjericks.github.io/py-gdalogr-cookbook/projection.html

from osgeo import ogr
from osgeo import osr

source = osr.SpatialReference()
source.ImportFromEPSG(4326)

target = osr.SpatialReference()
target.ImportFromEPSG(2229)

transform = osr.CoordinateTransformation(source, target)

point = ogr.CreateGeometryFromWkt("POINT (-119.118610 32.858542)")
point.Transform(transform)

print (point.ExportToWkt())
