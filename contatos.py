from PySide6.QtCore import QMetaObject, QRect, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFrame, QLabel, QLineEdit, QListView, QMainWindow, QVBoxLayout, QWidget, QScrollArea
from add_cntt import Ui_tela_add_contato
from editarcntt import Ui_Form as Ui_EditarContato  # Importando a tela de edição
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

        self.list_cntt = QListView(self.scroll_widget)
        self.scroll_layout.addWidget(self.list_cntt)

        self.label_add = QLabel(self.scroll_widget)
        self.label_add.setPixmap(QPixmap("xx.png"))
        self.label_add.setScaledContents(True)
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
        self.contatos = obter_contatos(self.usuario_id)  # Obtém os contatos do banco
        print(f"📋 Contatos carregados: {self.contatos}")  # 🔍 Verificar se os números estão vindo do banco
  

         

    
        for label in self.labels_contatos:
            label.deleteLater()
        for line in self.lines:
            line.deleteLater()
        for label_editar in self.labels_editar:
            label_editar.deleteLater()

        self.labels_contatos.clear()
        self.lines.clear()
        self.labels_editar.clear()

    # Adicionar contatos novamente
        y_offset = 90  
        for i, contato in enumerate(self.contatos):
            nome = contato.get("nome", "Sem Nome")  

            label = QLabel(self.scroll_widget)  # ✅ Usar `self.scroll_widget` em vez de `frame_principal_cntt`
            label.setObjectName(f"label_{nome}")
            label.setText(f"{nome}")  # Exibe apenas o nome na lista
            self.scroll_layout.addWidget(label)  # ✅ Adiciona ao layout de rolagem
            self.labels_contatos.append(label)

            line = QFrame(self.scroll_widget)
            line.setObjectName(f"line_{nome}")
            line.setStyleSheet("background-color: black;")
            self.scroll_layout.addWidget(line)
            self.lines.append(line)

            label_editar = QLabel(self.scroll_widget)
            label_editar.setObjectName(f"label_editar{i + 1}")
            label_editar.setPixmap(QPixmap(u"yy.png"))
            label_editar.setScaledContents(True)
            self.scroll_layout.addWidget(label_editar)
            self.labels_editar.append(label_editar)


            y_offset += 40  

    # ✅ Agora, atribuímos corretamente os eventos de clique nos botões de edição
        for i, label_editar in enumerate(self.labels_editar):
            label_editar.mousePressEvent = lambda event, i=i: self.editar_contato(i)

    def editar_contato(self, i):
        contato = self.contatos[i]  # Obtém o contato correto
        
       

        contato_info = {
            "nome": contato.get("nome", "Sem Nome"),
            "telefone": contato.get("telefone", "Sem Telefone"),
            "email": contato.get("email", "Sem Email"),
            "rede_social": contato.get("perfil_rede_social", "Sem Rede Social"),
            "notas": contato.get("notas", "Sem Notas")
    }

       

        self.tela_editar_contato = QMainWindow()
        self.ui_editar_contato = Ui_EditarContato()
        self.ui_editar_contato.setupUi(self.tela_editar_contato, contato_info)
        self.tela_editar_contato.show()

