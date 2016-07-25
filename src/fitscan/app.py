import csv
import sys
import time
import StringIO


from PySide import QtGui, QtCore
from PySide.QtGui import QApplication, QMessageBox
import pyperclip

from views.ui_mainwindow import Ui_MainWindow


class ClipThread(QtCore.QObject):
    finished = QtCore.Signal(str)

    def __init__(self, MainWindow, parent=None):
        super(ClipThread, self).__init__(parent)
        self.window = MainWindow
        pyperclip.copy('')
        self.last_clipboard = ''
        self.active = True
        print 'init'

    def process(self):
        print 'running'
        while self.active:
            tmp_val = pyperclip.paste()
            if tmp_val != self.last_clipboard:
                self.last_clipboard = tmp_val
                self.window.handleClipboard(tmp_val)
        time.sleep(0.1)

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.monitorClipboard = False

        self.ui.pushButton_exit.clicked.connect(self.sysexit)
        self.ui.pushButton_start.clicked.connect(self.startClipboard)
        self.ui.pushButton_stop.clicked.connect(self.stopClipboard)
        self.ui.pushButton_clear.clicked.connect(self.clearFitting)
        self.ui.pushButton_copy.clicked.connect(self.copyFitting)

        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        completer = QtGui.QCompleter(['Tengu', 'Proteus', 'Loki', 'Legion'], self)
        completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        self.ui.lineEdit_ship.setCompleter(completer)

        self.setupLabelIcons()

        self.clipboard_thread = None
        self.clipThread       = None
        # self.startClipboardThread()

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

    def setupLabelIcons(self):
        self.ui.label_highslot_icon.setPixmap(QtGui.QPixmap(":img/slot_high_small.png"))
        self.ui.label_midslot_icon.setPixmap(QtGui.QPixmap(":img/slot_med_small.png"))
        self.ui.label_lowslot_icon.setPixmap(QtGui.QPixmap(":img/slot_low_small.png"))
        self.ui.label_rig_icon.setPixmap(QtGui.QPixmap(":img/slot_rig_small.png"))
        self.ui.label_subsystem_icon.setPixmap(QtGui.QPixmap(":img/slot_subsystem_small.png"))

    def setListItems(self, mapped_items, slotType):
        if slotType is not "C":
            slot = mapped_items[slotType]
            listWidget = slot["list"]
            listWidget.clear()

            countLabel = slot["label"]

            labelText = "Count: " + str(len(slot["items"]))
            countLabel.setText(labelText)

            for item in sorted(slot["items"]):
                QtGui.QListWidgetItem(item, listWidget)

    def handleClipboard(self, clip):
        print 'Clipboarding'
        clipboard_lines = clip.splitlines()

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

    def clearFitting(self):
        for key in self.mapped_items:
            self.mapped_items[key]["items"] = []
            if key is not "C":
                self.mapped_items[key]["list"].clear()
                self.mapped_items[key]["label"].setText("Count: 0")

    def copyFitting(self):
        fit = []
        fit.append("[Metal Scraps, New Fit]")
        for key in self.mapped_items:
            for item in self.mapped_items[key]["items"]:
                fit.append(item)
            fit.append('')

        pyperclip.copy('')
        pyperclip.copy("\n".join(fit))


    def startClipboardThread(self):
        self.clipboard_thread = QtCore.QThread()
        self.clipThread = ClipThread(self)
        self.clipThread.moveToThread(self.clipboard_thread)
        self.clipboard_thread.started.connect(self.clipThread.process)
        self.clipboard_thread.start()

    def startClipboard(self):
        if (self.ui.pushButton_start.isEnabled()):
            self.ui.pushButton_start.setEnabled(False)
            self.ui.pushButton_stop.setEnabled(True)
            self.startClipboardThread()
            # self.monitorClipboard = True

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
            self.stopClipboardThread()

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

def run():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

