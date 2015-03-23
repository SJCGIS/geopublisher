#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_geopublisher
----------------------------------

Tests for `geopublisher` module.
"""

import os
import unittest
import arcpy
import zipfile
from datetime import date, datetime

from geopublisher import geopublisher


class TestGeopublisher(unittest.TestCase):

    def setUp(self):
        """
        Sets up the workspaces and geodatabases for the unit tests. You'll want
        to verify you have a 'data/Test_SDE.sde' database connection file to
        run enterprise geodatabase tests.
        """
        self.currentFolder = os.path.dirname(os.path.abspath(__file__))
        # File Geodatabase Settings
        self.testFgdb = os.path.join(self.currentFolder, 'data\Test_Fgdb.gdb')
        self.resultFgdb = os.path.join(self.currentFolder, 'results',
                                       'Results_Fgdb.gdb')
        # Shapefile Workspace Settings
        self.testShpWorkspace = os.path.join(self.currentFolder,
                                             'data\Test_Shapefiles')
        self.resultShpWorkspace = os.path.join(self.currentFolder,
                                               'results\Results_Shapefiles')
        # SDE Workspace Settings
        self.testSde = os.path.join(self.currentFolder, 'data\Test_SDE.sde')
        # Archive Workspace Settings
        self.archiveWorkspace = os.path.join(self.currentFolder,
                                             'results\Results_Archive')

    def test_publishFgdbToShapefile(self):
        """
        Test publishing a feature class from File Geodatabase to Shapefile
        """
        f1 = os.path.join(self.testFgdb, 'Fire_Stations')
        loc = self.resultShpWorkspace
        f2 = 'Fire_Stations.shp'
        geopublisher.publish_data(f1, loc, f2)
        self.assertTrue(arcpy.Exists(os.path.join(loc, f2)))

    def test_publishFgdbToShapefileAndArchive(self):
        """
        Test publishing and archiving a feature class from File Geodatabase to
        Shapefile
        """
        f1 = os.path.join(self.testFgdb, 'NOAA_Shorelines')
        loc = self.resultShpWorkspace
        f2 = 'NOAA_Shorelines.shp'
        zipFolder = self.archiveWorkspace
        zipFile = f2 + '_' + date.isoformat(datetime.now()) + '.zip'
        print zipFolder, zipFile
        geopublisher.publish_data(f1, loc, f2, zipFolder)
        self.assertTrue(arcpy.Exists(os.path.join(loc, f2)))
        self.assertTrue(zipfile.is_zipfile(os.path.join(zipFolder, zipFile)))

    def test_publishSdeToShapefile(self):
        """
        Test publishing a feature class from enterprise geodatabase (SDE) to
        Shapefile
        """
        f1 = os.path.join(self.testSde,
                          'Master_GISDATA.DBO.cadastral',
                          'Master_GISDATA.DBO.Plat_Boundaries')
        loc = self.resultShpWorkspace
        f2 = 'Plat_Boundaries.shp'
        geopublisher.publish_data(f1, loc, f2)
        self.assertTrue(arcpy.Exists(os.path.join(loc, f2)))

    def test_publishSdeToShapefileAndArchive(self):
        """
        Test publishing and archiving a feature class from enterprise
        geodatabase (SDE) to shapefile
        """
        f1 = os.path.join(self.testSde,
                          'Master_GISDATA.DBO.cadastral',
                          'Master_GISDATA.DBO.Parcel_Point')
        loc = self.resultShpWorkspace
        f2 = 'Parcel_point.shp'
        zipFolder = self.archiveWorkspace
        zipFile = f2 + '_' + date.isoformat(datetime.now()) + '.zip'
        print zipFolder, zipFile
        geopublisher.publish_data(f1, loc, f2, zipFolder)
        self.assertTrue(arcpy.Exists(os.path.join(loc, f2)))
        self.assertTrue(zipfile.is_zipfile(os.path.join(zipFolder, zipFile)))

    def test_publishShapefileToShapefile(self):
        """
        Test publishing a shapefile to another shapefile
        """
        f1 = os.path.join(self.testShpWorkspace, 'Airports.shp')
        loc = self.resultShpWorkspace
        f2 = 'Airport.shp'
        geopublisher.publish_data(f1, loc, f2)
        self.assertTrue(arcpy.Exists(os.path.join(loc, f2)))

    def test_publishShapefileToShapefileAndArchive(self):
        """
        Test publishing and archiving a shapefile to another shapefile
        """
        f1 = os.path.join(self.testShpWorkspace, 'bridges.shp')
        loc = self.resultShpWorkspace
        f2 = 'bridges.shp'
        zipFolder = self.archiveWorkspace
        zipFile = f2 + '_' + date.isoformat(datetime.now()) + '.zip'
        print zipFolder, zipFile
        geopublisher.publish_data(f1, loc, f2, zipFolder)
        self.assertTrue(arcpy.Exists(os.path.join(loc, f2)))
        self.assertTrue(zipfile.is_zipfile(os.path.join(zipFolder, zipFile)))

    def test_publishFgdbToFgdb(self):
        """
        Test publishing a feature class from a file geodatabase to
        another file geodatabase
        """
        f1 = os.path.join(self.testFgdb, 'Fire_Stations')
        loc = self.resultFgdb
        f2 = 'Fire_Stations'
        geopublisher.publish_data(f1, loc, f2)
        self.assertTrue(arcpy.Exists(os.path.join(loc, f2)))

    def test_publishFgdbToFgdbAndArchive(self):
        """
        Test publishing and archiving a feature class from a file
        geodatabase to another file geodatabase. The feature class
        is also archived as a shapefile
        """
        f1 = os.path.join(self.testFgdb, 'NOAA_Shorelines')
        loc = self.resultFgdb
        f2 = 'NOAA_Shorelines'
        zipFolder = self.archiveWorkspace
        zipFile = f2 + '_' + date.isoformat(datetime.now()) + '.zip'
        print zipFolder, zipFile
        geopublisher.publish_data(f1, loc, f2, zipFolder)
        self.assertTrue(arcpy.Exists(os.path.join(loc, f2)))
        self.assertTrue(zipfile.is_zipfile(os.path.join(zipFolder, zipFile)))

    def test_publishSdeToFgdb(self):
        """
        Test publishing a feature class from an enterprise geodatabase
        (SDE) to a file geodatabase.
        """
        f1 = os.path.join(self.testSde, 'Master_GISDATA.DBO.Roads',
                          'Master_GISDATA.DBO.MP_Markers_2008')
        loc = self.resultFgdb
        f2 = 'MP_Markers_2008'
        geopublisher.publish_data(f1, loc, f2)
        self.assertTrue(arcpy.Exists(os.path.join(loc, f2)))

    def test_publishSdeToFdgbAndArchive(self):
        """
        Test publishing and archiving a feature class from an enterprise
        geodatabase (SDE) to a file geodatabase. The feature class is also
        archived as a shapefile
        """
        f1 = os.path.join(self.testSde, 'Master_GISDATA.DBO.Roads',
                          'Master_GISDATA.DBO.MP_Routes_2008')
        loc = self.resultFgdb
        f2 = 'MP_Routes_2008'
        zipFolder = self.archiveWorkspace
        zipFile = f2 + '_' + date.isoformat(datetime.now()) + '.zip'
        print zipFolder, zipFile
        geopublisher.publish_data(f1, loc, f2, zipFolder)
        self.assertTrue(arcpy.Exists(os.path.join(loc, f2)))
        self.assertTrue(zipfile.is_zipfile(os.path.join(zipFolder, zipFile)))

    def test_publishShapefileToFgdb(self):
        """
        Test publishing a shapefile to a file geodatabase
        """
        f1 = os.path.join(self.testShpWorkspace, 'Airports.shp')
        loc = self.resultFgdb
        f2 = 'Airports'
        geopublisher.publish_data(f1, loc, f2)
        self.assertTrue(arcpy.Exists(os.path.join(loc, f2)))

    def test_publishShapefileToFgdbAndArchive(self):
        """
        Test publishing and archiving a shapefile to a file
        geodatabase. The feature class is also archived as a
        shapefile
        """
        f1 = os.path.join(self.testShpWorkspace, 'bridges.shp')
        loc = self.resultFgdb
        f2 = 'bridges'
        zipFolder = self.archiveWorkspace
        zipFile = f2 + '_' + date.isoformat(datetime.now()) + '.zip'
        geopublisher.publish_data(f1, loc, f2, zipFolder)
        self.assertTrue(arcpy.Exists(os.path.join(loc, f2)))
        self.assertTrue(zipfile.is_zipfile(os.path.join(zipFolder, zipFile)))

    def test_zipShapefile(self):
        """
        Test creation of a shapefile archive. The test creates the zip
        file and should only add the files necessary for the shapefile.
        In this case, the 'Airports.mxd' file is not a shapefile part and
        should be excluded from the archive.
        """
        shapefile = os.path.join(self.testShpWorkspace, 'Airports.shp')
        testZipFile = os.path.join(self.archiveWorkspace, 'testZip.zip')
        try:
            zf = zipfile.ZipFile(testZipFile, mode='w',
                                 compression=zipfile.ZIP_DEFLATED)
            geopublisher.shape_zipper(shapefile, zf)
        except arcpy.ExecuteError as e:
            raise e
        finally:
            zf.close()
        archiveFiles = zf.namelist()
        self.assertNotIn('Airports.mxd', archiveFiles)

    def tearDown(self):
        """
        Clean up the test results by deleting temporary shapefiles,
        feature classes and archives.
        """
        arcpy.env.workspace = self.resultShpWorkspace
        shapefiles = arcpy.ListFeatureClasses()
        for shp in shapefiles:
            arcpy.Delete_management(shp)
        arcpy.env.workspace = self.resultFgdb
        fcs = arcpy.ListFeatureClasses()
        for fc in fcs:
            arcpy.Delete_management(fc)
        for root, dirs, files in os.walk(self.archiveWorkspace):
            for file in files:
                os.remove(os.path.join(root, file))

if __name__ == '__main__':
    unittest.main()
