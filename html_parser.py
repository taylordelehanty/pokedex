#!/usr/bin/env python3

from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint

class HTMLParserForTMs(HTMLParser):

def __init__(self):
    HTMLParser.__init__(self)
    self.recording = 0
    self.data = []

    def handle_starttag(self, tag, attributes):
        if tag != 'td':
            return
        if self.recording:
            self.recording += 1
            return
        for name, value in attributes:
            if name == 'class' and value == 'cen':
                break
            else:
                return
        self.recording = 1

    def handle_endtag(self, tag):
        if tag == 'td' and self.recording:
            self.recording -= 1

    def handle_data(self, data):
        if 'TM' in data and self.recording:
            self.data.append(data)
