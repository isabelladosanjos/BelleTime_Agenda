# servicos_window.py 
import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox, QListWidgetItem 
from PySide6.QtCore import Qt 

from ui_janela_servicos import Ui_MainWindow 
import database

class ServicosWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Gerenciar Cardápio de Serviços")
        
        self.servico_id_selecionado = None
        
        # Conexões
        self.botao_salvar_servico.clicked.connect(self.salvar)
        self.botao_atualizar_servico.clicked.connect(self.atualizar)
        self.botao_excluir_servico.clicked.connect(self.excluir)
        self.lista_servicos_widget.currentItemChanged.connect(self.ao_clicar_na_lista)
        
        try:
            self.botao_fechar.clicked.connect(self.close)
        except AttributeError: pass

        self.carregar_lista()

    def carregar_lista(self):
        self.lista_servicos_widget.clear()
        lista = database.listar_servicos_crud()
        
        for servico in lista:

            texto_visivel = f"{servico['nome']} - R$ {servico['preco']} ({servico['duracao_minutos']} min)"
            item = QListWidgetItem(texto_visivel)
            item.setData(Qt.UserRole, servico['id'])
            self.lista_servicos_widget.addItem(item)

    def limpar_campos(self):
        self.campo_nome_servico.clear()
        self.campo_duracao.clear()
        self.campo_preco.clear()
        self.servico_id_selecionado = None

    def salvar(self):
        nome = self.campo_nome_servico.text()
        duracao = self.campo_duracao.text()
        preco = self.campo_preco.text().replace(",", ".")
        
        if not nome or not preco:
            QMessageBox.warning(self, "Atenção", "Preencha nome e preço.")
            return

        if database.adicionar_servico(nome, duracao, preco):
            QMessageBox.information(self, "Sucesso", "Serviço criado!")
            self.limpar_campos()
            self.carregar_lista()
        else:
            QMessageBox.critical(self, "Erro", "Falha ao salvar.")

    def ao_clicar_na_lista(self, item):
        if not item: return
        try:
            self.servico_id_selecionado = item.data(Qt.UserRole)
            
            servico = database.buscar_servico_por_id(self.servico_id_selecionado)
            if servico:
                self.campo_nome_servico.setText(servico['nome'])
                self.campo_duracao.setText(str(servico['duracao_minutos']))
                self.campo_preco.setText(str(servico['preco']))
        except Exception: pass

    def atualizar(self):
        if not self.servico_id_selecionado: 
            QMessageBox.warning(self, "Atenção", "Selecione um serviço para atualizar.")
            return
            
        nome = self.campo_nome_servico.text()
        duracao = self.campo_duracao.text()
        preco = self.campo_preco.text().replace(",", ".")
        
        if database.atualizar_servico(self.servico_id_selecionado, nome, duracao, preco):
            QMessageBox.information(self, "Sucesso", "Serviço atualizado!")
            self.carregar_lista()
            self.limpar_campos()

    def excluir(self):
        if not self.servico_id_selecionado: 
            QMessageBox.warning(self, "Atenção", "Selecione um serviço para excluir.")
            return
            
        confirm = QMessageBox.question(self, "Confirmar", "Excluir este serviço do cardápio?", QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.Yes:
            if database.excluir_servico(self.servico_id_selecionado):
                QMessageBox.information(self, "Sucesso", "Serviço excluído!")
                self.limpar_campos()
                self.carregar_lista()
            else:
                QMessageBox.critical(self, "Erro", "Não foi possível excluir.\nEste serviço provavelmente já foi realizado em algum agendamento passado.")
