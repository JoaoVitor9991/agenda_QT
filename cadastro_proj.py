from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QFrame, QLabel, QLineEdit, QMainWindow, QPushButton, QWidget, QMessageBox

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
        
        # Título "Criar Conta"
        self.txt_Criar_Conta = QLabel(self.frame)
        self.txt_Criar_Conta.setObjectName(u"txt_Criar_Conta")
        self.txt_Criar_Conta.setGeometry(QRect(100, 30, 161, 31))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(True)
        self.txt_Criar_Conta.setFont(font1)

        # Texto: "Já tem uma conta?"
        self.txt_jtemconta = QLabel(self.frame)
        self.txt_jtemconta.setObjectName(u"txt_jtemconta")
        self.txt_jtemconta.setGeometry(QRect(100, 60, 121, 16))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(True)
        self.txt_jtemconta.setFont(font2)

        # Link "Entrar"
        self.link_entrar = QLabel(self.frame)
        self.link_entrar.setObjectName(u"link_entrar")
        self.link_entrar.setGeometry(QRect(230, 60, 71, 16))
        self.link_entrar.setFont(font2)
        self.link_entrar.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.link_entrar.mousePressEvent = self.abrir_tela_login  # Função para abrir a tela de login

        # Campo de Nome
        self.txt_nome = QLabel(self.frame)
        self.txt_nome.setObjectName(u"txt_nome")
        self.txt_nome.setGeometry(QRect(100, 140, 121, 16))
        self.txt_nome.setFont(font2)
        self.line_nome = QLineEdit(self.frame)
        self.line_nome.setObjectName(u"line_nome")
        self.line_nome.setGeometry(QRect(100, 160, 551, 22))

        # Campo de Email
        self.txt_email = QLabel(self.frame)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(QRect(100, 200, 121, 16))
        self.txt_email.setFont(font2)
        self.line_email = QLineEdit(self.frame)
        self.line_email.setObjectName(u"line_email")
        self.line_email.setGeometry(QRect(100, 220, 551, 22))

        # Campo de Contato
        self.txt_contato = QLabel(self.frame)
        self.txt_contato.setObjectName(u"txt_contato")
        self.txt_contato.setGeometry(QRect(100, 260, 121, 16))
        self.txt_contato.setFont(font2)
        self.line_contato = QLineEdit(self.frame)
        self.line_contato.setObjectName(u"line_contato")
        self.line_contato.setGeometry(QRect(100, 280, 551, 22))

        # Campo de Senha
        self.txt_senha = QLabel(self.frame)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(100, 320, 121, 16))
        self.txt_senha.setFont(font2)
        self.line_senha = QLineEdit(self.frame)
        self.line_senha.setObjectName(u"line_senha")
        self.line_senha.setGeometry(QRect(100, 340, 551, 22))
        self.line_senha.setEchoMode(QLineEdit.Password)  # Ativando o EchoMode para ocultar a senha

        # Campo de Confirmação de Senha
        self.txt_confrimar_senha = QLabel(self.frame)
        self.txt_confrimar_senha.setObjectName(u"txt_confrimar_senha")
        self.txt_confrimar_senha.setGeometry(QRect(100, 380, 151, 16))
        self.txt_confrimar_senha.setFont(font2)
        self.line_Confirmar_senha = QLineEdit(self.frame)
        self.line_Confirmar_senha.setObjectName(u"line_Confirmar_senha")
        self.line_Confirmar_senha.setGeometry(QRect(100, 400, 551, 22))
        self.line_Confirmar_senha.setEchoMode(QLineEdit.Password)  # Ativando o EchoMode para ocultar a confirmação de senha

        # Botão de Cadastro
        self.pushButton_Cadastrar = QPushButton(self.frame)
        self.pushButton_Cadastrar.setObjectName(u"pushButton_Cadastrar")
        self.pushButton_Cadastrar.setGeometry(QRect(390, 480, 131, 51))
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(True)
        self.pushButton_Cadastrar.setFont(font3)
        self.pushButton_Cadastrar.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(0, 0, 255);")
        self.pushButton_Cadastrar.clicked.connect(self.realizar_cadastro)  # Função para cadastrar

        # Botão Voltar
        self.pushButton_Voltar = QPushButton(self.frame)
        self.pushButton_Voltar.setObjectName(u"pushButton_Voltar")
        self.pushButton_Voltar.setGeometry(QRect(250, 480, 131, 51))
        self.pushButton_Voltar.setFont(font3)
        self.pushButton_Voltar.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(255, 0, 0);")
        self.pushButton_Voltar.setText(QCoreApplication.translate("Tela_Cadastro", u"Voltar", None))
        self.pushButton_Voltar.clicked.connect(self.voltar_para_login)  # Função para voltar ao login

        Tela_Cadastro.setCentralWidget(self.centralwidget)
        self.retranslateUi(Tela_Cadastro)
        QMetaObject.connectSlotsByName(Tela_Cadastro)

    def retranslateUi(self, Tela_Cadastro):
        Tela_Cadastro.setWindowTitle(QCoreApplication.translate("Tela_Cadastro", u"Cadastro de Usuário", None))
        self.txt_Criar_Conta.setText(QCoreApplication.translate("Tela_Cadastro", u"Criar conta", None))
        self.txt_jtemconta.setText(QCoreApplication.translate("Tela_Cadastro", u"Já tem uma conta? ", None))
        self.link_entrar.setText(QCoreApplication.translate("Tela_Cadastro", u"Entrar", None))
        self.txt_nome.setText(QCoreApplication.translate("Tela_Cadastro", u"Nome:", None))
        self.txt_email.setText(QCoreApplication.translate("Tela_Cadastro", u"Email:", None))
        self.txt_contato.setText(QCoreApplication.translate("Tela_Cadastro", u"Contato:", None))
        self.txt_senha.setText(QCoreApplication.translate("Tela_Cadastro", u"Senha:", None))
        self.txt_confrimar_senha.setText(QCoreApplication.translate("Tela_Cadastro", u"Confirmação da Senha:", None))
        self.pushButton_Cadastrar.setText(QCoreApplication.translate("Tela_Cadastro", u"Cadastrar", None))

    def abrir_tela_login(self, event):
        from Tela_Login import Ui_Tela_Login  # Importe a tela de login
        self.window = QMainWindow()  # Crie uma nova janela
        self.ui = Ui_Tela_Login()  # Instancie a tela de login
        self.ui.setupUi(self.window)  # Configure a tela de login
        self.window.show()  # Exiba

    def voltar_para_login(self):
        self.abrir_tela_login(None)  # Volta para a tela de login

    def realizar_cadastro(self):
        nome = self.line_nome.text()
        email = self.line_email.text()
        contato = self.line_contato.text()
        senha = self.line_senha.text()
        confirmar_senha = self.line_Confirmar_senha.text()

        if senha != confirmar_senha:
            QMessageBox.warning(None, "Erro", "As senhas não coincidem. Tente novamente.")
        elif nome == "" or email == "" or contato == "" or senha == "":
            QMessageBox.warning(None, "Erro", "Preencha todos os campos.")
        else:
            QMessageBox.information(None, "Sucesso", "Cadastro realizado com sucesso!")
            self.voltar_para_login()  # Volta para a tela de login após o cadastro

if __name__ == "__main__":
    app = QApplication([])  # Criação da aplicação
    MainWindow = QMainWindow()  # Criação da janela principal
    ui = Ui_Tela_Cadastro()  # Instanciando a interface
    ui.setupUi(MainWindow)  # Configura a interface
    MainWindow.show()  # Exibe a janela principal
    app.exec()  # Inicia o loop de eventos da aplicação
