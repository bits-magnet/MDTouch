from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from Data.States import *

class addAdmin(object):
    def setup(self, addAdmin):
        addAdmin.setObjectName("addAdmin")
        addAdmin.resize(750, 482)
        self.frame = QtWidgets.QFrame(addAdmin)
        self.frame.setGeometry(QtCore.QRect(10, 60, 731, 341))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.firstNameLabel = QtWidgets.QLabel(self.frame)
        self.firstNameLabel.setGeometry(QtCore.QRect(30, 20, 101, 41))
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.firstName = QtWidgets.QLineEdit(self.frame)
        self.firstName.setGeometry(QtCore.QRect(140, 20, 211, 41))
        self.firstName.setObjectName("firstName")
        self.uploadImage = QtWidgets.QPushButton(self.frame)
        self.uploadImage.setGeometry(QtCore.QRect(100, 280, 131, 41))
        self.uploadImage.setObjectName("uploadImage")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setGeometry(QtCore.QRect(60, 70, 221, 201))
        self.widget.setAutoFillBackground(False)
        self.widget.setStyleSheet("image: url(:/selectImage.png);\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-color: rgb(0, 0, 0);")
        self.widget.setObjectName("widget")
        self.lastNameLabel = QtWidgets.QLabel(self.frame)
        self.lastNameLabel.setGeometry(QtCore.QRect(380, 20, 101, 41))
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.lastName = QtWidgets.QLineEdit(self.frame)
        self.lastName.setGeometry(QtCore.QRect(490, 20, 211, 41))
        self.lastName.setObjectName("lastName")
        self.stateLabel = QtWidgets.QLabel(self.frame)
        self.stateLabel.setGeometry(QtCore.QRect(350, 90, 111, 31))
        self.stateLabel.setObjectName("stateLabel")
        self.cityLabel = QtWidgets.QLabel(self.frame)
        self.cityLabel.setGeometry(QtCore.QRect(350, 160, 111, 31))
        self.cityLabel.setObjectName("cityLabel")
        self.hospitalLabel = QtWidgets.QLabel(self.frame)
        self.hospitalLabel.setGeometry(QtCore.QRect(350, 240, 111, 31))
        self.hospitalLabel.setObjectName("hospitalLabel")
        self.stateComboBox = QtWidgets.QComboBox(self.frame)
        self.stateComboBox.setGeometry(QtCore.QRect(460, 90, 161, 27))
        self.stateComboBox.setObjectName("stateComboBox")
        self.cityComboBox = QtWidgets.QComboBox(self.frame)
        self.cityComboBox.setGeometry(QtCore.QRect(460, 160, 161, 27))
        self.cityComboBox.setObjectName("cityComboBox")
        self.hospitalComboBox = QtWidgets.QComboBox(self.frame)
        self.hospitalComboBox.setGeometry(QtCore.QRect(460, 240, 161, 27))
        self.hospitalComboBox.setObjectName("hospitalComboBox")
        self.addButton = QtWidgets.QPushButton(addAdmin)
        self.addButton.setGeometry(QtCore.QRect(300, 420, 131, 41))
        self.addButton.setObjectName("addButton")
        self.title = QtWidgets.QLabel(addAdmin)
        self.title.setGeometry(QtCore.QRect(250, 0, 261, 51))
        self.title.setObjectName("title")

        self.retranslateUi(addAdmin)
        QtCore.QMetaObject.connectSlotsByName(addAdmin)

    def retranslateUi(self, addAdmin):
        _translate = QtCore.QCoreApplication.translate
        addAdmin.setWindowTitle(_translate("addAdmin", " "))
        self.firstNameLabel.setText(_translate("addAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">First Name : </span></p></body></html>"))
        self.uploadImage.setText(_translate("addAdmin", "Upload Image"))
        self.lastNameLabel.setText(_translate("addAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Last Name : </span></p></body></html>"))
        self.stateLabel.setText(_translate("addAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">State : </span></p></body></html>"))
        self.cityLabel.setText(_translate("addAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">City : </span></p></body></html>"))
        self.hospitalLabel.setText(_translate("addAdmin", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Hospital : </span></p></body></html>"))
        self.addButton.setText(_translate("addAdmin", "ADD"))
        self.title.setText(_translate("addAdmin", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Add Admin</span></p></body></html>"))
        self.events(addAdmin)

    def events(self,parent):
        self.stateAddFunction(parent)

    def stateAddFunction(self,parent):
        for i in states.values():
            self.stateComboBox.addItem(i)
        for i in cities["Andhra Pradesh"]:
            self.cityComboBox.addItem(i)
        self.stateComboBox.currentIndexChanged.connect(lambda : self.cityAddFunction(parent))

    def cityAddFunction(self,parent):
        state = self.stateComboBox.currentText()

        while self.cityComboBox.count() > 0:
            self.cityComboBox.removeItem(0)
        for i in cities[state]:
            self.cityComboBox.addItem(i)