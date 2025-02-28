from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QFrame, QLineEdit, QLabel, QDateEdit, QVBoxLayout, QHBoxLayout

class Ui_tela_add_contato(object):
    def setupUi(self, tela_add_contato, main_window):
        if not tela_add_contato.objectName():
            tela_add_contato.setObjectName(u"tela_add_contato")
        tela_add_contato.resize(800, 671)
        self.centralwidget = QWidget(tela_add_contato)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(-10, 0, 811, 671)
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        
        # Setup dos campos de entrada
        self.txt_nome = QLabel(self.frame)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(80, 60, 121, 16)
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        self.txt_nome.setFont(font)
        self.line_nome = QLineEdit(self.frame)
        self.line_nome.setObjectName(u"line_nome")
        self.line_nome.setGeometry(80, 80, 551, 22)
        
        # Campos restantes
        self.txt_contato = QLabel(self.frame)
        self.txt_contato.setObjectName(u"txt_contato")
        self.txt_contato.setGeometry(80, 130, 121, 16)
        self.txt_contato.setFont(font)
        self.line_contato = QLineEdit(self.frame)
        self.line_contato.setObjectName(u"line_contato")
        self.line_contato.setGeometry(80, 150, 551, 22)

        self.txt_email = QLabel(self.frame)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(80, 200, 121, 16)
        self.txt_email.setFont(font)
        self.line_email = QLineEdit(self.frame)
        self.line_email.setObjectName(u"line_email")
        self.line_email.setGeometry(80, 220, 551, 22)
        
        self.txt_data_nascimento = QLabel(self.frame)
        self.txt_data_nascimento.setObjectName(u"txt_data_nascimento")
        self.txt_data_nascimento.setGeometry(80, 270, 141, 16)
        self.txt_data_nascimento.setFont(font)
        self.dateEdit_Data_nascimento = QDateEdit(self.frame)
        self.dateEdit_Data_nascimento.setObjectName(u"dateEdit_Data_nascimento")
        self.dateEdit_Data_nascimento.setGeometry(80, 300, 110, 22)
        
        self.txt_perfil_rede_social = QLabel(self.frame)
        self.txt_perfil_rede_social.setObjectName(u"txt_perfil_rede_social")
        self.txt_perfil_rede_social.setGeometry(80, 350, 141, 16)
        self.txt_perfil_rede_social.setFont(font)
        self.line_perfil_rede_social = QLineEdit(self.frame)
        self.line_perfil_rede_social.setObjectName(u"line_perfil_rede_social")
        self.line_perfil_rede_social.setGeometry(80, 370, 551, 22)

        self.txt_notas = QLabel(self.frame)
        self.txt_notas.setObjectName(u"txt_notas")
        self.txt_notas.setGeometry(80, 420, 141, 16)
        self.txt_notas.setFont(font)
        self.line_notas = QLineEdit(self.frame)
        self.line_notas.setObjectName(u"line_notas")
        self.line_notas.setGeometry(80, 450, 551, 141)

        # Botões
        self.pushButton_Entrar = QPushButton(self.frame)
        self.pushButton_Entrar.setObjectName(u"pushButton_Entrar")
        self.pushButton_Entrar.setGeometry(630, 610, 131, 41)
        font1 = QFont()
        font1.setBold(True)
        font1.setItalic(True)
        self.pushButton_Entrar.setFont(font1)
        self.pushButton_Entrar.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(0, 0, 255);")
        
        self.pushButton_Entrar_2 = QPushButton(self.frame)
        self.pushButton_Entrar_2.setObjectName(u"pushButton_Entrar_2")
        self.pushButton_Entrar_2.setGeometry(620, 10, 131, 41)
        self.pushButton_Entrar_2.setFont(font1)
        self.pushButton_Entrar_2.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(0, 0, 255);")
        
        tela_add_contato.setCentralWidget(self.centralwidget)

        self.retranslateUi(tela_add_contato)
        
        # Conectar o botão de voltar à função
        self.pushButton_Entrar_2.clicked.connect(lambda: self.voltar_para_contatos(tela_add_contato, main_window))

        QMetaObject.connectSlotsByName(tela_add_contato)

    def retranslateUi(self, tela_add_contato):
        tela_add_contato.setWindowTitle(QCoreApplication.translate("tela_add_contato", u"Adicionar Contato", None))
        self.txt_nome.setText(QCoreApplication.translate("tela_add_contato", u"Nome:", None))
        self.txt_contato.setText(QCoreApplication.translate("tela_add_contato", u"Contato:", None))
        self.txt_email.setText(QCoreApplication.translate("tela_add_contato", u"Email:", None))
        self.txt_data_nascimento.setText(QCoreApplication.translate("tela_add_contato", u"Data de Nascimento:", None))
        self.txt_perfil_rede_social.setText(QCoreApplication.translate("tela_add_contato", u"Perfil de Rede Social:", None))
        self.txt_notas.setText(QCoreApplication.translate("tela_add_contato", u"Notas:", None))
        self.pushButton_Entrar.setText(QCoreApplication.translate("tela_add_contato", u"Salvar", None))
        self.pushButton_Entrar_2.setText(QCoreApplication.translate("tela_add_contato", u"Voltar", None))

    def voltar_para_contatos(self, tela_add_contato, main_window):
        tela_add_contato.close()  # Fecha a tela de adicionar contato
        main_window.show()  # Exibe a tela principal (onde a lista de contatos seria mostrada)

if __name__ == "__main__":
    app = QApplication([])  # Criação da aplicação
    MainWindow = QMainWindow()  # Criação da janela principal
    ui = Ui_tela_add_contato()  # Instancia a tela de adicionar contato
    ui.setupUi(MainWindow, MainWindow)  # Configura a interface de adicionar contato e passa a main_window
    MainWindow.show()  # Exibe a janela principal
    app.exec()  # Inicia o loop de eventos da aplicação
