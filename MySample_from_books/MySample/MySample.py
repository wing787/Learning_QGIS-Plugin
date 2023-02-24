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
from .resources import *

# Reading Menu
from .MySample_Menu_01 import MySample_Menu_01
from .MySample_Menu_02 import MySample_Menu_02

import os
import os.path
import sys
import codecs

QString = str

try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
    
class MySample:
    def __init__(self, iface):
        self.iface = iface
        self.canvas = self.iface.mapCanvas()

        self.plugin_dir = os.path.dirname(__file__)
        locale = QSettings().value('locale/userLocale')[0:2]
        locate_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'MySample_{}.qm'.format(locale))
        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)
        self.actions = []
        self.menu = u'MySample'
        self.toolbar = self.iface.addToolBar(u'MySample')
        self.toolbar.setObjectName(u'MySample')

    def tr(self, message):
        return QCoreApplication.translate('MySample', message)
    
    def add_action(
            self,
            icon_path,
            text,
            callback,
            enabled_flag=True,
            add_to_menu=True,
            add_to_toolbar=True,
            status_tip=None,
            whats_this=None,
            parent=None):
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)
        if status_tip is not None:
            action.setStatusTip(status_tip)
        if whats_this is not None:
            action.setWhatsThis(whats_this)
        if add_to_toolbar:
            self.toolbar.addAction(action)
        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)
        self.actions.append(action)
        return action
    
    def initGui(self):
        self.win = self.iface.mainWindow()
        icon_path = ':/plugins/MySample/icon.png'
        # Setting Menu
        self.add_action(
            icon_path=None,
            text=u"Menu01",
            callback=self.Menu01,
            parent=self.win)
        self.add_action(
            icon_path=None,
            text=u"Menu02",
            callback=self.Menu02,
            parent=self.win)
        
    def unload(self):
        for action in self.actions:
            self.iface.removePluginMenu(
                u'MySample',
                action)
            self.iface.removeToolBarIcon(action)
        del self.toolbar

    # Menu01 Menu click
    def Menu01(self):
        # reading SampleMenu01
        self.sample_Menu01 = MySample_Menu_01(self.iface)
        # Menu01 Click to display message
        self.sample_Menu01.message_add()

    # Menu02 Menu click
    def Menu02(self):
        # reading SampleMenu02
        self.sample_Menu02 = MySample_Menu_02(self.iface)
        # Menu02 Click to display message
        self.sample_Menu02.dig.show()

    def run(self):
        pass