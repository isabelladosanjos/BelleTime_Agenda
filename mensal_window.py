import sys
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox, QAbstractItemView
from PySide6.QtCore import Qt, Signal

from ui_janela_mensal import Ui_MainWindow 
import database

class MensalWindow(QMainWindow, Ui_MainWindow):
    agendamento_excluido = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Relatório Mensal Detalhado")
        
        try:
            self.botao_fechar.clicked.connect(self.close)
        except AttributeError: pass

        try:
            self.botao_excluir_agendamento.clicked.connect(self.deletar_agendamento)
        except AttributeError: 
            print("Aviso: Botão 'botao_excluir_agendamento' não encontrado.")

        self.tabela_mensal.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tabela_mensal.setSelectionMode(QAbstractItemView.SingleSelection)

        self.carregar_tabela()

    def carregar_tabela(self):
        """Preenche a tabela e atualiza o faturamento."""
        dados = database.listar_agendamentos_mes_tabela()

        self.tabela_mensal.setRowCount(0)
        self.tabela_mensal.setRowCount(len(dados))
        self.tabela_mensal.setColumnCount(4)
        self.tabela_mensal.setHorizontalHeaderLabels(["Data", "Cliente", "Serviço", "Valor"])
        
        for linha, ag in enumerate(dados):
            try:
                data_fmt = ag['data_hora'].strftime("%d/%m/%Y %H:%M")
                preco_fmt = f"R$ {ag['preco']:.2f}"
                
                item_data = QTableWidgetItem(data_fmt)
                item_data.setData(Qt.UserRole, ag['id']) 
                
                self.tabela_mensal.setItem(linha, 0, item_data)
                self.tabela_mensal.setItem(linha, 1, QTableWidgetItem(ag['cliente']))
                self.tabela_mensal.setItem(linha, 2, QTableWidgetItem(ag['servico']))
                self.tabela_mensal.setItem(linha, 3, QTableWidgetItem(preco_fmt))
            except Exception as e:
                print(f"Erro ao preencher linha {linha}: {e}")

        faturamento_total = sum(ag['preco'] for ag in dados)
        
        texto_dinheiro = f"Faturamento Total: R$ {faturamento_total:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        
        try:
            self.label_faturamento_mensal.setText(texto_dinheiro)
        except AttributeError:
            pass 

    def deletar_agendamento(self):
        """Exclui o agendamento da linha selecionada."""
        linha_atual = self.tabela_mensal.currentRow()
        
        if linha_atual == -1:
            QMessageBox.warning(self, "Atenção", "Selecione um agendamento na tabela para excluir.")
            return
            
        item_data = self.tabela_mensal.item(linha_atual, 0)
        id_agendamento = item_data.data(Qt.UserRole)
        
        confirm = QMessageBox.question(self, "Confirmar", "Tem certeza que deseja excluir este agendamento?", QMessageBox.Yes | QMessageBox.No)
        
        if confirm == QMessageBox.Yes:
            if database.excluir_agendamento(id_agendamento):
                QMessageBox.information(self, "Sucesso", "Agendamento excluído!")
                self.carregar_tabela()
                self.agendamento_excluido.emit()
            else:
                QMessageBox.critical(self, "Erro", "Não foi possível excluir.")