import sys
from PySide6.QtCore import QMetaObject, QRect
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
from bancodedados import autenticar_usuario
from contatos import Ui_Form  # Importa a tela de contatos
from cadastro_proj import Ui_Tela_Cadastro  

class Ui_Tela_Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Tela_Login")
        self.setFixedSize(800, 600)

        
        self.frame = QWidget(self)
        self.frame.setGeometry(0, 0, 800, 600)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")

        
        self.txt_Login = QLabel("Login", self.frame)
        self.txt_Login.setGeometry(100, 30, 121, 31)
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(True)
        self.txt_Login.setFont(font1)

        
        self.txt_email = QLabel("Email:", self.frame)
        self.txt_email.setGeometry(100, 340, 121, 16)
        font2 = QFont()
        font2.setPointSize(10)
        self.txt_email.setFont(font2)
        self.line_email = QLineEdit(self.frame)
        self.line_email.setGeometry(100, 360, 551, 22)

        
        self.txt_senha = QLabel("Senha:", self.frame)
        self.txt_senha.setGeometry(100, 400, 121, 16)
        self.txt_senha.setFont(font2)
        self.line_senha = QLineEdit(self.frame)
        self.line_senha.setGeometry(100, 420, 551, 22)
        self.line_senha.setEchoMode(QLineEdit.EchoMode.Password)

        
        self.pushButton_Entrar = QPushButton("Entrar", self.frame)
        self.pushButton_Entrar.setGeometry(320, 480, 131, 51)
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(True)
        self.pushButton_Entrar.setFont(font3)
        self.pushButton_Entrar.setStyleSheet("color: rgb(255, 255, 255); background-color: rgb(0, 0, 255);")

        
        self.link_cadastrar = QLabel("<a href='#'>Cadastre-se</a>", self.frame)
        self.link_cadastrar.setGeometry(80, 70, 121, 16)
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        font4.setItalic(True)
        self.link_cadastrar.setFont(font4)
        self.link_cadastrar.setStyleSheet("color: rgb(0, 0, 255);")
        self.link_cadastrar.setOpenExternalLinks(False)

        
        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(215, 20, 341, 331))
        self.label.setPixmap(QPixmap("asc.png"))
        self.label.setScaledContents(True)

class TelaLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Tela_Login()
        self.setCentralWidget(self.ui)

        
        self.ui.pushButton_Entrar.clicked.connect(self.realizar_login)
        self.ui.link_cadastrar.mousePressEvent = self.abrir_tela_cadastro

    def realizar_login(self):
        """Verifica as credenciais do usuário e abre a tela de contatos."""
        email = self.ui.line_email.text()
        senha = self.ui.line_senha.text()

        autenticado, usuario_id, nome_usuario = autenticar_usuario(email, senha)

        if autenticado:
            QMessageBox.information(self, "Sucesso", f"Bem-vindo, {nome_usuario}!")
            self.abrir_tela_contatos(usuario_id)
        else:
            QMessageBox.warning(self, "Erro", "Email ou senha incorretos. Tente novamente.")

    def abrir_tela_contatos(self, usuario_id):
        """Abre a tela de contatos e passa o usuário logado."""
        self.tela_contatos = QMainWindow()
        self.ui_contatos = Ui_Form(usuario_id)  # ✅ Agora passamos o usuario_id corretamente
        self.ui_contatos.setupUi(self.tela_contatos)
        self.tela_contatos.show()

    def abrir_tela_cadastro(self, event):
        """Abre a tela de cadastro."""
        self.tela_cadastro = QMainWindow()
        self.ui_cadastro = Ui_Tela_Cadastro()
        self.ui_cadastro.setupUi(self.tela_cadastro)
        self.tela_cadastro.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = TelaLogin()
    main_window.show()
    sys.exit(app.exec())
