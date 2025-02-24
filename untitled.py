# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
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
import TEST

import mysql.connector
 
def create_connection():
    try:
        return mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='login_system'
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
 
def log_attempt(username, password, status):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO login_attempts (username, password, attempt_status)
        VALUES (%s, %s, %s)
        ''', (username, password, status))
        conn.commit()
        cursor.close()
        conn.close()
 
def check_credentials(username, password):
    conn = create_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute('''
        SELECT * FROM users WHERE username = %s AND password = %s
        ''', (username, password))
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return result is not None
    return False
 

class Ui_Tela_Login(object):
    def setupUi(self, Tela_Login):
        if not Tela_Login.objectName():
            Tela_Login.setObjectName(u"Tela_Login")
        Tela_Login.resize(818, 600)
        self.centralwidget = QWidget(Tela_Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, -10, 821, 611))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        
        self.txt_Entrar = QLabel(self.frame)
        self.txt_Entrar.setObjectName(u"txt_Entrar")
        self.txt_Entrar.setGeometry(QRect(80, 40, 161, 31))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.txt_Entrar.setFont(font)
        
        self.link_cadastrar = QLabel(self.frame)
        self.link_cadastrar.setObjectName(u"link_cadastrar")
        self.link_cadastrar.setGeometry(QRect(80, 70, 121, 16))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setItalic(True)
        self.link_cadastrar.setFont(font1)
        self.link_cadastrar.setStyleSheet(u"color: rgb(0, 0, 255);")
        
        # Adicionando o label "E-mail:"
        self.txt_email = QLabel(self.frame)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(100, 410, 121, 16))  # Posicionado acima do campo de email
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(True)
        self.txt_email.setFont(font2)
        self.txt_email.setText(QCoreApplication.translate("Tela_Login", u"E-mail:", None))
        
        self.line_email = QLineEdit(self.frame)
        self.line_email.setObjectName(u"line_email")
        self.line_email.setGeometry(QRect(100, 430, 551, 22))
        
        self.txt_senha = QLabel(self.frame)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(100, 460, 121, 16))
        self.txt_senha.setFont(font2)
        self.txt_senha.setText(QCoreApplication.translate("Tela_Login", u"Senha:", None))
        
        self.line_senha = QLineEdit(self.frame)
        self.line_senha.setObjectName(u"line_senha")
        self.line_senha.setGeometry(QRect(100, 480, 551, 22))
        self.line_senha.setEchoMode(QLineEdit.EchoMode.Password)
        
        self.pushButton_Entrar = QPushButton(self.frame)
        self.pushButton_Entrar.setObjectName(u"pushButton_Entrar")
        self.pushButton_Entrar.setGeometry(QRect(340, 530, 131, 51))
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(True)
        self.pushButton_Entrar.setFont(font3)
        self.pushButton_Entrar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255);")
        
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(190, 100, 341, 331))
        self.label.setPixmap(QPixmap(u":/newPrefix/pngtree-avatar-icon-profile-icon-member-login-vector-isolated-png-image_1978396.jpg"))
        
        Tela_Login.setCentralWidget(self.centralwidget)
        self.retranslateUi(Tela_Login)
        QMetaObject.connectSlotsByName(Tela_Login)
    
    def retranslateUi(self, Tela_Login):
        Tela_Login.setWindowTitle(QCoreApplication.translate("Tela_Login", u"MainWindow", None))
        self.txt_Entrar.setText(QCoreApplication.translate("Tela_Login", u"Entrar", None))
        self.link_cadastrar.setText(QCoreApplication.translate("Tela_Login", u"CADASTRE-SE", None))
        self.pushButton_Entrar.setText(QCoreApplication.translate("Tela_Login", u"Entrar", None))
    
if __name__ == "__main__":
    app = QApplication([]) 
    mainWindow = QMainWindow()  
    ui = Ui_Tela_Login()
    ui.setupUi(mainWindow)  
    mainWindow.show()  
    app.exec()
