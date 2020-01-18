-- enable PostGIS in your database
create extension postgis;

-- create a geospatial table based on lat/lon values in WGS84 (epsg: 4326)
create table oa_california_4326 as select
myid,
src,
number,
street,
unit,
city,
region,
postcode,
ST_SetSRID(ST_MakePoint(cast(lon as double precision),cast(lat as double precision)),4326) as geom 
from oa_california_text;

-- create spatial index for the above table
CREATE INDEX oa_california_4326_idx
    ON public.oa_california_4326 USING gist (geom);

-- project the above table from WGS84 to California Zone 5 (epsg: 2229) for your locator
create table oa_california_2229 as select
myid,
src,
number,
street,
unit,
city,
region,
postcode,
ST_Transform(geom, 2229) as geom
from oa_california_4326;

-- create spatial index for the above table
CREATE INDEX oa_california_2229_idx
    ON public.oa_california_2229 USING gist (geom);
