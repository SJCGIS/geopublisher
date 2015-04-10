# -*- coding: utf-8 -*-

import os
import glob
import arcpy
from datetime import date, datetime
import zipfile


def publish_data(input_fc, output_location, output_fc, archive_folder=None):
    """
    input_fc: Feature class to be exported
    output_location: Folder or geodatabase location for output feature
    output_fc: Feature class to be created (existing feature classes with this
    name will be deleted)
    archive_folder: Folder for archived data to be exported as zip file
    (optional)

    Exports a feature class from one type to another. Existing feature classes
    with same name will be deleted. We can also create an archived zip file of
    the output feature class at a location we specify. The zip file is
    automatically named after the output feature class with the current date
    (ex. 'Buildings.shp_20150318.zip')
    """
    try:
        output_file = os.path.join(output_location, output_fc)
        print(output_file)
        print('Publishing ' + input_fc + ' to ' + output_file)
        if arcpy.Exists(output_file):
            print (output_file + ' exists, trying to delete...')
            arcpy.Delete_management(output_file)
        print('Exporting %s to %s' % (input_fc, output_file))
        arcpy.CopyFeatures_management(input_fc, output_file)
        if archive_folder:
            try:
                create_archive(archive_folder, output_file)
            except arcpy.ExecuteError as e:
                raise e
    except arcpy.ExecuteError as e:
        raise e


def create_archive(archive_folder, output_file):
    """
    archive_folder: Folder to store zip file
    output_file: Feature class to be archived

    Creates a zip file containing a shapefile representation of the
    output_file.
    If the output_file is not a shapefile, it creates a temporary shapefile to
    add to the archive.
    """
    output_desc = arcpy.Describe(output_file)
    if not output_desc.dataType == 'ShapeFile':
        """
        If output_file isn't a shapefile, create a temporary one to
        use for archiving
        """
        temp_name = arcpy.CreateScratchName('tmp', '', 'Shapefile',
                                            arcpy.env.scratchFolder)
        temp_file = os.path.join(os.environ['TMP'], temp_name)
        arcpy.CopyFeatures_management(output_file, temp_file)
        output_file = temp_file
        print('Creating temporary shapefile %s for archiving' % output_file)
    print('output_desc.file: %s' % output_desc.file)
    archive_file = output_desc.file
    archive_file += '_'
    archive_file += date.isoformat(datetime.now())
    archive_file += '.zip'
    archive_filepath = os.path.join(archive_folder, archive_file)
    print('Archiving %s to %s' % (output_file, archive_filepath))
    output_desc = arcpy.Describe(output_file)
    try:
        with zipfile.ZipFile(archive_filepath, mode='w',
                             compression=zipfile.ZIP_DEFLATED) as zf:
            shape_zipper(output_file, zf)
            zip_info(zf)
    except arcpy.ExecuteError as e:
        raise e


def shape_zipper(shapefile, zip):
    """
    shapefile: Path of shapefile to be zipped
    zip: zip file to add shapefile to

    Takes a shapefile name and adds all possible shapefile file extensions to
    the given zip file.
    """

    files = get_shapefile_files(shapefile)
    for file in files:
            try:
                print('Adding %s...' % file)
                name = os.path.basename(file)
                zip.write(file, arcname=name)
            except arcpy.ExecuteError as e:
                raise e


def get_shapefile_files(shp_name):
    """
    shp_name: The name of the shapefile (ex. Parcels.shp)

    Takes the base name of a shapefile and finds all possible shapefile files
    extensions in the same directory. Returns a list of all shapefile files.
    """

    shapefile_extensions = ['.shp', '.shx', '.dbf', '.sbn', '.sbx', '.fbn',
                            '.fbx', '.ain', '.aih', '.atx', '.ixs', '.mxs',
                            '.prj', '.xml', '.cpg']
    shapefile_wildcard = os.path.splitext(shp_name)[0] + ".*"
    files = []
    for file in glob.glob(shapefile_wildcard):
        if os.path.splitext(file)[1] in shapefile_extensions:
            files.append(file)
    return files


def zip_info(zip):
    for info in zip.infolist():
        print(info.filename)
        print('\tComment:\t', info.comment)
        print('\tModified:\t', datetime(*info.date_time))
        print('\tSystem:\t\t', info.create_system, '(0 = Windows, 3 = Unix)')
        print('\tZIP version:\t', info.create_version)
        print('\tCompressed:\t', info.compress_size, 'bytes')
        print('\tUncompressed:\t', info.file_size, 'bytes')
        print()
