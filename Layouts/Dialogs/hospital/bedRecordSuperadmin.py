# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bedRecordSuperadmin.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bedviewlialog(object):
    def setupUi(self, bedviewlialog):
        bedviewlialog.setObjectName("bedviewlialog")
        bedviewlialog.resize(548, 428)
        self.frame = QtWidgets.QFrame(bedviewlialog)
        self.frame.setGeometry(QtCore.QRect(10, 60, 521, 321))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 501, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.titleLabel = QtWidgets.QLabel(bedviewlialog)
        self.titleLabel.setGeometry(QtCore.QRect(90, 10, 361, 41))
        self.titleLabel.setStyleSheet("font-size:14pt;\n"
"font-weight: bold;")
        self.titleLabel.setObjectName("titleLabel")
        self.closeButton = QtWidgets.QPushButton(bedviewlialog)
        self.closeButton.setGeometry(QtCore.QRect(490, 390, 51, 25))
        self.closeButton.setObjectName("closeButton")
        self.billingButton = QtWidgets.QPushButton(bedviewlialog)
        self.billingButton.setGeometry(QtCore.QRect(0, 390, 131, 25))
        self.billingButton.setObjectName("billingButton")
        self.appointmentButton = QtWidgets.QPushButton(bedviewlialog)
        self.appointmentButton.setGeometry(QtCore.QRect(140, 390, 171, 25))
        self.appointmentButton.setObjectName("appointmentButton")
        self.maintainanceRecord = QtWidgets.QPushButton(bedviewlialog)
        self.maintainanceRecord.setGeometry(QtCore.QRect(320, 390, 161, 25))
        self.maintainanceRecord.setObjectName("maintainanceRecord")

        self.retranslateUi(bedviewlialog)
        QtCore.QMetaObject.connectSlotsByName(bedviewlialog)

    def retranslateUi(self, bedviewlialog):
        _translate = QtCore.QCoreApplication.translate
        bedviewlialog.setWindowTitle(_translate("bedviewlialog", "Beds"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("bedviewlialog", "S.No"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("bedviewlialog", "Bed ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("bedviewlialog", "Type"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("bedviewlialog", "Status"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("bedviewlialog", "Patient ID"))
        self.titleLabel.setText(_translate("bedviewlialog", "<html><head/><body><p><span style=\" font-size:22pt; text-decoration: underline;\">Bed Management System</span></p></body></html>"))
        self.closeButton.setText(_translate("bedviewlialog", "Close"))
        self.billingButton.setText(_translate("bedviewlialog", "Billing Records"))
        self.appointmentButton.setText(_translate("bedviewlialog", "See Bed Appointments"))
        self.maintainanceRecord.setText(_translate("bedviewlialog", "Maintainance Records"))

