import mysql.connector
from PySide6.QtCore import QCoreApplication, QMetaObject
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QFrame, QLineEdit, QLabel, QDateEdit, QTextEdit, QMessageBox

def conectar():
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="agenda"
        )
        return conexao
    except mysql.connector.Error as e:
        print(f"❌ Erro ao conectar ao MySQL: {e}")
        return None

def salvar_contato_db(nome, email, telefone, data_nascimento, perfil_rede_social, notas, usuario_id=1):
    """Insere um novo contato no banco de dados."""
    conexao = conectar()
    if conexao is None:
        print("⚠ Erro na conexão com o banco de dados.")
        return False

    cursor = None
    try:
        cursor = conexao.cursor()
        print(f"📞 Salvando no banco - Nome: {nome}, Telefone: {telefone}, Data: {data_nascimento}")
        sql = "INSERT INTO contatos (nome, email, telefone, data_nascimento, perfil_rede_social, notas, usuario_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        valores = (nome, email, telefone, data_nascimento, perfil_rede_social, notas, usuario_id)
        cursor.execute(sql, valores)
        conexao.commit()
        print("✅ Contato salvo com sucesso!")
        return True
    except mysql.connector.Error as e:
        print(f"❌ Erro ao salvar contato: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

class Ui_tela_add_contato(object):
    def setupUi(self, tela_add_contato, main_window):
        self.main_window = main_window
        tela_add_contato.setObjectName("tela_add_contato")
        tela_add_contato.resize(800, 600)

        self.centralwidget = QWidget(tela_add_contato)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QFrame(self.centralwidget)
        self.frame.setGeometry(0, 0, 800, 600)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)

        font_label = QFont()
        font_label.setPointSize(10)
        font_label.setBold(True)

        self.txt_nome = QLabel("Nome:", self.frame)
        self.txt_nome.setFont(font_label)
        self.txt_nome.setGeometry(50, 50, 200, 20)

        self.line_nome = QLineEdit(self.frame)
        self.line_nome.setGeometry(50, 80, 700, 25)

        self.txt_contato = QLabel("Contato:", self.frame)
        self.txt_contato.setFont(font_label)
        self.txt_contato.setGeometry(50, 120, 200, 20)

        self.line_contato = QLineEdit(self.frame)
        self.line_contato.setGeometry(50, 150, 700, 25)
        #self.line_contato.setInputMask("(99) 99999-9999")  # Descomente se quiser a máscara

        self.txt_email = QLabel("Email:", self.frame)
        self.txt_email.setFont(font_label)
        self.txt_email.setGeometry(50, 190, 200, 20)

        self.line_email = QLineEdit(self.frame)
        self.line_email.setGeometry(50, 220, 700, 25)

        self.txt_data_nascimento = QLabel("Data de Nascimento:", self.frame)
        self.txt_data_nascimento.setFont(font_label)
        self.txt_data_nascimento.setGeometry(50, 260, 200, 20)

        self.dateEdit_Data_nascimento = QDateEdit(self.frame)
        self.dateEdit_Data_nascimento.setGeometry(50, 290, 150, 25)

        self.txt_perfil_rede_social = QLabel("Perfil de Rede Social:", self.frame)
        self.txt_perfil_rede_social.setFont(font_label)
        self.txt_perfil_rede_social.setGeometry(50, 330, 200, 20)

        self.line_perfil_rede_social = QLineEdit(self.frame)
        self.line_perfil_rede_social.setGeometry(50, 360, 700, 25)

        self.txt_notas = QLabel("Notas:", self.frame)
        self.txt_notas.setFont(font_label)
        self.txt_notas.setGeometry(50, 400, 200, 20)

        self.textEdit_notas = QTextEdit(self.frame)
        self.textEdit_notas.setGeometry(50, 430, 700, 100)

        font_button = QFont()
        font_button.setBold(True)

        self.pushButton_Salvar = QPushButton("Salvar", self.frame)
        self.pushButton_Salvar.setFont(font_button)
        self.pushButton_Salvar.setGeometry(620, 550, 130, 40)
        self.pushButton_Salvar.setStyleSheet("color: white; background-color: blue;")

        self.pushButton_Voltar = QPushButton("Voltar", self.frame)
        self.pushButton_Voltar.setFont(font_button)
        self.pushButton_Voltar.setGeometry(50, 550, 130, 40)
        self.pushButton_Voltar.setStyleSheet("color: white; background-color: red;")

        tela_add_contato.setCentralWidget(self.centralwidget)

        self.retranslateUi(tela_add_contato)
        self.pushButton_Salvar.clicked.connect(self.salvar_contato)
        self.pushButton_Voltar.clicked.connect(lambda: self.voltar_para_contatos(tela_add_contato, main_window))
        QMetaObject.connectSlotsByName(tela_add_contato)

    def retranslateUi(self, tela_add_contato):
        tela_add_contato.setWindowTitle("Adicionar Contato")

    def salvar_contato(self):
        nome = self.line_nome.text()
        telefone = self.line_contato.text().strip()  # Ajustado para "telefone"
        email = self.line_email.text()
        data_nascimento = self.dateEdit_Data_nascimento.date().toString("yyyy-MM-dd")
        perfil_rede_social = self.line_perfil_rede_social.text()
        notas = self.textEdit_notas.toPlainText()

        usuario_id = getattr(self, "usuario_id", None)
        if usuario_id is None:
            QMessageBox.warning(None, "Erro", "ID do usuário não encontrado")
            return

        
        sucesso = salvar_contato_db(nome, email, telefone, data_nascimento, perfil_rede_social, notas, usuario_id)

        if sucesso:
            QMessageBox.information(None, "Sucesso", "Contato salvo com sucesso!")
            if self.main_window and hasattr(self.main_window, "carregar_contatos"):
                self.main_window.carregar_contatos()  # Atualiza a lista na tela principal
            self.voltar_para_contatos(None, None)
        else:
            QMessageBox.warning(None, "Erro", "Falha ao salvar o contato!")

    def voltar_para_contatos(self, tela_add_contato, main_window):
        if tela_add_contato:
            tela_add_contato.close()

if __name__ == "__main__":
    app = QApplication([])
    MainWindow = QMainWindow()
    ui = Ui_tela_add_contato()
    ui.setupUi(MainWindow, MainWindow)
    MainWindow.show()
    app.exec()