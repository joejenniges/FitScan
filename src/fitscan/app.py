import sys
import time
from PySide import QtGui, QtCore
from PySide.QtGui import QApplication, QMessageBox
import pyperclip

from fitscan.views.ui_mainWindow import Ui_MainWindow

class ClipboardThread(QtCore.QThread):
    def __init__(self, MainWindow):
        QtCore.QThread.__init__(self)
        self.window = MainWindow
        self.last_clipboard = pyperclip.paste()

    def run(self):
        print 'Running Thread'
        while True:
            if (self.window.monitorClipboard):
                tmp_val = pyperclip.paste()
                if (tmp_val != self.last_clipboard):
                    self.last_clipboard = tmp_val
                    self.window.handleClipboard(tmp_val)
        time.sleep(0.1)

    def stop(self):
        self.terminate()



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

        self.threads = []
        self.startClipboardThread()

        self.setupFitTable()

        self.items = {}

    def setupFitTable(self):
        self.ui.tableWidget_fit.setColumnCount(2)
        self.ui.tableWidget_fit.setHorizontalHeaderLabels([
            "Item", "Count"
        ])
        self.ui.tableWidget_fit.setColumnWidth(0, 400)
        self.ui.tableWidget_fit.setColumnWidth(1, 50)

    def startClipboardThread(self):
        clipboard = ClipboardThread(self)
        self.threads.append(clipboard)
        clipboard.start()

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

    def startClipboard(self):
        if (self.ui.pushButton_start.isEnabled()):
            self.ui.pushButton_start.setEnabled(False)
            self.ui.pushButton_stop.setEnabled(True)
            self.monitorClipboard = True


    def stopClipboard(self):
        if (self.ui.pushButton_stop.isEnabled()):
            self.ui.pushButton_stop.setEnabled(False)
            self.ui.pushButton_start.setEnabled(True)
            self.monitorClipboard = False

    def sysexit(self):
        if QMessageBox.question(None, '', "Are you sure you want to quit?",
                                QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.No) == QMessageBox.Yes:
            QApplication.quit()

def run():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
