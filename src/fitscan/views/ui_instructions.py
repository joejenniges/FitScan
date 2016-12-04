# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources\ui\instructions.ui'
#
# Created: Sun Dec 04 15:49:11 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Instructions(object):
    def setupUi(self, Instructions):
        Instructions.setObjectName("Instructions")
        Instructions.setEnabled(True)
        Instructions.resize(400, 300)
        Instructions.setMinimumSize(QtCore.QSize(400, 300))
        Instructions.setMaximumSize(QtCore.QSize(400, 300))
        self.label = QtGui.QLabel(Instructions)
        self.label.setGeometry(QtCore.QRect(20, 10, 361, 271))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.pushButton_OK = QtGui.QPushButton(Instructions)
        self.pushButton_OK.setGeometry(QtCore.QRect(300, 260, 75, 23))
        self.pushButton_OK.setObjectName("pushButton_OK")

        self.retranslateUi(Instructions)
        QtCore.QMetaObject.connectSlotsByName(Instructions)

    def retranslateUi(self, Instructions):
        Instructions.setWindowTitle(QtGui.QApplication.translate("Instructions", "Instructions", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Instructions", "<html><head/><body><p>How to use:</p><p>1. Type in a ship name, hit enter or click -&gt; button</p><p>2. Start clipboard monitoring</p><p>3. Scan ships, select all (ctrl + a), and copy (ctrl + c)</p><p>4. Once you are satisfied, copy the fit</p><p>5. Clear fit to start again</p><p>6. Contact GunfighterJ with questions</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_OK.setText(QtGui.QApplication.translate("Instructions", "OK", None, QtGui.QApplication.UnicodeUTF8))

