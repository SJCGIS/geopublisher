import sys
import datetime
import os
from arcpy import GetMessages


class Logger:
    log = ''
    logFolder = os.path.join(os.getcwd(), 'Logs')
    scriptName = ''
    addLogsToArcpyMessages = False

    def __init__(self, addLogsToArcpyMessages=False):
        self.addLogsToArcpyMessages = addLogsToArcpyMessages
        now = datetime.datetime.now()
        today = datetime.date.isoformat(now.date())
        time = datetime.time.isoformat(now.time())
        self.scriptName = os.path.split(sys.argv[0])[1]
        self.log = "{0} || {1} || {2} || {3}".format(self.scriptName, today, time, os.getenv('COMPUTERNAME'))

        if not os.path.exists(self.logFolder):
            os.mkdir(self.logFolder)

        self.logFile = os.path.join(self.logFolder, today + '.txt')
        print('Logger Initialized: {0}'.format(self.log))

    def logMsg(self, msg, printMsg=True):
        """
        msg: message text to be logged
        printMsg: boolean value whether or not to print the message
        to the screen

        Logs a message and can also print it to the screen if
        necessary
        """

        time = datetime.time.isoformat(datetime.datetime.now().time())
        self.log = '{0}\n{1} | {2}'.format(self.log, time, msg)
        if printMsg:
            print msg

        if self.addLogsToArcpyMessages:
            from arcpy import AddMessage
            AddMessage(msg)

    def logGPMsg(self, printMsg=True):
        """
        printMsg: boolean value whether or not to print the message
        to the screen

        Logs the geoprocessing messages and can also print them to the
        screen if necessary
        """

        msgs = GetMessages()
        try:
            self.logMsg(msgs, printMsg)
        except:
            self.logMsg('Error getting arcpy message', printMsg)

    def writeLogToFile(self):
        """
        Writes the log to a file
        """

        with open(self.logFile, mode='a') as f:
            f.write('\n\n{0}'.format(self.log))

    def logError(self, printMsg=True):
        """
        Logs the error traceback
        """

        import traceback

        self.logMsg('**ERROR**', printMsg)
        errMsg = traceback.format_exc()
        self.logMsg(errMsg, printMsg)
