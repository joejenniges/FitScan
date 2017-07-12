
C:\Python27\Lib\site-packages\PySide\pyside-rcc.exe resources\resources.qrc -o src\fitscan\views\resources_rc.py
C:\Python27\Scripts\pyside-uic resources\ui\mainwindow.ui -o src\fitscan\views\ui_mainwindow.py
C:\Python27\Scripts\pyside-uic resources\ui\instructions.ui -o src\fitscan\views\ui_instructions.py

echo import resources_rc >> src\fitscan\views\ui_mainwindow.py