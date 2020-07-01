/*
The statements below can be used for some basic cleanup of the 80 or so files reoresenting addresses across 
California posted on openaddresses.io.
*/
-- you'll want to copy/paste the lines into pgAdmin's query tool

vacuum analyze;

select count(*) from oa_california_text;
--9593685
--8808841

-- no street name or number
delete from oa_california_text where street is null;
delete from oa_california_text where number is null;

-- values with non-numeric text values in lat/lon fields
delete from oa_california_text where lat !~ '^[0-9\.]+$';
delete from oa_california_text where lon !~ '^[-+]?[0-9]*\.?[0-9]+$';

-- lat/lon values outside of California (obvious location errors)
delete from oa_california_text where cast(lat as double precision) NOT BETWEEN 32.4 AND 42.5;
delete from oa_california_text where cast(LON as double precision) NOT BETWEEN -124.7 AND -113.8;

-- city values with '(Unincorp)' - Sonoma County
update oa_california_text set city = trim(replace(city, '(Unincorp)', '')) where city like '%(Unincorp)%';

-- street values 'unassigned'
delete from oa_california_text where street like 'UNASSIGNED%';

-- update 'CA' as the value for the region field - you'll use this later
update oa_california_text set region = 'CA';

-- update cities from city source csv files
update oa_california_text set city = upper(replace(replace(replace(src, 'city_of_', ''), '.csv', ''), '_', ' '))
where src like 'city_of%' and city is null;

-- street numbers with non numeric text
delete from oa_california_text where
number like '-'
or number like '?'
or number like '['
or number like 'Test'
or number like 'UNKNOWN'
;
