#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """Acccess a file and logs a message with timestampt.

    Attributes:
        None
    """

    def __init__(self, logfilename):
        """
        Args:
            logfilename (str): Name of file to be accessed.
            msgs (list): List of messages to be logged.
        """
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """
        Args:
            msg (str): Message.
            timestamp (float): Unix Time Stamp.

        Examples:
        >>> loggin.log('some_message')
        >>> loggin.msgs
        [(1429725298.676674, 'some_message')]
        """
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """Opens file and logs message in file.

        Args:
            handled (list): List of handled messages.

        Examples:
        >>> newfile = 'Somefilename'
        >>> loggin = CustomLogger(newfile)
        """
        handled = []
        try:
            fhandler = open(self.logfilename, 'a')
            for index, entry in enumerate(self.msgs):
                fhandler.write(str(entry) + '\n')
                handled.append(index)

            fhandler.close()

            for index in handled[::-1]:
                del self.msgs[index]
        except IOError:
            self.log(IOError)
            raise IOError
