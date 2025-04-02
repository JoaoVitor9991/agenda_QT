import sys
from PySide6.QtCore import QMetaObject, Qt
from PySide6.QtGui import QPixmap, QFont, QIcon
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
        self.mensagem_aniversario_exibida = False

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(988, 579)
        Form.setWindowTitle("Agenda de Contatos")
        Form.setWindowIcon(QIcon("agenda.png"))
        
        # Widget central com gradiente mais suave
        self.centralwidget = QWidget(Form)
        self.centralwidget.setStyleSheet("""
            background: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 rgb(25, 25, 35),
                stop: 0.5 rgb(45, 55, 75),
                stop: 1 rgb(60, 70, 90)
            );
        """)
        Form.setCentralWidget(self.centralwidget)

        # Layout principal
        self.main_layout = QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(25, 25, 25, 25)
        self.main_layout.setSpacing(15)

        # Foto de perfil e botão
        self.foto_layout = QHBoxLayout()
        self.foto_layout.setAlignment(Qt.AlignCenter)
        self.foto_layout.setSpacing(15)

        self.label_foto = QLabel()
        self.label_foto.setFixedSize(110, 110)
        self.label_foto.setStyleSheet("""
            border: 2px solid rgb(100, 150, 255);
            border-radius: 55px;
            background-color: rgb(35, 35, 45);
            box-shadow: 0px 0px 10px rgba(100, 150, 255, 0.3);
        """)
        self.label_foto.setAlignment(Qt.AlignCenter)
        self.label_foto.setScaledContents(True)

        foto_data = obter_foto_usuario(self.usuario_id)
        if foto_data:
            pixmap = QPixmap()
            pixmap.loadFromData(foto_data)
            self.label_foto.setPixmap(pixmap)
        else:
            self.label_foto.setText("Sem Foto")
            self.label_foto.setStyleSheet(self.label_foto.styleSheet() + "color: rgb(150, 150, 200);")

        self.foto_layout.addWidget(self.label_foto)

        self.btn_trocar_foto = QPushButton("Trocar Foto")
        self.btn_trocar_foto.setFixedSize(120, 35)
        self.btn_trocar_foto.setFont(QFont("Segoe UI", 10, QFont.Bold))
        self.btn_trocar_foto.setStyleSheet("""
            QPushButton {
                color: rgb(255, 255, 255);
                background-color: rgb(100, 150, 255);
                border-radius: 8px;
                padding: 6px;
                border: 1px solid rgb(120, 170, 255);
            }
            QPushButton:hover {
                background-color: rgb(120, 170, 255);
                border: 1px solid rgb(140, 190, 255);
            }
            QPushButton:pressed {
                background-color: rgb(80, 130, 220);
                border: 1px solid rgb(100, 150, 255);
            }
        """)
        self.btn_trocar_foto.setCursor(Qt.PointingHandCursor)
        self.btn_trocar_foto.clicked.connect(self.trocar_foto)
        self.foto_layout.addWidget(self.btn_trocar_foto)

        self.main_layout.addLayout(self.foto_layout)

        # Área de rolagem com design mais elegante
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                background-color: rgb(40, 40, 50);
                border: 1px solid rgb(70, 80, 100);
                border-radius: 10px;
            }
            QScrollBar:vertical {
                border: none;
                background: rgb(50, 60, 80);
                width: 8px;
                margin: 0px;
                border-radius: 4px;
            }
            QScrollBar::handle:vertical {
                background: rgb(100, 150, 255);
                min-height: 20px;
                border-radius: 4px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
        """)

        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setAlignment(Qt.AlignTop)
        self.scroll_layout.setContentsMargins(15, 15, 15, 15)
        self.scroll_layout.setSpacing(10)
        self.scroll_area.setWidget(self.scroll_widget)

        # Título "Contatos" com gradiente
        self.label_Cntt = QLabel("Contatos")
        font_title = QFont("Segoe UI", 16, QFont.Bold)
        self.label_Cntt.setFont(font_title)
        self.label_Cntt.setStyleSheet("""
            color: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 0,
                stop: 0 rgb(220, 220, 255),
                stop: 1 rgb(100, 150, 255)
            );
            background-color: transparent;
            padding: 5px;
        """)
        self.scroll_layout.addWidget(self.label_Cntt)

        # Campo de busca estilizado
        self.line_buscar_cntt = QLineEdit()
        self.line_buscar_cntt.setPlaceholderText("🔍 Buscar Contatos...")
        self.line_buscar_cntt.setFixedHeight(40)
        self.line_buscar_cntt.setStyleSheet("""
            QLineEdit {
                background-color: rgb(35, 35, 45);
                color: rgb(220, 220, 255);
                border: 1px solid rgb(70, 80, 100);
                border-radius: 8px;
                padding: 8px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
                background-color: rgb(40, 40, 55);
            }
        """)
        self.scroll_layout.addWidget(self.line_buscar_cntt)

        # Botão de adicionar contato
        self.label_add = QLabel()
        self.label_add.setPixmap(QPixmap("xx.png"))
        self.label_add.setScaledContents(True)
        self.label_add.setFixedSize(36, 36)
        self.label_add.setStyleSheet("""
            background-color: rgb(100, 150, 255);
            border-radius: 18px;
            padding: 5px;
        """)
        self.label_add.mousePressEvent = self.adicionar_contato
        self.scroll_layout.addWidget(self.label_add, alignment=Qt.AlignRight)

        self.main_layout.addWidget(self.scroll_area)

        self.contatos = []
        self.labels_contatos = []
        self.labels_editar = []
        self.lines = []

        self.line_buscar_cntt.textChanged.connect(self.filtrar_contatos)
        self.carregar_contatos()
        QMetaObject.connectSlotsByName(Form)

    def trocar_foto(self):
        arquivo, _ = QFileDialog.getOpenFileName(self.centralwidget, "Selecionar Foto", "", "Imagens (*.png *.jpg *.jpeg)")
        if arquivo:
            pixmap = QPixmap(arquivo)
            self.label_foto.setPixmap(pixmap)

            with open(arquivo, "rb") as f:
                foto_data = f.read()

            if atualizar_foto_usuario(self.usuario_id, foto_data):
                self.show_custom_message("Sucesso", "Foto atualizada com sucesso!", QMessageBox.Information)
            else:
                self.show_custom_message("Erro", "Erro ao atualizar a foto. Tente novamente.", QMessageBox.Warning)

    def show_custom_message(self, title, text, icon=QMessageBox.Information):
        msg = QMessageBox(self.centralwidget)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(icon)
        msg.setStyleSheet("""
            QMessageBox {
                background-color: rgb(40, 40, 50);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 8px;
                color: rgb(220, 220, 255);
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QMessageBox QLabel {
                color: rgb(220, 220, 255);
                padding: 5px;
            }
            QMessageBox QPushButton {
                background-color: rgb(100, 150, 255);
                color: rgb(255, 255, 255);
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
        msg.exec()

    def exibir_mensagem_aniversario(self, aniversariantes):
        if not aniversariantes or self.mensagem_aniversario_exibida:
            return

        mensagem = "🎉 <b>Hoje é um dia especial!</b> 🎂<br><br>"
        mensagem += "Parabéns a:<br>"
        mensagem += "<br>".join([f"🎈 <b>{nome}</b>" for nome in aniversariantes])
        mensagem += "<br><br>Não esqueça de parabenizá-los 🥳"

        msg_box = QMessageBox()
        msg_box.setWindowTitle("🎂 Aniversários do Dia 🎂")
        msg_box.setText(mensagem)
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                font-family: Segoe UI;
                font-size: 14pt;
            }
            QMessageBox QLabel {
                color: rgb(220, 220, 255);
            }
            QMessageBox QPushButton {
                background-color: rgb(100, 150, 255);
                color: white;
                border-radius: 5px;
                padding: 8px;
                min-width: 80px;
            }
            QMessageBox QPushButton:hover {
                background-color: rgb(120, 170, 255);
            }
            QMessageBox QPushButton:pressed {
                background-color: rgb(80, 130, 235);
            }
        """)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()
        self.mensagem_aniversario_exibida = True

    def verificar_aniversarios(self):
        hoje = datetime.now()
        dia_atual = hoje.day
        mes_atual = hoje.month

        aniversariantes = []
        for contato in self.contatos:
            data_nascimento = contato.get("data_nascimento")
            if data_nascimento:
                if data_nascimento.day == dia_atual and data_nascimento.month == mes_atual:
                    aniversariantes.append(contato["nome"])

        if aniversariantes:
            self.exibir_mensagem_aniversario(aniversariantes)

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
        foto_data_usuario = obter_foto_usuario(self.usuario_id)
        if foto_data_usuario:
            pixmap = QPixmap()
            pixmap.loadFromData(foto_data_usuario)
            self.label_foto.setPixmap(pixmap)
        else:
            self.label_foto.setText("Sem Foto")

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

            contato_layout = QHBoxLayout()
            contato_layout.setAlignment(Qt.AlignLeft)
            contato_layout.setSpacing(15)

            label = QLabel()
            label.setObjectName(f"label_{nome}_{i}")
            label.setText(f"📞 {nome} - {telefone}")
            label.setStyleSheet("""
                color: rgb(220, 220, 255);
                background-color: rgb(45, 45, 55);
                font-family: Segoe UI;
                font-size: 12pt;
                padding: 8px;
                border-radius: 5px;
            """)
            label.setMinimumHeight(40)
            contato_layout.addWidget(label)
            self.labels_contatos.append(label)

            label_editar = QLabel()
            label_editar.setObjectName(f"label_editar_{i}")
            label_editar.setPixmap(QPixmap("yy.png"))
            label_editar.setScaledContents(True)
            label_editar.setFixedSize(28, 28)
            label_editar.setStyleSheet("""
                background-color: rgb(100, 150, 255);
                border-radius: 14px;
                padding: 4px;
            """)
            label_editar.mousePressEvent = lambda event, idx=i: self.editar_contato(idx)
            contato_layout.addWidget(label_editar)
            self.labels_editar.append(label_editar)

            self.scroll_layout.addLayout(contato_layout)

            line = QFrame()
            line.setObjectName(f"line_{nome}_{i}")
            line.setFrameShape(QFrame.HLine)
            line.setStyleSheet("""
                background-color: rgb(70, 80, 100);
                height: 1px;
                border: none;
            """)
            self.scroll_layout.addWidget(line)
            self.lines.append(line)

        self.verificar_aniversarios()

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
        }

        self.tela_editar_contato = QMainWindow()
        self.ui_editar_contato = Ui_EditarContato()
        self.ui_editar_contato.setupUi(self.tela_editar_contato, contato_info, self)
        self.tela_editar_contato.destroyed.connect(self.carregar_contatos)
        self.tela_editar_contato.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_Form(1)
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())