# -*- coding: utf-8 -*-
"""
/***************************************************************************
 MySample
                                 A QGIS plugin
 QGIS Sample Plugin
                              -------------------
        begin                : 2023-02-24
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Tsubasa Moriguchi
        license              : GNU General Public License v2.0
 ***************************************************************************/
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qgis.core import *
from qgis.gui import *

QString = str

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
    
class MySample01:
    def __init__(self, iface):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()

    def message_add(self):
        # Menu01 Click to display message
        QMessageBox.information(None, u'ウィンドウ名', u'MySample_Menu01!')