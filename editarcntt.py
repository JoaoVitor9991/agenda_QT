from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (QMainWindow, QWidget, QFrame, QLabel, QLineEdit, QPushButton, 
                               QTextEdit, QMessageBox, QScrollArea, QVBoxLayout, QHBoxLayout)
from bancodedados import atualizar_contato, deletar_contato
from datetime import datetime

class Ui_Form(object):
    def setupUi(self, tela_editar_contato, contato_info, tela_contatos):
        self.tela_editar_contato = tela_editar_contato
        self.contato_info = contato_info
        self.tela_contatos = tela_contatos

        tela_editar_contato.setObjectName("tela_editar_contato")
        tela_editar_contato.resize(800, 600)
        tela_editar_contato.setWindowTitle("Agenda de Contatos")
        tela_editar_contato.setWindowIcon(QIcon("agenda.png"))
        self.centralwidget = QWidget(tela_editar_contato)
        self.centralwidget.setStyleSheet("""
            background: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 rgb(20, 20, 30),
                stop: 1 rgb(50, 60, 80)
            );
        """)
        tela_editar_contato.setCentralWidget(self.centralwidget)

        self.main_layout = QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        self.frame = QFrame()
        self.frame.setStyleSheet("""
            background-color: rgb(40, 40, 50);
            border-radius: 10px;
        """)
        self.main_layout.addWidget(self.frame)

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

        self.scroll_layout = QVBoxLayout(self.frame)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_layout.addWidget(self.scroll_area)

        self.scroll_widget = QWidget()
        self.scroll_widget_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_widget_layout.setAlignment(Qt.AlignTop)
        self.scroll_widget_layout.setSpacing(10)
        self.scroll_widget_layout.setContentsMargins(20, 20, 20, 20)
        self.scroll_area.setWidget(self.scroll_widget)

        self.txt_editar_contato = QLabel("Editar Contato")
        font1 = QFont("Segoe UI", 18, QFont.Bold)
        self.txt_editar_contato.setFont(font1)
        self.txt_editar_contato.setStyleSheet("color: rgb(220, 220, 255); background-color: transparent;")
        self.txt_editar_contato.setAlignment(Qt.AlignCenter)
        self.scroll_widget_layout.addWidget(self.txt_editar_contato)

        font2 = QFont("Segoe UI", 12)

        self.txt_nome = QLabel("Nome:")
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

        self.txt_email = QLabel("Email:")
        self.txt_email.setFont(font2)
        self.txt_email.setStyleSheet("color: rgb(200, 200, 200);")
        self.scroll_widget_layout.addWidget(self.txt_email)

        self.line_email = QLineEdit()
        self.line_email.setFixedHeight(40)
        self.line_email.setText(contato_info["email"])
        self.line_email.setStyleSheet(self.line_nome.styleSheet())
        self.scroll_widget_layout.addWidget(self.line_email)

        self.txt_telefone = QLabel("Telefone:")
        self.txt_telefone.setFont(font2)
        self.txt_telefone.setStyleSheet("color: rgb(200, 200, 200);")
        self.scroll_widget_layout.addWidget(self.txt_telefone)

        self.line_telefone = QLineEdit()
        self.line_telefone.setFixedHeight(40)
        self.line_telefone.setInputMask("(99) 99999-9999")
        self.line_telefone.setText(contato_info["telefone"])
        self.line_telefone.setStyleSheet(self.line_nome.styleSheet())
        self.scroll_widget_layout.addWidget(self.line_telefone)

        self.txt_data_nascimento = QLabel("Data de Nascimento (dd/mm/aaaa):")
        self.txt_data_nascimento.setFont(font2)
        self.txt_data_nascimento.setStyleSheet("color: rgb(200, 200, 200);")
        self.scroll_widget_layout.addWidget(self.txt_data_nascimento)

        self.line_data_nascimento = QLineEdit()
        self.line_data_nascimento.setFixedHeight(40)
        self.line_data_nascimento.setInputMask("99/99/9999")
        self.line_data_nascimento.setPlaceholderText("Ex: 02/04/1990")
        data_nascimento = contato_info.get("data_nascimento", "")
        if data_nascimento:
            try:
                data = datetime.strptime(data_nascimento, "%Y-%m-%d")
                self.line_data_nascimento.setText(data.strftime("%d/%m/%Y"))
            except ValueError:
                self.line_data_nascimento.setText("")
        self.line_data_nascimento.setStyleSheet("""
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
        self.scroll_widget_layout.addWidget(self.line_data_nascimento)

        self.txt_rede_social = QLabel("Rede Social:")
        self.txt_rede_social.setFont(font2)
        self.txt_rede_social.setStyleSheet("color: rgb(200, 200, 200);")
        self.scroll_widget_layout.addWidget(self.txt_rede_social)

        self.line_rede_social = QLineEdit()
        self.line_rede_social.setFixedHeight(40)
        self.line_rede_social.setText(contato_info["rede_social"])
        self.line_rede_social.setStyleSheet(self.line_nome.styleSheet())
        self.scroll_widget_layout.addWidget(self.line_rede_social)

        self.txt_notas = QLabel("Notas:")
        self.txt_notas.setFont(font2)
        self.txt_notas.setStyleSheet("color: rgb(200, 200, 200);")
        self.scroll_widget_layout.addWidget(self.txt_notas)

        self.line_notas = QTextEdit()
        self.line_notas.setFixedHeight(80)
        self.line_notas.setText(contato_info["notas"])
        self.line_notas.setStyleSheet(self.line_nome.styleSheet().replace("QLineEdit", "QTextEdit"))
        self.scroll_widget_layout.addWidget(self.line_notas)

        self.button_layout = QHBoxLayout()
        self.button_layout.setAlignment(Qt.AlignRight)
        self.button_layout.setSpacing(10)

        font3 = QFont("Segoe UI", 12, QFont.Bold)

        self.pushButton_deletar = QPushButton("Deletar")
        self.pushButton_deletar.setFixedSize(100, 40)
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
        self.pushButton_salvar.setStyleSheet(self.pushButton_deletar.styleSheet().replace("255, 100, 100", "100, 150, 255").replace("200, 70, 70", "70, 100, 200"))
        self.pushButton_salvar.setCursor(Qt.PointingHandCursor)
        self.pushButton_salvar.clicked.connect(self.salvar_contato)
        self.button_layout.addWidget(self.pushButton_salvar)

        self.scroll_widget_layout.addLayout(self.button_layout)
        self.scroll_widget_layout.addSpacing(20)

    def show_custom_message(self, title, text, icon=QMessageBox.Information, buttons=QMessageBox.Ok):
        msg = QMessageBox(self.tela_editar_contato)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(icon)
        msg.setStandardButtons(buttons)
        msg.setStyleSheet("""
            QMessageBox {
                background-color: rgb(245, 245, 250);
                border: 1px solid rgb(200, 200, 210);
                border-radius: 8px;
                color: rgb(50, 50, 60);
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QMessageBox QLabel {
                color: rgb(50, 50, 60);
                padding: 5px;
            }
            QMessageBox QPushButton {
                background-color: rgb(100, 150, 255);
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 15px;
                min-width: 80px;
                font-family: Segoe UI;
                font-size: 10pt;
                font-weight: bold;
            }
            QMessageBox QPushButton:hover {
                background-color: rgb(120, 170, 255);
            }
            QMessageBox QPushButton:pressed {
                background-color: rgb(80, 130, 220);
            }
        """)
        # Ajustar a cor da barra superior dependendo do tipo de mensagem
        if icon == QMessageBox.Warning:
            msg.setStyleSheet(msg.styleSheet() + "QMessageBox { border-top: 4px solid rgb(255, 120, 120); }")
        elif icon == QMessageBox.Information:
            msg.setStyleSheet(msg.styleSheet() + "QMessageBox { border-top: 4px solid rgb(100, 150, 255); }")
        elif icon == QMessageBox.Question:
            msg.setStyleSheet(msg.styleSheet() + "QMessageBox { border-top: 4px solid rgb(255, 220, 100); }")
        return msg.exec()

    def salvar_contato(self):
        nome = self.line_nome.text()
        email = self.line_email.text()
        telefone = self.line_telefone.text()
        data_nascimento_str = self.line_data_nascimento.text()
        perfil_rede_social = self.line_rede_social.text()
        notas = self.line_notas.toPlainText()

        if nome == "":
            self.show_custom_message("Erro", "O campo Nome é obrigatório.", QMessageBox.Warning)
            self.line_nome.setStyleSheet(self.line_nome.styleSheet().replace("rgb(80, 80, 100)", "rgb(255, 100, 100)"))
            return

        # Converter a data para o formato "yyyy-MM-dd" ou None se estiver vazia/inválida
        data_nascimento_formatada = None
        if data_nascimento_str and data_nascimento_str != "__/__/____":
            try:
                data_nasc = datetime.strptime(data_nascimento_str, "%d/%m/%Y")
                data_nascimento_formatada = data_nasc.strftime("%Y-%m-%d")
            except ValueError:
                self.show_custom_message("Erro", "Data de nascimento inválida. Use o formato dd/mm/aaaa.", QMessageBox.Warning)
                return

        if atualizar_contato(self.contato_info["id"], nome, email, telefone, data_nascimento_formatada, perfil_rede_social, notas, None):
            self.show_custom_message("Sucesso", "Contato atualizado com sucesso!", QMessageBox.Information)
            self.tela_contatos.carregar_contatos()
            self.tela_editar_contato.close()
        else:
            self.show_custom_message("Erro", "Erro ao atualizar contato. Tente novamente.", QMessageBox.Warning)

    def deletar_contato(self):
        resposta = self.show_custom_message("Confirmação", "Tem certeza que deseja deletar este contato?",
                                            QMessageBox.Question, QMessageBox.Yes | QMessageBox.No)
        if resposta == QMessageBox.Yes:
            if deletar_contato(self.contato_info["id"]):
                self.show_custom_message("Sucesso", "Contato deletado com sucesso!", QMessageBox.Information)
                self.tela_contatos.carregar_contatos()
                self.tela_editar_contato.close()
            else:
                self.show_custom_message("Erro", "Erro ao deletar contato. Tente novamente.", QMessageBox.Warning)