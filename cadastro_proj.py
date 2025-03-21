from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QFrame, QLabel, QLineEdit, QMainWindow, QPushButton, QWidget, QMessageBox
from bancodedados import salvar_usuario

class Ui_Tela_Cadastro(object):
    def setupUi(self, Tela_Cadastro):
        if not Tela_Cadastro.objectName():
            Tela_Cadastro.setObjectName("Tela_Cadastro")
        Tela_Cadastro.resize(800, 600)
        self.centralwidget = QWidget(Tela_Cadastro)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(-10, 0, 811, 601))
        font = QFont()
        font.setPointSize(12)
        self.frame.setFont(font)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)

        self.txt_Criar_Conta = QLabel(self.frame)
        self.txt_Criar_Conta.setObjectName("txt_Criar_Conta")
        self.txt_Criar_Conta.setGeometry(QRect(100, 30, 161, 31))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(True)
        self.txt_Criar_Conta.setFont(font1)

        self.txt_jtemconta = QLabel(self.frame)
        self.txt_jtemconta.setObjectName("txt_jtemconta")
        self.txt_jtemconta.setGeometry(QRect(100, 60, 121, 16))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setItalic(True)
        self.txt_jtemconta.setFont(font2)

        self.link_entrar = QLabel(self.frame)
        self.link_entrar.setObjectName("link_entrar")
        self.link_entrar.setGeometry(QRect(230, 60, 71, 16))
        self.link_entrar.setFont(font2)
        self.link_entrar.setStyleSheet("color: rgb(0, 0, 255);")
        self.link_entrar.mousePressEvent = self.abrir_tela_login

        self.txt_nome = QLabel(self.frame)
        self.txt_nome.setObjectName("txt_nome")
        self.txt_nome.setGeometry(QRect(100, 140, 121, 16))
        self.txt_nome.setFont(font2)
        self.line_nome = QLineEdit(self.frame)
        self.line_nome.setObjectName("line_nome")
        self.line_nome.setGeometry(QRect(100, 160, 551, 22))

        self.asterisco_nome = QLabel(self.frame)
        self.asterisco_nome.setObjectName("asterisco_nome")
        self.asterisco_nome.setGeometry(QRect(140, 140, 10, 16))
        self.asterisco_nome.setText("*")
        self.asterisco_nome.setFont(QFont("Arial", 12))
        self.asterisco_nome.setStyleSheet("color: red;")

        self.txt_email = QLabel(self.frame)
        self.txt_email.setObjectName("txt_email")
        self.txt_email.setGeometry(QRect(100, 200, 121, 16))
        self.txt_email.setFont(font2)
        self.line_email = QLineEdit(self.frame)
        self.line_email.setObjectName("line_email")
        self.line_email.setGeometry(QRect(100, 220, 551, 22))

        self.asterisco_email = QLabel(self.frame)
        self.asterisco_email.setObjectName("asterisco_email")
        self.asterisco_email.setGeometry(QRect(140, 200, 10, 16))
        self.asterisco_email.setText("*")
        self.asterisco_email.setFont(QFont("Arial", 12))
        self.asterisco_email.setStyleSheet("color: red;")

        self.txt_contato = QLabel(self.frame)
        self.txt_contato.setObjectName("txt_contato")
        self.txt_contato.setGeometry(QRect(100, 260, 121, 16))
        self.txt_contato.setFont(font2)
        self.line_contato = QLineEdit(self.frame)
        self.line_contato.setObjectName("line_contato")
        self.line_contato.setGeometry(QRect(100, 280, 551, 22))
        self.line_contato.setInputMask("(99) 99999-9999")

        self.txt_senha = QLabel(self.frame)
        self.txt_senha.setObjectName("txt_senha")
        self.txt_senha.setGeometry(QRect(100, 320, 121, 16))
        self.txt_senha.setFont(font2)
        self.line_senha = QLineEdit(self.frame)
        self.line_senha.setObjectName("line_senha")
        self.line_senha.setGeometry(QRect(100, 340, 551, 22))
        self.line_senha.setEchoMode(QLineEdit.Password)

        self.asterisco_senha = QLabel(self.frame)
        self.asterisco_senha.setObjectName("asterisco_senha")
        self.asterisco_senha.setGeometry(QRect(141, 320, 10, 16))
        self.asterisco_senha.setText("*")
        self.asterisco_senha.setFont(QFont("Arial", 12))
        self.asterisco_senha.setStyleSheet("color: red;")

        self.txt_confrimar_senha = QLabel(self.frame)
        self.txt_confrimar_senha.setObjectName("txt_confrimar_senha")
        self.txt_confrimar_senha.setGeometry(QRect(100, 380, 151, 16))
        self.txt_confrimar_senha.setFont(font2)
        self.line_Confirmar_senha = QLineEdit(self.frame)
        self.line_Confirmar_senha.setObjectName("line_Confirmar_senha")
        self.line_Confirmar_senha.setGeometry(QRect(100, 400, 551, 22))
        self.line_Confirmar_senha.setEchoMode(QLineEdit.Password)

        self.asterisco_conf_senha = QLabel(self.frame)
        self.asterisco_conf_senha.setObjectName("asterisco_conf_senha")
        self.asterisco_conf_senha.setGeometry(QRect(243, 380, 10, 16))
        self.asterisco_conf_senha.setText("*")
        self.asterisco_conf_senha.setFont(QFont("Arial", 12))
        self.asterisco_conf_senha.setStyleSheet("color: red;")

        self.pushButton_Cadastrar = QPushButton(self.frame)
        self.pushButton_Cadastrar.setObjectName("pushButton_Cadastrar")
        self.pushButton_Cadastrar.setGeometry(QRect(390, 480, 131, 51))
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(True)
        self.pushButton_Cadastrar.setFont(font3)
        self.pushButton_Cadastrar.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(0, 0, 255);")
        self.pushButton_Cadastrar.clicked.connect(lambda: self.realizar_cadastro(Tela_Cadastro))

        self.pushButton_Voltar = QPushButton(self.frame)
        self.pushButton_Voltar.setObjectName("pushButton_Voltar")
        self.pushButton_Voltar.setGeometry(QRect(250, 480, 131, 51))
        self.pushButton_Voltar.setFont(font3)
        self.pushButton_Voltar.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(255, 0, 0);")
        self.pushButton_Voltar.clicked.connect(lambda: self.voltar_para_login(Tela_Cadastro))

        self.retranslateUi(Tela_Cadastro)
        QMetaObject.connectSlotsByName(Tela_Cadastro)

    def retranslateUi(self, Tela_Cadastro):
        Tela_Cadastro.setWindowTitle(QCoreApplication.translate("Tela_Cadastro", "Cadastro de Usuário", None))
        self.txt_Criar_Conta.setText(QCoreApplication.translate("Tela_Cadastro", "Criar conta", None))
        self.txt_jtemconta.setText(QCoreApplication.translate("Tela_Cadastro", "Já tem uma conta? ", None))
        self.link_entrar.setText(QCoreApplication.translate("Tela_Cadastro", "Entrar", None))
        self.txt_nome.setText(QCoreApplication.translate("Tela_Cadastro", "Nome:", None))
        self.txt_email.setText(QCoreApplication.translate("Tela_Cadastro", "Email:", None))
        self.txt_contato.setText(QCoreApplication.translate("Tela_Cadastro", "Contato:", None))
        self.txt_senha.setText(QCoreApplication.translate("Tela_Cadastro", "Senha:", None))
        self.txt_confrimar_senha.setText(QCoreApplication.translate("Tela_Cadastro", "Confirmação da Senha:", None))
        self.pushButton_Cadastrar.setText(QCoreApplication.translate("Tela_Cadastro", "Cadastrar", None))
        self.pushButton_Voltar.setText(QCoreApplication.translate("Tela_Cadastro", "Voltar", None))

    def abrir_tela_login(self, event):
        from Tela_Login import Ui_Tela_Login
        self.window = QMainWindow()
        self.ui = Ui_Tela_Login()
        self.ui.setupUi()
        self.window.setCentralWidget(self.ui)
        self.window.show()
        self.frame.parent().close()  # Fecha a tela de cadastro

    def voltar_para_login(self, Tela_Cadastro):
        self.abrir_tela_login(None)
        Tela_Cadastro.close()

    def realizar_cadastro(self, Tela_Cadastro):
        nome = self.line_nome.text()
        email = self.line_email.text()
        contato = self.line_contato.text()
        senha = self.line_senha.text()
        confirmar_senha = self.line_Confirmar_senha.text()

        self.limpar_bordas()

        if senha != confirmar_senha:
            QMessageBox.warning(None, "Erro", "As senhas não coincidem. Tente novamente.")
        elif nome == "" or email == "" or senha == "":
            QMessageBox.warning(None, "Erro", "Preencha todos os campos obrigatórios.")
            self.validar_campos_vazios(nome, email, contato, senha, confirmar_senha)
        else:
            if salvar_usuario(nome, email, contato, senha):
                QMessageBox.information(None, "Sucesso", "Cadastro realizado com sucesso!")
                self.voltar_para_login(Tela_Cadastro)
            else:
                QMessageBox.warning(None, "Erro", "Erro ao cadastrar! Tente outro e-mail ou verifique os dados.")

    def limpar_bordas(self):
        self.line_nome.setStyleSheet("")
        self.line_email.setStyleSheet("")
        self.line_contato.setStyleSheet("")
        self.line_senha.setStyleSheet("")
        self.line_Confirmar_senha.setStyleSheet("")

    def validar_campos_vazios(self, nome, email, contato, senha, confirmar_senha):
        if nome == "":
            self.line_nome.setStyleSheet("border: 1px solid red;")
        if email == "":
            self.line_email.setStyleSheet("border: 1px solid red;")
        if contato == "":
            self.line_contato.setStyleSheet("border: 1px solid red;")
        if senha == "":
            self.line_senha.setStyleSheet("border: 1px solid red;")
        if confirmar_senha == "":
            self.line_Confirmar_senha.setStyleSheet("border: 1px solid red;")

if __name__ == "__main__":
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = Ui_Tela_Cadastro()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()