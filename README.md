# oadownload
Python 3.x scripts used for downloading and cleaning up CSV's from <a href="https://openaddresses.io/">openaddresses.io</a>

It is assumed the user is familiar with Python, PostGIS and pgAdmin geoprocessing tools. The <a href="https://pypi.org/project/psycopg2/">psycopg2</a> library needs to be installed for working with PostgreSQL. If the user has access to Esri's ArcGIS Pro, an Esri-based geocode locator file can be created with the results.

1. Run <b>download_cal.py</b> to download everthing in California except Los Angeles County into the folder these scripts will be used.
2. Run <b>extraxct_zip.py</b> to extract CSV files from ZIP files.
3. Use pgAdmin to create a PostGres database for your tables.
4. Update <b>my_postgres_credentials.py</b> with your postgres database name, user, and password.
5. Run <b>load_csv.py</b> to create and populate a table oa_california_text from your CSVs.
6. In pgAdmin, run the statements in <b>cleanup.sql</b>. Copy/pasting indivdual statements is best practice for new users.
7. In pgAdmin run <b>gis.sql</b>	for converting your final geospatial tables.
8. in ArcGIS Pro, import your final PostGIS table as a feature class and <a heref="https://pro.arcgis.com/en/pro-app/help/data/geocoding/create-a-locator.htm">create your locator file</a>.

These last two scripts might be useful:
<ul>
  <li><b>csv_numlines.py</b>: outputs your CSVs along with number of rows in each file</li>
  <li><b>move_zip.py</b>: creates a folder 'zip' and moves all your files there</li>
</ul>

This small project is a quick fix to supplement our current geocoding workflows. <a href="https://pelias.io/">Pelias</a>, anyone?
