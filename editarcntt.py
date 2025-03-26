from PySide6.QtCore import QRect, Qt, QDate
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtWidgets import (QMainWindow, QWidget, QFrame, QLabel, QLineEdit, QPushButton, 
                               QDateEdit, QTextEdit, QMessageBox, QScrollArea, QVBoxLayout, QHBoxLayout, QFileDialog)
from bancodedados import atualizar_contato, deletar_contato

class Ui_Form(object):
    def setupUi(self, tela_editar_contato, contato_info, tela_contatos):
        self.tela_editar_contato = tela_editar_contato
        self.contato_info = contato_info
        self.tela_contatos = tela_contatos
        self.foto_data = contato_info.get("foto")  # Armazenar os dados da foto existente (se houver)

        tela_editar_contato.setObjectName("tela_editar_contato")
        tela_editar_contato.resize(800, 600)

        self.centralwidget = QWidget(tela_editar_contato)
        self.centralwidget.setStyleSheet("""
            background: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 rgb(20, 20, 30),
                stop: 1 rgb(50, 60, 80)
            );
        """)
        tela_editar_contato.setCentralWidget(self.centralwidget)

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

        # Título "Editar Contato"
        self.txt_editar_contato = QLabel("Editar Contato")
        font1 = QFont("Segoe UI", 18, QFont.Bold)
        self.txt_editar_contato.setFont(font1)
        self.txt_editar_contato.setStyleSheet("""
            color: rgb(220, 220, 255);
            background-color: transparent;
        """)
        self.txt_editar_contato.setAlignment(Qt.AlignCenter)
        self.scroll_widget_layout.addWidget(self.txt_editar_contato)

        # Campo Nome
        self.txt_nome = QLabel("Nome:")
        font2 = QFont("Segoe UI", 12)
        self.txt_nome.setFont(font2)
        self.txt_nome.setStyleSheet("color: rgb(200, 200, 200);")
        self.scroll_widget_layout.addWidget(self.txt_nome)

        self.line_nome = QLineEdit()
        self.line_nome.setFixedHeight(40)
        self.line_nome.setText(contato_info["nome"])
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
        self.line_email.setText(contato_info["email"])
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
        self.line_telefone.setText(contato_info["telefone"])
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
        data_nascimento = contato_info.get("data_nascimento", "")
        if data_nascimento:
            try:
                date = QDate.fromString(data_nascimento, "yyyy-MM-dd")
                if date.isValid():
                    self.date_nascimento.setDate(date)
                else:
                    self.date_nascimento.setDate(QDate(1, 1, 1))
            except ValueError as e:
                print(f"Erro ao converter data de nascimento: {data_nascimento}, erro: {e}")
                self.date_nascimento.setDate(QDate(1, 1, 1))
        else:
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
        self.line_rede_social.setText(contato_info["rede_social"])
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
        self.line_notas.setText(contato_info["notas"])
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
        # Carregar a foto existente (se houver)
        if self.foto_data:
            pixmap = QPixmap()
            pixmap.loadFromData(self.foto_data)
            self.label_foto_contato.setPixmap(pixmap)
        else:
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

        # Botões Salvar e Deletar
        self.button_layout = QHBoxLayout()
        self.button_layout.setAlignment(Qt.AlignRight)
        self.button_layout.setSpacing(10)

        self.pushButton_deletar = QPushButton("Deletar")
        self.pushButton_deletar.setFixedSize(100, 40)
        font3 = QFont("Segoe UI", 12, QFont.Bold)
        self.pushButton_deletar.setFont(font3)
        self.pushButton_deletar.setStyleSheet("""
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
        self.pushButton_deletar.setCursor(Qt.PointingHandCursor)
        self.pushButton_deletar.clicked.connect(self.deletar_contato)
        self.button_layout.addWidget(self.pushButton_deletar)

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

        if atualizar_contato(self.contato_info["id"], nome, email, telefone, data_nascimento_str, perfil_rede_social, notas, self.foto_data):
            QMessageBox.information(None, "Sucesso", "Contato atualizado com sucesso!")
            self.tela_contatos.carregar_contatos()
            self.tela_editar_contato.close()
        else:
            QMessageBox.warning(None, "Erro", "Erro ao atualizar contato. Tente novamente.")

    def deletar_contato(self):
        resposta = QMessageBox.question(None, "Confirmação", "Tem certeza que deseja deletar este contato?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if resposta == QMessageBox.Yes:
            if deletar_contato(self.contato_info["id"]):
                QMessageBox.information(None, "Sucesso", "Contato deletado com sucesso!")
                self.tela_contatos.carregar_contatos()
                self.tela_editar_contato.close()
            else:
                QMessageBox.warning(None, "Erro", "Erro ao deletar contato. Tente novamente.")