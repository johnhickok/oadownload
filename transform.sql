create table table6_2229 as select
ogc_fid,
number,
street,
unit,
city,
district,
region,
postcode,
ST_Transform(geom, 2229) from
table6
;