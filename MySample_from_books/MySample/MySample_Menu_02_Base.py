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

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MySampleMenu02Base(object):
    def setupUi(self, MySampleMenu02Base):
        MySampleMenu02Base.setObjectName("MySampleMenu02Base")
        MySampleMenu02Base.resize(336, 152)
        self.pushButton = QtWidgets.QPushButton(MySampleMenu02Base)
        self.pushButton.setGeometry(QtCore.QRect(90, 90, 101, 41))
        self.pushButton_go.setObjectName("pushButton_go")
        self.pushButton_cancel = QtWidgets.QPushButton(MySampleMenu02Base)
        self.pushButton_cancel.setGeometry(QtCore.QRect(210, 90, 101, 41))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.lineEdit = QtWidgets.QLineEdit(MySampleMenu02Base)
        self.lineEdit.setGeometry(QtCore.QRect(30, 30, 251, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(MySampleMenu02Base)
        QtCore.QMetaObject.connectSlotsByName(MySampleMenu02Base)

    def retranslateUi(self, MySampleMenu02Base):
        _translate = QtCore.QCoreApplication.translate
        MySampleMenu02Base.setWindowTitle(_translate("MySampleMenu02Base", "Form"))
        self.pushButton.setText(_translate("MySampleMenu02Base", "Run"))
        self.pushButton_cancel.setText(_translate("MySampleMenu02Base", "キャンセル"))