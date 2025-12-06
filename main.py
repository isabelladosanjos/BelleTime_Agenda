# main.py
import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

# Importa o design da pasta 'views'
from views.ui_janela_cliente import Ui_MainWindow 

# Importa as outras janelas (controladores)
from agenda_window import AgendaWindow
from mensal_window import MensalWindow
from servicos_window import ServicosWindow
from login_window import LoginWindow

import database

# --- FUNÇÃO PARA LOCALIZAR ARQUIVOS (No .exe ou no VS Code) ---
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Belle Time Agenda - Gerenciador")
        
        self.cliente_id_selecionado = None
        self.janela_agenda = None
        self.janela_mensal = None
        self.janela_servicos = None
        
        # Conexões
        self.botao_salvar.clicked.connect(self.salvar_novo_cliente)
        self.botao_atualizar.clicked.connect(self.atualizar_cliente_selecionado)
        self.botao_excluir.clicked.connect(self.deletar_cliente_selecionado)
        self.lista_clientes_widget.currentItemChanged.connect(self.ao_clicar_na_lista)
        
        try: self.botao_novo_agendamento.clicked.connect(self.abrir_janela_agenda)
        except AttributeError: pass
        try: self.botao_ver_mensal.clicked.connect(self.abrir_mensal)
        except AttributeError: pass
        try: self.botao_gerenciar_servicos.clicked.connect(self.abrir_servicos)
        except AttributeError: pass
        try: self.botao_fechar.clicked.connect(self.close)
        except AttributeError: pass
        
        self.carregar_lista_na_tela()
        self.atualizar_relatorios()

    def carregar_lista_na_tela(self):
        self.lista_clientes_widget.clear()
        lista = database.listar_clientes()
        if lista is None: lista = []
        for c in lista:
            # Lista Limpa (usando QListWidgetItem se quiser, ou texto simples aqui)
            from PySide6.QtWidgets import QListWidgetItem
            from PySide6.QtCore import Qt
            
            texto = f"{c['nome']} - {c['telefone']}"
            item = QListWidgetItem(texto)
            item.setData(Qt.UserRole, c['id'])
            self.lista_clientes_widget.addItem(item)
            
    def salvar_novo_cliente(self):
        nome = self.campo_nome.text()
        fone = self.campo_telefone.text()
        if not nome or not fone:
            QMessageBox.warning(self, "Atenção", "Preencha nome e telefone.")
            return
        if database.adicionar_cliente(nome, fone, ""):
            QMessageBox.information(self, "Sucesso", "Cliente salvo!")
            self.campo_nome.clear()
            self.campo_telefone.clear()
            self.carregar_lista_na_tela()
            self.atualizar_relatorios()
        else:
            QMessageBox.critical(self, "Erro", "Falha ao salvar.")

    def ao_clicar_na_lista(self, item):
        if not item: return
        try:
            from PySide6.QtCore import Qt
            self.cliente_id_selecionado = item.data(Qt.UserRole)
            cliente = database.buscar_cliente_por_id(self.cliente_id_selecionado)
            if cliente:
                self.campo_nome.setText(cliente['nome'])
                self.campo_telefone.setText(cliente['telefone'])
        except Exception: pass

    def atualizar_cliente_selecionado(self):
        if not self.cliente_id_selecionado: return
        if database.atualizar_cliente(self.cliente_id_selecionado, self.campo_nome.text(), self.campo_telefone.text(), ""):
            QMessageBox.information(self, "Sucesso", "Atualizado!")
            self.carregar_lista_na_tela()

    def deletar_cliente_selecionado(self):
        if not self.cliente_id_selecionado: return
        if QMessageBox.question(self, "Confirmar", "Excluir?", QMessageBox.Yes|QMessageBox.No) == QMessageBox.Yes:
            if database.excluir_cliente(self.cliente_id_selecionado):
                QMessageBox.information(self, "Sucesso", "Excluído!")
                self.campo_nome.clear()
                self.campo_telefone.clear()
                self.carregar_lista_na_tela()
                self.atualizar_relatorios()
            else:
                QMessageBox.critical(self, "Erro", "Falha ao excluir.")
    
    def atualizar_relatorios(self):
        self.label_total_clientes.setText(f"Total de Clientes: {database.contar_total_clientes()}")
        self.lista_agendamentos_hoje.clear()
        agendamentos = database.listar_agendamentos_hoje()
        if not agendamentos:
            self.lista_agendamentos_hoje.addItem("Nenhum agendamento para hoje.")
        for ag in agendamentos:
            try:
                hora = str(ag['data_hora'])[-8:-3]
                self.lista_agendamentos_hoje.addItem(f"{hora}h | {ag['nome_cliente']} - {ag['nome_servico']}")
            except: pass

    def abrir_janela_agenda(self):
        if self.janela_agenda is None:
            self.janela_agenda = AgendaWindow()
            self.janela_agenda.agendamento_salvo.connect(self.atualizar_relatorios)
        self.janela_agenda.show()
        self.janela_agenda.activateWindow()

    def abrir_mensal(self):
        if self.janela_mensal is None:
            self.janela_mensal = MensalWindow()
            self.janela_mensal.agendamento_excluido.connect(self.atualizar_relatorios)
        self.janela_mensal.carregar_tabela()
        self.janela_mensal.show()
        self.janela_mensal.activateWindow()

    def abrir_servicos(self):
        if self.janela_servicos is None:
            self.janela_servicos = ServicosWindow()
        self.janela_servicos.carregar_lista()
        self.janela_servicos.show()
        self.janela_servicos.activateWindow()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # --- CAMINHO CORRIGIDO PARA A PASTA ASSETS ---
    try:
        style_path = resource_path("assets/style.qss")
        with open(style_path, "r") as f:
            app.setStyleSheet(f.read())
    except FileNotFoundError: pass

    # Abre Login
    login = LoginWindow()
    login.show()
    app.exec() 
    
    if login.login_sucesso:
        window = MainWindow()
        window.show()
        sys.exit(app.exec())
    else:
        sys.exit()