import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from Tela_Login import Ui_Tela_Login
from cadastro_proj import Ui_Tela_Cadastro

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela Principal")

        # Criação do widget principal que permitirá alternar entre as telas de login e cadastro
        self.stacked_widget = QStackedWidget(self)

        # Inicializando as telas de login e cadastro
        self.login_window = Ui_Tela_Login()
        self.cadastro_window = Ui_Tela_Cadastro()

        # Configuração da tela de login e tela de cadastro
        self.login_window.setupUi(self)  # Configura a interface de login
        self.cadastro_window.setupUi(self)  # Configura a interface de cadastro

        # Adicionando as telas ao QStackedWidget
        self.stacked_widget.addWidget(self.login_window.centralwidget)
        self.stacked_widget.addWidget(self.cadastro_window.centralwidget)

        # Definindo a tela inicial (login)
        self.setCentralWidget(self.stacked_widget)

        # Conectar ações para alternar entre telas
        self.login_window.abrir_tela_cadastro = self.show_cadastro_screen
        self.cadastro_window.voltar_para_login = self.show_login_screen

    def show_cadastro_screen(self):
        """Exibe a tela de cadastro."""
        self.stacked_widget.setCurrentWidget(self.cadastro_window.centralwidget)

    def show_login_screen(self):
        """Exibe a tela de login."""
        self.stacked_widget.setCurrentWidget(self.login_window.centralwidget)

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Criação da aplicação
    window = MainWindow()  # Criação da janela principal
    window.show()  # Exibe a janela principal
    sys.exit(app.exec())  # Inicia o loop de eventos da aplicação
