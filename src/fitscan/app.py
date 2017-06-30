import csv
import sys
import time
import StringIO


from PySide import QtGui, QtCore
from PySide.QtGui import QApplication, QMessageBox
import pyperclip

from views.ui_mainwindow import Ui_MainWindow
from views.ui_instructions import Ui_Instructions


class ClipThread(QtCore.QObject):
    copied = QtCore.Signal(str)

    def __init__(self, MainWindow, parent=None):
        super(ClipThread, self).__init__(parent)
        self.window = MainWindow
        pyperclip.copy('')
        self.last_clipboard = ''
        self.active = True

    def process(self):
        while self.active:
            tmp_val = pyperclip.paste()
            if tmp_val != self.last_clipboard:
                self.last_clipboard = tmp_val
                self.copied.emit(tmp_val)
                # self.window.handleClipboard(tmp_val)
            time.sleep(0.1)

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.pushButton_exit.clicked.connect(self.sysexit)
        self.ui.pushButton_start.clicked.connect(self.startClipboard)
        self.ui.pushButton_stop.clicked.connect(self.stopClipboard)
        self.ui.pushButton_clear.clicked.connect(self.clearFitting)
        self.ui.pushButton_copy.clicked.connect(self.copyFitting)
        self.ui.lineEdit_ship.returnPressed.connect(self.processShipType)
        self.ui.lineEdit_ship.editingFinished.connect(self.processShipType)
        self.ui.pushButton_submit_ship.clicked.connect(self.processShipType)
        self.ui.pushButton_help.clicked.connect(self.showInstructions)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.setupLabelIcons()

        self.clipboard_thread = None
        self.clipThread       = None

        self.items = {}
        self.mapped_items = {
            "H": {
                "items": [],
                "list": self.ui.listWidget_highslots,
                "label": self.ui.label_highslot_count,
                "icon": self.ui.label_highslot_icon,
            },
            "M": {
                "items": [],
                "list": self.ui.listWidget_midslots,
                "label": self.ui.label_midslot_count,
                "icon": self.ui.label_midslot_icon
            },
            "L": {
                "items": [],
                "list": self.ui.listWidget_lowslots,
                "label": self.ui.label_lowslot_count,
                "icon": self.ui.label_lowslot_icon
            },
            "R": {
                "items": [],
                "list": self.ui.listWidget_rigs,
                "label": self.ui.label_rig_count,
                "icon": self.ui.label_rig_icon
            },
            "S": {
                "items": [],
                "list": self.ui.listWidget_subsystems,
                "label": self.ui.label_subsystem_count,
                "icon": self.ui.label_subsystem_icon
            },
            "C": {
                "items": []
            }
        }

        self.slotMap = self.getItemSlotMapping()
        self.shipMap = self.getShipSlotMapping()
        self.subsMap = self.getSubsystemMapping()

        self.shipName = ""
        self.shipInfo = {}

        completer = QtGui.QCompleter(sorted(self.shipMap.keys()), self)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui.lineEdit_ship.setCompleter(completer)

    def showInstructions(self):
        instructions = InstructionDialog()
        instructions.exec_()

    def setupLabelIcons(self):
        self.ui.label_highslot_icon.setPixmap(QtGui.QPixmap(":img/slot_high_small.png"))
        self.ui.label_midslot_icon.setPixmap(QtGui.QPixmap(":img/slot_med_small.png"))
        self.ui.label_lowslot_icon.setPixmap(QtGui.QPixmap(":img/slot_low_small.png"))
        self.ui.label_rig_icon.setPixmap(QtGui.QPixmap(":img/slot_rig_small.png"))
        self.ui.label_subsystem_icon.setPixmap(QtGui.QPixmap(":img/slot_subsystem_small.png"))

    def updateCountLabels(self):
        for slotType in self.mapped_items.keys():
            if slotType == "C":
                continue

            slot = self.mapped_items[slotType]
            itemCount = len(slot["items"])
            label = slot["label"]
            list  = slot["list"]

            if self.shipName and slotType in self.shipInfo.keys():
                maxCount = self.shipInfo[slotType]
                int_maxCount = int(maxCount)
                label.setText("Count: {}/{}".format(itemCount, maxCount))
                if itemCount == int_maxCount:
                    label.setStyleSheet("color: green")
                    list.setStyleSheet("background-color: #5fba7d")
                else:
                    label.setStyleSheet("color: black")
                    list.setStyleSheet("background-color: white")
            else:
                label.setText("Count: {}".format(itemCount))
                label.setStyleSheet("color: black")
                list.setStyleSheet("background-color: white")


    def setListItems(self, mapped_items, slotType):
        if slotType is not "C":
            slot = mapped_items[slotType]
            listWidget = slot["list"]
            listWidget.clear()

            for item in sorted(slot["items"]):
                QtGui.QListWidgetItem(item, listWidget)


    def handleClipboard(self, clip):
        print 'Clipboarding'
        clipboard_lines = clip.splitlines()
        print clipboard_lines

        temp_items = {}

        # Get clipboard data, add to a temp list
        for line in clipboard_lines:
            item = line.strip()

            if item in temp_items.keys():
                temp_items[item] = temp_items[item] + 1
            else:
                temp_items[item] = 1

        # Merge temp list sof items into main list of items
        for item, total in temp_items.iteritems():

            if item in self.items.keys():
                if self.items[item] < total:
                    self.items[item] = total
            else:
                self.items[item] = total
        # print "Keys: " + len(self.items.keys())

        # Clear list of items
        for key in self.mapped_items.keys():
            self.mapped_items[key]["items"] = []

        # Get each item, get their slot, add to appropriate list
        for item, total in self.items.iteritems():
            slotType = "C"

            if item in self.slotMap.keys():
                slotType = self.slotMap[item]

            for i in range(0, total):
                self.mapped_items[slotType]["items"].append(item)

        for slotType in self.mapped_items.keys():
            self.setListItems(self.mapped_items, slotType)
        self.updateCountLabels()

    def clearFitting(self):
        print 'Clearing Fit'
        self.items = {}
        for key in self.mapped_items.keys():
            self.mapped_items[key]["items"] = []
            if key is not "C":
                self.mapped_items[key]["list"].clear()
        self.updateCountLabels()
        wasEnabled = self.ui.pushButton_stop.isEnabled()
        self.stopClipboard()
        if wasEnabled:
            self.startClipboard()

    def copyFitting(self):
        self.stopClipboard()
        fit = []
        ship = self.shipName if self.shipName else 'Metal Scraps'
        fit.append("[{}, New Fit]".format(ship))
        for key in self.mapped_items:
            for item in self.mapped_items[key]["items"]:
                fit.append(item)
            fit.append('')

        pyperclip.copy('')
        pyperclip.copy("\n".join(fit))

    def processShipType(self):
        shipName = self.ui.lineEdit_ship.text()
        if shipName in self.shipMap.keys():
            self.shipName = shipName
            self.shipInfo = self.shipMap[shipName]
            self.setLabelMessage(self.ui.label_ship_message, "Success", "green")
        else:
            self.setLabelMessage(self.ui.label_ship_message, "Ship not found!", "red")
            self.shipName = ""
            self.shipInfo = {}
        self.updateCountLabels()


    def startClipboardThread(self):
        self.clipboard_thread = QtCore.QThread()
        self.clipThread = ClipThread(self)
        self.clipThread.moveToThread(self.clipboard_thread)
        self.clipboard_thread.started.connect(self.clipThread.process)
        self.clipThread.copied.connect(self.handleClipboard)
        self.clipboard_thread.start()

    def startClipboard(self):
        if (self.ui.pushButton_start.isEnabled()):
            self.ui.pushButton_start.setEnabled(False)
            self.ui.pushButton_stop.setEnabled(True)
            self.ui.pushButton_stop.setStyleSheet("color: red")
            self.ui.pushButton_start.setStyleSheet("color: grey")
            self.startClipboardThread()

    def stopClipboardThread(self):
        self.clipThread.active = False
        self.clipboard_thread.quit()
        while(self.clipboard_thread.isRunning()):
            time.sleep(0.01)
        self.clipThread = None
        self.clipboard_thread = None

    def stopClipboard(self):
        if (self.ui.pushButton_stop.isEnabled()):
            self.ui.pushButton_stop.setEnabled(False)
            self.ui.pushButton_start.setEnabled(True)
            self.ui.pushButton_stop.setStyleSheet("color: grey")
            self.ui.pushButton_start.setStyleSheet("color: green")
            self.stopClipboardThread()

    def setLabelMessage(self, label, message, color="black"):
        label.setText(message)
        label.setStyleSheet("color: {}".format(color))

    def getShipSlotMapping(self):
        qfile = QtCore.QFile(":db/shipMap.csv")
        items = {}

        if qfile.open(QtCore.QIODevice.ReadOnly | QtCore.QIODevice.Text):
            data = qfile.readAll()
            content = StringIO.StringIO(data)
            reader = csv.reader(content, delimiter=',')

            for row in reader:
                shipName = row[0].decode('utf-8')
                high     = row[1].decode('utf-8')
                mid      = row[2].decode('utf-8')
                low      = row[3].decode('utf-8')
                rig      = row[4].decode('utf-8')
                sub      = row[5].decode('utf-8')

                items[shipName] = {
                    "H": high,
                    "M": mid,
                    "L": low,
                    "R": rig,
                    "S": sub
                }
            qfile.close()
            return items

        QMessageBox.critical(None, 'Database Failure', 'Failed to read ship mappings from database', QMessageBox.Ok)
        self.stop()

    def getSubsystemMapping(self):
        qfile = QtCore.QFile(":db/subsystemMap.csv")
        items = {}

        if qfile.open(QtCore.QIODevice.ReadOnly | QtCore.QIODevice.Text):
            data = qfile.readAll()
            content = StringIO.StringIO(data)
            reader = csv.reader(content, delimiter=',')

            for row in reader:
                shipName = row[0].decode('utf-8')
                high = row[1].decode('utf-8')
                mid = row[2].decode('utf-8')
                low = row[3].decode('utf-8')

                items[shipName] = {
                    "H": high,
                    "M": mid,
                    "L": low,
                }
            qfile.close()
            return items

        QMessageBox.critical(None, 'Database Failure', 'Failed to read subsystem mappings from database', QMessageBox.Ok)
        self.stop()


    def getItemSlotMapping(self):
        qfile = QtCore.QFile(":db/slotMap.csv")
        items = {}
        if qfile.open(QtCore.QIODevice.ReadOnly | QtCore.QIODevice.Text):
            data = qfile.readAll()
            content = StringIO.StringIO(data)
            reader = csv.reader(content, delimiter=',')

            for row in reader:
                items[row[0].decode('utf-8')] = row[1].decode('utf-8')
            return items

        QMessageBox.critical(None, 'Database Failure', 'Failed to read item mappings from database', QMessageBox.Ok)
        self.stop()

    def stop(self):
        if self.clipThread is not None:
            self.stopClipboardThread()
        QApplication.exit()
        sys.exit()

    def sysexit(self):
        if QMessageBox.question(None, '', "Are you sure you want to quit?",
                                QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.No) == QMessageBox.Yes:
            self.stop()

class InstructionDialog(QtGui.QDialog, Ui_Instructions):
    def __init__(self, parent=None):
        super(InstructionDialog, self).__init__(parent)
        self.setupUi(self)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        self.setWindowFlags(QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        self.pushButton_OK.clicked.connect(self.close)

def run():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

