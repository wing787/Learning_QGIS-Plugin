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

from PyQt5 import uic, QtWidgets, QtCore

# Reading Ui_MySampleMenu02Base
from .MySample_Menu_02_Base import Ui_MySampleMenu02Base

class MySampleMenu02Dialog(QtWidgets.QDialog, Ui_MySampleMenu02Base):
    def __init__(self, parent=None):
        """Constructor."""
        super(MySampleMenu02Dialog, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        
        #self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)