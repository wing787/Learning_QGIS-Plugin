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

def classFactory(iface):
    from .MySample import MySample
    return MySample(iface)