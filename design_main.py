# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(811, 690)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.search_prodName_lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.search_prodName_lineEdit.setObjectName("search_prodName_lineEdit")
        self.horizontalLayout.addWidget(self.search_prodName_lineEdit)
        self.verticalLayout_7.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.from_dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.from_dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2019, 1, 1), QtCore.QTime(0, 0, 0)))
        self.from_dateEdit.setObjectName("from_dateEdit")
        self.horizontalLayout_2.addWidget(self.from_dateEdit)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.to_dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.to_dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.to_dateEdit.setObjectName("to_dateEdit")
        self.horizontalLayout_2.addWidget(self.to_dateEdit)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.save_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.save_pushButton.setObjectName("save_pushButton")
        self.horizontalLayout_3.addWidget(self.save_pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_3.addWidget(self.progressBar)
        self.search_prodName_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.search_prodName_pushButton.setObjectName("search_prodName_pushButton")
        self.horizontalLayout_3.addWidget(self.search_prodName_pushButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.contracts_listWidget = QtWidgets.QListWidget(self.groupBox)
        self.contracts_listWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.contracts_listWidget.setAlternatingRowColors(True)
        self.contracts_listWidget.setWordWrap(True)
        self.contracts_listWidget.setObjectName("contracts_listWidget")
        self.verticalLayout_7.addWidget(self.contracts_listWidget)
        self.horizontalLayout_8.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.summary_textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.summary_textBrowser.setObjectName("summary_textBrowser")
        self.gridLayout.addWidget(self.summary_textBrowser, 0, 0, 1, 1)
        self.horizontalLayout_8.addWidget(self.groupBox_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.year_price_qlabel = QtWidgets.QLabel(self.groupBox_3)
        self.year_price_qlabel.setFrameShape(QtWidgets.QFrame.Box)
        self.year_price_qlabel.setText("")
        self.year_price_qlabel.setObjectName("year_price_qlabel")
        self.horizontalLayout_4.addWidget(self.year_price_qlabel)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.price_from_lineEdit = QtWidgets.QLineEdit(self.groupBox_5)
        self.price_from_lineEdit.setObjectName("price_from_lineEdit")
        self.horizontalLayout_5.addWidget(self.price_from_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox_5)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.price_to_lineEdit = QtWidgets.QLineEdit(self.groupBox_5)
        self.price_to_lineEdit.setObjectName("price_to_lineEdit")
        self.horizontalLayout_6.addWidget(self.price_to_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addWidget(self.groupBox_5)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_7.setObjectName("groupBox_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.regression_checkBox = QtWidgets.QCheckBox(self.groupBox_7)
        self.regression_checkBox.setObjectName("regression_checkBox")
        self.verticalLayout_3.addWidget(self.regression_checkBox)
        self.verticalLayout_4.addWidget(self.groupBox_7)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.units_listWidget = QtWidgets.QListWidget(self.groupBox_6)
        self.units_listWidget.setAlternatingRowColors(True)
        self.units_listWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.units_listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.units_listWidget.setSelectionRectVisible(False)
        self.units_listWidget.setObjectName("units_listWidget")
        self.verticalLayout.addWidget(self.units_listWidget)
        self.verticalLayout_6.addWidget(self.groupBox_6)
        self.horizontalLayout_4.addWidget(self.groupBox_4)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 811, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Поиск по наименованию продукта"))
        self.label_3.setText(_translate("MainWindow", "Наименование:"))
        self.search_prodName_lineEdit.setText(_translate("MainWindow", "Гистологические кассеты"))
        self.label.setText(_translate("MainWindow", "Временной период:"))
        self.label_2.setText(_translate("MainWindow", "-"))
        self.save_pushButton.setText(_translate("MainWindow", "Сохранить"))
        self.search_prodName_pushButton.setText(_translate("MainWindow", "Поиск"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Превью данных"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Анализ данных"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Настройки"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Диапазон цен"))
        self.label_4.setText(_translate("MainWindow", "От"))
        self.label_5.setText(_translate("MainWindow", "До"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Опции"))
        self.regression_checkBox.setText(_translate("MainWindow", "Регрессия?"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Единицы измерения"))

