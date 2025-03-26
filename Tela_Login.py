import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPixmap, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QMessageBox, QVBoxLayout
from bancodedados import autenticar_usuario
from contatos import Ui_Form

class Ui_Tela_Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Tela_Login")
        self.setMinimumSize(800, 600)  # Permite redimensionamento com tamanho mínimo

        # Layout principal (vertical)
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(20)

        # Garantir que o fundo da tela seja um azul forte
        self.setStyleSheet("""
            QWidget#Tela_Login {
                background: rgb(0, 51, 102);  # Azul forte
            }
        """)

        # Título "Bem-vindo!"
        self.txt_Login = QLabel("Bem-vindo!")
        font1 = QFont("Segoe UI", 20, QFont.Bold)
        self.txt_Login.setFont(font1)
        self.txt_Login.setStyleSheet("""
            color: rgb(220, 220, 255);
            background-color: transparent;
        """)
        self.txt_Login.setAlignment(Qt.AlignCenter)
        self.txt_Login.setFixedSize(600, 35)
        self.main_layout.addWidget(self.txt_Login, alignment=Qt.AlignCenter)

        # Label para foto
        self.label_foto = QLabel()
        self.label_foto.setFixedSize(100, 100)
        self.label_foto.setStyleSheet("""
            border: 1px solid rgb(80, 80, 100);
            border-radius: 50px;
            background-color: rgb(40, 40, 50);
        """)
        self.label_foto.setAlignment(Qt.AlignCenter)
        self.label_foto.setScaledContents(True)
        self.main_layout.addWidget(self.label_foto, alignment=Qt.AlignCenter)

        # Campo Email
        self.txt_email = QLabel("Email:")
        font2 = QFont("Segoe UI", 12)
        self.txt_email.setFont(font2)
        self.txt_email.setStyleSheet("""
            color: rgb(0, 0, 0);
            background-color: transparent;
        """)
        self.main_layout.addWidget(self.txt_email, alignment=Qt.AlignLeft)

        self.line_email = QLineEdit()
        self.line_email.setFixedSize(500, 40)
        self.line_email.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: "Segoe UI";
                font-size: 12pt;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)
        self.main_layout.addWidget(self.line_email, alignment=Qt.AlignCenter)

        # Campo Senha
        self.txt_senha = QLabel("Senha:")
        self.txt_senha.setFont(font2)
        self.txt_senha.setStyleSheet("""
            color: rgb(0, 0, 0);
            background-color: transparent;
        """)
        self.main_layout.addWidget(self.txt_senha, alignment=Qt.AlignLeft)

        self.line_senha = QLineEdit()
        self.line_senha.setFixedSize(500, 40)
        self.line_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.line_senha.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: "Segoe UI";
                font-size: 12pt;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)
        self.main_layout.addWidget(self.line_senha, alignment=Qt.AlignCenter)

        # Botão Entrar
        self.pushButton_Entrar = QPushButton("Entrar")
        self.pushButton_Entrar.setFixedSize(100, 40)
        font3 = QFont("Segoe UI", 12, QFont.Bold)
        self.pushButton_Entrar.setFont(font3)
        self.pushButton_Entrar.setStyleSheet("""
            QPushButton {
                color: rgb(255, 255, 255);
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(100, 150, 255),
                    stop: 1 rgb(70, 100, 200)
                );
                border-radius: 8px;
                padding: 5px;
            }
            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(120, 170, 255),
                    stop: 1 rgb(90, 120, 220)
                );
            }
            QPushButton:pressed {
                background: rgb(50, 80, 180);
            }
        """)
        self.pushButton_Entrar.setCursor(Qt.PointingHandCursor)
        self.main_layout.addWidget(self.pushButton_Entrar, alignment=Qt.AlignCenter)

        # Link Cadastre-se
        self.link_cadastrar = QPushButton("Cadastre-se")
        font4 = QFont("Segoe UI", 10)
        self.link_cadastrar.setFont(font4)
        self.link_cadastrar.setStyleSheet("""
            QPushButton {
                color: rgb(255, 220, 100);
                background-color: transparent;
                border: none;
            }
            QPushButton:hover {
                color: rgb(255, 200, 80);
                text-decoration: underline;
            }
        """)
        self.link_cadastrar.setFixedSize(100, 20)
        self.link_cadastrar.setCursor(Qt.PointingHandCursor)
        self.main_layout.addWidget(self.link_cadastrar, alignment=Qt.AlignCenter)

        # Adicionar um espaço extra no final
        self.main_layout.addStretch()

class TelaLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Tela_Login()
        self.setCentralWidget(self.ui)
        self.ui.pushButton_Entrar.clicked.connect(self.realizar_login)
        self.ui.link_cadastrar.clicked.connect(self.abrir_tela_cadastro)
        # Definir título e ícone da janela principal
        self.setWindowTitle("Agenda de Contatos")
        self.setWindowIcon(QIcon("icone.ico"))  # Substitua "icone.ico" pelo caminho do seu ícone

    def realizar_login(self):
        email = self.ui.line_email.text()
        senha = self.ui.line_senha.text()
        autenticado, usuario_id, nome_usuario, foto = autenticar_usuario(email, senha)

        if autenticado:
            QMessageBox.information(self, "Sucesso", f"Bem-vindo, {nome_usuario}!")
            if foto:
                pixmap = QPixmap()
                pixmap.loadFromData(foto)
                self.ui.label_foto.setPixmap(pixmap)
            self.abrir_tela_contatos(usuario_id)
            self.close()
        else:
            QMessageBox.warning(self, "Erro", "Email ou senha incorretos.")

    def abrir_tela_contatos(self, usuario_id):
        self.tela_contatos = QMainWindow()
        self.ui_contatos = Ui_Form(usuario_id)
        self.ui_contatos.setupUi(self.tela_contatos)
        # Definir título e ícone para a janela de contatos
        self.tela_contatos.setWindowTitle("Agenda de Contatos")
        self.tela_contatos.setWindowIcon(QIcon("agenda.png"))  # Substitua pelo seu ícone
        self.tela_contatos.show()
        self.ui_contatos.carregar_contatos()

    def abrir_tela_cadastro(self):
        from cadastro_proj import Ui_Tela_Cadastro
        self.tela_cadastro = QMainWindow()
        self.ui_cadastro = Ui_Tela_Cadastro()
        self.ui_cadastro.setupUi(self.tela_cadastro)
        self.tela_cadastro.setCentralWidget(self.ui_cadastro.centralwidget)
        # Definir título e ícone para a janela de cadastro
        self.tela_cadastro.setWindowTitle("Agenda de Contatos")
        self.tela_cadastro.setWindowIcon(QIcon("icone.ico"))  # Substitua pelo seu ícone
        self.tela_cadastro.show()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    main_window = TelaLogin()
    main_window.show()
    sys.exit(app.exec())