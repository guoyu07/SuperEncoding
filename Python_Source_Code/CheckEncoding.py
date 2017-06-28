#!/usr/bin/env python
import chardet


class CheckEncoding(object):
    def __init__(self, file=None):
        assert file, "File path is invalid"
        self.file = file

    def GetEncoding(self):
        f = open(self.file, 'r')
        encoding = chardet.detect(f.read(1024))
        f.close()
        return encoding
