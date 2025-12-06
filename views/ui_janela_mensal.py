# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_mensal.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabela_mensal = QTableWidget(self.centralwidget)
        if (self.tabela_mensal.columnCount() < 4):
            self.tabela_mensal.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabela_mensal.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabela_mensal.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabela_mensal.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabela_mensal.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabela_mensal.setObjectName(u"tabela_mensal")
        self.tabela_mensal.setGeometry(QRect(140, 100, 401, 221))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 20, 111, 71))
        self.botao_fechar = QPushButton(self.centralwidget)
        self.botao_fechar.setObjectName(u"botao_fechar")
        self.botao_fechar.setGeometry(QRect(440, 370, 101, 51))
        self.botao_excluir_agendamento = QPushButton(self.centralwidget)
        self.botao_excluir_agendamento.setObjectName(u"botao_excluir_agendamento")
        self.botao_excluir_agendamento.setGeometry(QRect(140, 370, 161, 51))
        self.label_faturamento_mensal = QLabel(self.centralwidget)
        self.label_faturamento_mensal.setObjectName(u"label_faturamento_mensal")
        self.label_faturamento_mensal.setGeometry(QRect(260, 470, 221, 51))
        font = QFont()
        font.setBold(True)
        self.label_faturamento_mensal.setFont(font)
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
        ___qtablewidgetitem = self.tabela_mensal.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem1 = self.tabela_mensal.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem2 = self.tabela_mensal.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Servi\u00e7o", None));
        ___qtablewidgetitem3 = self.tabela_mensal.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Relat\u00f3rio Mensal", None))
        self.botao_fechar.setText(QCoreApplication.translate("MainWindow", u"Fechar", None))
        self.botao_excluir_agendamento.setText(QCoreApplication.translate("MainWindow", u"Excluir Selecionado", None))
        self.label_faturamento_mensal.setText(QCoreApplication.translate("MainWindow", u"Faturamento Mensal: R$: 0,00", None))
    # retranslateUi

