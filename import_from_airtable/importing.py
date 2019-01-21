# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'importing.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(553, 159)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.apiKey = QtWidgets.QLineEdit(Dialog)
        self.apiKey.setToolTip("")
        self.apiKey.setWhatsThis("")
        self.apiKey.setInputMask("")
        self.apiKey.setObjectName("apiKey")
        self.horizontalLayout.addWidget(self.apiKey)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.baseKey = QtWidgets.QLineEdit(Dialog)
        self.baseKey.setText("")
        self.baseKey.setObjectName("baseKey")
        self.horizontalLayout_2.addWidget(self.baseKey)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.tableName = QtWidgets.QLineEdit(Dialog)
        self.tableName.setObjectName("tableName")
        self.horizontalLayout_3.addWidget(self.tableName)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.csvPath = QtWidgets.QLineEdit(Dialog)
        self.csvPath.setObjectName("csvPath")
        self.horizontalLayout_4.addWidget(self.csvPath)
        self.openBtn = QtWidgets.QPushButton(Dialog)
        self.openBtn.setObjectName("openBtn")
        self.horizontalLayout_4.addWidget(self.openBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.importBtn = QtWidgets.QPushButton(Dialog)
        self.importBtn.setObjectName("importBtn")
        self.horizontalLayout_5.addWidget(self.importBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Dialog)
        self.importBtn.clicked.connect(Dialog.accept)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Import from Airtable"))
        self.label.setText(_translate("Dialog", "Airtable API key (<a href=\"https://airtable.com/account\">https://airtable.com/account</a>):"))
        self.apiKey.setPlaceholderText(_translate("Dialog", "keyrhbKBk6UQfNTPP"))
        self.label_2.setText(_translate("Dialog", "Base API key (<a href=\"https://airtable.com/api\">https://airtable.com/api</a>):"))
        self.baseKey.setPlaceholderText(_translate("Dialog", "appHjRH699hyH52Kt"))
        self.label_3.setText(_translate("Dialog", "Table Name:"))
        self.tableName.setPlaceholderText(_translate("Dialog", "Books"))
        self.label_4.setText(_translate("Dialog", "Path to the CSV file:"))
        self.csvPath.setPlaceholderText(_translate("Dialog", "C:\\Users\\Admin\\Downloads\\Books-Grid view.csv"))
        self.openBtn.setText(_translate("Dialog", "Open"))
        self.importBtn.setText(_translate("Dialog", "Import"))

