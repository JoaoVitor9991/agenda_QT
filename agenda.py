import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from Tela_Login import Ui_Tela_Login
from cadastro_proj import Ui_Tela_Cadastro

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela Principal")

        
        self.stacked_widget = QStackedWidget(self)

        
        self.login_window = Ui_Tela_Login()
        self.cadastro_window = Ui_Tela_Cadastro()

       
        self.login_window.setupUi(self) 
        self.cadastro_window.setupUi(self)  

        
        self.stacked_widget.addWidget(self.login_window.centralwidget)
        self.stacked_widget.addWidget(self.cadastro_window.centralwidget)

        
        self.setCentralWidget(self.stacked_widget)

        
        self.login_window.abrir_tela_cadastro = self.show_cadastro_screen
        self.cadastro_window.voltar_para_login = self.show_login_screen

    def show_cadastro_screen(self):
        """Exibe a tela de cadastro."""
        self.stacked_widget.setCurrentWidget(self.cadastro_window.centralwidget)

    def show_login_screen(self):
        """Exibe a tela de login."""
        self.stacked_widget.setCurrentWidget(self.login_window.centralwidget)

if __name__ == "__main__":
    app = QApplication(sys.argv)  
    window = MainWindow()  
    window.show()  
    sys.exit(app.exec())  
