from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QFrame, QLabel, QLineEdit, QListView, QMainWindow
from add_cntt import Ui_tela_add_contato
from PySide6.QtCore import QSortFilterProxyModel, QStringListModel
from editarcntt import Ui_Form as Ui_EditarContato  # Importando a tela de edição

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

        self.contatos = ["Abgail", "Bento", "João", "Maria"]
        y_positions = [90, 130, 170, 210]
        self.labels_contatos = []
        self.labels_editar = []
        self.lines = []

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

        self.line_buscar_cntt.textChanged.connect(self.filtrar_contatos)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

        
        for i, label_editar in enumerate(self.labels_editar):
            label_editar.mousePressEvent = lambda event, i=i: self.editar_contato(i)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Contatos", None))
        self.label_Cntt.setText(QCoreApplication.translate("Form", u"Contatos", None))

    def filtrar_contatos(self):
        texto_busca = self.line_buscar_cntt.text().lower()
        
        y_offset = 90  

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
        self.tela_add_contato = QMainWindow()
        self.ui_add_contato = Ui_tela_add_contato()

        # 🔹 Passar o usuario_id para a tela de adicionar contato
        self.ui_add_contato.setupUi(self.tela_add_contato, self.tela_add_contato, self.usuario_id)
    
        self.tela_add_contato.show()
        event.accept()


if __name__ == "__main__":
    app = QApplication([]) 
    MainWindow = QMainWindow()  
    ui = Ui_Form()  
    ui.setupUi(MainWindow)  
    MainWindow.show()  
    app.exec()  