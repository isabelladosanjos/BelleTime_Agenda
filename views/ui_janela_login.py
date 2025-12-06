# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'janela_login.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(480, 298)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.campo_usuario = QLineEdit(self.centralwidget)
        self.campo_usuario.setObjectName(u"campo_usuario")
        self.campo_usuario.setGeometry(QRect(160, 70, 141, 31))
        self.campo_senha = QLineEdit(self.centralwidget)
        self.campo_senha.setObjectName(u"campo_senha")
        self.campo_senha.setGeometry(QRect(160, 110, 141, 31))
        self.campo_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.botao_entrar = QPushButton(self.centralwidget)
        self.botao_entrar.setObjectName(u"botao_entrar")
        self.botao_entrar.setGeometry(QRect(210, 160, 91, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 20, 101, 31))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(True)
        self.label.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 480, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.campo_usuario.setText("")
        self.campo_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.campo_senha.setText("")
        self.campo_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.botao_entrar.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Belle Time", None))
    # retranslateUi

