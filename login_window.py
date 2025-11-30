# login_window.py
import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox
from ui_janela_login import Ui_MainWindow
import database

class LoginWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Login - Belle Time")
        
        self.botao_entrar.clicked.connect(self.tentar_login)
        # Permite apertar ENTER no campo de senha para entrar
        self.campo_senha.returnPressed.connect(self.tentar_login)
        
        self.login_sucesso = False # Variável de controle

    def tentar_login(self):
        # AQUI É O ERRO: SEMPRE LIMPE O INPUT ANTES DE ENVIAR
        usuario = self.campo_usuario.text().strip()
        senha = self.campo_senha.text().strip()
        
        if database.verificar_login(usuario, senha):
            self.login_sucesso = True
            self.close() # ...
        else:
            QMessageBox.warning(self, "Erro", "Login incorreto!")