# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TelaResultado.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SaidaFerramenta(object):
    def setupUi(self, SaidaFerramenta):
        SaidaFerramenta.setObjectName("SaidaFerramenta")
        SaidaFerramenta.resize(503, 418)
        self.centralwidget = QtWidgets.QWidget(SaidaFerramenta)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textEdit_Saida = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_Saida.setObjectName("textEdit_Saida")
        self.verticalLayout_2.addWidget(self.textEdit_Saida)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_Extra = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Extra.setObjectName("pushButton_Extra")
        self.verticalLayout.addWidget(self.pushButton_Extra)
        self.pushButton_Voltar = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Voltar.setStyleSheet("background-color: rgb(196, 160, 0);")
        self.pushButton_Voltar.setObjectName("pushButton_Voltar")
        self.verticalLayout.addWidget(self.pushButton_Voltar)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        SaidaFerramenta.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SaidaFerramenta)
        self.statusbar.setObjectName("statusbar")
        SaidaFerramenta.setStatusBar(self.statusbar)

        self.retranslateUi(SaidaFerramenta)
        QtCore.QMetaObject.connectSlotsByName(SaidaFerramenta)

    def retranslateUi(self, SaidaFerramenta):
        _translate = QtCore.QCoreApplication.translate
        SaidaFerramenta.setWindowTitle(_translate("SaidaFerramenta", "Pagina dos Resultados"))
        self.pushButton_Extra.setText(_translate("SaidaFerramenta", "Botao Extra"))
        self.pushButton_Voltar.setText(_translate("SaidaFerramenta", "Voltar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SaidaFerramenta = QtWidgets.QMainWindow()
    ui = Ui_SaidaFerramenta()
    ui.setupUi(SaidaFerramenta)
    SaidaFerramenta.show()
    sys.exit(app.exec_())
