from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QFrame, QLabel, QLineEdit, QListView, QMainWindow
from add_cntt import Ui_tela_add_contato

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

        
        contatos = ["Abgail", "Bento", "João", "Maria"]
        y_positions = [90, 130, 170, 210]
        self.labels_contatos = []
        self.labels_editar = []
        self.lines = []  

        for i, nome in enumerate(contatos):
            
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
            label_editar.setObjectName(f"label_editar{i+1}")
            label_editar.setGeometry(QRect(590, y_positions[i], 20, 20))
            label_editar.setPixmap(QPixmap(u"yy.png"))
            label_editar.setScaledContents(True)
            self.labels_editar.append(label_editar)

        
        self.label_add = QLabel(self.frame_principal_cntt)
        self.label_add.setObjectName(u"label_add")
        self.label_add.setGeometry(QRect(580, 40, 31, 31))
        self.label_add.setPixmap(QPixmap(u"xx.png"))
        self.label_add.setScaledContents(True)

        
        self.label_add.mousePressEvent = self.adicionar_contato
        for i, label_editar in enumerate(self.labels_editar):
            label_editar.mousePressEvent = lambda event, index=i: self.editar_contato(index)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)
    
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Contatos", None))
        self.label_Cntt.setText(QCoreApplication.translate("Form", u"Contatos", None))

    def editar_contato(self, index):
       
        print(f"Editando contato {index}")
    
    def adicionar_contato(self, event):
        
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
