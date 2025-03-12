from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QApplication, QFrame, QLabel, QLineEdit, QMainWindow, QPushButton, QWidget, QMessageBox
import mysql.connector
from bancodedados import autenticar_usuario

class Ui_Tela_Login(object):
    def setupUi(self, Tela_Login):
        if not Tela_Login.objectName():
            Tela_Login.setObjectName(u"Tela_Login")
        Tela_Login.resize(800, 600)

        # Central Widget
        self.centralwidget = QWidget(Tela_Login)
        self.centralwidget.setObjectName(u"centralwidget")

        # Frame para a tela
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(0, 0, 800, 600)  # Ajustado para o tamanho da janela
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        # Título "Login"
        self.txt_Login = QLabel(self.frame)
        self.txt_Login.setObjectName(u"txt_Login")
        self.txt_Login.setGeometry(100, 30, 121, 31)
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(True)
        self.txt_Login.setFont(font1)

        # Campo de E-mail
        self.txt_email = QLabel(self.frame)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(100, 340, 121, 16)
        font2 = QFont()
        font2.setPointSize(10)
        self.txt_email.setFont(font2)
        self.line_email = QLineEdit(self.frame)
        self.line_email.setObjectName(u"line_email")
        self.line_email.setGeometry(100, 360, 551, 22)

        # Campo de Senha
        self.txt_senha = QLabel(self.frame)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(100, 400, 121, 16)
        self.txt_senha.setFont(font2)
        self.line_senha = QLineEdit(self.frame)
        self.line_senha.setObjectName(u"line_senha")
        self.line_senha.setGeometry(100, 420, 551, 22)
        self.line_senha.setEchoMode(QLineEdit.EchoMode.Password)

        # Botão de Login
        self.pushButton_Entrar = QPushButton(self.frame)
        self.pushButton_Entrar.setObjectName(u"pushButton_Entrar")
        self.pushButton_Entrar.setGeometry(320, 480, 131, 51)
        font3 = QFont()
        font3.setBold(True)
        font3.setItalic(True)
        self.pushButton_Entrar.setFont(font3)
        self.pushButton_Entrar.setStyleSheet(u"color: rgb(255, 255, 255); background-color: rgb(0, 0, 255);")
        self.pushButton_Entrar.clicked.connect(self.realizar_login)  # Conectar ao método de login

        # Link para Cadastro
        self.link_cadastrar = QLabel(self.frame)
        self.link_cadastrar.setObjectName(u"link_cadastrar")
        self.link_cadastrar.setGeometry(80, 70, 121, 16)
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        font4.setItalic(True)
        self.link_cadastrar.setFont(font4)
        self.link_cadastrar.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.link_cadastrar.setText("Cadastre-se")
        self.link_cadastrar.mousePressEvent = self.abrir_tela_cadastro  # Link clicável

        # Exibindo a imagem corretamente
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(215, 20, 341, 331))
        self.label.setPixmap(QPixmap("asc.png"))  
        self.label.setScaledContents(True)  
        self.label.raise_()  

        Tela_Login.setCentralWidget(self.centralwidget)
        self.retranslateUi(Tela_Login)
        QMetaObject.connectSlotsByName(Tela_Login)

    def retranslateUi(self, Tela_Login):
        Tela_Login.setWindowTitle(QCoreApplication.translate("Tela_Login", u"Login de Usuário", None))
        self.txt_Login.setText(QCoreApplication.translate("Tela_Login", u"Login", None))
        self.txt_email.setText(QCoreApplication.translate("Tela_Login", u"Email:", None))
        self.txt_senha.setText(QCoreApplication.translate("Tela_Login", u"Senha:", None))
        self.pushButton_Entrar.setText(QCoreApplication.translate("Tela_Login", u"Entrar", None))

    def abrir_tela_cadastro(self, event):
        from cadastro_proj import Ui_Tela_Cadastro  
        self.window = QMainWindow()  
        self.ui = Ui_Tela_Cadastro()  
        self.ui.setupUi(self.window)  
        self.window.show()  

    def realizar_login(self):
        email = self.line_email.text()
        senha = self.line_senha.text()

    # 🔹 Obtém o usuario_id e o nome do usuário do banco de dados
        autenticado, usuario_id, nome_usuario = autenticar_usuario(email, senha)

        if autenticado:
            QMessageBox.information(None, "Sucesso", f"Bem-vindo, {nome_usuario}!")

        # 🔹 Abre a tela de contatos e passa usuario_id
            self.abrir_tela_contatos(usuario_id)
        else:
            QMessageBox.warning(None, "Erro", "Email ou senha incorretos. Tente novamente.")


    def close_window(self):
       
        if hasattr(self, 'window'):
            self.window.close() 
        else:
            print("Erro: A janela principal não foi inicializada corretamente.")

    def open_contact_screen(self):
        
        from contatos import Ui_Form  
        self.window = QMainWindow()  
        self.ui = Ui_Form()  
        self.ui.setupUi(self.window)  
        self.window.show()  

    def abrir_tela_contatos(self, usuario_id):
        """Abre a tela de contatos e passa o usuário logado."""
        from contatos import Ui_Form  # Importa a tela de contatos

        self.window = QMainWindow()  
        self.ui = Ui_Form()  
        self.ui.setupUi(self.window)  # <-- Agora passando o argumento correto

        # Passando o usuário logado para a tela de contatos (se precisar)
        self.ui.usuario_id = usuario_id  

        self.window.show()


if __name__ == "__main__":
    app = QApplication([])  
    MainWindow = QMainWindow()  
    ui = Ui_Tela_Login()  
    ui.setupUi(MainWindow)  
    MainWindow.show()  
    app.exec()  
