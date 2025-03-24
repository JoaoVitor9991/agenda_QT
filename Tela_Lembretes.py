from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QListWidget, QDialog, QComboBox, QLineEdit, QTextEdit, QMessageBox
from bancodedados import carregar_lembretes, salvar_lembrete, atualizar_lembrete, excluir_lembrete, carregar_contatos
from datetime import datetime

class TelaLembretes(QMainWindow):
    def __init__(self, usuario_id):
        super().__init__()
        self.usuario_id = usuario_id
        self.setWindowTitle("Gerenciar Lembretes")
        self.setFixedSize(600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        self.central_widget.setStyleSheet("""
            background: qlineargradient(
                x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 rgb(20, 20, 30),
                stop: 1 rgb(50, 60, 80)
            );
        """)

        self.btn_adicionar = QPushButton("Adicionar Lembrete")
        self.btn_adicionar.setFont(QFont("Segoe UI", 12, QFont.Bold))
        self.btn_adicionar.setStyleSheet("""
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
        self.btn_adicionar.clicked.connect(self.abrir_tela_adicionar)

        self.lista_lembretes = QListWidget()
        self.lista_lembretes.setStyleSheet("""
            QListWidget {
                background-color: rgb(40, 40, 50);
                color: rgb(255, 255, 255);
                border: 1px solid rgb(80, 80, 100);
                border-radius: 5px;
                padding: 5px;
                font-family: Segoe UI;
                font-size: 12pt;
            }
        """)
        self.lista_lembretes.itemDoubleClicked.connect(self.editar_lembrete)

        self.layout.addWidget(self.btn_adicionar)
        self.layout.addWidget(self.lista_lembretes)

        self.carregar_lembretes()

    def carregar_lembretes(self):
        self.lista_lembretes.clear()
        self.lembretes = carregar_lembretes(self.usuario_id)
        for lembrete in self.lembretes:
            self.lista_lembretes.addItem(f"{lembrete['titulo']} - {lembrete['data_hora']}")

    def validar_data_hora(self, data_hora):
        try:
            datetime.strptime(data_hora, "%Y-%m-%d %H:%M")
            return True
        except ValueError:
            return False

    def abrir_tela_adicionar(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Adicionar Lembrete")
        dialog.setFixedSize(400, 300)
        layout = QVBoxLayout(dialog)

        combo_contato = QComboBox()
        combo_contato.addItem("Nenhum contato", None)
        contatos = carregar_contatos(self.usuario_id)
        for contato in contatos:
            combo_contato.addItem(contato['nome'], contato['id'])

        line_titulo = QLineEdit()
        line_titulo.setPlaceholderText("Título (ex.: Reunião com João)")
        line_data_hora = QLineEdit()
        line_data_hora.setPlaceholderText("Data e hora (YYYY-MM-DD HH:MM)")
        text_descricao = QTextEdit()
        text_descricao.setPlaceholderText("Descrição (opcional)")

        btn_salvar = QPushButton("Salvar")
        btn_salvar.clicked.connect(lambda: self.salvar_lembrete(combo_contato.currentData(), line_titulo.text(), line_data_hora.text(), text_descricao.toPlainText(), dialog))

        layout.addWidget(combo_contato)
        layout.addWidget(line_titulo)
        layout.addWidget(line_data_hora)
        layout.addWidget(text_descricao)
        layout.addWidget(btn_salvar)
        dialog.exec()

    def salvar_lembrete(self, contato_id, titulo, data_hora, descricao, dialog):
        if not titulo or not data_hora:
            QMessageBox.warning(self, "Erro", "Título e data/hora são obrigatórios.")
            return
        if not self.validar_data_hora(data_hora):
            QMessageBox.warning(self, "Erro", "Formato de data/hora inválido. Use o formato YYYY-MM-DD HH:MM (ex.: 2025-03-24 14:00).")
            return
        salvar_lembrete(self.usuario_id, contato_id, titulo, data_hora, descricao)
        self.carregar_lembretes()
        dialog.accept()

    def editar_lembrete(self, item):
        index = self.lista_lembretes.row(item)
        lembrete = self.lembretes[index]

        dialog = QDialog(self)
        dialog.setWindowTitle("Editar Lembrete")
        dialog.setFixedSize(400, 300)
        layout = QVBoxLayout(dialog)

        combo_contato = QComboBox()
        combo_contato.addItem("Nenhum contato", None)
        contatos = carregar_contatos(self.usuario_id)
        for contato in contatos:
            combo_contato.addItem(contato['nome'], contato['id'])
        if lembrete['contato_id']:
            for i in range(combo_contato.count()):
                if combo_contato.itemData(i) == lembrete['contato_id']:
                    combo_contato.setCurrentIndex(i)
                    break

        line_titulo = QLineEdit(lembrete['titulo'])
        line_data_hora = QLineEdit(lembrete['data_hora'])
        text_descricao = QTextEdit(lembrete['descricao'] if lembrete['descricao'] else "")

        btn_salvar = QPushButton("Salvar")
        btn_salvar.clicked.connect(lambda: self.atualizar_lembrete(lembrete['id'], combo_contato.currentData(), line_titulo.text(), line_data_hora.text(), text_descricao.toPlainText(), dialog))

        btn_excluir = QPushButton("Excluir")
        btn_excluir.clicked.connect(lambda: self.excluir_lembrete(lembrete['id'], dialog))

        layout.addWidget(combo_contato)
        layout.addWidget(line_titulo)
        layout.addWidget(line_data_hora)
        layout.addWidget(text_descricao)
        layout.addWidget(btn_salvar)
        layout.addWidget(btn_excluir)
        dialog.exec()

    def atualizar_lembrete(self, lembrete_id, contato_id, titulo, data_hora, descricao, dialog):
        if not titulo or not data_hora:
            QMessageBox.warning(self, "Erro", "Título e data/hora são obrigatórios.")
            return
        if not self.validar_data_hora(data_hora):
            QMessageBox.warning(self, "Erro", "Formato de data/hora inválido. Use o formato YYYY-MM-DD HH:MM (ex.: 2025-03-24 14:00).")
            return
        atualizar_lembrete(lembrete_id, contato_id, titulo, data_hora, descricao)
        self.carregar_lembretes()
        dialog.accept()

    def excluir_lembrete(self, lembrete_id, dialog):
        if QMessageBox.question(self, "Confirmação", "Deseja excluir este lembrete?") == QMessageBox.Yes:
            excluir_lembrete(lembrete_id)
            self.carregar_lembretes()
            dialog.accept()