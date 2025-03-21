import sys
from PySide6.QtCore import QMetaObject, QRect, Qt
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtWidgets import QFrame, QLabel, QLineEdit, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea, QMessageBox
from add_cntt import Ui_tela_add_contato
from editarcntt import Ui_Form as Ui_EditarContato
from bancodedados import obter_contatos, obter_foto_usuario
from datetime import datetime

class Ui_Form(object):
    def __init__(self, usuario_id):
        self.usuario_id = usuario_id

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(988, 579)

        # Widget central
        self.centralwidget = QWidget(Form)
        self.centralwidget.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:1, 
            stop:0 #ECF0F1, stop:1 #BDC3C7);
        """)
        Form.setCentralWidget(self.centralwidget)

        # Foto de perfil no topo
        self.label_foto = QLabel(self.centralwidget)
        self.label_foto.setGeometry(QRect(444, 10, 100, 100))  # Centralizado no topo (988/2 - 50)
        self.label_foto.setStyleSheet("border: 1px solid #BDC3C7; border-radius: 50px;")
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

        # Área de scroll para contatos
        self.scroll_area = QScrollArea(self.centralwidget)
        self.scroll_area.setGeometry(QRect(170, 120, 651, 401))  # Ajustado para dar espaço à foto
        self.scroll_area.setWidgetResizable(True)

        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_area.setWidget(self.scroll_widget)

        self.label_Cntt = QLabel("Contatos", self.scroll_widget)
        self.label_Cntt.setStyleSheet("font: 700 12pt 'Segoe Print';")
        self.scroll_layout.addWidget(self.label_Cntt)

        self.line_buscar_cntt = QLineEdit(self.scroll_widget)
        self.line_buscar_cntt.setPlaceholderText("Buscar Contatos...")
        self.scroll_layout.addWidget(self.line_buscar_cntt)

        self.label_add = QLabel(self.scroll_widget)
        self.label_add.setPixmap(QPixmap("xx.png"))
        self.label_add.setScaledContents(True)
        self.label_add.setFixedSize(32, 32)
        self.label_add.mousePressEvent = self.adicionar_contato
        self.scroll_layout.addWidget(self.label_add)

        self.contatos = []
        self.labels_contatos = []
        self.labels_editar = []
        self.lines = []

        self.line_buscar_cntt.textChanged.connect(self.filtrar_contatos)
        self.carregar_contatos()  # Carrega os contatos
        QMetaObject.connectSlotsByName(Form)

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

            contato_layout = QHBoxLayout()

            label = QLabel(self.scroll_widget)
            label.setObjectName(f"label_{nome}_{i}")
            label.setText(f"{nome} - {telefone}")
            contato_layout.addWidget(label)
            self.labels_contatos.append(label)

            label_editar = QLabel(self.scroll_widget)
            label_editar.setObjectName(f"label_editar_{i}")
            label_editar.setPixmap(QPixmap("yy.png"))
            label_editar.setScaledContents(True)
            label_editar.setFixedSize(24, 24)
            label_editar.mousePressEvent = lambda event, idx=i: self.editar_contato(idx)
            contato_layout.addWidget(label_editar)
            self.labels_editar.append(label_editar)

            self.scroll_layout.addLayout(contato_layout)

            line = QFrame(self.scroll_widget)
            line.setObjectName(f"line_{nome}_{i}")
            line.setFrameShape(QFrame.HLine)
            line.setStyleSheet("background-color: black;")
            self.scroll_layout.addWidget(line)
            self.lines.append(line)

        self.verificar_aniversarios()  # Verifica aniversários após carregar os contatos

    def editar_contato(self, i):
        contato = self.contatos[i]
        contato_info = {
            "id": contato.get("id"),
            "nome": contato.get("nome", "Sem Nome"),
            "telefone": contato.get("telefone", "Sem Telefone"),
            "email": contato.get("email", "Sem Email"),
            "rede_social": contato.get("perfil_rede_social", "Sem Rede Social"),
            "notas": contato.get("notas", "Sem Notas")
        }

        self.tela_editar_contato = QMainWindow()
        self.ui_editar_contato = Ui_EditarContato()
        self.ui_editar_contato.setupUi(self.tela_editar_contato, contato_info, self)
        self.tela_editar_contato.destroyed.connect(self.carregar_contatos)
        self.tela_editar_contato.show()

if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    Form = QMainWindow()
    ui = Ui_Form(1)  # Exemplo com ID 1
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())