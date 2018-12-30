# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bloodBankHome.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_bloodBankHome(object):
    def setupUi(self, bloodBankHome):
        bloodBankHome.setObjectName("bloodBankHome")
        bloodBankHome.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(bloodBankHome)
        self.centralwidget.setObjectName("centralwidget")
        self.donation = QtWidgets.QPushButton(self.centralwidget)
        self.donation.setGeometry(QtCore.QRect(980, 310, 100, 100))
        self.donation.setMinimumSize(QtCore.QSize(100, 100))
        self.donation.setMaximumSize(QtCore.QSize(100, 100))
        self.donation.setStyleSheet("border:none;")
        self.donation.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Images/blood_donation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.donation.setIcon(icon)
        self.donation.setIconSize(QtCore.QSize(100, 100))
        self.donation.setObjectName("donation")
        self.changePassword = QtWidgets.QPushButton(self.centralwidget)
        self.changePassword.setGeometry(QtCore.QRect(1200, 490, 100, 100))
        self.changePassword.setMinimumSize(QtCore.QSize(100, 100))
        self.changePassword.setMaximumSize(QtCore.QSize(100, 100))
        self.changePassword.setStyleSheet("border:none;")
        self.changePassword.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Images/change_password.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changePassword.setIcon(icon1)
        self.changePassword.setIconSize(QtCore.QSize(100, 100))
        self.changePassword.setObjectName("changePassword")
        self.writeReceipt = QtWidgets.QPushButton(self.centralwidget)
        self.writeReceipt.setGeometry(QtCore.QRect(1200, 150, 100, 100))
        self.writeReceipt.setMinimumSize(QtCore.QSize(100, 100))
        self.writeReceipt.setMaximumSize(QtCore.QSize(100, 100))
        self.writeReceipt.setStyleSheet("border:none;")
        self.writeReceipt.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../Images/write_bill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.writeReceipt.setIcon(icon2)
        self.writeReceipt.setIconSize(QtCore.QSize(100, 100))
        self.writeReceipt.setObjectName("writeReceipt")
        self.bloodEntry = QtWidgets.QPushButton(self.centralwidget)
        self.bloodEntry.setGeometry(QtCore.QRect(1000, 140, 100, 100))
        self.bloodEntry.setMinimumSize(QtCore.QSize(100, 100))
        self.bloodEntry.setMaximumSize(QtCore.QSize(100, 100))
        self.bloodEntry.setStyleSheet("border:none;")
        self.bloodEntry.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../../Images/blood_entry.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bloodEntry.setIcon(icon3)
        self.bloodEntry.setIconSize(QtCore.QSize(100, 100))
        self.bloodEntry.setObjectName("bloodEntry")
        self.bloodTransfers = QtWidgets.QPushButton(self.centralwidget)
        self.bloodTransfers.setGeometry(QtCore.QRect(1200, 320, 100, 100))
        self.bloodTransfers.setMinimumSize(QtCore.QSize(100, 100))
        self.bloodTransfers.setMaximumSize(QtCore.QSize(100, 100))
        self.bloodTransfers.setStyleSheet("border:none;")
        self.bloodTransfers.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../../Images/blood_transfer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bloodTransfers.setIcon(icon4)
        self.bloodTransfers.setIconSize(QtCore.QSize(100, 100))
        self.bloodTransfers.setObjectName("bloodTransfers")
        self.bloodEntryLabel = QtWidgets.QLabel(self.centralwidget)
        self.bloodEntryLabel.setGeometry(QtCore.QRect(950, 260, 171, 31))
        self.bloodEntryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bloodEntryLabel.setObjectName("bloodEntryLabel")
        self.donationLabel = QtWidgets.QLabel(self.centralwidget)
        self.donationLabel.setGeometry(QtCore.QRect(950, 430, 171, 31))
        self.donationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.donationLabel.setObjectName("donationLabel")
        self.bloodTransfersLabel = QtWidgets.QLabel(self.centralwidget)
        self.bloodTransfersLabel.setGeometry(QtCore.QRect(1150, 430, 201, 31))
        self.bloodTransfersLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bloodTransfersLabel.setObjectName("bloodTransfersLabel")
        self.writeReceiptLabel = QtWidgets.QLabel(self.centralwidget)
        self.writeReceiptLabel.setGeometry(QtCore.QRect(1160, 260, 181, 31))
        self.writeReceiptLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.writeReceiptLabel.setObjectName("writeReceiptLabel")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(240, 150, 701, 461))
        self.widget.setStyleSheet("image: url(:/bar-graph-horiz.svg);\n"
"background-color: rgb(255, 255, 127);")
        self.widget.setObjectName("widget")
        self.quantityGraphLabel = QtWidgets.QLabel(self.centralwidget)
        self.quantityGraphLabel.setGeometry(QtCore.QRect(460, 630, 261, 31))
        self.quantityGraphLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.quantityGraphLabel.setObjectName("quantityGraphLabel")
        self.profile = QtWidgets.QPushButton(self.centralwidget)
        self.profile.setGeometry(QtCore.QRect(990, 490, 100, 100))
        self.profile.setMinimumSize(QtCore.QSize(100, 100))
        self.profile.setMaximumSize(QtCore.QSize(100, 100))
        self.profile.setStyleSheet("border:none;")
        self.profile.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../../Images/profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.profile.setIcon(icon5)
        self.profile.setIconSize(QtCore.QSize(100, 100))
        self.profile.setObjectName("profile")
        self.profileLabel = QtWidgets.QLabel(self.centralwidget)
        self.profileLabel.setGeometry(QtCore.QRect(940, 600, 201, 31))
        self.profileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.profileLabel.setObjectName("profileLabel")
        self.changePasswordLabel = QtWidgets.QLabel(self.centralwidget)
        self.changePasswordLabel.setGeometry(QtCore.QRect(1150, 600, 201, 31))
        self.changePasswordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.changePasswordLabel.setObjectName("changePasswordLabel")
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(1300, 10, 50, 50))
        self.logout.setMinimumSize(QtCore.QSize(50, 50))
        self.logout.setMaximumSize(QtCore.QSize(50, 50))
        self.logout.setStyleSheet("border:none;")
        self.logout.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../../Images/LogoutIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout.setIcon(icon6)
        self.logout.setIconSize(QtCore.QSize(50, 50))
        self.logout.setObjectName("logout")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(550, 20, 281, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setMinimumSize(QtCore.QSize(0, 50))
        self.title.setMaximumSize(QtCore.QSize(400, 70))
        self.title.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.title.setObjectName("title")
        self.bloodBankName = QtWidgets.QLabel(self.centralwidget)
        self.bloodBankName.setGeometry(QtCore.QRect(110, 30, 400, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bloodBankName.sizePolicy().hasHeightForWidth())
        self.bloodBankName.setSizePolicy(sizePolicy)
        self.bloodBankName.setMinimumSize(QtCore.QSize(100, 30))
        self.bloodBankName.setMaximumSize(QtCore.QSize(400, 100))
        self.bloodBankName.setStyleSheet("font-size:20pt;\n"
"font-weight:bold;\n"
"text-decoration: underline")
        self.bloodBankName.setObjectName("bloodBankName")
        self.inbox = QtWidgets.QPushButton(self.centralwidget)
        self.inbox.setGeometry(QtCore.QRect(1230, 10, 50, 50))
        self.inbox.setMinimumSize(QtCore.QSize(50, 50))
        self.inbox.setMaximumSize(QtCore.QSize(50, 50))
        self.inbox.setStyleSheet("border:none;")
        self.inbox.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../../Images/inbox_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.inbox.setIcon(icon7)
        self.inbox.setIconSize(QtCore.QSize(50, 50))
        self.inbox.setObjectName("inbox")
        self.eventsLabel = QtWidgets.QLabel(self.centralwidget)
        self.eventsLabel.setGeometry(QtCore.QRect(10, 590, 221, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eventsLabel.sizePolicy().hasHeightForWidth())
        self.eventsLabel.setSizePolicy(sizePolicy)
        self.eventsLabel.setMinimumSize(QtCore.QSize(100, 30))
        self.eventsLabel.setMaximumSize(QtCore.QSize(400, 100))
        self.eventsLabel.setStyleSheet("font-size:14pt;\n"
"font-weight:bold;\n"
"text-decoration: underline")
        self.eventsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.eventsLabel.setObjectName("eventsLabel")
        self.events = QtWidgets.QPushButton(self.centralwidget)
        self.events.setGeometry(QtCore.QRect(70, 480, 100, 100))
        self.events.setMinimumSize(QtCore.QSize(100, 100))
        self.events.setMaximumSize(QtCore.QSize(100, 100))
        self.events.setStyleSheet("border:none;")
        self.events.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../../Images/event.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.events.setIcon(icon8)
        self.events.setIconSize(QtCore.QSize(100, 100))
        self.events.setObjectName("events")
        self.bloodRequests = QtWidgets.QPushButton(self.centralwidget)
        self.bloodRequests.setGeometry(QtCore.QRect(70, 140, 100, 100))
        self.bloodRequests.setMinimumSize(QtCore.QSize(100, 100))
        self.bloodRequests.setMaximumSize(QtCore.QSize(100, 100))
        self.bloodRequests.setStyleSheet("border:none;")
        self.bloodRequests.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../../Images/request_blood.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bloodRequests.setIcon(icon9)
        self.bloodRequests.setIconSize(QtCore.QSize(100, 100))
        self.bloodRequests.setObjectName("bloodRequests")
        self.notices = QtWidgets.QPushButton(self.centralwidget)
        self.notices.setGeometry(QtCore.QRect(70, 310, 100, 100))
        self.notices.setMinimumSize(QtCore.QSize(100, 100))
        self.notices.setMaximumSize(QtCore.QSize(100, 100))
        self.notices.setStyleSheet("border:none;")
        self.notices.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../../Images/notices.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notices.setIcon(icon10)
        self.notices.setIconSize(QtCore.QSize(100, 100))
        self.notices.setObjectName("notices")
        self.noticesLabel = QtWidgets.QLabel(self.centralwidget)
        self.noticesLabel.setGeometry(QtCore.QRect(10, 410, 221, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noticesLabel.sizePolicy().hasHeightForWidth())
        self.noticesLabel.setSizePolicy(sizePolicy)
        self.noticesLabel.setMinimumSize(QtCore.QSize(100, 30))
        self.noticesLabel.setMaximumSize(QtCore.QSize(400, 100))
        self.noticesLabel.setStyleSheet("font-size:14pt;\n"
"font-weight:bold;\n"
"text-decoration: underline")
        self.noticesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.noticesLabel.setObjectName("noticesLabel")
        self.bloodRequestsLabel = QtWidgets.QLabel(self.centralwidget)
        self.bloodRequestsLabel.setGeometry(QtCore.QRect(10, 230, 221, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bloodRequestsLabel.sizePolicy().hasHeightForWidth())
        self.bloodRequestsLabel.setSizePolicy(sizePolicy)
        self.bloodRequestsLabel.setMinimumSize(QtCore.QSize(100, 30))
        self.bloodRequestsLabel.setMaximumSize(QtCore.QSize(400, 100))
        self.bloodRequestsLabel.setStyleSheet("font-size:14pt;\n"
"font-weight:bold;\n"
"text-decoration: underline")
        self.bloodRequestsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bloodRequestsLabel.setObjectName("bloodRequestsLabel")
        bloodBankHome.setCentralWidget(self.centralwidget)

        self.retranslateUi(bloodBankHome)
        QtCore.QMetaObject.connectSlotsByName(bloodBankHome)

    def retranslateUi(self, bloodBankHome):
        _translate = QtCore.QCoreApplication.translate
        bloodBankHome.setWindowTitle(_translate("bloodBankHome", "MainWindow"))
        self.bloodEntryLabel.setText(_translate("bloodBankHome", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Blood Entry</span></p></body></html>"))
        self.donationLabel.setText(_translate("bloodBankHome", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Blood Donation</span></p></body></html>"))
        self.bloodTransfersLabel.setText(_translate("bloodBankHome", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Blood Transfers</span></p></body></html>"))
        self.writeReceiptLabel.setText(_translate("bloodBankHome", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Write Receipts</span></p></body></html>"))
        self.quantityGraphLabel.setText(_translate("bloodBankHome", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; text-decoration: underline;\">Quantity Graph</span></p></body></html>"))
        self.profileLabel.setText(_translate("bloodBankHome", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Profile</span></p></body></html>"))
        self.changePasswordLabel.setText(_translate("bloodBankHome", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Change Password</span></p></body></html>"))
        self.title.setText(_translate("bloodBankHome", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; text-decoration: underline;\">MDTouch</span></p></body></html>"))
        self.bloodBankName.setText(_translate("bloodBankHome", "blood_bank_name"))
        self.eventsLabel.setText(_translate("bloodBankHome", "<html><head/><body><p><span style=\" font-size:16pt;\">Events</span></p></body></html>"))
        self.noticesLabel.setText(_translate("bloodBankHome", "<html><head/><body><p><span style=\" font-size:16pt;\">Notices</span></p></body></html>"))
        self.bloodRequestsLabel.setText(_translate("bloodBankHome", "<html><head/><body><p><span style=\" font-size:16pt;\">Blood Requests</span></p></body></html>"))

import img_rc
