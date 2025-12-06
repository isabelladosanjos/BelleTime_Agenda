# login_window.py
import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox
# Importa da pasta VIEWS
from views.ui_janela_login import Ui_MainWindow
import database

class LoginWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Acesso Restrito")
        self.login_sucesso = False
        
        self.botao_entrar.clicked.connect(self.tentar_login)
        self.campo_senha.returnPressed.connect(self.tentar_login)

    def tentar_login(self):
        user = self.campo_usuario.text().strip()
        pwd = self.campo_senha.text().strip()
        
        if database.verificar_login(user, pwd):
            self.login_sucesso = True
            self.close() 
        else:
            QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos.")