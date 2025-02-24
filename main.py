from PySide6.QtWidgets import QApplication, QMainWindow
from untitled import Ui_Tela_Login
from contatos import Ui_tela_contatos
import sys
class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tela_contatos = Ui_tela_contatos()
        self.tela_login = Ui_Tela_Login()

        self.tela_login.setupUi(self)
    def conectar(self):
        
        self.window_login.login()  
        self.window_contatos.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = main_window()
    window.show()
    sys.exit(app.exec())

