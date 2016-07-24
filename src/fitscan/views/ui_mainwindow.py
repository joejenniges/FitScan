# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources\ui\mainwindow.ui'
#
# Created: Sun Jul 24 16:00:40 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(830, 550)
        MainWindow.setMinimumSize(QtCore.QSize(830, 550))
        MainWindow.setMaximumSize(QtCore.QSize(830, 550))
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.groupBox = QtGui.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(640, 10, 180, 251))
        self.groupBox.setMinimumSize(QtCore.QSize(180, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtGui.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 160, 217))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_clipboard = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_clipboard.setMargin(5)
        self.label_clipboard.setObjectName("label_clipboard")
        self.verticalLayout.addWidget(self.label_clipboard)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_start = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_start.setStyleSheet("color: green")
        self.pushButton_start.setObjectName("pushButton_start")
        self.gridLayout_2.addWidget(self.pushButton_start, 0, 0, 1, 1)
        self.pushButton_stop = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_stop.setEnabled(False)
        self.pushButton_stop.setStyleSheet("color: red")
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.gridLayout_2.addWidget(self.pushButton_stop, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.line_2 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.line_2)
        self.pushButton_copy = QtGui.QPushButton(self.verticalLayoutWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("clipboard_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_copy.setIcon(icon)
        self.pushButton_copy.setObjectName("pushButton_copy")
        self.verticalLayout.addWidget(self.pushButton_copy)
        self.pushButton_clear = QtGui.QPushButton(self.verticalLayoutWidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("delete_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_clear.setIcon(icon1)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.verticalLayout.addWidget(self.pushButton_clear)
        self.line = QtGui.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.pushButton_exit = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.verticalLayout.addWidget(self.pushButton_exit)
        self.line_3 = QtGui.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit_ship = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_ship.setObjectName("lineEdit_ship")
        self.verticalLayout.addWidget(self.lineEdit_ship)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 302, 573))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_highslot_icon = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_highslot_icon.setMaximumSize(QtCore.QSize(16, 16777215))
        self.label_highslot_icon.setText("")
        self.label_highslot_icon.setObjectName("label_highslot_icon")
        self.horizontalLayout.addWidget(self.label_highslot_icon)
        self.label_highslots = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_highslots.setObjectName("label_highslots")
        self.horizontalLayout.addWidget(self.label_highslots)
        self.label_highslot_count = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_highslot_count.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_highslot_count.setObjectName("label_highslot_count")
        self.horizontalLayout.addWidget(self.label_highslot_count)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.listWidget_highslots = QtGui.QListWidget(self.verticalLayoutWidget_2)
        self.listWidget_highslots.setMinimumSize(QtCore.QSize(300, 0))
        self.listWidget_highslots.setMaximumSize(QtCore.QSize(300, 150))
        self.listWidget_highslots.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget_highslots.setObjectName("listWidget_highslots")
        self.verticalLayout_2.addWidget(self.listWidget_highslots)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_midslot_icon = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_midslot_icon.setMaximumSize(QtCore.QSize(16, 16777215))
        self.label_midslot_icon.setText("")
        self.label_midslot_icon.setObjectName("label_midslot_icon")
        self.horizontalLayout_2.addWidget(self.label_midslot_icon)
        self.label_midslots = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_midslots.setObjectName("label_midslots")
        self.horizontalLayout_2.addWidget(self.label_midslots)
        self.label_midslot_count = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_midslot_count.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_midslot_count.setObjectName("label_midslot_count")
        self.horizontalLayout_2.addWidget(self.label_midslot_count)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.listWidget_midslots = QtGui.QListWidget(self.verticalLayoutWidget_2)
        self.listWidget_midslots.setMinimumSize(QtCore.QSize(300, 0))
        self.listWidget_midslots.setMaximumSize(QtCore.QSize(300, 150))
        self.listWidget_midslots.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget_midslots.setObjectName("listWidget_midslots")
        self.verticalLayout_2.addWidget(self.listWidget_midslots)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_lowslot_icon = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_lowslot_icon.setMaximumSize(QtCore.QSize(16, 16777215))
        self.label_lowslot_icon.setText("")
        self.label_lowslot_icon.setObjectName("label_lowslot_icon")
        self.horizontalLayout_3.addWidget(self.label_lowslot_icon)
        self.label_lowslots = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_lowslots.setObjectName("label_lowslots")
        self.horizontalLayout_3.addWidget(self.label_lowslots)
        self.label_lowslot_count = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_lowslot_count.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_lowslot_count.setObjectName("label_lowslot_count")
        self.horizontalLayout_3.addWidget(self.label_lowslot_count)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.listWidget_lowslots = QtGui.QListWidget(self.verticalLayoutWidget_2)
        self.listWidget_lowslots.setMinimumSize(QtCore.QSize(300, 0))
        self.listWidget_lowslots.setMaximumSize(QtCore.QSize(300, 150))
        self.listWidget_lowslots.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget_lowslots.setObjectName("listWidget_lowslots")
        self.verticalLayout_2.addWidget(self.listWidget_lowslots)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayoutWidget_3 = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(320, 10, 302, 571))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_rig_icon = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_rig_icon.setMaximumSize(QtCore.QSize(16, 16777215))
        self.label_rig_icon.setText("")
        self.label_rig_icon.setObjectName("label_rig_icon")
        self.horizontalLayout_4.addWidget(self.label_rig_icon)
        self.label_rigs = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_rigs.setObjectName("label_rigs")
        self.horizontalLayout_4.addWidget(self.label_rigs)
        self.label_rig_count = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_rig_count.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_rig_count.setObjectName("label_rig_count")
        self.horizontalLayout_4.addWidget(self.label_rig_count)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.listWidget_rigs = QtGui.QListWidget(self.verticalLayoutWidget_3)
        self.listWidget_rigs.setMinimumSize(QtCore.QSize(300, 0))
        self.listWidget_rigs.setMaximumSize(QtCore.QSize(300, 150))
        self.listWidget_rigs.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget_rigs.setObjectName("listWidget_rigs")
        self.verticalLayout_3.addWidget(self.listWidget_rigs)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_subsystem_icon = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_subsystem_icon.setMaximumSize(QtCore.QSize(16, 16777215))
        self.label_subsystem_icon.setText("")
        self.label_subsystem_icon.setObjectName("label_subsystem_icon")
        self.horizontalLayout_5.addWidget(self.label_subsystem_icon)
        self.label_subsystems = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_subsystems.setObjectName("label_subsystems")
        self.horizontalLayout_5.addWidget(self.label_subsystems)
        self.label_subsystem_count = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.label_subsystem_count.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_subsystem_count.setObjectName("label_subsystem_count")
        self.horizontalLayout_5.addWidget(self.label_subsystem_count)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.listWidget_subsystems = QtGui.QListWidget(self.verticalLayoutWidget_3)
        self.listWidget_subsystems.setMinimumSize(QtCore.QSize(300, 0))
        self.listWidget_subsystems.setMaximumSize(QtCore.QSize(300, 150))
        self.listWidget_subsystems.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listWidget_subsystems.setObjectName("listWidget_subsystems")
        self.verticalLayout_3.addWidget(self.listWidget_subsystems)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_2.setGeometry(QtCore.QRect(640, 270, 181, 231))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 161, 211))
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "FitScan", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Controls", None, QtGui.QApplication.UnicodeUTF8))
        self.label_clipboard.setText(QtGui.QApplication.translate("MainWindow", "Clipboard Monitoring", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_start.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_stop.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_copy.setText(QtGui.QApplication.translate("MainWindow", "Copy Fit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_clear.setText(QtGui.QApplication.translate("MainWindow", "Clear Fitting", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_exit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Ship", None, QtGui.QApplication.UnicodeUTF8))
        self.label_highslots.setText(QtGui.QApplication.translate("MainWindow", "High Slots", None, QtGui.QApplication.UnicodeUTF8))
        self.label_highslot_count.setText(QtGui.QApplication.translate("MainWindow", "Count: 0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_midslots.setText(QtGui.QApplication.translate("MainWindow", "Mid Slots", None, QtGui.QApplication.UnicodeUTF8))
        self.label_midslot_count.setText(QtGui.QApplication.translate("MainWindow", "Count: 0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_lowslots.setText(QtGui.QApplication.translate("MainWindow", "Low Slots", None, QtGui.QApplication.UnicodeUTF8))
        self.label_lowslot_count.setText(QtGui.QApplication.translate("MainWindow", "Count: 0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rigs.setText(QtGui.QApplication.translate("MainWindow", "Rigs", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rig_count.setText(QtGui.QApplication.translate("MainWindow", "Count: 0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_subsystems.setText(QtGui.QApplication.translate("MainWindow", "Subsystems", None, QtGui.QApplication.UnicodeUTF8))
        self.label_subsystem_count.setText(QtGui.QApplication.translate("MainWindow", "Count: 0", None, QtGui.QApplication.UnicodeUTF8))
        self.plainTextEdit.setPlainText(QtGui.QApplication.translate("MainWindow", "How to use:\n"
"1. Start clipboard monitoring\n"
"2. Scan ships, select all (ctrl + a), and copy (ctrl + v)\n"
"3. Once you are satisfied, STOP the monitoring\n"
"4. Copy the fit using the button. It only lists metal scrap as the ship until I can get the rest working\n"
"5. The Ship box does not work yet\n"
"6. Contact GunfighterJ with questions", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc 