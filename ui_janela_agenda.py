# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_agenda.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateTimeEdit, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 60, 71, 41))
        self.combo_servicos = QComboBox(self.centralwidget)
        self.combo_servicos.setObjectName(u"combo_servicos")
        self.combo_servicos.setGeometry(QRect(90, 120, 241, 41))
        self.combo_clientes = QComboBox(self.centralwidget)
        self.combo_clientes.setObjectName(u"combo_clientes")
        self.combo_clientes.setGeometry(QRect(90, 60, 241, 41))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 190, 121, 41))
        self.campo_data_hora = QDateTimeEdit(self.centralwidget)
        self.campo_data_hora.setObjectName(u"campo_data_hora")
        self.campo_data_hora.setGeometry(QRect(30, 240, 201, 41))
        self.botao_salvar_agendamento = QPushButton(self.centralwidget)
        self.botao_salvar_agendamento.setObjectName(u"botao_salvar_agendamento")
        self.botao_salvar_agendamento.setGeometry(QRect(30, 310, 201, 41))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 120, 71, 41))
        self.botao_fechar = QPushButton(self.centralwidget)
        self.botao_fechar.setObjectName(u"botao_fechar")
        self.botao_fechar.setGeometry(QRect(240, 310, 91, 41))
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
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cliente:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Data e Hor\u00e1rio:", None))
        self.botao_salvar_agendamento.setText(QCoreApplication.translate("MainWindow", u"Salvar Agendamento", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Servi\u00e7o:", None))
        self.botao_fechar.setText(QCoreApplication.translate("MainWindow", u"Fechar", None))
    # retranslateUi

