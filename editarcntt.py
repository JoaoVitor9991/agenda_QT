import sys
from PySide6.QtCore import QRect, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, QLabel, QLineEdit, QPushButton, QMessageBox, QScrollArea
from bancodedados import atualizar_contato, deletar_contato, conectar

class Ui_Form(object):
    def setupUi(self, Tela_Editar_Contato, contato_info, tela_contatos):
        self.contato_info = contato_info
        self.tela_contatos = tela_contatos
        Tela_Editar_Contato.setObjectName("Tela_Editar_Contato")
        Tela_Editar_Contato.resize(800, 600)

        # Widget central com gradiente escuro
        self.centralwidget = QWidget(Tela_Editar_Contato)
        self.centralwidget.setStyleSheet("""
            background: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 rgb(20, 20, 30),
                stop: 1 rgb(50, 60, 80)
            );
        """)
        Tela_Editar_Contato.setCentralWidget(self.centralwidget)

        # Área de rolagem
        self.scroll_area = QScrollArea(self.centralwidget)
        self.scroll_area.setGeometry(QRect(0, 0, 800, 600))
        self.scroll_area.setWidgetResizable(True)

        self.scroll_widget = QWidget()
        self.scroll_widget.setMinimumHeight(700)
        self.scroll_area.setWidget(self.scroll_widget)

        # Frame central com fundo escuro
        self.frame = QFrame(self.scroll_widget)
        self.frame.setGeometry(QRect(150, 50, 500, 600))
        self.frame.setStyleSheet("""
            background-color: rgb(40, 40, 50);
            border-radius: 10px;
        """)
        font = QFont("Segoe UI", 12)
        self.frame.setFont(font)

        # Título
        self.txt_editar_contato = QLabel("Editar Contato", self.frame)
        self.txt_editar_contato.setGeometry(QRect(0, 20, 500, 40))
        font1 = QFont("Segoe UI", 18, QFont.Bold)
        self.txt_editar_contato.setFont(font1)
        self.txt_editar_contato.setStyleSheet("""
            color: rgb(220, 220, 255);
            background-color: transparent;
        """)
        self.txt_editar_contato.setAlignment(Qt.AlignCenter)

        # Campo Nome
        self.txt_nome = QLabel("Nome:", self.frame)
        self.txt_nome.setGeometry(QRect(50, 80, 100, 20))
        font2 = QFont("Segoe UI", 12)
        self.txt_nome.setFont(font2)
        self.txt_nome.setStyleSheet("color: rgb(200, 200, 200);")
        self.line_nome = QLineEdit(self.frame)
        self.line_nome.setGeometry(QRect(50, 100, 400, 40))
        self.line_nome.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)
        self.line_nome.setText(self.contato_info["nome"])

        # Campo Telefone
        self.txt_telefone = QLabel("Telefone:", self.frame)
        self.txt_telefone.setGeometry(QRect(50, 150, 100, 20))
        self.txt_telefone.setFont(font2)
        self.txt_telefone.setStyleSheet("color: rgb(200, 200, 200);")
        self.line_telefone = QLineEdit(self.frame)
        self.line_telefone.setGeometry(QRect(50, 170, 400, 40))
        self.line_telefone.setInputMask("(99) 99999-9999")
        self.line_telefone.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)
        self.line_telefone.setText(self.contato_info["telefone"])

        # Campo Email
        self.txt_email = QLabel("Email:", self.frame)
        self.txt_email.setGeometry(QRect(50, 220, 100, 20))
        self.txt_email.setFont(font2)
        self.txt_email.setStyleSheet("color: rgb(200, 200, 200);")
        self.line_email = QLineEdit(self.frame)
        self.line_email.setGeometry(QRect(50, 240, 400, 40))
        self.line_email.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)
        self.line_email.setText(self.contato_info["email"])

        # Campo Perfil Rede Social
        self.txt_rede_social = QLabel("Perfil Rede Social:", self.frame)
        self.txt_rede_social.setGeometry(QRect(50, 290, 150, 20))
        self.txt_rede_social.setFont(font2)
        self.txt_rede_social.setStyleSheet("color: rgb(200, 200, 200);")
        self.line_rede_social = QLineEdit(self.frame)
        self.line_rede_social.setGeometry(QRect(50, 310, 400, 40))
        self.line_rede_social.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)
        self.line_rede_social.setText(self.contato_info["rede_social"])

        # Campo Notas
        self.txt_notas = QLabel("Notas:", self.frame)
        self.txt_notas.setGeometry(QRect(50, 360, 100, 20))
        self.txt_notas.setFont(font2)
        self.txt_notas.setStyleSheet("color: rgb(200, 200, 200);")
        self.line_notas = QLineEdit(self.frame)
        self.line_notas.setGeometry(QRect(50, 380, 400, 40))
        self.line_notas.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)
        self.line_notas.setText(self.contato_info["notas"])

        # Campo Data de Nascimento
        self.txt_data_nascimento = QLabel("Data de Nascimento:", self.frame)
        self.txt_data_nascimento.setGeometry(QRect(50, 430, 150, 20))
        self.txt_data_nascimento.setFont(font2)
        self.txt_data_nascimento.setStyleSheet("color: rgb(200, 200, 200);")
        self.line_data_nascimento = QLineEdit(self.frame)
        self.line_data_nascimento.setGeometry(QRect(50, 450, 400, 40))
        self.line_data_nascimento.setInputMask("9999-99-99")
        self.line_data_nascimento.setStyleSheet("""
            QLineEdit {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
            QLineEdit:focus {
                border: 1px solid rgb(100, 150, 255);
            }
        """)
        # Preencher data de nascimento (se existir no banco)
        conexao = conectar()
        if conexao:
            cursor = conexao.cursor()
            cursor.execute("SELECT data_nascimento FROM contatos WHERE id = %s", (self.contato_info["id"],))
            data = cursor.fetchone()
            if data and data[0]:
                self.line_data_nascimento.setText(data[0].strftime("%Y-%m-%d"))
            cursor.close()
            conexao.close()

        # Botão Salvar
        self.btn_salvar = QPushButton("Salvar", self.frame)
        self.btn_salvar.setGeometry(QRect(350, 510, 100, 40))
        font3 = QFont("Segoe UI", 12, QFont.Bold)
        self.btn_salvar.setFont(font3)
        self.btn_salvar.setStyleSheet("""
            QPushButton {
                color: rgb(255, 255, 255);
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(100, 150, 255),
                    stop: 1 rgb(70, 100, 200)
                );
                border-radius: 8px;
                padding: 5px;
            }
            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(120, 170, 255),
                    stop: 1 rgb(90, 120, 220)
                );
            }
            QPushButton:pressed {
                background: rgb(50, 80, 180);
            }
        """)
        self.btn_salvar.setCursor(Qt.PointingHandCursor)
        self.btn_salvar.clicked.connect(self.salvar_alteracoes)

        # Botão Voltar
        self.btn_voltar = QPushButton("Voltar", self.frame)
        self.btn_voltar.setGeometry(QRect(240, 510, 100, 40))
        self.btn_voltar.setFont(font3)
        self.btn_voltar.setStyleSheet("""
            QPushButton {
                color: rgb(255, 255, 255);
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(255, 100, 100),
                    stop: 1 rgb(200, 70, 70)
                );
                border-radius: 8px;
                padding: 5px;
            }
            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(255, 120, 120),
                    stop: 1 rgb(220, 90, 90)
                );
            }
            QPushButton:pressed {
                background: rgb(180, 50, 50);
            }
        """)
        self.btn_voltar.setCursor(Qt.PointingHandCursor)
        self.btn_voltar.clicked.connect(Tela_Editar_Contato.close)

        # Botão Deletar
        self.btn_deletar = QPushButton("Deletar", self.frame)
        self.btn_deletar.setGeometry(QRect(130, 510, 100, 40))
        self.btn_deletar.setFont(font3)
        self.btn_deletar.setStyleSheet("""
            QPushButton {
                color: rgb(255, 255, 255);
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(150, 150, 150),
                    stop: 1 rgb(100, 100, 100)
                );
                border-radius: 8px;
                padding: 5px;
            }
            QPushButton:hover {
                background: qlineargradient(
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 rgb(170, 170, 170),
                    stop: 1 rgb(120, 120, 120)
                );
            }
            QPushButton:pressed {
                background: rgb(80, 80, 80);
            }
        """)
        self.btn_deletar.setCursor(Qt.PointingHandCursor)
        self.btn_deletar.clicked.connect(self.deletar_contato)

    def salvar_alteracoes(self):
        nome = self.line_nome.text()
        telefone = self.line_telefone.text()
        email = self.line_email.text()
        perfil_rede_social = self.line_rede_social.text()
        notas = self.line_notas.text()
        data_nascimento = self.line_data_nascimento.text() if self.line_data_nascimento.text() != "    -  -  " else None

        if not nome:
            QMessageBox.warning(None, "Erro", "O campo 'Nome' é obrigatório.")
            return

        if atualizar_contato(self.contato_info["id"], nome, email, telefone, data_nascimento, perfil_rede_social, notas):
            QMessageBox.information(None, "Sucesso", "Contato atualizado com sucesso!")
            self.tela_contatos.carregar_contatos()
            self.frame.parent().parent().parent().close()
        else:
            QMessageBox.warning(None, "Erro", "Erro ao atualizar contato.")

    def deletar_contato(self):
        resposta = QMessageBox.question(None, "Confirmação", "Deseja realmente deletar este contato?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if resposta == QMessageBox.Yes:
            if deletar_contato(self.contato_info["id"]):
                QMessageBox.information(None, "Sucesso", "Contato deletado com sucesso!")
                self.tela_contatos.carregar_contatos()
                self.frame.parent().parent().parent().close()
            else:
                QMessageBox.warning(None, "Erro", "Erro ao deletar contato.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    contato_info = {"id": 1, "nome": "Teste", "telefone": "123456789", "email": "teste@example.com", "rede_social": "@teste", "notas": "Nota teste"}
    ui = Ui_Form()
    ui.setupUi(MainWindow, contato_info, None)
    MainWindow.show()
    sys.exit(app.exec())