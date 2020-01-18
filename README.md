# oadownload
Python 3.x scripts used for downloading and cleaning up CSV's from <a href="https://openaddresses.io/">openaddresses.io</a>

The psycopg2 library needs to be installed in addition to the standard libraries. It is assumed the user is familiar with Python, PostGIS and pgAdmin geoprocessing tools. It is assumed the user has access to and is proficient with Esri's ArcGIS Pro for creating geocode locator files.

1. Run download_cal.py to download everthing in California except Los Angeles County into the folder these scripts will be used.
2. Run extraxct_zip.py to extract CSV files from ZIP files.
3. Use pgAdmin to create a PostGres database for your tables.
4. Update my_postgres_credentials.py with your postgres database name, user, and password.
5. Run load_csv.py to create and populate a table oa_california_text from your CSVs.
6. In pgAdmin, run the statements in cleanup.sql. Copy/pasting indivdual statements is best practice for new users.
7. In pgAdmin run gis.sql	for converting your final geospatial tables.
8. in ArcGIS Pro, import your final PostGIS table as a feature class and <a heref="https://pro.arcgis.com/en/pro-app/help/data/geocoding/create-a-locator.htm">create your locator file</a>.

These last two scripts are usefil:
csv_numlines.py: outputs your CSVs along with number of rows in each file
move_zip.py: creates a folder 'zip' and moves all your files there
