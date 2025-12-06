# agenda_window.py
import sys
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import QDateTime, Signal

# Importa da pasta VIEWS
from views.ui_janela_agenda import Ui_MainWindow 
import database

class AgendaWindow(QMainWindow, Ui_MainWindow):
    agendamento_salvo = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Novo Agendamento")
        self.botao_salvar_agendamento.clicked.connect(self.salvar_agendamento)
        
        try: self.botao_fechar.clicked.connect(self.close)
        except AttributeError: pass
        
        self.campo_data_hora.setDateTime(QDateTime.currentDateTime())
        self.campo_data_hora.setCalendarPopup(True) 
        self.carregar_dropdowns()

    def carregar_dropdowns(self):
        self.combo_clientes.clear()
        lista_clientes = database.listar_clientes_dropdown()
        for cliente in lista_clientes:
            self.combo_clientes.addItem(cliente['nome'], userData=cliente['id'])
            
        self.combo_servicos.clear()
        lista_servicos = database.listar_servicos_dropdown()
        for servico in lista_servicos:
            texto = f"{servico['nome']} (R$ {servico['preco']})"
            self.combo_servicos.addItem(texto, userData=servico['id'])
            
    def salvar_agendamento(self):
        cliente_id = self.combo_clientes.currentData()
        servico_id = self.combo_servicos.currentData()
        
        data_hora_suja = self.campo_data_hora.dateTime().toPython()
        data_hora = data_hora_suja.replace(second=0, microsecond=0)
        
        if not cliente_id or not servico_id:
            QMessageBox.warning(self, "Atenção", "Selecione Cliente e Serviço!")
            return

        if database.verificar_horario_ocupado(data_hora):
            hora_fmt = data_hora.strftime("%d/%m às %H:%M")
            QMessageBox.warning(self, "Horário Indisponível", f"Já existe um agendamento para {hora_fmt}.")
            return 

        if database.adicionar_agendamento(cliente_id, servico_id, data_hora):
            QMessageBox.information(self, "Sucesso", "Agendamento criado!")
            self.agendamento_salvo.emit()
            self.close()
        else:
            QMessageBox.critical(self, "Erro", "Falha ao agendar.")