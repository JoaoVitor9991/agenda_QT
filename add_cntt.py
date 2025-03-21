import sys
from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, QLabel, QLineEdit, QPushButton, QMessageBox, QScrollArea
from bancodedados import salvar_contato

class Ui_tela_add_contato(object):
    def __init__(self):
        self.usuario_id = None

    def setupUi(self, Tela_Add_Contato, tela_contatos):
        self.tela_contatos = tela_contatos
        Tela_Add_Contato.setObjectName("Tela_Add_Contato")
        Tela_Add_Contato.resize(800, 600)

        # Widget central com gradiente
        self.centralwidget = QWidget(Tela_Add_Contato)
        self.centralwidget.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
            stop:0 #ECF0F1, stop:1 #BDC3C7);
        """)
        Tela_Add_Contato.setCentralWidget(self.centralwidget)

        # Área de rolagem
        self.scroll_area = QScrollArea(self.centralwidget)
        self.scroll_area.setGeometry(QRect(0, 0, 800, 600))
        self.scroll_area.setWidgetResizable(True)

        self.scroll_widget = QWidget()
        self.scroll_widget.setMinimumHeight(700)
        self.scroll_area.setWidget(self.scroll_widget)

        # Frame central
        self.frame = QFrame(self.scroll_widget)
        self.frame.setGeometry(QRect(150, 50, 500, 600))
        self.frame.setStyleSheet("background-color: #FFFFFF; border-radius: 10px;")
        font = QFont("Segoe UI", 12)
        self.frame.setFont(font)

        # Título
        self.txt_adicionar_contato = QLabel("Adicionar Contato", self.frame)
        self.txt_adicionar_contato.setGeometry(QRect(0, 20, 500, 40))
        font1 = QFont("Segoe UI", 18, QFont.Bold)
        self.txt_adicionar_contato.setFont(font1)
        self.txt_adicionar_contato.setStyleSheet("color: #2C3E50;")
        self.txt_adicionar_contato.setAlignment(Qt.AlignCenter)

        # Campo Nome
        self.txt_nome = QLabel("Nome:", self.frame)
        self.txt_nome.setGeometry(QRect(50, 80, 100, 20))
        font2 = QFont("Segoe UI", 12)
        self.txt_nome.setFont(font2)
        self.txt_nome.setStyleSheet("color: #34495E;")
        self.line_nome = QLineEdit(self.frame)
        self.line_nome.setGeometry(QRect(50, 100, 400, 40))
        self.line_nome.setStyleSheet("""
            background-color: #FFFFFF;
            border: 1px solid #BDC3C7;
            border-radius: 5px;
            padding: 5px;
            font-family: Segoe UI;
            font-size: 12pt;
        """)

        # Campo Telefone
        self.txt_telefone = QLabel("Telefone:", self.frame)
        self.txt_telefone.setGeometry(QRect(50, 150, 100, 20))
        self.txt_telefone.setFont(font2)
        self.txt_telefone.setStyleSheet("color: #34495E;")
        self.line_telefone = QLineEdit(self.frame)
        self.line_telefone.setGeometry(QRect(50, 170, 400, 40))
        self.line_telefone.setInputMask("(99) 99999-9999")
        self.line_telefone.setStyleSheet("""
            background-color: #FFFFFF;
            border: 1px solid #BDC3C7;
            border-radius: 5px;
            padding: 5px;
            font-family: Segoe UI;
            font-size: 12pt;
        """)

        # Campo Email
        self.txt_email = QLabel("Email:", self.frame)
        self.txt_email.setGeometry(QRect(50, 220, 100, 20))
        self.txt_email.setFont(font2)
        self.txt_email.setStyleSheet("color: #34495E;")
        self.line_email = QLineEdit(self.frame)
        self.line_email.setGeometry(QRect(50, 240, 400, 40))
        self.line_email.setStyleSheet("""
            background-color: #FFFFFF;
            border: 1px solid #BDC3C7;
            border-radius: 5px;
            padding: 5px;
            font-family: Segoe UI;
            font-size: 12pt;
        """)

        # Campo Perfil Rede Social
        self.txt_rede_social = QLabel("Perfil Rede Social:", self.frame)
        self.txt_rede_social.setGeometry(QRect(50, 290, 150, 20))
        self.txt_rede_social.setFont(font2)
        self.txt_rede_social.setStyleSheet("color: #34495E;")
        self.line_rede_social = QLineEdit(self.frame)
        self.line_rede_social.setGeometry(QRect(50, 310, 400, 40))
        self.line_rede_social.setStyleSheet("""
            background-color: #FFFFFF;
            border: 1px solid #BDC3C7;
            border-radius: 5px;
            padding: 5px;
            font-family: Segoe UI;
            font-size: 12pt;
        """)

        # Campo Notas
        self.txt_notas = QLabel("Notas:", self.frame)
        self.txt_notas.setGeometry(QRect(50, 360, 100, 20))
        self.txt_notas.setFont(font2)
        self.txt_notas.setStyleSheet("color: #34495E;")
        self.line_notas = QLineEdit(self.frame)
        self.line_notas.setGeometry(QRect(50, 380, 400, 40))
        self.line_notas.setStyleSheet("""
            background-color: #FFFFFF;
            border: 1px solid #BDC3C7;
            border-radius: 5px;
            padding: 5px;
            font-family: Segoe UI;
            font-size: 12pt;
        """)

        # Campo Data de Nascimento
        self.txt_data_nascimento = QLabel("Data de Nascimento:", self.frame)
        self.txt_data_nascimento.setGeometry(QRect(50, 430, 150, 20))
        self.txt_data_nascimento.setFont(font2)
        self.txt_data_nascimento.setStyleSheet("color: #34495E;")
        self.line_data_nascimento = QLineEdit(self.frame)
        self.line_data_nascimento.setGeometry(QRect(50, 450, 400, 40))
        self.line_data_nascimento.setInputMask("9999-99-99")  # Formato YYYY-MM-DD
        self.line_data_nascimento.setStyleSheet("""
            background-color: #FFFFFF;
            border: 1px solid #BDC3C7;
            border-radius: 5px;
            padding: 5px;
            font-family: Segoe UI;
            font-size: 12pt;
        """)

        # Botão Adicionar
        self.btn_adicionar = QPushButton("Adicionar", self.frame)
        self.btn_adicionar.setGeometry(QRect(350, 510, 100, 40))
        font3 = QFont("Segoe UI", 12, QFont.Bold)
        self.btn_adicionar.setFont(font3)
        self.btn_adicionar.setStyleSheet("""
            background-color: #2C3E50;
            color: white;
            border-radius: 5px;
            padding: 5px;
        """)
        self.btn_adicionar.clicked.connect(self.adicionar_contato)

        # Botão Voltar
        self.btn_voltar = QPushButton("Voltar", self.frame)
        self.btn_voltar.setGeometry(QRect(240, 510, 100, 40))
        self.btn_voltar.setFont(font3)
        self.btn_voltar.setStyleSheet("""
            background-color: #E74C3C;
            color: white;
            border-radius: 5px;
            padding: 5px;
        """)
        self.btn_voltar.clicked.connect(Tela_Add_Contato.close)

    def adicionar_contato(self):
        nome = self.line_nome.text()
        telefone = self.line_telefone.text()
        email = self.line_email.text()
        perfil_rede_social = self.line_rede_social.text()
        notas = self.line_notas.text()
        data_nascimento = self.line_data_nascimento.text() if self.line_data_nascimento.text() != "    -  -  " else None

        if not nome:
            QMessageBox.warning(None, "Erro", "O campo 'Nome' é obrigatório.")
            return

        if salvar_contato(nome, email, telefone, data_nascimento, perfil_rede_social, notas, self.usuario_id):
            QMessageBox.information(None, "Sucesso", "Contato adicionado com sucesso!")
            self.tela_contatos.carregar_contatos()
            self.frame.parent().parent().parent().close()  # Fecha a tela de adicionar
        else:
            QMessageBox.warning(None, "Erro", "Erro ao adicionar contato.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_tela_add_contato()
    ui.usuario_id = 1  # Exemplo, ajust