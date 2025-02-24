from PySide6.QtCore import QCoreApplication, Qt, QMetaObject
from PySide6.QtWidgets import QApplication, QFrame, QLabel, QLineEdit, QMainWindow, QPushButton, QSizePolicy, QWidget, QListWidget, QVBoxLayout, QHBoxLayout, QInputDialog

class Ui_tela_contatos(object):
    def setupUi(self, tela_contatos):
        if not tela_contatos.objectName():
            tela_contatos.setObjectName(u"tela_contatos")
        tela_contatos.resize(822, 648)
        self.centralwidget = QWidget(tela_contatos)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(0, 0, 822, 648)
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.txt_Entrar = QLabel(self.frame)
        self.txt_Entrar.setObjectName(u"txt_Entrar")
        self.txt_Entrar.setGeometry(50, 20, 161, 31)
        font = self.txt_Entrar.font()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.txt_Entrar.setFont(font)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(50, 60, 321, 22)
        self.lineEdit.setPlaceholderText("Buscar contatos...")

        self.pushButton_add_Contato = QPushButton(self.frame)
        self.pushButton_add_Contato.setObjectName(u"pushButton")
        self.pushButton_add_Contato.setGeometry(630, 30, 111, 24)
        self.pushButton_add_Contato.setText("Adicionar contato")
        self.pushButton_add_Contato.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255);")


        self.txt_email = QLabel(self.frame)
        self.txt_email.setObjectName(u"txt_email")
        self.txt_email.setGeometry(50, 120, 121, 16)
        font1 = self.txt_email.font()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(True)
        self.txt_email.setFont(font1)

        # Lista de contatos
        self.contact_list = QListWidget(self.frame)
        self.contact_list.setGeometry(50, 150, 700, 350)
        self.contact_list.addItems(["Almir", "João", "Maria"])  # Exemplo de contatos

        tela_contatos.setCentralWidget(self.centralwidget)
        self.retranslateUi(tela_contatos)

        QMetaObject.connectSlotsByName(tela_contatos)

    def retranslateUi(self, tela_contatos):
        tela_contatos.setWindowTitle(QCoreApplication.translate("tela_contatos", u"Contatos", None))
        self.txt_Entrar.setText(QCoreApplication.translate("tela_contatos", u"Contatos", None))
        self.txt_email.setText(QCoreApplication.translate("tela_contatos", u"Nome do contato:", None))

    def add_contact(self):
        # Exemplo de janela para adicionar um novo contato
        text, ok = QInputDialog.getText(None, "Adicionar Contato", "Digite o nome do contato:")
        if ok and text:
            self.contact_list.addItem(text)
        
    def filter_contacts(self):
        # Filtro da lista de contatos baseado no que for digitado no campo de busca
        search_text = self.lineEdit.text().lower()
        for i in range(self.contact_list.count()):
            item = self.contact_list.item(i)
            item.setHidden(not search_text in item.text().lower())

if __name__ == "__main__":
    app = QApplication([])
    mainWindow = QMainWindow()
    ui = Ui_tela_contatos()
    ui.setupUi(mainWindow)
    mainWindow.show()
    app.exec()
