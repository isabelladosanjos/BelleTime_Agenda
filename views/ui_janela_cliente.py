# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_cliente.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.campo_nome = QLineEdit(self.centralwidget)
        self.campo_nome.setObjectName(u"campo_nome")
        self.campo_nome.setGeometry(QRect(80, 60, 191, 41))
        self.campo_telefone = QLineEdit(self.centralwidget)
        self.campo_telefone.setObjectName(u"campo_telefone")
        self.campo_telefone.setGeometry(QRect(80, 120, 191, 41))
        self.lista_agendamentos_hoje = QListWidget(self.centralwidget)
        self.lista_agendamentos_hoje.setObjectName(u"lista_agendamentos_hoje")
        self.lista_agendamentos_hoje.setGeometry(QRect(20, 340, 256, 192))
        self.lista_clientes_widget = QListWidget(self.centralwidget)
        self.lista_clientes_widget.setObjectName(u"lista_clientes_widget")
        self.lista_clientes_widget.setGeometry(QRect(320, 50, 281, 171))
        self.botao_salvar = QPushButton(self.centralwidget)
        self.botao_salvar.setObjectName(u"botao_salvar")
        self.botao_salvar.setGeometry(QRect(20, 190, 81, 31))
        self.botao_atualizar = QPushButton(self.centralwidget)
        self.botao_atualizar.setObjectName(u"botao_atualizar")
        self.botao_atualizar.setGeometry(QRect(200, 190, 81, 31))
        self.botao_excluir = QPushButton(self.centralwidget)
        self.botao_excluir.setObjectName(u"botao_excluir")
        self.botao_excluir.setGeometry(QRect(110, 190, 81, 31))
        self.label_total_clientes = QLabel(self.centralwidget)
        self.label_total_clientes.setObjectName(u"label_total_clientes")
        self.label_total_clientes.setGeometry(QRect(20, 240, 231, 51))
        self.botao_novo_agendamento = QPushButton(self.centralwidget)
        self.botao_novo_agendamento.setObjectName(u"botao_novo_agendamento")
        self.botao_novo_agendamento.setGeometry(QRect(320, 430, 161, 41))
        self.botao_ver_mensal = QPushButton(self.centralwidget)
        self.botao_ver_mensal.setObjectName(u"botao_ver_mensal")
        self.botao_ver_mensal.setGeometry(QRect(320, 490, 161, 41))
        self.botao_fechar = QPushButton(self.centralwidget)
        self.botao_fechar.setObjectName(u"botao_fechar")
        self.botao_fechar.setGeometry(QRect(620, 490, 161, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 141, 41))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 141, 41))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 120, 141, 41))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(320, 10, 191, 41))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 290, 121, 41))
        self.botao_gerenciar_servicos = QPushButton(self.centralwidget)
        self.botao_gerenciar_servicos.setObjectName(u"botao_gerenciar_servicos")
        self.botao_gerenciar_servicos.setGeometry(QRect(320, 370, 161, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.botao_salvar.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.botao_atualizar.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.botao_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.label_total_clientes.setText(QCoreApplication.translate("MainWindow", u"Total de clientes do sal\u00e3o: 0", None))
        self.botao_novo_agendamento.setText(QCoreApplication.translate("MainWindow", u"Novo Agendamento", None))
        self.botao_ver_mensal.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio Mensal", None))
        self.botao_fechar.setText(QCoreApplication.translate("MainWindow", u"Fechar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Adicionar Cliente:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nome:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Telefone:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Clientes Cadastrados: ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Agendados hoje:", None))
        self.botao_gerenciar_servicos.setText(QCoreApplication.translate("MainWindow", u"Gerenciar Servi\u00e7os", None))
    # retranslateUi

