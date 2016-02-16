#!/usr/bin/env python3

from PyQt4 import QtGui
import sys
import os
import urllib.request
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication, QPixmap, QWidget, QLabel

class PokemonDisplay():
    url = 'http://vignette1.wikia.nocookie.net/nintendo/images/e/e6/Pokemon_Logo.png/revision/latest?cb=20100831014812&path-prefix=en'

    def __init__(self, url):
        self.url = url

    def draw_image(self):
        data = urllib.request.urlopen(self.url).read()
        image = QtGui.QImage()
        image.loadFromData(data)
        
        app = QApplication(sys.argv)
        w = QWidget()
        w.setWindowTitle('Pokemon')
        
        label = QLabel(w)
        pixmap = QPixmap(image)
        label.setPixmap(pixmap)
        w.resize(pixmap.width(), pixmap.height())
        
        w.show()
        app.exec_()
