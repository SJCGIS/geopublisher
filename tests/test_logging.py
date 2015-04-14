import sys
import datetime
import os
import shutil
import geopublisher.logging
import unittest


class ArcpyStub(object):
    """
    This is a stub we can use for testing arcpy functions rather
    than loading the arcpy library.
    """
    def __init__(self):
        pass

    def GetMessages(self):
        return '{0}\n{1}\n{2}'.format('msg1', 'msg2', 'msg3')


class TestLogger(unittest.TestCase):

    logTxt = 'test log text'
    errTxt = 'test error test'

    def setUp(self):
        """
        Sets up the Logger class
        """

        self.now = datetime.datetime.now()
        self.logger = geopublisher.logging.Logger()

    def tearDown(self):
        """
        Delete the Logger class
        """
        del self.logger

    def test_init(self):
        """
        Should get the name of the script and date
        """

        logString = '{0} || {1} || {2} || {3}'.format(os.path.split(sys.argv[0])[1],
                                                      datetime.date.isoformat(self.now.date()),
                                                      datetime.time.isoformat(self.now.time()),
                                                      os.getenv('COMPUTERNAME'))
        self.assertEqual(self.logger.log, logString)

    def test_logMsg(self):
        """
        Should append the log message
        """

        log = self.logger.log[:] # create a copy
        self.logger.logMsg(self.logTxt)
        time = datetime.time.isoformat(datetime.datetime.now().time())
        self.assertEqual(self.logger.log, '{0}\n{1} | {2}'.format(log, time, self.logTxt))

    def test_logGPMsg(self):
        """
        Should call get messages on arcpy
        """

        log = self.logger.log[:]
        arcpyStub = ArcpyStub()
        geopublisher.logging.GetMessages = arcpyStub.GetMessages
        self.logger.logGPMsg()
        time = datetime.time.isoformat(datetime.datetime.now().time())
        self.assertEqual(self.logger.log, '{0}\n{1} | msg1\nmsg2\nmsg3'.format(log, time))

    def test_writeToLogFile(self):
        """
        The log messages should append to the log file
        """
        self.logger.writeLogToFile()
        with open(self.logger.logFile, mode='r') as f:
            log = f.read()
        self.assertIn(self.logger.log, log)

    def test_logError(self):
        """
        Errors should log a traceback
        """
        log = self.logger.log[:]
        self.logger.logError()
        time = datetime.time.isoformat(datetime.datetime.now().time())
        self.assertEqual(self.logger.log, '{0}\n{1} | **ERROR**\n{2} | None\n'.format(log, time, time))
