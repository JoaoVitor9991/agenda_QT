import sys
from PySide6.QtCore import QMetaObject, QRect, Qt
from PySide6.QtCore import QMetaObject, QRect
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox
from bancodedados import autenticar_usuario
from contatos import Ui_Form

class Ui_Tela_Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Tela_Login")
        self.setFixedSize(800, 600)

        # Fundo com gradiente
        self.frame = QWidget(self)
        self.frame.setGeometry(0, 0, 800, 600)
        self.frame.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
            stop:0 #ECF0F1, stop:1 #BDC3C7);
        """)

        # Título
        self.txt_Login = QLabel("Bem-vindo!", self.frame)
        self.txt_Login.setGeometry(QRect(300, 50, 200, 40))
        font1 = QFont("Segoe UI", 20, QFont.Bold)
        self.txt_Login.setFont(font1)
        self.txt_Login.setStyleSheet("color: #2C3E50;")
        self.txt_Login.setAlignment(Qt.AlignCenter)

        # Campo Email
        self.txt_email = QLabel("Email:", self.frame)
        self.txt_email.setGeometry(QRect(150, 200, 100, 20))
        font2 = QFont("Segoe UI", 12)
        self.txt_email.setFont(font2)
        self.txt_email.setStyleSheet("color: #34495E;")
        self.line_email = QLineEdit(self.frame)
        self.line_email.setGeometry(QRect(150, 230, 500, 40))
        self.line_email.setStyleSheet("""
            background-color: #FFFFFF;
            border: 1px solid #BDC3C7;
            border-radius: 5px;
            padding: 5px;
            font-family: Segoe UI;
            font-size: 12pt;
        """)

        # Campo Senha
        self.txt_senha = QLabel("Senha:", self.frame)
        self.txt_senha.setGeometry(QRect(150, 290, 100, 20))
        self.txt_senha.setFont(font2)
        self.txt_senha.setStyleSheet("color: #34495E;")
        self.line_senha = QLineEdit(self.frame)
        self.line_senha.setGeometry(QRect(150, 320, 500, 40))
        self.line_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.line_senha.setStyleSheet("""
            background-color: #FFFFFF;
            border: 1px solid #BDC3C7;
            border-radius: 5px;
            padding: 5px;
            font-family: Segoe UI;
            font-size: 12pt;
        """)

        # Botão Entrar
        self.pushButton_Entrar = QPushButton("Entrar", self.frame)
        self.pushButton_Entrar.setGeometry(QRect(350, 400, 100, 40))
        font3 = QFont("Segoe UI", 12, QFont.Bold)
        self.pushButton_Entrar.setFont(font3)
        self.pushButton_Entrar.setStyleSheet("""
            background-color: #2C3E50;
            color: white;
            border-radius: 5px;
            padding: 5px;
        """)
        self.pushButton_Entrar.setCursor(Qt.PointingHandCursor)

        # Link Cadastre-se
        self.link_cadastrar = QLabel("<a href='#'>Cadastre-se</a>", self.frame)
        self.link_cadastrar.setGeometry(QRect(350, 450, 100, 20))
        font4 = QFont("Segoe UI", 10)
        self.link_cadastrar.setFont(font4)
        self.link_cadastrar.setStyleSheet("color: #2C3E50; text-decoration: underline;")
        self.link_cadastrar.setAlignment(Qt.AlignCenter)
        self.link_cadastrar.setOpenExternalLinks(False)

        # Imagem (opcional)
        self.label = QLabel(self.frame)
        self.label.setGeometry(QRect(300, 100, 200, 100))
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
        email = self.ui.line_email.text()
        senha = self.ui.line_senha.text()
        autenticado, usuario_id, nome_usuario = autenticar_usuario(email, senha)
        if autenticado:
            QMessageBox.information(self, "Sucesso", f"Bem-vindo, {nome_usuario}!")
            self.abrir_tela_contatos(usuario_id)
            self.close()
        else:
            QMessageBox.warning(self, "Erro", "Email ou senha incorretos.")

    def abrir_tela_contatos(self, usuario_id):
        self.tela_contatos = QMainWindow()
        self.ui_contatos = Ui_Form(usuario_id)
        self.ui_contatos.setupUi(self.tela_contatos)
        self.tela_contatos.show()
        self.ui_contatos.carregar_contatos()

    def abrir_tela_cadastro(self, event):
        from cadastro_proj import Ui_Tela_Cadastro
        self.tela_cadastro = QMainWindow()
        self.ui_cadastro = Ui_Tela_Cadastro()
        self.ui_cadastro.setupUi(self.tela_cadastro)
        self.tela_cadastro.setCentralWidget(self.ui_cadastro.centralwidget)
        self.tela_cadastro.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = TelaLogin()
    main_window.show()
    sys.exit(app.exec())