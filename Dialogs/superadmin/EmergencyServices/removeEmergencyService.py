from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Dialogs.messageBox import *

class removeEmergencyService(object):
    def setup(self, removeEmergencyService,esData):
        removeEmergencyService.setObjectName("removeEmergencyService")
        removeEmergencyService.resize(555, 453)
        removeEmergencyService.setWindowTitle("")
        removeEmergencyService.setMinimumSize(QtCore.QSize(555, 453))
        removeEmergencyService.setMaximumSize(QtCore.QSize(555, 453))
        self.frame = QtWidgets.QFrame(removeEmergencyService)
        self.frame.setGeometry(QtCore.QRect(10, 50, 531, 341))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.state = QtWidgets.QLabel(self.frame)
        self.state.setGeometry(QtCore.QRect(140, 220, 181, 21))
        self.state.setStyleSheet("font-size:12pt;")
        self.state.setObjectName("state")
        self.name = QtWidgets.QLabel(self.frame)
        self.name.setGeometry(QtCore.QRect(140, 40, 371, 41))
        self.name.setStyleSheet("font-size:16pt;")
        self.name.setObjectName("name")
        self.pinCode = QtWidgets.QLabel(self.frame)
        self.pinCode.setGeometry(QtCore.QRect(140, 180, 181, 21))
        self.pinCode.setStyleSheet("font-size:12pt;")
        self.pinCode.setObjectName("pinCode")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(15, 210, 101, 41))
        self.stateLabel.setObjectName("stateLabel")
        self.contact = QtWidgets.QLabel(self.frame)
        self.contact.setGeometry(QtCore.QRect(140, 300, 191, 21))
        self.contact.setStyleSheet("font-size:12pt;")
        self.contact.setObjectName("contact")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(15, 250, 101, 41))
        self.cityLabel.setObjectName("cityLabel")
        self.IDLabel = QtWidgets.QLabel(self.frame)
        self.IDLabel.setGeometry(QtCore.QRect(15, 10, 131, 41))
        self.IDLabel.setObjectName("IDLabel")
        self.nameLabel = QtWidgets.QLabel(self.frame)
        self.nameLabel.setGeometry(QtCore.QRect(15, 40, 101, 41))
        self.nameLabel.setObjectName("nameLabel")
        self.pinCodeLabel = QtWidgets.QLabel(self.frame)
        self.pinCodeLabel.setGeometry(QtCore.QRect(15, 170, 101, 41))
        self.pinCodeLabel.setObjectName("pinCodeLabel")
        self.contactLabel = QtWidgets.QLabel(self.frame)
        self.contactLabel.setGeometry(QtCore.QRect(15, 300, 131, 21))
        self.contactLabel.setObjectName("contactLabel")
        self.address = QtWidgets.QTextBrowser(self.frame)
        self.address.setGeometry(QtCore.QRect(140, 90, 371, 61))
        self.address.setStyleSheet("background-color:transparent;\n"
"border:none;")
        self.address.setObjectName("address")
        self.addressLabel = QtWidgets.QLabel(self.frame)
        self.addressLabel.setGeometry(QtCore.QRect(15, 90, 101, 41))
        self.addressLabel.setObjectName("addressLabel")
        self.city = QtWidgets.QLabel(self.frame)
        self.city.setGeometry(QtCore.QRect(140, 260, 181, 21))
        self.city.setStyleSheet("font-size:12pt;")
        self.city.setObjectName("city")
        self.dispensaryID = QtWidgets.QLabel(self.frame)
        self.dispensaryID.setGeometry(QtCore.QRect(140, 10, 371, 41))
        self.dispensaryID.setStyleSheet("font-size:14pt;\n"
"font-weight: bold;")
        self.dispensaryID.setObjectName("dispensaryID")
        self.removeButton = QtWidgets.QPushButton(removeEmergencyService)
        self.removeButton.setGeometry(QtCore.QRect(210, 400, 131, 41))
        self.removeButton.setObjectName("removeButton")
        self.title = QtWidgets.QLabel(removeEmergencyService)
        self.title.setGeometry(QtCore.QRect(40, 0, 451, 51))
        self.title.setObjectName("title")

        self.retranslateUi(removeEmergencyService,esData)
        QtCore.QMetaObject.connectSlotsByName(removeEmergencyService)

    def retranslateUi(self, removeEmergencyService,esData):
        _translate = QtCore.QCoreApplication.translate
        removeEmergencyService.setWindowTitle(_translate("removeEmergencyService", " "))
        self.state.setText(_translate("removeEmergencyService", "State"))
        self.name.setText(_translate("removeEmergencyService", "Name"))
        self.pinCode.setText(_translate("removeEmergencyService", "PinCode"))
        self.stateLabel.setText(_translate("removeEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State :</span></p></body></html>"))
        self.contact.setText(_translate("removeEmergencyService", "1234567890"))
        self.cityLabel.setText(_translate("removeEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City :</span></p></body></html>"))
        self.IDLabel.setText(_translate("removeEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">ID :</span></p></body></html>"))
        self.nameLabel.setText(_translate("removeEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Name :</span></p></body></html>"))
        self.pinCodeLabel.setText(_translate("removeEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Pin Code :</span></p></body></html>"))
        self.contactLabel.setText(_translate("removeEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Contact No. :</span></p></body></html>"))
        self.address.setPlaceholderText(_translate("removeEmergencyService", "Street, Landmark, Area"))
        self.addressLabel.setText(_translate("removeEmergencyService", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Address :</span></p></body></html>"))
        self.city.setText(_translate("removeEmergencyService", "City"))
        self.dispensaryID.setText(_translate("removeEmergencyService", "EmergencyServiceID"))
        self.removeButton.setText(_translate("removeEmergencyService", "REMOVE"))
        self.title.setText(_translate("removeEmergencyService", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Remove Emergency Service</span></p></body></html>"))

        self.clickEvents(removeEmergencyService,esData)

    def clickEvents(self, parent,esData):
        self.state.setText(esData["state"])
        self.city.setText(esData["city"])
        self.contact.setText(str(esData["contact_number"]))
        self.dispensaryID.setText(str(esData["id"]))
        self.address.setText(esData["address"])
        self.name.setText(esData["name"])
        self.pinCode.setText(str(esData["pin"]))
        self.removeButton.clicked.connect(lambda: self.clickOnRemoveButton(parent,esData))

    def clickOnRemoveButton(self, parent,esData):
        print(esData)
        parent.close()
        self.window = messageBox()
        self.window.infoBox("Emergency Service with ID : " + str(esData["id"]) + " is deleted.")

        # Deleting Hospital
        import requests
        URL = "https://mdtouch.herokuapp.com/MDTouch/api/login/" + str(esData["username"])
        r = requests.delete(url=URL)
        print(r)
        pass