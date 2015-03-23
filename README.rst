===============================
GeoPublisher
===============================

Tools to publish GIS data using Esri's Arcpy.

* Free software: Apache License 2.0
* Documentation: https://geopublisher.readthedocs.org.

Features
--------

* Publishes to/from shapefiles, file geodatabases, enterprise geodatabases (SDE)

* Can create zip archives of published feature classes by exporting them
  (if necessary) to shapefiles with a date in the filename
  (ex. 'Buildings.shp_20150318.zip').


Installation
------------

* git clone or download and extract zip file

* At the command line::

    easy_install geopublisher

* Build documentation::

    cd docs

    make html

TODO
----

* Add table publishing capabilities

* Flesh out documentation

Tests
-----

* Install tox::

    pip install tox

* Run tests::

    tox
