from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QFont, QPixmap, QIcon
from PySide6.QtWidgets import (QMainWindow, QWidget, QFrame, QLabel, QLineEdit, QPushButton, 
                               QDateEdit, QTextEdit, QMessageBox, QScrollArea, QVBoxLayout, 
                               QHBoxLayout, QFileDialog)
from bancodedados import salvar_contato

class Ui_tela_add_contato(object):
    def __init__(self):
        self.usuario_id = None
        self.foto_data = None  # Para armazenar os dados da foto

    def setupUi(self, tela_add_contato, tela_contatos):
        self.tela_add_contato = tela_add_contato
        self.tela_contatos = tela_contatos

        tela_add_contato.setObjectName("tela_add_contato")
        tela_add_contato.resize(800, 600)
        tela_add_contato.setWindowTitle("Agenda de Contatos")
        tela_add_contato.setWindowIcon(QIcon("icone.ico"))
        self.centralwidget = QWidget(tela_add_contato)
        self.centralwidget.setStyleSheet("""
            background: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 rgb(20, 20, 30),
                stop: 1 rgb(50, 60, 80)
            );
        """)
        tela_add_contato.setCentralWidget(self.centralwidget)

        # Layout principal (vertical)
        self.main_layout = QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        # Frame principal
        self.frame = QFrame()
        self.frame.setStyleSheet("""
            background-color: rgb(40, 40, 50);
            border-radius: 10px;
        """)
        self.main_layout.addWidget(self.frame)

        # Adicionar uma QScrollArea para permitir rolagem
        self.scroll_area = QScrollArea(self.frame)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                background-color: rgb(40, 40, 50);
                border: none;
                border-radius: 10px;
            }
            QScrollBar:vertical {
                border: none;
                background: rgb(80, 80, 100);
                width: 10px;
                margin: 0px 0px 0px 0px;
                border-radius: 5px;
            }
            QScrollBar::handle:vertical {
                background: rgb(100, 150, 255);
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)

        # Layout para o QScrollArea
        self.scroll_layout = QVBoxLayout(self.frame)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_layout.addWidget(self.scroll_area)

        # Widget interno para o conteúdo rolável
        self.scroll_widget = QWidget()
        self.scroll_widget_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_widget_layout.setAlignment(Qt.AlignTop)
        self.scroll_widget_layout.setSpacing(10)
        self.scroll_widget_layout.setContentsMargins(20, 20, 20, 20)
        self.scroll_area.setWidget(self.scroll_widget)

        # Título "Adicionar Contato"
        self.txt_add_contato = QLabel("Adicionar Contato")
        font1 = QFont("Segoe UI", 18, QFont.Bold)
        self.txt_add_contato.setFont(font1)
        self.txt_add_contato.setStyleSheet("""
            color: rgb(220, 220, 255);
            background-color: transparent;
        """)
        self.txt_add_contato.setAlignment(Qt.AlignCenter)
        self.scroll_widget_layout.addWidget(self.txt_add_contato)

        # Campo Nome
        self.txt_nome = QLabel("Nome:")
        font2 = QFont("Segoe UI", 12)
        self.txt_nome.setFont(font2)
        self.txt_nome.setStyleSheet("color: rgb(200, 200, 200);")
        self.scroll_widget_layout.addWidget(self.txt_nome)

        self.line_nome = QLineEdit()
        self.line_nome.setFixedHeight(40)
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
        self.scroll_widget_layout.addWidget(self.line_nome)

        self.asterisco_nome = QLabel("*")
        self.asterisco_nome.setFont(font2)
        self.asterisco_nome.setStyleSheet("color: rgb(255, 100, 100);")
        self.scroll_widget_layout.addWidget(self.asterisco_nome)

        # Campo Email
        self.txt_email = QLabel("Email:")
        self.txt_email.setFont(font2)
        self.txt_email.setStyleSheet("color: rgb(200, 200, 200);")
        self.scroll_widget_layout.addWidget(self.txt_email)

        self.line_email = QLineEdit()
        self.line_email.setFixedHeight(40)
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
        self.scroll_widget_layout.addWidget(self.line_email)

        # Campo Telefone
        self.txt_telefone = QLabel("Telefone:")
        self.txt_telefone.setFont(font2)
        self.txt_telefone.setStyleSheet("color: rgb(200, 200, 200);")
        self.scroll_widget_layout.addWidget(self.txt_telefone)

        self.line_telefone = QLineEdit()
        self.line_telefone.setFixedHeight(40)
        self.line_telefone.setInputMask("(99) 99999-9999")
        self.line_telefone.setStyleSheet("""
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
        self.scroll_widget_layout.addWidget(self.line_telefone)

        # Campo Data de Nascimento
        self.txt_data_nascimento = QLabel("Data de Nascimento:")
        self.txt_data_nascimento.setFont(font2)
        self.txt_data_nascimento.setStyleSheet("color: rgb(200, 200, 200);")
        self.scroll_widget_layout.addWidget(self.txt_data_nascimento)

        self.date_nascimento = QDateEdit()
        self.date_nascimento.setFixedHeight(40)
        self.date_nascimento.setCalendarPopup(True)
        self.date_nascimento.setMinimumDate(QDate(1900, 1, 1))
        self.date_nascimento.setSpecialValueText("Sem data")
        self.date_nascimento.setMinimumDate(QDate(1, 1, 1))
        self.date_nascimento.setDate(QDate(1, 1, 1))
        self.date_nascimento.setStyleSheet("""
            QDateEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QDateEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)
        self.scroll_widget_layout.addWidget(self.date_nascimento)

        # Campo Rede Social
        self.txt_rede_social = QLabel("Rede Social:")
        self.txt_rede_social.setFont(font2)
        self.txt_rede_social.setStyleSheet("color: rgb(200, 200, 200);")
        self.scroll_widget_layout.addWidget(self.txt_rede_social)

        self.line_rede_social = QLineEdit()
        self.line_rede_social.setFixedHeight(40)
        self.line_rede_social.setStyleSheet("""
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
        self.scroll_widget_layout.addWidget(self.line_rede_social)

        # Campo Notas
        self.txt_notas = QLabel("Notas:")
        self.txt_notas.setFont(font2)
        self.txt_notas.setStyleSheet("color: rgb(200, 200, 200);")
        self.scroll_widget_layout.addWidget(self.txt_notas)

        self.line_notas = QTextEdit()
        self.line_notas.setFixedHeight(80)
        self.line_notas.setStyleSheet("""
            QTextEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QTextEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)
        self.scroll_widget_layout.addWidget(self.line_notas)

        # Campo para a foto do contato
        self.txt_foto = QLabel("Foto do Contato:")
        self.txt_foto.setFont(font2)
        self.txt_foto.setStyleSheet("color: rgb(200, 200, 200);")
        self.scroll_widget_layout.addWidget(self.txt_foto)

        self.label_foto_contato = QLabel()
        self.label_foto_contato.setFixedSize(100, 100)
        self.label_foto_contato.setStyleSheet("""
            border: 1px solid rgb(80, 80, 100);
            border-radius: 50px;
            background-color: rgb(40, 40, 50);
        """)
        self.label_foto_contato.setAlignment(Qt.AlignCenter)
        self.label_foto_contato.setScaledContents(True)
        self.label_foto_contato.setText("Sem Foto")
        self.scroll_widget_layout.addWidget(self.label_foto_contato)

        self.btn_selecionar_foto = QPushButton("Selecionar Foto")
        self.btn_selecionar_foto.setFixedSize(120, 30)
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
        self.scroll_widget_layout.addWidget(self.btn_selecionar_foto)

        # Botões Salvar e Voltar
        self.button_layout = QHBoxLayout()
        self.button_layout.setAlignment(Qt.AlignRight)
        self.button_layout.setSpacing(10)

        self.pushButton_voltar = QPushButton("Voltar")
        self.pushButton_voltar.setFixedSize(100, 40)
        font3 = QFont("Segoe UI", 12, QFont.Bold)
        self.pushButton_voltar.setFont(font3)
        self.pushButton_voltar.setStyleSheet("""
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
        self.pushButton_voltar.setCursor(Qt.PointingHandCursor)
        self.pushButton_voltar.clicked.connect(lambda: self.tela_add_contato.close())
        self.button_layout.addWidget(self.pushButton_voltar)

        self.pushButton_salvar = QPushButton("Salvar")
        self.pushButton_salvar.setFixedSize(100, 40)
        self.pushButton_salvar.setFont(font3)
        self.pushButton_salvar.setStyleSheet("""
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
        self.pushButton_salvar.setCursor(Qt.PointingHandCursor)
        self.pushButton_salvar.clicked.connect(self.salvar_contato)
        self.button_layout.addWidget(self.pushButton_salvar)

        self.scroll_widget_layout.addLayout(self.button_layout)

        # Adicionar um espaço extra no final
        self.scroll_widget_layout.addSpacing(20)

    def selecionar_foto(self):
        arquivo, _ = QFileDialog.getOpenFileName(self.centralwidget, "Selecionar Foto", "", "Imagens (*.png *.jpg *.jpeg)")
        if arquivo:
            # Carregar a nova foto na interface
            pixmap = QPixmap(arquivo)
            self.label_foto_contato.setPixmap(pixmap)

            # Ler os dados da nova foto
            with open(arquivo, "rb") as f:
                self.foto_data = f.read()

    def salvar_contato(self):
        nome = self.line_nome.text()
        email = self.line_email.text()
        telefone = self.line_telefone.text()
        data_nascimento = self.date_nascimento.date()
        data_nascimento_str = None if data_nascimento == QDate(1, 1, 1) else data_nascimento.toString("yyyy-MM-dd")
        perfil_rede_social = self.line_rede_social.text()
        notas = self.line_notas.toPlainText()

        if nome == "":
            QMessageBox.warning(None, "Erro", "O campo Nome é obrigatório.")
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
            return

        if salvar_contato(nome, email, telefone, data_nascimento_str, perfil_rede_social, notas, self.usuario_id, self.foto_data):
            QMessageBox.information(None, "Sucesso", "Contato salvo com sucesso!")
            self.tela_contatos.carregar_contatos()  # Atualiza a lista de contatos
            self.tela_add_contato.close()  # Fecha a janela após salvar
        else:
            QMessageBox.warning(None, "Erro", "Erro ao salvar contato. Tente novamente.")