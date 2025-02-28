from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QFrame, QLabel, QLineEdit, QListView, QMainWindow
from add_cntt import Ui_tela_add_contato
from PySide6.QtCore import QSortFilterProxyModel, QStringListModel, Qt

class Ui_Form(object):
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

        # Criar a lista de contatos
        self.contatos = ["Abgail", "Bento", "João", "Maria"]  # Lista de nomes

        # Criar um modelo para armazenar os contatos
        self.model = QStringListModel(self.contatos)

        # Criar um modelo de filtro para permitir buscas
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)  # Conectar ao modelo original
        self.proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)  # Deixar a busca sem diferenciação de maiúsculas e minúsculas
        self.proxy_model.setFilterKeyColumn(0)  # Aplicar filtro na coluna de nomes

        # Associar a lista de contatos ao QListView
        self.list_cntt.setModel(self.proxy_model)

        # Conectar a barra de busca ao filtro
        self.line_buscar_cntt.textChanged.connect(self.proxy_model.setFilterFixedString)

        # Adicionar ação para o botão de adicionar contato
        self.label_add = QLabel(self.frame_principal_cntt)
        self.label_add.setObjectName(u"label_add")
        self.label_add.setGeometry(QRect(580, 40, 31, 31))
        self.label_add.setPixmap(QPixmap(u"xx.png"))
        self.label_add.setScaledContents(True)
        self.label_add.mousePressEvent = self.adicionar_contato

        # Conectar ação de editar ao item da lista
        self.list_cntt.clicked.connect(self.editar_contato)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Contatos", None))
        self.label_Cntt.setText(QCoreApplication.translate("Form", u"Contatos", None))

    def editar_contato(self, index):
        # Pega o contato selecionado e faz a edição
        contato = self.proxy_model.data(index, Qt.DisplayRole)
        print(f"Editando contato: {contato}")

    def adicionar_contato(self, event):
        # Ação de adicionar um novo contato
        self.tela_add_contato = QMainWindow()
        self.ui_add_contato = Ui_tela_add_contato()
        self.ui_add_contato.setupUi(self.tela_add_contato, self.tela_add_contato)
        self.tela_add_contato.show()
        event.accept()

if __name__ == "__main__":
    app = QApplication([])  # Criação da aplicação
    MainWindow = QMainWindow()  # Criação da janela principal
    ui = Ui_Form()  # Instancia a tela principal
    ui.setupUi(MainWindow)  # Configura a interface da tela principal
    MainWindow.show()  # Exibe a janela principal
    app.exec()  # Inicia o loop de eventos da aplicação
