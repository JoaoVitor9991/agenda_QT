from PySide6.QtCore import QMetaObject, QRect, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFrame, QLabel, QLineEdit, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QScrollArea
from add_cntt import Ui_tela_add_contato
from editarcntt import Ui_Form as Ui_EditarContato
from bancodedados import obter_contatos

class Ui_Form(object):
    def __init__(self, usuario_id):
        self.usuario_id = usuario_id

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(988, 579)

        self.scroll_area = QScrollArea(Form)
        self.scroll_area.setGeometry(QRect(170, 80, 651, 401))
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

        # Label para adicionar contato
        self.label_add = QLabel(self.scroll_widget)
        self.label_add.setPixmap(QPixmap("xx.png"))
        self.label_add.setScaledContents(True)
        self.label_add.setFixedSize(32, 32)  # Tamanho fixo de 32x32 pixels
        self.label_add.mousePressEvent = self.adicionar_contato
        self.scroll_layout.addWidget(self.label_add)

        self.contatos = []
        self.labels_contatos = []
        self.labels_editar = []
        self.lines = []

        self.line_buscar_cntt.textChanged.connect(self.filtrar_contatos)
        self.carregar_contatos()
        QMetaObject.connectSlotsByName(Form)

    def filtrar_contatos(self):
        texto_busca = self.line_buscar_cntt.text().lower()
        for label in self.labels_contatos:
            label.setVisible(texto_busca in label.text().lower())

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

        # Limpa os contatos da interface
        for label in self.labels_contatos:
            label.deleteLater()
        for line in self.lines:
            line.deleteLater()
        for label_editar in self.labels_editar:
            label_editar.deleteLater()

        self.labels_contatos.clear()
        self.lines.clear()
        self.labels_editar.clear()

        # Adiciona os contatos na interface
        for i, contato in enumerate(self.contatos):
            nome = contato.get("nome", "Sem Nome")
            telefone = str(contato.get("telefone", "Sem Telefone"))

            # Criar um layout horizontal para cada contato
            contato_layout = QHBoxLayout()

            # Label com nome e telefone
            label = QLabel(self.scroll_widget)
            label.setObjectName(f"label_{nome}_{i}")
            label.setText(f"{nome} - {telefone}")
            contato_layout.addWidget(label)
            self.labels_contatos.append(label)

            # Botão de edição ao lado do nome
            label_editar = QLabel(self.scroll_widget)
            label_editar.setObjectName(f"label_editar_{i}")
            label_editar.setPixmap(QPixmap("yy.png"))
            label_editar.setScaledContents(True)
            label_editar.setFixedSize(24, 24)  # Tamanho fixo de 24x24 pixels
            label_editar.mousePressEvent = lambda event, idx=i: self.editar_contato(idx)
            contato_layout.addWidget(label_editar)
            self.labels_editar.append(label_editar)

            # Adiciona o layout horizontal ao layout principal
            self.scroll_layout.addLayout(contato_layout)

            # Linha divisória abaixo de cada contato
            line = QFrame(self.scroll_widget)
            line.setObjectName(f"line_{nome}_{i}")
            line.setFrameShape(QFrame.HLine)
            line.setStyleSheet("background-color: black;")
            self.scroll_layout.addWidget(line)
            self.lines.append(line)

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
        self.ui_editar_contato.setupUi(self.tela_editar_contato, contato_info)
        self.tela_editar_contato.destroyed.connect(self.carregar_contatos)
        self.tela_editar_contato.show()
