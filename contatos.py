# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'contatos.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_tela_contatos(object):
    def setupUi(self, tela_contatos):
        if not tela_contatos.objectName():
            tela_contatos.setObjectName(u"tela_contatos")
        tela_contatos.resize(822, 648)
        self.centralwidget = QWidget(tela_contatos)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-11, -1, 831, 651))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.txt_Entrar = QLabel(self.frame)
        self.txt_Entrar.setObjectName(u"txt_Entrar")
        self.txt_Entrar.setGeometry(QRect(50, 20, 161, 31))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.txt_Entrar.setFont(font)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(630, 30, 111, 24))
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 60, 321, 22))
        self.txt_email = QLabel(self.frame)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(50, 120, 121, 16))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(True)
        self.txt_email.setFont(font1)
        tela_contatos.setCentralWidget(self.centralwidget)

        self.retranslateUi(tela_contatos)

        QMetaObject.connectSlotsByName(tela_contatos)
    # setupUi

    def retranslateUi(self, tela_contatos):
        tela_contatos.setWindowTitle(QCoreApplication.translate("tela_contatos", u"MainWindow", None))
        self.txt_Entrar.setText(QCoreApplication.translate("tela_contatos", u"Contatos", None))
        self.pushButton.setText(QCoreApplication.translate("tela_contatos", u"Adicionar contato", None))
        self.lineEdit.setText(QCoreApplication.translate("tela_contatos", u"Buscar", None))
        self.txt_email.setText(QCoreApplication.translate("tela_contatos", u"Almir", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication([]) 
    mainWindow = QMainWindow()  
    ui = Ui_tela_contatos()  
    ui.setupUi(mainWindow)  
    mainWindow.show()  
    app.exec()  