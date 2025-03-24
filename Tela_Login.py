import sys

from PySide6.QtCore import QMetaObject, QRect, Qt

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
 
        # Frame principal com gradiente moderno

        self.frame = QWidget(self)

        self.frame.setGeometry(0, 0, 800, 600)

        self.frame.setStyleSheet("""

            background: qlineargradient(

                x1: 0, y1: 0, x2: 1, y2: 1,

                stop: 0 rgb(20, 20, 30),

                stop: 1 rgb(50, 60, 80)

            );

        """)
 
        # Label para foto

        self.label_foto = QLabel(self.frame)

        self.label_foto.setGeometry(QRect(350, 100, 100, 100))

        self.label_foto.setStyleSheet("""

            border: 1px solid rgb(80, 80, 100);

            border-radius: 50px;

            background-color: rgb(40, 40, 50);

        """)

        self.label_foto.setAlignment(Qt.AlignCenter)

        self.label_foto.setScaledContents(True)
 
        # Título "Bem-vindo!"

        self.txt_Login = QLabel("Bem-vindo!", self.frame)

        self.txt_Login.setGeometry(QRect(100, 30, 600, 35))

        font1 = QFont("Segoe UI", 20, QFont.Bold)

        self.txt_Login.setFont(font1)

        self.txt_Login.setStyleSheet("""

            color: rgb(220, 220, 255);

            background-color: transparent;

        """)

        self.txt_Login.setAlignment(Qt.AlignCenter)
 
        # Campo Email

        self.txt_email = QLabel("Email:", self.frame)

        self.txt_email.setGeometry(QRect(150, 230, 35, 14))

        font2 = QFont("Segoe UI", 12)

        self.txt_email.setFont(font2)

        self.txt_email.setStyleSheet("color: rgb(200, 200, 200);")

        self.line_email = QLineEdit(self.frame)

        self.line_email.setGeometry(QRect(150, 250, 500, 40))

        self.line_email.setStyleSheet("""

            QLineEdit {

                background-color: rgb(40, 40, 50);

                color: rgb(255, 255, 255);

                border: 1px solid rgb(80, 80, 100);

                border-radius: 5px;

                padding: 5px;

                font-family: Segoe UI;

                font-size: 12pt;

            }

            QLineEdit:focus {

                border: 1px solid rgb(100, 150, 255);

            }

        """)
 
        # Campo Senha

        self.txt_senha = QLabel("Senha:", self.frame)

        self.txt_senha.setGeometry(QRect(150, 310, 39, 14))

        self.txt_senha.setFont(font2)

        self.txt_senha.setStyleSheet("color: rgb(200, 200, 200);")

        self.line_senha = QLineEdit(self.frame)

        self.line_senha.setGeometry(QRect(150, 330, 500, 40))

        self.line_senha.setEchoMode(QLineEdit.EchoMode.Password)

        self.line_senha.setStyleSheet("""

            QLineEdit {

                background-color: rgb(40, 40, 50);

                color: rgb(255, 255, 255);

                border: 1px solid rgb(80, 80, 100);

                border-radius: 5px;

                padding: 5px;

                font-family: Segoe UI;

                font-size: 12pt;

            }

            QLineEdit:focus {

                border: 1px solid rgb(100, 150, 255);

            }

        """)
 
        # Botão Entrar

        self.pushButton_Entrar = QPushButton("Entrar", self.frame)

        self.pushButton_Entrar.setGeometry(QRect(350, 400, 100, 40))

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
 
        # Link Cadastre-se

        self.link_cadastrar = QLabel("<a href='#'>Cadastre-se</a>", self.frame)

        self.link_cadastrar.setGeometry(QRect(350, 450, 100, 20))

        font4 = QFont("Segoe UI", 10)

        self.link_cadastrar.setFont(font4)

        self.link_cadastrar.setStyleSheet("""

            color: rgb(220, 220, 255);

            background-color: transparent;

        """)

        self.link_cadastrar.setAlignment(Qt.AlignCenter)

        self.link_cadastrar.setOpenExternalLinks(False)
 
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
 