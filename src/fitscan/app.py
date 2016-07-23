import sys
import time
from PySide import QtGui, QtCore
from PySide.QtGui import QApplication, QMessageBox
import pyperclip

from views.ui_mainWindow import Ui_MainWindow


class ClipThread(QtCore.QObject):
    finished = QtCore.Signal(str)

    def __init__(self, MainWindow, parent=None):
        super(ClipThread, self).__init__(parent)
        self.window = MainWindow
        self.last_clipboard = pyperclip.paste()
        self.active = True
        print 'init'

    def process(self):
        print 'running'
        while self.active:
            if (self.window.monitorClipboard):
                tmp_val = pyperclip.paste()
                if (tmp_val != self.last_clipboard):
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

        self.clipboard_thread = None
        # self.startClipboardThread()

        self.setupFitTable()

        self.items = {}

    def setupFitTable(self):
        self.ui.tableWidget_fit.setColumnCount(2)
        self.ui.tableWidget_fit.setHorizontalHeaderLabels([
            "Item", "Count"
        ])
        self.ui.tableWidget_fit.setColumnWidth(0, 400)
        self.ui.tableWidget_fit.setColumnWidth(1, 50)



    def handleClipboard(self, clip):
        lines = clip.splitlines()

        temp_items = {}

        for line in lines:
            item = line.strip()

            if item in temp_items.keys():
                temp_items[item] = temp_items[item] + 1
            else:
                temp_items[item] = 1

        for item, total in temp_items.iteritems():

            if item in self.items.keys():
                if self.items[item] < total:
                    self.items[item] = total
            else:
                self.items[item] = total

        self.ui.tableWidget_fit.setRowCount(0)

        count = len(self.items.keys())

        self.ui.tableWidget_fit.setRowCount(0)
        self.ui.tableWidget_fit.setRowCount(count)

        i = 0
        for item, total in self.items.iteritems():
            qitem_item  = QtGui.QTableWidgetItem("{}".format(item))
            qitem_total = QtGui.QTableWidgetItem("{}".format(total))
            self.ui.tableWidget_fit.setItem(i, 0, qitem_item)
            self.ui.tableWidget_fit.setItem(i, 1, qitem_total)
            i = i+1

    def clearFitting(self):
        self.ui.tableWidget_fit.setRowCount(0)
        self.items = {}

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

    def sysexit(self):
        if QMessageBox.question(None, '', "Are you sure you want to quit?",
                                QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.No) == QMessageBox.Yes:
            self.stopClipboardThread()
            QApplication.quit()

def run():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
