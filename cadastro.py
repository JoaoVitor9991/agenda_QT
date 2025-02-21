# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
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

class Ui_Tela_Cadastro(object):
    def setupUi(self, Tela_Cadastro):
        if not Tela_Cadastro.objectName():
            Tela_Cadastro.setObjectName(u"Tela_Cadastro")
        Tela_Cadastro.resize(800, 600)
        self.centralwidget = QWidget(Tela_Cadastro)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, 0, 811, 601))
        font = QFont()
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.txt_Criar_Conta = QLabel(self.frame)
        self.txt_Criar_Conta.setObjectName(u"txt_Criar_Conta")
        self.txt_Criar_Conta.setGeometry(QRect(100, 30, 161, 31))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(True)
        self.txt_Criar_Conta.setFont(font1)
        self.txt_jtemconta = QLabel(self.frame)
        self.txt_jtemconta.setObjectName(u"txt_jtemconta")
        self.txt_jtemconta.setGeometry(QRect(100, 60, 121, 16))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(True)
        self.txt_jtemconta.setFont(font2)
        self.link_entrar = QLabel(self.frame)
        self.link_entrar.setObjectName(u"link_entrar")
        self.link_entrar.setGeometry(QRect(230, 60, 71, 16))
        self.link_entrar.setFont(font2)
        self.link_entrar.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.txt_nome = QLabel(self.frame)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(100, 140, 121, 16))
        self.txt_nome.setFont(font2)
        self.line_nome = QLineEdit(self.frame)
        self.line_nome.setObjectName(u"line_nome")
        self.line_nome.setGeometry(QRect(100, 160, 551, 22))
        self.txt_email = QLabel(self.frame)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(100, 200, 121, 16))
        self.txt_email.setFont(font2)
        self.line_email = QLineEdit(self.frame)
        self.line_email.setObjectName(u"line_email")
        self.line_email.setGeometry(QRect(100, 220, 551, 22))
        self.txt_contato = QLabel(self.frame)
        self.txt_contato.setObjectName(u"txt_contato")
        self.txt_contato.setGeometry(QRect(100, 260, 121, 16))
        self.txt_contato.setFont(font2)
        self.line_contato = QLineEdit(self.frame)
        self.line_contato.setObjectName(u"line_contato")
        self.line_contato.setGeometry(QRect(100, 280, 271, 22))
        self.txt_senha = QLabel(self.frame)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(100, 320, 121, 16))
        self.txt_senha.setFont(font2)
        self.line_senha = QLineEdit(self.frame)
        self.line_senha.setObjectName(u"line_senha")
        self.line_senha.setGeometry(QRect(100, 340, 311, 22))
        self.txt_confrimar_senha = QLabel(self.frame)
        self.txt_confrimar_senha.setObjectName(u"txt_confrimar_senha")
        self.txt_confrimar_senha.setGeometry(QRect(100, 380, 151, 16))
        self.txt_confrimar_senha.setFont(font2)
        self.line_Confirmar_senha = QLineEdit(self.frame)
        self.line_Confirmar_senha.setObjectName(u"line_Confirmar_senha")
        self.line_Confirmar_senha.setGeometry(QRect(100, 400, 311, 22))
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(310, 510, 151, 16))
        self.label_9.setFont(font2)
        self.pushButton_Cadastrar = QPushButton(self.frame)
        self.pushButton_Cadastrar.setObjectName(u"pushButton_Cadastrar")
        self.pushButton_Cadastrar.setGeometry(QRect(350, 480, 131, 51))
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(True)
        self.pushButton_Cadastrar.setFont(font3)
        self.pushButton_Cadastrar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255);")
        Tela_Cadastro.setCentralWidget(self.centralwidget)

        self.retranslateUi(Tela_Cadastro)

        QMetaObject.connectSlotsByName(Tela_Cadastro)
    # setupUi

    def retranslateUi(self, Tela_Cadastro):
        Tela_Cadastro.setWindowTitle(QCoreApplication.translate("Tela_Cadastro", u"MainWindow", None))
        self.txt_Criar_Conta.setText(QCoreApplication.translate("Tela_Cadastro", u"Criar conta", None))
        self.txt_jtemconta.setText(QCoreApplication.translate("Tela_Cadastro", u"J\u00e1 tem uma conta? ", None))
        self.link_entrar.setText(QCoreApplication.translate("Tela_Cadastro", u"Entrar", None))
        self.txt_nome.setText(QCoreApplication.translate("Tela_Cadastro", u"Nome:", None))
        self.txt_email.setText(QCoreApplication.translate("Tela_Cadastro", u"Email:", None))
        self.txt_contato.setText(QCoreApplication.translate("Tela_Cadastro", u"Contato:", None))
        self.txt_senha.setText(QCoreApplication.translate("Tela_Cadastro", u"Senha:", None))
        self.txt_confrimar_senha.setText(QCoreApplication.translate("Tela_Cadastro", u"Confirma\u00e7\u00e3o da Senha:", None))
        self.label_9.setText("")
        self.pushButton_Cadastrar.setText(QCoreApplication.translate("Tela_Cadastro", u"Cadastrar", None))
    # retranslateUi

if __name__ == "__main__":
    app = QApplication([]) 
    mainWindow = QMainWindow()  
    ui = Ui_Tela_Cadastro ()
    ui.setupUi(mainWindow)  
    mainWindow.show()  
    app.exec()  