import sys
from PySide6.QtCore import QMetaObject, Qt
from PySide6.QtGui import QPixmap, QFont,QIcon
from PySide6.QtWidgets import (QFrame, QLabel, QLineEdit, QMainWindow, QVBoxLayout, 
                               QHBoxLayout, QWidget, QScrollArea, QMessageBox, QPushButton, 
                               QFileDialog, QApplication)
from add_cntt import Ui_tela_add_contato
from editarcntt import Ui_Form as Ui_EditarContato
from bancodedados import obter_contatos, obter_foto_usuario, atualizar_foto_usuario
from datetime import datetime

class Ui_Form(object):
    def __init__(self, usuario_id):
        self.usuario_id = usuario_id

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(988, 579)

        # Widget central com gradiente escuro
        self.centralwidget = QWidget(Form)
        self.centralwidget.setStyleSheet("""
            background: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 rgb(20, 20, 30),
                stop: 1 rgb(50, 60, 80)
            );
        """)
        Form.setCentralWidget(self.centralwidget)

        # Layout principal (vertical)
        self.main_layout = QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(10)

        # Foto de perfil e botão "Trocar Foto" (layout horizontal)
        self.foto_layout = QHBoxLayout()
        self.foto_layout.setAlignment(Qt.AlignCenter)

        self.label_foto = QLabel()
        self.label_foto.setFixedSize(100, 100)
        self.label_foto.setStyleSheet("""
            border: 1px solid rgb(80, 80, 100);
            border-radius: 50px;
            background-color: rgb(40, 40, 50);
        """)
        self.label_foto.setAlignment(Qt.AlignCenter)
        self.label_foto.setScaledContents(True)

        # Carregar foto do banco
        foto_data = obter_foto_usuario(self.usuario_id)
        if foto_data:
            pixmap = QPixmap()
            pixmap.loadFromData(foto_data)
            self.label_foto.setPixmap(pixmap)
        else:
            self.label_foto.setText("Sem Foto")

        self.foto_layout.addWidget(self.label_foto)

        self.btn_trocar_foto = QPushButton("Trocar Foto")
        self.btn_trocar_foto.setFixedSize(100, 30)
        self.btn_trocar_foto.setFont(QFont("Segoe UI", 10, QFont.Bold))
        self.btn_trocar_foto.setStyleSheet("""
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
        self.btn_trocar_foto.setCursor(Qt.PointingHandCursor)
        self.btn_trocar_foto.clicked.connect(self.trocar_foto)
        self.foto_layout.addWidget(self.btn_trocar_foto)

        self.main_layout.addLayout(self.foto_layout)

        # Área de scroll para contatos
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                background-color: rgb(40, 40, 50);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
            }
        """)

        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setAlignment(Qt.AlignTop)
        self.scroll_area.setWidget(self.scroll_widget)

        # Título "Contatos"
        self.label_Cntt = QLabel("Contatos")
        font_title = QFont("Segoe UI", 14, QFont.Bold)
        self.label_Cntt.setFont(font_title)
        self.label_Cntt.setStyleSheet("""
            color: rgb(220, 220, 255);
            background-color: transparent;
            padding: 5px;
        """)
        self.scroll_layout.addWidget(self.label_Cntt)

        # Campo de busca
        self.line_buscar_cntt = QLineEdit()
        self.line_buscar_cntt.setPlaceholderText("Buscar Contatos...")
        self.line_buscar_cntt.setStyleSheet("""
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
        self.scroll_layout.addWidget(self.line_buscar_cntt)

        # Ícone de adicionar
        self.label_add = QLabel()
        self.label_add.setPixmap(QPixmap("xx.png"))
        self.label_add.setScaledContents(True)
        self.label_add.setFixedSize(32, 32)
        self.label_add.setStyleSheet("""
            background-color: transparent;
        """)
        self.label_add.mousePressEvent = self.adicionar_contato
        self.scroll_layout.addWidget(self.label_add)

        self.main_layout.addWidget(self.scroll_area)

        self.contatos = []
        self.labels_contatos = []
        self.labels_editar = []
        self.lines = []

        self.line_buscar_cntt.textChanged.connect(self.filtrar_contatos)
        self.carregar_contatos()  # Carrega os contatos
        QMetaObject.connectSlotsByName(Form)

    def trocar_foto(self):
        arquivo, _ = QFileDialog.getOpenFileName(self.centralwidget, "Selecionar Foto", "", "Imagens (*.png *.jpg *.jpeg)")
        if arquivo:
            # Carregar a nova foto na interface
            pixmap = QPixmap(arquivo)
            self.label_foto.setPixmap(pixmap)

            # Ler os dados da nova foto
            with open(arquivo, "rb") as f:
                foto_data = f.read()

            # Atualizar a foto no banco de dados
            if atualizar_foto_usuario(self.usuario_id, foto_data):
                QMessageBox.information(None, "Sucesso", "Foto atualizada com sucesso!")
            else:
                QMessageBox.warning(None, "Erro", "Erro ao atualizar a foto. Tente novamente.")

    def verificar_aniversarios(self):
        hoje = datetime.now()
        dia_atual = hoje.day
        mes_atual = hoje.month

        aniversariantes = []
        for contato in self.contatos:
            data_nascimento = contato.get("data_nascimento")
            if data_nascimento:  # Verifica se a data existe
                if data_nascimento.day == dia_atual and data_nascimento.month == mes_atual:
                    aniversariantes.append(contato["nome"])

        if aniversariantes:
            mensagem = "Hoje é aniversário de:\n" + "\n".join(aniversariantes)
            QMessageBox.information(None, "Aniversários", mensagem)

    def filtrar_contatos(self):
        texto_busca = self.line_buscar_cntt.text().lower()
        for i, label in enumerate(self.labels_contatos):
            visivel = texto_busca in label.text().lower()
            label.setVisible(visivel)
            if i < len(self.labels_editar):
                self.labels_editar[i].setVisible(visivel)
            if i < len(self.lines):
                self.lines[i].setVisible(visivel)
        self.scroll_widget.adjustSize()
        self.scroll_area.update()

    def adicionar_contato(self, event):
        self.tela_add_contato = QMainWindow()
        self.ui_add_contato = Ui_tela_add_contato()
        self.ui_add_contato.usuario_id = self.usuario_id
        self.ui_add_contato.setupUi(self.tela_add_contato, self)
        self.tela_add_contato.destroyed.connect(self.carregar_contatos)
        self.tela_add_contato.show()
        event.accept()

    def carregar_contatos(self):
        self.contatos = obter_contatos(self.usuario_id)

        for label in self.labels_contatos:
            label.deleteLater()
        for line in self.lines:
            line.deleteLater()
        for label_editar in self.labels_editar:
            label_editar.deleteLater()

        self.labels_contatos.clear()
        self.lines.clear()
        self.labels_editar.clear()

        for i, contato in enumerate(self.contatos):
            nome = contato.get("nome", "Sem Nome")
            telefone = str(contato.get("telefone", "Sem Telefone"))

            # Layout para cada contato (foto + nome/telefone + botão editar)
            contato_layout = QHBoxLayout()
            contato_layout.setAlignment(Qt.AlignLeft)
            contato_layout.setSpacing(10)

            # Foto do contato
            label_foto_contato = QLabel()
            label_foto_contato.setFixedSize(40, 40)
            label_foto_contato.setStyleSheet("""
                border: 1px solid rgb(80, 80, 100);
                border-radius: 20px;
                background-color: rgb(40, 40, 50);
            """)
            label_foto_contato.setAlignment(Qt.AlignCenter)
            label_foto_contato.setScaledContents(True)

            # Carregar a foto do contato (se existir)
            foto_data = contato.get("foto")
            if foto_data:
                pixmap = QPixmap()
                pixmap.loadFromData(foto_data)
                label_foto_contato.setPixmap(pixmap)
            else:
                label_foto_contato.setText("Sem Foto")

            contato_layout.addWidget(label_foto_contato)

            # Nome e telefone
            label = QLabel()
            label.setObjectName(f"label_{nome}_{i}")
            label.setText(f"{nome} - {telefone}")
            label.setStyleSheet("""
                color: rgb(255, 255, 255);
                background-color: transparent;
                font-family: Segoe UI;
                font-size: 12pt;
                padding: 5px;
            """)
            contato_layout.addWidget(label)
            self.labels_contatos.append(label)

            # Botão editar
            label_editar = QLabel()
            label_editar.setObjectName(f"label_editar_{i}")
            label_editar.setPixmap(QPixmap("yy.png"))
            label_editar.setScaledContents(True)
            label_editar.setFixedSize(24, 24)
            label_editar.setStyleSheet("""
                background-color: transparent;
            """)
            label_editar.mousePressEvent = lambda event, idx=i: self.editar_contato(idx)
            contato_layout.addWidget(label_editar)
            self.labels_editar.append(label_editar)

            self.scroll_layout.addLayout(contato_layout)

            # Linha separadora
            line = QFrame()
            line.setObjectName(f"line_{nome}_{i}")
            line.setFrameShape(QFrame.HLine)
            line.setStyleSheet("background-color: rgb(80, 80, 100);")
            self.scroll_layout.addWidget(line)
            self.lines.append(line)

        self.verificar_aniversarios()  # Verifica aniversários após carregar os contatos

    def editar_contato(self, i):
        contato = self.contatos[i]
        data_nascimento = contato.get("data_nascimento")
        data_nascimento_str = data_nascimento.strftime("%Y-%m-%d") if data_nascimento else ""
        
        contato_info = {
            "id": contato.get("id"),
            "nome": contato.get("nome", "Sem Nome"),
            "telefone": contato.get("telefone", "Sem Telefone"),
            "email": contato.get("email", "Sem Email"),
            "rede_social": contato.get("perfil_rede_social", "Sem Rede Social"),
            "notas": contato.get("notas", "Sem Notas"),
            "data_nascimento": data_nascimento_str,
            "foto": contato.get("foto")  # Passar a foto para a tela de edição
        }

        self.tela_editar_contato = QMainWindow()
        self.ui_editar_contato = Ui_EditarContato()
        self.ui_editar_contato.setupUi(self.tela_editar_contato, contato_info, self)
        self.tela_editar_contato.destroyed.connect(self.carregar_contatos)
        self.tela_editar_contato.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_Form(1)  # Exemplo com ID 1
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())