from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import QApplication, QFrame, QLabel, QLineEdit, QMainWindow, QPushButton, QWidget, QMessageBox, QFileDialog, QScrollArea, QVBoxLayout
from bancodedados import salvar_usuario

class Ui_Tela_Cadastro(object):
    def setupUi(self, Tela_Cadastro):
        if not Tela_Cadastro.objectName():
            Tela_Cadastro.setObjectName("Tela_Cadastro")
        Tela_Cadastro.resize(800, 600)

        # Widget central com gradiente escuro
        self.centralwidget = QWidget(Tela_Cadastro)
        self.centralwidget.setStyleSheet("""
            background: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 rgb(20, 20, 30),
                stop: 1 rgb(50, 60, 80)
            );
        """)
        Tela_Cadastro.setCentralWidget(self.centralwidget)

        # Área de rolagem
        self.scroll_area = QScrollArea(self.centralwidget)
        self.scroll_area.setGeometry(QRect(0, 0, 800, 600))
        self.scroll_area.setWidgetResizable(True)

        # Widget de conteúdo dentro da área de rolagem
        self.scroll_widget = QWidget()
        self.scroll_widget.setMinimumHeight(700)  # Aumentado para caber todo o conteúdo
        self.scroll_area.setWidget(self.scroll_widget)

        # Frame dentro do widget de rolagem
        self.frame = QFrame(self.scroll_widget)
        self.frame.setGeometry(QRect(150, 50, 500, 650))  # Aumentei a altura do frame
        font = QFont("Segoe UI", 12)
        self.frame.setFont(font)
        self.frame.setStyleSheet("""
            background-color: rgb(40, 40, 50);
            border-radius: 10px;
        """)

        # Foto de perfil (inicialmente vazia)
        self.label_foto = QLabel(self.frame)
        self.label_foto.setGeometry(QRect(200, 20, 100, 100))
        self.label_foto.setStyleSheet("""
            border: 1px solid rgb(80, 80, 100);
            border-radius: 50px;
            background-color: rgb(40, 40, 50);
        """)
        self.label_foto.setAlignment(Qt.AlignCenter)
        self.label_foto.setScaledContents(True)
        self.foto_data = None

        # Botão para selecionar foto
        self.btn_selecionar_foto = QPushButton("Selecionar Foto", self.frame)
        self.btn_selecionar_foto.setGeometry(QRect(200, 130, 100, 30))
        self.btn_selecionar_foto.setFont(QFont("Segoe UI", 10, QFont.Bold))
        self.btn_selecionar_foto.setStyleSheet("""
            QPushButton {
                color: rgb(255, 255, 255);
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(100, 150, 255),
                    stop: 1 rgb(70, 100, 200)
                );
                border-radius: 5px;
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
        self.btn_selecionar_foto.setCursor(Qt.PointingHandCursor)
        self.btn_selecionar_foto.clicked.connect(self.selecionar_foto)

        # Título
        self.txt_Criar_Conta = QLabel("Crie sua conta", self.frame)
        self.txt_Criar_Conta.setGeometry(QRect(0, 170, 500, 40))
        font1 = QFont("Segoe UI", 18, QFont.Bold)
        self.txt_Criar_Conta.setFont(font1)
        self.txt_Criar_Conta.setStyleSheet("""
            color: rgb(220, 220, 255);
            background-color: transparent;
        """)
        self.txt_Criar_Conta.setAlignment(Qt.AlignCenter)

        # Campo Nome
        self.txt_nome = QLabel("Nome:", self.frame)
        self.txt_nome.setGeometry(QRect(50, 220, 100, 20))
        font2 = QFont("Segoe UI", 12)
        self.txt_nome.setFont(font2)
        self.txt_nome.setStyleSheet("color: rgb(200, 200, 200);")
        self.line_nome = QLineEdit(self.frame)
        self.line_nome.setGeometry(QRect(50, 240, 400, 40))
        self.line_nome.setStyleSheet("""
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
        self.asterisco_nome = QLabel("*", self.frame)
        self.asterisco_nome.setGeometry(QRect(150, 220, 10, 20))
        self.asterisco_nome.setFont(font2)
        self.asterisco_nome.setStyleSheet("color: rgb(255, 100, 100);")

        # Campo Email
        self.txt_email = QLabel("Email:", self.frame)
        self.txt_email.setGeometry(QRect(50, 290, 100, 20))
        self.txt_email.setFont(font2)
        self.txt_email.setStyleSheet("color: rgb(200, 200, 200);")
        self.line_email = QLineEdit(self.frame)
        self.line_email.setGeometry(QRect(50, 310, 400, 40))
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
        self.asterisco_email = QLabel("*", self.frame)
        self.asterisco_email.setGeometry(QRect(150, 290, 10, 20))
        self.asterisco_email.setFont(font2)
        self.asterisco_email.setStyleSheet("color: rgb(255, 100, 100);")

        # Campo Contato
        self.txt_contato = QLabel("Contato:", self.frame)
        self.txt_contato.setGeometry(QRect(50, 360, 100, 20))
        self.txt_contato.setFont(font2)
        self.txt_contato.setStyleSheet("color: rgb(200, 200, 200);")
        self.line_contato = QLineEdit(self.frame)
        self.line_contato.setGeometry(QRect(50, 380, 400, 40))
        self.line_contato.setInputMask("(99) 99999-9999")
        self.line_contato.setStyleSheet("""
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
        self.txt_senha.setGeometry(QRect(50, 430, 100, 20))
        self.txt_senha.setFont(font2)
        self.txt_senha.setStyleSheet("color: rgb(200, 200, 200);")
        self.line_senha = QLineEdit(self.frame)
        self.line_senha.setGeometry(QRect(50, 450, 400, 40))
        self.line_senha.setEchoMode(QLineEdit.Password)
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
        self.asterisco_senha = QLabel("*", self.frame)
        self.asterisco_senha.setGeometry(QRect(150, 430, 10, 20))
        self.asterisco_senha.setFont(font2)
        self.asterisco_senha.setStyleSheet("color: rgb(255, 100, 100);")

        # Campo Confirmação de Senha
        self.txt_confrimar_senha = QLabel("Confirmar Senha:", self.frame)
        self.txt_confrimar_senha.setGeometry(QRect(50, 500, 150, 20))
        self.txt_confrimar_senha.setFont(font2)
        self.txt_confrimar_senha.setStyleSheet("color: rgb(200, 200, 200);")
        self.line_Confirmar_senha = QLineEdit(self.frame)
        self.line_Confirmar_senha.setGeometry(QRect(50, 520, 400, 40))
        self.line_Confirmar_senha.setEchoMode(QLineEdit.Password)
        self.line_Confirmar_senha.setStyleSheet("""
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
        self.asterisco_conf_senha = QLabel("*", self.frame)
        self.asterisco_conf_senha.setGeometry(QRect(200, 500, 10, 20))
        self.asterisco_conf_senha.setFont(font2)
        self.asterisco_conf_senha.setStyleSheet("color: rgb(255, 100, 100);")

        # Botão Cadastrar
        self.pushButton_Cadastrar = QPushButton("Cadastrar", self.frame)
        self.pushButton_Cadastrar.setGeometry(QRect(350, 570, 100, 40))
        font3 = QFont("Segoe UI", 12, QFont.Bold)
        self.pushButton_Cadastrar.setFont(font3)
        self.pushButton_Cadastrar.setStyleSheet("""
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
        self.pushButton_Cadastrar.setCursor(Qt.PointingHandCursor)
        self.pushButton_Cadastrar.clicked.connect(lambda: self.realizar_cadastro(Tela_Cadastro))

        # Botão Voltar
        self.pushButton_Voltar = QPushButton("Voltar", self.frame)
        self.pushButton_Voltar.setGeometry(QRect(240, 570, 100, 40))
        self.pushButton_Voltar.setFont(font3)
        self.pushButton_Voltar.setStyleSheet("""
            QPushButton {
                color: rgb(255, 255, 255);
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(255, 100, 100),
                    stop: 1 rgb(200, 70, 70)
                );
                border-radius: 8px;
                padding: 5px;
            }
            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(255, 120, 120),
                    stop: 1 rgb(220, 90, 90)
                );
            }
            QPushButton:pressed {
                background: rgb(180, 50, 50);
            }
        """)
        self.pushButton_Voltar.setCursor(Qt.PointingHandCursor)
        self.pushButton_Voltar.clicked.connect(lambda: self.voltar_para_login(Tela_Cadastro))

        # Link Entrar
        self.txt_jtemconta = QLabel("Já tem conta?", self.frame)
        self.txt_jtemconta.setGeometry(QRect(180, 620, 100, 20))
        self.txt_jtemconta.setFont(font2)
        self.txt_jtemconta.setStyleSheet("color: rgb(200, 200, 200);")
        self.link_entrar = QLabel("<a href='#'>Entrar</a>", self.frame)
        self.link_entrar.setGeometry(QRect(280, 620, 100, 20))
        self.link_entrar.setFont(font2)
        self.link_entrar.setStyleSheet("""
            color: rgb(220, 220, 255);
            text-decoration: underline;
            background-color: transparent;
        """)
        self.link_entrar.mousePressEvent = lambda event: self.abrir_tela_login(Tela_Cadastro)

        self.retranslateUi(Tela_Cadastro)
        QMetaObject.connectSlotsByName(Tela_Cadastro)

    def retranslateUi(self, Tela_Cadastro):
        Tela_Cadastro.setWindowTitle("Cadastro de Usuário")
        self.txt_Criar_Conta.setText("Crie sua conta")
        self.txt_jtemconta.setText("Já tem conta?")
        self.link_entrar.setText("Entrar")
        self.txt_nome.setText("Nome:")
        self.txt_email.setText("Email:")
        self.txt_contato.setText("Contato:")
        self.txt_senha.setText("Senha:")
        self.txt_confrimar_senha.setText("Confirmar Senha:")
        self.pushButton_Cadastrar.setText("Cadastrar")
        self.pushButton_Voltar.setText("Voltar")

    def selecionar_foto(self):
        arquivo, _ = QFileDialog.getOpenFileName(self.frame, "Selecionar Foto", "", "Imagens (*.png *.jpg *.jpeg)")
        if arquivo:
            pixmap = QPixmap(arquivo)
            self.label_foto.setPixmap(pixmap)
            with open(arquivo, "rb") as f:
                self.foto_data = f.read()

    def abrir_tela_login(self, Tela_Cadastro):
        from Tela_Login import TelaLogin
        self.tela_login = TelaLogin()
        self.tela_login.show()
        Tela_Cadastro.close()  # Fecha a tela de cadastro

    def voltar_para_login(self, Tela_Cadastro):
        self.abrir_tela_login(Tela_Cadastro)

    def realizar_cadastro(self, Tela_Cadastro):
        nome = self.line_nome.text()
        email = self.line_email.text()
        contato = self.line_contato.text()
        senha = self.line_senha.text()
        confirmar_senha = self.line_Confirmar_senha.text()

        self.limpar_bordas()

        if senha != confirmar_senha:
            QMessageBox.warning(None, "Erro", "As senhas não coincidem.")
        elif nome == "" or email == "" or senha == "":
            QMessageBox.warning(None, "Erro", "Preencha todos os campos obrigatórios.")
            self.validar_campos_vazios(nome, email, contato, senha, confirmar_senha)
        else:
            if salvar_usuario(nome, email, contato, senha, self.foto_data):
                QMessageBox.information(None, "Sucesso", "Cadastro realizado com sucesso!")
                self.voltar_para_login(Tela_Cadastro)
            else:
                QMessageBox.warning(None, "Erro", "Erro ao cadastrar! Verifique os dados.")

    def limpar_bordas(self):
        self.line_nome.setStyleSheet("""
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
        self.line_contato.setStyleSheet("""
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
        self.line_Confirmar_senha.setStyleSheet("""
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

    def validar_campos_vazios(self, nome, email, contato, senha, confirmar_senha):
        if nome == "":
            self.line_nome.setStyleSheet("""
                QLineEdit {
                    background-color: rgb(40, 40, 50);
                    color: rgb(255, 255, 255);
                    border: 1px solid rgb(255, 100, 100);
                    border-radius: 5px;
                    padding: 5px;
                    font-family: Segoe UI;
                    font-size: 12pt;
                }
                QLineEdit:focus {
                    border: 1px solid rgb(100, 150, 255);
                }
            """)
        if email == "":
            self.line_email.setStyleSheet("""
                QLineEdit {
                    background-color: rgb(40, 40, 50);
                    color: rgb(255, 255, 255);
                    border: 1px solid rgb(255, 100, 100);
                    border-radius: 5px;
                    padding: 5px;
                    font-family: Segoe UI;
                    font-size: 12pt;
                }
                QLineEdit:focus {
                    border: 1px solid rgb(100, 150, 255);
                }
            """)
        if contato == "":
            self.line_contato.setStyleSheet("""
                QLineEdit {
                    background-color: rgb(40, 40, 50);
                    color: rgb(255, 255, 255);
                    border: 1px solid rgb(255, 100, 100);
                    border-radius: 5px;
                    padding: 5px;
                    font-family: Segoe UI;
                    font-size: 12pt;
                }
                QLineEdit:focus {
                    border: 1px solid rgb(100, 150, 255);
                }
            """)
        if senha == "":
            self.line_senha.setStyleSheet("""
                QLineEdit {
                    background-color: rgb(40, 40, 50);
                    color: rgb(255, 255, 255);
                    border: 1px solid rgb(255, 100, 100);
                    border-radius: 5px;
                    padding: 5px;
                    font-family: Segoe UI;
                    font-size: 12pt;
                }
                QLineEdit:focus {
                    border: 1px solid rgb(100, 150, 255);
                }
            """)
        if confirmar_senha == "":
            self.line_Confirmar_senha.setStyleSheet("""
                QLineEdit {
                    background-color: rgb(40, 40, 50);
                    color: rgb(255, 255, 255);
                    border: 1px solid rgb(255, 100, 100);
                    border-radius: 5px;
                    padding: 5px;
                    font-family: Segoe UI;
                    font-size: 12pt;
                }
                QLineEdit:focus {
                    border: 1px solid rgb(100, 150, 255);
                }
            """)

if __name__ == "__main__":
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = Ui_Tela_Cadastro()
    ui.setupUi(MainWindow)
    MainWindow.show()
    app.exec()