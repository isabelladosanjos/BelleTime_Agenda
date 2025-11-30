# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_servicos.ui'
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
        self.lista_servicos_widget = QListWidget(self.centralwidget)
        self.lista_servicos_widget.setObjectName(u"lista_servicos_widget")
        self.lista_servicos_widget.setGeometry(QRect(370, 20, 371, 231))
        self.campo_nome_servico = QLineEdit(self.centralwidget)
        self.campo_nome_servico.setObjectName(u"campo_nome_servico")
        self.campo_nome_servico.setGeometry(QRect(110, 20, 181, 31))
        self.campo_duracao = QLineEdit(self.centralwidget)
        self.campo_duracao.setObjectName(u"campo_duracao")
        self.campo_duracao.setGeometry(QRect(110, 80, 181, 31))
        self.campo_preco = QLineEdit(self.centralwidget)
        self.campo_preco.setObjectName(u"campo_preco")
        self.campo_preco.setGeometry(QRect(110, 140, 181, 31))
        self.botao_salvar_servico = QPushButton(self.centralwidget)
        self.botao_salvar_servico.setObjectName(u"botao_salvar_servico")
        self.botao_salvar_servico.setGeometry(QRect(30, 210, 91, 41))
        self.botao_atualizar_servico = QPushButton(self.centralwidget)
        self.botao_atualizar_servico.setObjectName(u"botao_atualizar_servico")
        self.botao_atualizar_servico.setGeometry(QRect(130, 210, 91, 41))
        self.botao_excluir_servico = QPushButton(self.centralwidget)
        self.botao_excluir_servico.setObjectName(u"botao_excluir_servico")
        self.botao_excluir_servico.setGeometry(QRect(230, 210, 91, 41))
        self.botao_fechar = QPushButton(self.centralwidget)
        self.botao_fechar.setObjectName(u"botao_fechar")
        self.botao_fechar.setGeometry(QRect(650, 280, 91, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 20, 91, 31))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 81, 41))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 130, 91, 41))
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
        self.botao_salvar_servico.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
        self.botao_atualizar_servico.setText(QCoreApplication.translate("MainWindow", u"Atualizar", None))
        self.botao_excluir_servico.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.botao_fechar.setText(QCoreApplication.translate("MainWindow", u"Fechar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Servi\u00e7o:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Dura\u00e7\u00e3o:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Pre\u00e7o:", None))
    # retranslateUi

