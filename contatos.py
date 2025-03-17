from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QFrame, QLabel, QLineEdit, QListView, QMainWindow
from add_cntt import Ui_tela_add_contato
from PySide6.QtCore import QSortFilterProxyModel, QStringListModel
from editarcntt import Ui_Form as Ui_EditarContato  # Importando a tela de edição
from bancodedados import salvar_contato
from bancodedados import obter_contatos

class Ui_Form(object):
    def __init__(self, usuario_id):
        self.usuario_id = usuario_id

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(988, 579)

        self.frame_principal_cntt = QFrame(Form)
        self.frame_principal_cntt.setObjectName(u"frame_principal_cntt")
        self.frame_principal_cntt.setGeometry(QRect(170, 80, 651, 401))
        self.frame_principal_cntt.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.label_Cntt = QLabel(self.frame_principal_cntt)
        self.label_Cntt.setObjectName(u"label_Cntt")
        self.label_Cntt.setGeometry(QRect(30, 20, 71, 16))
        self.label_Cntt.setStyleSheet(u"font: 700 12pt \"Segoe Print\";")

        self.line_buscar_cntt = QLineEdit(self.frame_principal_cntt)
        self.line_buscar_cntt.setObjectName(u"line_buscar_cntt")
        self.line_buscar_cntt.setGeometry(QRect(30, 40, 181, 22))
        self.line_buscar_cntt.setPlaceholderText("Buscar Contatos...")

        self.list_cntt = QListView(self.frame_principal_cntt)
        self.list_cntt.setObjectName(u"list_cntt")
        self.list_cntt.setGeometry(QRect(30, 80, 591, 291))

        # Inicialmente, sem contatos
        self.contatos = []  
        self.labels_contatos = []
        self.labels_editar = []
        self.lines = []

        self.label_add = QLabel(self.frame_principal_cntt)
        self.label_add.setObjectName(u"label_add")
        self.label_add.setGeometry(QRect(580, 40, 31, 31))
        self.label_add.setPixmap(QPixmap(u"xx.png"))
        self.label_add.setScaledContents(True)
        self.label_add.mousePressEvent = self.adicionar_contato
        
        self.line_buscar_cntt.textChanged.connect(self.filtrar_contatos)
        self.carregar_contatos()
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)
        
        # Conecta a ação de edição para todos os contatos
        for i, label_editar in enumerate(self.labels_editar):
            label_editar.mousePressEvent = lambda event, i=i: self.editar_contato(i)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Contatos", None))
        self.label_Cntt.setText(QCoreApplication.translate("Form", u"Contatos", None))

    def filtrar_contatos(self):
        texto_busca = self.line_buscar_cntt.text().lower()

        y_offset = 90

        # Atualiza os contatos visíveis com base na busca
        for i, label in enumerate(self.labels_contatos):
            nome_contato = label.text().lower()

            if texto_busca in nome_contato:
                self.labels_contatos[i].setVisible(True)
                self.lines[i].setVisible(True)
                self.labels_editar[i].setVisible(True)

                self.labels_contatos[i].move(40, y_offset)
                self.lines[i].move(40, y_offset + 18)
                self.labels_editar[i].move(590, y_offset)

                y_offset += 40
            else:
                self.labels_contatos[i].setVisible(False)
                self.lines[i].setVisible(False)
                self.labels_editar[i].setVisible(False)

    def editar_contato(self, i):
        contato = self.contatos[i]
        print(f"Editando contato: {contato}")

        contato_info = {
            "nome": contato,
            "contato": "(11) 99999-9999",
            "email": "exemplo@email.com",
            "rede_social": "@exemplo",
            "notas": "Notas do contato"
        }

        self.tela_editar_contato = QMainWindow()
        self.ui_editar_contato = Ui_EditarContato()
        self.ui_editar_contato.setupUi(self.tela_editar_contato, contato_info)
        self.tela_editar_contato.show()

    def adicionar_contato(self, event):
        """Abre a tela de adicionar contato sem criar um contato vazio."""

        # Criando a janela para adicionar contato
        self.tela_add_contato = QMainWindow()
    
        # Criando a interface da tela de adicionar contato (sem passar argumentos)
        self.ui_add_contato = Ui_tela_add_contato()
    
        # Definindo o ID do usuário dentro do objeto da tela de adicionar contato
        self.ui_add_contato.usuario_id = self.usuario_id  # ✅ Agora o usuário logado será salvo corretamente
    
        # Configurando e exibindo a tela
        self.ui_add_contato.setupUi(self.tela_add_contato, self)
        self.tela_add_contato.show()

        event.accept()

    def atualizar_contatos(self):
        # Remover todos os widgets antigos
        for label in self.labels_contatos:
            label.deleteLater()
        for line in self.lines:
            line.deleteLater()
        for label_editar in self.labels_editar:
            label_editar.deleteLater()

        # Limpar as listas de widgets
        self.labels_contatos.clear()
        self.lines.clear()
        self.labels_editar.clear()

        # Adicionar novamente os contatos
        y_positions = [90 + (i * 40) for i in range(len(self.contatos))]
        for i, nome in enumerate(self.contatos):
            label = QLabel(self.frame_principal_cntt)
            label.setObjectName(f"label_{nome}")
            label.setGeometry(QRect(40, y_positions[i], 50, 16))
            label.setText(nome)
            self.labels_contatos.append(label)

            line = QFrame(self.frame_principal_cntt)
            line.setObjectName(f"line_{nome}")
            line.setGeometry(QRect(40, y_positions[i] + 18, 550, 1))
            line.setStyleSheet("background-color: black;")
            self.lines.append(line)

            label_editar = QLabel(self.frame_principal_cntt)
            label_editar.setObjectName(f"label_editar{i + 1}")
            label_editar.setGeometry(QRect(590, y_positions[i], 20, 20))
            label_editar.setPixmap(QPixmap(u"yy.png"))
            label_editar.setScaledContents(True)
            self.labels_editar.append(label_editar)

        # Reatribuir o evento de clique para cada ícone de edição
        for i, label_editar in enumerate(self.labels_editar):
            label_editar.mousePressEvent = lambda event, i=i: self.editar_contato(i)
    

    
    def carregar_contatos(self):
        """Atualiza a lista de contatos na interface gráfica."""
        self.contatos = obter_contatos(self.usuario_id)  # Obtém os contatos do banco
    
        # Remove widgets antigos para evitar duplicação
        for label in self.labels_contatos:
            label.deleteLater()
        for line in self.lines:
            line.deleteLater()
        for label_editar in self.labels_editar:
            label_editar.deleteLater()

        self.labels_contatos.clear()
        self.lines.clear()
        self.labels_editar.clear()

        # Adiciona os contatos novamente
        y_offset = 90  # Posição inicial para exibir os contatos
        for i, contato in enumerate(self.contatos):
            nome = contato["nome"]
            telefone = contato["telefone"]

        # Criar um rótulo para exibir o nome e telefone do contato
        label = QLabel(self.frame_principal_cntt)
        label.setObjectName(f"label_{nome}")
        label.setGeometry(QRect(40, y_offset, 200, 16))
        label.setText(f"{nome} - {telefone}")
        self.labels_contatos.append(label)

        # Linha de separação entre os contatos
        line = QFrame(self.frame_principal_cntt)
        line.setObjectName(f"line_{nome}")
        line.setGeometry(QRect(40, y_offset + 18, 550, 1))
        line.setStyleSheet("background-color: black;")
        self.lines.append(line)

        # Ícone de edição ao lado do contato
        label_editar = QLabel(self.frame_principal_cntt)
        label_editar.setObjectName(f"label_editar{i + 1}")
        label_editar.setGeometry(QRect(590, y_offset, 20, 20))
        label_editar.setPixmap(QPixmap(u"yy.png"))
        label_editar.setScaledContents(True)
        self.labels_editar.append(label_editar)

        y_offset += 40  # Move a próxima linha para baixo

    # Reatribuir evento de clique para editar contatos
        for i, label_editar in enumerate(self.labels_editar):
            label_editar.mousePressEvent = lambda event, i=i: self.editar_contato(i)

        
