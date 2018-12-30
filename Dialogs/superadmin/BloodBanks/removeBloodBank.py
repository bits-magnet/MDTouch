from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Data.States import *
from Dialogs.messageBox import *

class removeBloodBank(object):
    def setup(self, removeBloodBank,bbData):
        removeBloodBank.setObjectName("removeBloodBank")
        removeBloodBank.resize(562, 440)
        removeBloodBank.setMinimumSize(QtCore.QSize(562, 440))
        removeBloodBank.setMaximumSize(QtCore.QSize(562, 440))
        removeBloodBank.setWindowTitle("")
        self.removeButton = QtWidgets.QPushButton(removeBloodBank)
        self.removeButton.setGeometry(QtCore.QRect(240, 400, 131, 28))
        self.removeButton.setObjectName("removeButton")
        self.title = QtWidgets.QLabel(removeBloodBank)
        self.title.setGeometry(QtCore.QRect(130, 0, 331, 51))
        self.title.setObjectName("title")
        self.frame = QtWidgets.QFrame(removeBloodBank)
        self.frame.setGeometry(QtCore.QRect(10, 50, 541, 341))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.nameLabel = QtWidgets.QLabel(self.frame)
        self.nameLabel.setGeometry(QtCore.QRect(25, 30, 101, 41))
        self.nameLabel.setObjectName("nameLabel")
        self.addressLabel = QtWidgets.QLabel(self.frame)
        self.addressLabel.setGeometry(QtCore.QRect(25, 80, 101, 41))
        self.addressLabel.setObjectName("addressLabel")
        self.contactLabel = QtWidgets.QLabel(self.frame)
        self.contactLabel.setGeometry(QtCore.QRect(25, 280, 131, 41))
        self.contactLabel.setObjectName("contactLabel")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(25, 200, 101, 41))
        self.stateLabel.setObjectName("stateLabel")
        self.pinCodeLabel = QtWidgets.QLabel(self.frame)
        self.pinCodeLabel.setGeometry(QtCore.QRect(25, 160, 101, 41))
        self.pinCodeLabel.setObjectName("pinCodeLabel")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(25, 240, 101, 41))
        self.cityLabel.setObjectName("cityLabel")
        self.address = QtWidgets.QTextBrowser(self.frame)
        self.address.setGeometry(QtCore.QRect(150, 80, 371, 61))
        self.address.setStyleSheet("background-color:transparent;\n"
"border:none;")
        self.address.setObjectName("address")
        self.pinCode = QtWidgets.QLabel(self.frame)
        self.pinCode.setGeometry(QtCore.QRect(150, 170, 181, 21))
        self.pinCode.setStyleSheet("font-size:12pt;")
        self.pinCode.setObjectName("pinCode")
        self.state = QtWidgets.QLabel(self.frame)
        self.state.setGeometry(QtCore.QRect(150, 210, 181, 21))
        self.state.setStyleSheet("font-size:12pt;")
        self.state.setObjectName("state")
        self.city = QtWidgets.QLabel(self.frame)
        self.city.setGeometry(QtCore.QRect(150, 250, 181, 21))
        self.city.setStyleSheet("font-size:12pt;")
        self.city.setObjectName("city")
        self.contact = QtWidgets.QLabel(self.frame)
        self.contact.setGeometry(QtCore.QRect(150, 290, 181, 21))
        self.contact.setStyleSheet("font-size:12pt;")
        self.contact.setObjectName("contact")
        self.name = QtWidgets.QLabel(self.frame)
        self.name.setGeometry(QtCore.QRect(150, 30, 371, 41))
        self.name.setStyleSheet("font-size:16pt;")
        self.name.setObjectName("name")
        self.IDLabel = QtWidgets.QLabel(self.frame)
        self.IDLabel.setGeometry(QtCore.QRect(25, 0, 131, 41))
        self.IDLabel.setObjectName("IDLabel")
        self.bloodBankID = QtWidgets.QLabel(self.frame)
        self.bloodBankID.setGeometry(QtCore.QRect(150, 0, 371, 41))
        self.bloodBankID.setStyleSheet("font-size:14pt;\n"
"font-weight: bold;")
        self.bloodBankID.setObjectName("bloodBankID")

        self.retranslateUi(removeBloodBank,bbData)
        QtCore.QMetaObject.connectSlotsByName(removeBloodBank)

    def retranslateUi(self, removeBloodBank,bbData):
        _translate = QtCore.QCoreApplication.translate
        removeBloodBank.setWindowTitle(_translate("removeBloodBank", " "))
        self.removeButton.setText(_translate("removeBloodBank", "REMOVE"))
        self.title.setText(_translate("removeBloodBank", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Remove Blood Bank</span></p></body></html>"))
        self.nameLabel.setText(_translate("removeBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Name :</span></p></body></html>"))
        self.addressLabel.setText(_translate("removeBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Address :</span></p></body></html>"))
        self.contactLabel.setText(_translate("removeBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Contact No. :</span></p></body></html>"))
        self.stateLabel.setText(_translate("removeBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State :</span></p></body></html>"))
        self.pinCodeLabel.setText(_translate("removeBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Pin Code :</span></p></body></html>"))
        self.cityLabel.setText(_translate("removeBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City :</span></p></body></html>"))
        self.address.setPlaceholderText(_translate("removeBloodBank", "Street, Landmark, Area"))
        self.pinCode.setText(_translate("removeBloodBank", "PinCode"))
        self.state.setText(_translate("removeBloodBank", "State"))
        self.city.setText(_translate("removeBloodBank", "City"))
        self.contact.setText(_translate("removeBloodBank", "1234567890"))
        self.name.setText(_translate("removeBloodBank", "Name"))
        self.IDLabel.setText(_translate("removeBloodBank", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">ID :</span></p></body></html>"))
        self.bloodBankID.setText(_translate("removeBloodBank", "BloodBankID"))

        self.clickEvents(removeBloodBank,bbData)

    def clickEvents(self,parent,bbData):
        self.bloodBankID.setText(str(bbData["id"]))
        self.name.setText(bbData["name"])
        self.pinCode.setText(str(bbData["pin"]))
        self.city.setText(str(bbData["city"]))
        self.state.setText(str(bbData["state"]))
        self.contact.setText(str(bbData["contact"]))
        self.address.setText(str(bbData["address"]))
        self.removeButton.clicked.connect(lambda: self.clickOnRemoveBloodBank(parent,bbData))

    def clickOnRemoveBloodBank(self, parent,bbData):
        parent.close()
        self.window = messageBox()
        self.window.infoBox("Hospital with ID : " + str(bbData["id"]) + " is deleted.")

        # Deleting Hospital
        import requests
        URL = "https://mdtouch.herokuapp.com/MDTouch/api/login/" + str(bbData["username"])
        r = requests.delete(url=URL)
        print(r)

