
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from Data.UI import Ui_MainWindow
from googlesearch import search
import os
from PyQt5.QtWidgets import QMessageBox
import webbrowser
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import *
from PyQt5.QtGui import QMouseEvent
import sqlite3
import threading
import time
class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btn_Github.clicked.connect(self.GitHub_Button)
        self.ui.btn_Exit.clicked.connect(self.Exit)
        self.oldPos = self.pos()
        self.show()
        self.ComboAdd()
        self.ui.cmb_Dork.currentIndexChanged.connect(self.ComboUpdate)
        self.ui.cmb_Language.currentIndexChanged.connect(self.LanguageControl)
        self.NumberSelect()
        self.SelectLanguage()
        self.ui.btn_Start.clicked.connect(self.searchGoogle)
    def Start(self):
        msg = QMessageBox()
        msg.setWindowTitle("İşlem Başlatıldı")
        msg.setText("""
        İşlemin bitmesi 20 saniye kadar sürecek, lütfen bekleyiniz. 
        """)
        x = msg.exec_()
    def GitHub_Button(self):
        webbrowser.open("https://github.com/nickzsche")
    def Exit(self):
        self.close()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()
    def ComboAdd(self):
        os.chdir("Data")
        veritabani = sqlite3.connect("Dorks.db")
        cursor = veritabani.cursor()
        cursor.execute("""SELECT DorkSelect FROM dorks """)
        veriler = cursor.fetchall()
        for i in veriler:
            a = ((i))
            self.ui.cmb_Dork.addItem(a[0])    
            veritabani = sqlite3.connect("Dorks.db")
            cursor = veritabani.cursor()
            cursor.execute("""SELECT SqlList FROM SqlDorkList """)
            veriler = cursor.fetchall()
            for i in veriler:
                a = ((i))
                self.ui.cmb_SelectDock.addItem(a[0])
            veritabani.close()
    
    def ComboUpdate(self):
        if self.ui.cmb_Dork.currentIndex() == 0:
            self.ui.cmb_SelectDock.clear()
            print(self.ui.cmb_Dork.currentIndex())
            veritabani = sqlite3.connect("Dorks.db")
            cursor = veritabani.cursor()
            cursor.execute("""SELECT SqlList FROM SqlDorkList """)
            veriler = cursor.fetchall()
            for i in veriler:
                a = ((i))
                self.ui.cmb_SelectDock.addItem(a[0])
            veritabani.close()
        elif self.ui.cmb_Dork.currentIndex() == 1:
            print(self.ui.cmb_Dork.currentIndex())
            self.ui.cmb_SelectDock.clear()
            veritabani = sqlite3.connect("Dorks.db")
            cursor = veritabani.cursor()
            cursor.execute("""SELECT WordPressList FROM WordPressDorkList """)
            veriler = cursor.fetchall()
            for i in veriler:
                a = ((i))
                self.ui.cmb_SelectDock.addItem(a[0])
            veritabani.close()
        elif self.ui.cmb_Dork.currentIndex() == 2:
            print(self.ui.cmb_Dork.currentIndex())
            self.ui.cmb_SelectDock.clear()
            veritabani = sqlite3.connect("Dorks.db")
            cursor = veritabani.cursor()
            cursor.execute("""SELECT XssDork FROM XssDorkList """)
            veriler = cursor.fetchall()
            for i in veriler:
                a = ((i))
                self.ui.cmb_SelectDock.addItem(a[0])
            veritabani.close()
        elif self.ui.cmb_Dork.currentIndex() ==3:
            print(self.ui.cmb_Dork.currentIndex())
            self.ui.cmb_SelectDock.clear()
            veritabani = sqlite3.connect("Dorks.db")
            cursor = veritabani.cursor()
            cursor.execute("""SELECT FtpList FROM FtpDorkList """)
            veriler = cursor.fetchall()
            for i in veriler:
                a = ((i))
                self.ui.cmb_SelectDock.addItem(a[0])
            veritabani.close()
        elif self.ui.cmb_Dork.currentIndex() ==4:
            print(self.ui.cmb_Dork.currentIndex())
            self.ui.cmb_SelectDock.clear()
            veritabani = sqlite3.connect("Dorks.db")
            cursor = veritabani.cursor()
            cursor.execute("""SELECT CameraList FROM CameraDorkList """)
            veriler = cursor.fetchall()
            for i in veriler:
                a = ((i))
                self.ui.cmb_SelectDock.addItem(a[0])
            veritabani.close()
    def NumberSelect(self):
        veritabani = sqlite3.connect("Dorks.db")
        cursor = veritabani.cursor()
        cursor.execute("""SELECT NumberList FROM SqlListNumbar """)
        veriler = cursor.fetchall()
        for i in veriler:
            a = ((i))
            self.ui.cmb_Number.addItem(a[0])
            veritabani.close()
    def SelectLanguage(self):
        veritabani = sqlite3.connect("Dorks.db")
        cursor = veritabani.cursor()
        cursor_2 = veritabani.cursor()
        cursor.execute("""SELECT SelectLangDork FROM SqlDorkSelectLanguage """)
        cursor_2.execute("""SELECT Language FROM LanguageSelect """)
        veriler = cursor.fetchall()
        veriler_2 = cursor_2.fetchall()
        for i in veriler:
            a = ((i))
            self.ui.cmb_DorkLanguage.addItem(a[0])
            veritabani.close()
        for i in veriler_2:
            a = ((i))
            self.ui.cmb_Language.addItem(a[0])
            veritabani.close()
    def LanguageControl(self):
        if self.ui.cmb_Language.currentIndex() == 0:
            self.ui.lbl_DorkType.setText("Dork Type") 
            self.ui.lbl_SelectDork.setText("Select A Dork") 
            self.ui.lbl_SelectNumber.setText("Number") 
            self.ui.lbl_SelectDorkLanguage.setText("Dork Language") 
            self.ui.lbl_SelectLanguage.setText("Select Language")
            self.ui.btn_Exit.setText("Exit")
            self.ui.btn_Start.setText("Start")
        elif self.ui.cmb_Language.currentIndex() == 1:
            self.ui.lbl_DorkType.setText("Dork Tipi") 
            self.ui.lbl_SelectDork.setText("Dork Seçin") 
            self.ui.lbl_SelectNumber.setText("Adet") 
            self.ui.lbl_SelectDorkLanguage.setText("Dork Dili Seçin") 
            self.ui.lbl_SelectLanguage.setText("Program Dili Seçin")
            self.ui.btn_Exit.setText("Çıkış")
            self.ui.btn_Start.setText("Çalıştır")
    def searchGoogle(self):
        def searchGoogleThread():
            for url in search(self.ui.cmb_SelectDock.currentText()):
                textFile = open("DorkList.txt","a")
                time.sleep(4)
                textFile.writelines(url)
                textFile.close()
                print(url)
        searchGoogle = threading.Thread(
                target=searchGoogleThread)
        searchGoogle.start()



def app():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    win = MyApp()
    win.show()
    sys.exit(app.exec_())


app()