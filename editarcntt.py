from PySide6.QtCore import QCoreApplication, QMetaObject, QRect
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QLabel,
    QLineEdit, QPushButton, QMainWindow, QWidget, QMessageBox, QTextEdit)
from bancodedados import atualizar_contato, deletar_contato

class Ui_Form(object):
    def setupUi(self, Form, contato_info=None, main_window=None):  # Adicionado main_window
        self.main_window = main_window  # Armazena a referência da tela principal
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(988, 579)

        self.frame_editarcntt = QFrame(Form)
        self.frame_editarcntt.setObjectName("frame_editarcntt")
        self.frame_editarcntt.setGeometry(QRect(170, 50, 651, 479))
        self.frame_editarcntt.setStyleSheet("background-color: rgb(255, 255, 255);")

        # Labels
        self.label_Nome = QLabel("Nome:", self.frame_editarcntt)
        self.label_Nome.setGeometry(QRect(20, 20, 100, 20))

        self.label_Contato = QLabel("Contato:", self.frame_editarcntt)
        self.label_Contato.setGeometry(QRect(20, 80, 100, 20))

        self.label_Email = QLabel("Email:", self.frame_editarcntt)
        self.label_Email.setGeometry(QRect(20, 140, 100, 20))

        self.label_DataNasc = QLabel("Data de Nascimento:", self.frame_editarcntt)
        self.label_DataNasc.setGeometry(QRect(20, 200, 150, 20))

        self.label_Rede_Social = QLabel("Perfil de Rede Social:", self.frame_editarcntt)
        self.label_Rede_Social.setGeometry(QRect(20, 260, 150, 20))

        self.label_Notas = QLabel("Notas:", self.frame_editarcntt)
        self.label_Notas.setGeometry(QRect(20, 320, 100, 20))

        # Inputs
        self.lineEdit_nome = QLineEdit(self.frame_editarcntt)
        self.lineEdit_nome.setGeometry(QRect(20, 40, 600, 30))

        self.lineEdit_Cntt = QLineEdit(self.frame_editarcntt)
        self.lineEdit_Cntt.setGeometry(QRect(20, 100, 600, 30))
        self.lineEdit_Cntt.setInputMask("(99) 99999-9999")

        self.lineEdit_Email = QLineEdit(self.frame_editarcntt)
        self.lineEdit_Email.setGeometry(QRect(20, 160, 600, 30))

        self.data_Nasc = QDateEdit(self.frame_editarcntt)
        self.data_Nasc.setGeometry(QRect(20, 220, 150, 30))

        self.lineEdit_RedeSocial = QLineEdit(self.frame_editarcntt)
        self.lineEdit_RedeSocial.setGeometry(QRect(20, 280, 600, 30))

        self.textEdit_Notas = QTextEdit(self.frame_editarcntt)
        self.textEdit_Notas.setGeometry(QRect(20, 340, 600, 100))

        # Botões
        self.pushButton_voltar = QPushButton("Cancelar", self.frame_editarcntt)
        self.pushButton_voltar.setGeometry(QRect(555, 5, 75, 30))
        self.pushButton_voltar.setStyleSheet("background-color: transparent; border: none; color: rgb(0, 0, 255); font-weight: bold;")
        self.pushButton_voltar.clicked.connect(Form.close)

        self.pushButton_Salvar = QPushButton("Salvar", self.frame_editarcntt)
        self.pushButton_Salvar.setGeometry(QRect(545, 430, 75, 30))
        self.pushButton_Salvar.setStyleSheet("background-color: rgb(0, 0, 255); color: rgb(255, 255, 255);")
        self.pushButton_Salvar.clicked.connect(lambda: self.salvar_contato(Form))

        self.pushButton_Apagar = QPushButton("Excluir Contato", self.frame_editarcntt)
        self.pushButton_Apagar.setGeometry(QRect(20, 430, 90, 30))
        self.pushButton_Apagar.setStyleSheet("background-color: transparent; border: none; color: rgb(255, 0, 0); font-weight: bold;")
        self.pushButton_Apagar.clicked.connect(self.apagar_contato)

        # Carregar dados do contato
        if contato_info:
            self.contato_id = contato_info.get("id")
            self.lineEdit_nome.setText(contato_info.get("nome", ""))
            self.lineEdit_Cntt.setText(contato_info.get("telefone", ""))
            self.lineEdit_Email.setText(contato_info.get("email", ""))
            self.lineEdit_RedeSocial.setText(contato_info.get("rede_social", ""))
            self.textEdit_Notas.setPlainText(contato_info.get("notas", ""))

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Editar Contato"))

    def salvar_contato(self, Form):
        if not hasattr(self, "contato_id") or not self.contato_id:
            QMessageBox.warning(None, "Erro", "ID do contato não encontrado.")
            return

        nome = self.lineEdit_nome.text()
        telefone = self.lineEdit_Cntt.text().strip()
        email = self.lineEdit_Email.text()
        data_nascimento = self.data_Nasc.date().toString("yyyy-MM-dd")
        perfil_rede_social = self.lineEdit_RedeSocial.text()
        notas = self.textEdit_Notas.toPlainText()

        sucesso = atualizar_contato(self.contato_id, nome, email, telefone, data_nascimento, perfil_rede_social, notas)
        if sucesso:
            QMessageBox.information(None, "Sucesso", "Contato atualizado com sucesso!")
            if self.main_window and hasattr(self.main_window, "carregar_contatos"):
                self.main_window.carregar_contatos()  # Atualiza a lista
            Form.close()
        else:
            QMessageBox.warning(None, "Erro", "Falha ao atualizar o contato.")

    def apagar_contato(self):
        resposta = QMessageBox.question(None, "Confirmação", "Tem certeza que deseja deletar este contato?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if resposta == QMessageBox.Yes:
            sucesso = deletar_contato(self.contato_id)
            if sucesso:
                QMessageBox.information(None, "Sucesso", "Contato deletado com sucesso!")
                if self.main_window and hasattr(self.main_window, "carregar_contatos"):
                    self.main_window.carregar_contatos()  # Atualiza a lista
                self.frame_editarcntt.parent().close()  # Fecha a janela
            else:
                QMessageBox.warning(None, "Erro", "Falha ao deletar o contato!")

if __name__ == "__main__":
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = Ui_Form()
    contato_exemplo = {
        "id": 1,
        "nome": "João Silva",
        "telefone": "(11) 99999-9999",
        "email": "joao@email.com",
        "rede_social": "@joaosilva",
        "notas": "Amigo de infância"
    }
    ui.setupUi(MainWindow, contato_exemplo)
    MainWindow.show()
    app.exec()