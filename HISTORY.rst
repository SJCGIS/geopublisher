.. :changelog:

History
-------

0.1.2 (2015-04-10)
---------------------
* Fixed
  * Test tearDown no longer deletes .blank file in tests/data/results/Results_Archive directory
  * Similarly named shapefiles were getting matched too broadly and both were getting copied to a single zip file. Example: "TaxMap.shp" and "TaxMap_join.shp" are in the same folder. When trying to only zip "TaxMap.shp", "TaxMap_join.shp" is also added to the archive.
  * tox was looking for a missing pep8 dependency when running tests.

* Changed
  * Split the methods for finding files part of a shapefile into a new, testable function rather than as part of shape_zipper.
  * Modified test for above change.

* Added
  * Added tests for get_shapefile_files function.
  * Added easy_install to setup.cfg

0.1.1 (2015-03-25)
---------------------

* Fixed
  * Added two missing directories. Because Git doesn't support adding empty directories, I've added 'stub' files to the directories so they get picked up correctly. Without these directories, most of the tests were failing.
  * When the tests failed, the zf object couldn't be properly referenced in the finally blocks. I've switched to the contextlib / with syntax which avoids this issue and has other advantages.

0.1.0 (2015-03-23)
---------------------

* First release
