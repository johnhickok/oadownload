--PostgreSQL code used to convert text to GIS point features
--drop table table oa_california_2229;
create table oa_california_2229 as select
myid,
src,
number,
street,
unit,
city,
region,
postcode,
ST_Transform(ST_SetSRID(ST_MakePoint(cast(lon as double precision),cast(lat as double precision)),4326), 2229) as geom 
from oa_california_text;

CREATE INDEX oa_california_2229_idx
    ON public.oa_california_2229 USING gist (geom);

-- Add an id unique identifier
alter table oa_california_2229 add column id serial primary key;



