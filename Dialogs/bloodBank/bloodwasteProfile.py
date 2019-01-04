from PyQt5 import QtCore, QtGui, QtWidgets

class bloodwasteReciept(object):
    def setup(self, bloodwasteReciept,data):
        self.data = data
        bloodwasteReciept.setObjectName("bloodwasteReciept")
        bloodwasteReciept.setWindowModality(QtCore.Qt.ApplicationModal)
        bloodwasteReciept.resize(342, 467)
        self.frame = QtWidgets.QFrame(bloodwasteReciept)
        self.frame.setGeometry(QtCore.QRect(10, 10, 321, 401))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bloodBillingLabel = QtWidgets.QLabel(self.frame)
        self.bloodBillingLabel.setGeometry(QtCore.QRect(20, -10, 291, 61))
        self.bloodBillingLabel.setStyleSheet("font-size:14pt;\n"
"font-weight: bold;")
        self.bloodBillingLabel.setObjectName("bloodBillingLabel")
        self.bloodTypeLabel = QtWidgets.QLabel(self.frame)
        self.bloodTypeLabel.setGeometry(QtCore.QRect(20, 80, 151, 41))
        self.bloodTypeLabel.setStyleSheet("font-size:14pt;\n"
"font-weight: bold;")
        self.bloodTypeLabel.setObjectName("bloodTypeLabel")
        self.quantityLabel = QtWidgets.QLabel(self.frame)
        self.quantityLabel.setGeometry(QtCore.QRect(20, 120, 151, 41))
        self.quantityLabel.setStyleSheet("font-size:14pt;\n"
"font-weight: bold;")
        self.quantityLabel.setObjectName("quantityLabel")
        self.reasonLabel = QtWidgets.QLabel(self.frame)
        self.reasonLabel.setGeometry(QtCore.QRect(20, 210, 151, 41))
        self.reasonLabel.setStyleSheet("font-size:14pt;\n"
"font-weight: bold;")
        self.reasonLabel.setObjectName("reasonLabel")
        self.reason = QtWidgets.QTextBrowser(self.frame)
        self.reason.setGeometry(QtCore.QRect(20, 250, 291, 141))
        self.reason.setObjectName("reason")
        self.quantity = QtWidgets.QLabel(self.frame)
        self.quantity.setGeometry(QtCore.QRect(150, 130, 151, 17))
        self.quantity.setObjectName("quantity")
        self.bloodtype = QtWidgets.QLabel(self.frame)
        self.bloodtype.setGeometry(QtCore.QRect(160, 90, 67, 17))
        self.bloodtype.setObjectName("bloodtype")
        self.idLabel = QtWidgets.QLabel(self.frame)
        self.idLabel.setGeometry(QtCore.QRect(20, 40, 51, 41))
        self.idLabel.setStyleSheet("font-size:14pt;\n"
"font-weight: bold;")
        self.idLabel.setObjectName("idLabel")
        self.id = QtWidgets.QLabel(self.frame)
        self.id.setGeometry(QtCore.QRect(100, 50, 67, 17))
        self.id.setObjectName("id")
        self.dateLabel = QtWidgets.QLabel(self.frame)
        self.dateLabel.setGeometry(QtCore.QRect(20, 160, 81, 41))
        self.dateLabel.setStyleSheet("font-size:14pt;\n"
"font-weight: bold;")
        self.dateLabel.setObjectName("dateLabel")
        self.date = QtWidgets.QLabel(self.frame)
        self.date.setGeometry(QtCore.QRect(110, 170, 151, 17))
        self.date.setObjectName("date")
        self.exitbutton = QtWidgets.QPushButton(bloodwasteReciept)
        self.exitbutton.setGeometry(QtCore.QRect(120, 420, 89, 25))
        self.exitbutton.setObjectName("exitbutton")

        self.retranslateUi(bloodwasteReciept)
        QtCore.QMetaObject.connectSlotsByName(bloodwasteReciept)

    def retranslateUi(self, bloodwasteReciept):
        _translate = QtCore.QCoreApplication.translate
        bloodwasteReciept.setWindowTitle(_translate("bloodwasteReciept", "Record"))
        self.bloodBillingLabel.setText(_translate("bloodwasteReciept", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; text-decoration: underline;\">Blood Waste Record</span></p></body></html>"))
        self.bloodTypeLabel.setText(_translate("bloodwasteReciept", "<html><head/><body><p>Blood Type :</p></body></html>"))
        self.quantityLabel.setText(_translate("bloodwasteReciept", "<html><head/><body><p>Quantity :</p></body></html>"))
        self.reasonLabel.setText(_translate("bloodwasteReciept", "<html><head/><body><p>Reason : </p></body></html>"))
        self.quantity.setText(_translate("bloodwasteReciept", "TextLabel"))
        self.bloodtype.setText(_translate("bloodwasteReciept", "TextLabel"))
        self.idLabel.setText(_translate("bloodwasteReciept", "<html><head/><body><p>ID :</p></body></html>"))
        self.id.setText(_translate("bloodwasteReciept", "TextLabel"))
        self.dateLabel.setText(_translate("bloodwasteReciept", "<html><head/><body><p>Date :</p></body></html>"))
        self.date.setText(_translate("bloodwasteReciept", "TextLabel"))
        self.exitbutton.setText(_translate("bloodwasteReciept", "Exit"))
        self.exitbutton.clicked.connect(lambda : bloodwasteReciept.close())
        self.date.setText(str(self.data["date"]))
        self.quantity.setText(str(self.data["quantity"]))
        self.reason.setText(str(self.data["reason"]))
        self.id.setText(str(self.data["id"]))
        self.bloodtype.setText(str(self.data["quantity"]))
