from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Dialogs.superadmin.BloodBanks.addBloodBank import *
from Dialogs.superadmin.BloodBanks.selectBloodBank import *
from Dialogs.broadcast import *
from Dialogs.superadmin.BloodBanks.viewBloodBanks import *
from Dialogs.Message.messageList import *

class BloodBank(object):
    def setup(self, bloodBank, superadmin):
        bloodBank.setObjectName("bloodBank")
        bloodBank.resize(1366, 768)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(bloodBank.sizePolicy().hasHeightForWidth())
        bloodBank.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(bloodBank)
        self.centralwidget.setObjectName("centralwidget")
        self.addDoctorLabel = QtWidgets.QLabel(self.centralwidget)
        self.addDoctorLabel.setGeometry(QtCore.QRect(240, 370, 171, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addDoctorLabel.sizePolicy().hasHeightForWidth())
        self.addDoctorLabel.setSizePolicy(sizePolicy)
        self.addDoctorLabel.setObjectName("addDoctorLabel")
        self.broadcastLabel = QtWidgets.QLabel(self.centralwidget)
        self.broadcastLabel.setGeometry(QtCore.QRect(960, 650, 161, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.broadcastLabel.sizePolicy().hasHeightForWidth())
        self.broadcastLabel.setSizePolicy(sizePolicy)
        self.broadcastLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.broadcastLabel.setObjectName("broadcastLabel")
        self.viewBloodBanksLabel = QtWidgets.QLabel(self.centralwidget)
        self.viewBloodBanksLabel.setGeometry(QtCore.QRect(600, 370, 195, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewBloodBanksLabel.sizePolicy().hasHeightForWidth())
        self.viewBloodBanksLabel.setSizePolicy(sizePolicy)
        self.viewBloodBanksLabel.setObjectName("viewBloodBanksLabel")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(550, 20, 255, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setMinimumSize(QtCore.QSize(0, 50))
        self.title.setMaximumSize(QtCore.QSize(400, 70))
        self.title.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.title.setObjectName("title")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(30, 0, 101, 100))
        self.back.setStyleSheet("border:none;")
        self.back.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../MDTouch/Images/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon)
        self.back.setIconSize(QtCore.QSize(80, 80))
        self.back.setObjectName("back")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 500, 1311, 161))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fraud = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.fraud.setMaximumSize(QtCore.QSize(120, 120))
        self.fraud.setMouseTracking(True)
        self.fraud.setStyleSheet("border:none;")
        self.fraud.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../MDTouch/Images/fraud.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fraud.setIcon(icon1)
        self.fraud.setIconSize(QtCore.QSize(100, 100))
        self.fraud.setCheckable(False)
        self.fraud.setObjectName("fraud")
        self.horizontalLayout_3.addWidget(self.fraud)
        self.statistics = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.statistics.setMaximumSize(QtCore.QSize(120, 120))
        self.statistics.setMouseTracking(True)
        self.statistics.setStyleSheet("border:none;")
        self.statistics.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../MDTouch/Images/statistics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.statistics.setIcon(icon2)
        self.statistics.setIconSize(QtCore.QSize(100, 100))
        self.statistics.setCheckable(False)
        self.statistics.setObjectName("statistics")
        self.horizontalLayout_3.addWidget(self.statistics)
        self.broadcast = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.broadcast.setMaximumSize(QtCore.QSize(120, 120))
        self.broadcast.setStyleSheet("border:none;\n")
        self.broadcast.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../MDTouch/Images/broadcast.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.broadcast.setIcon(icon3)
        self.broadcast.setIconSize(QtCore.QSize(100, 100))
        self.broadcast.setObjectName("broadcast")
        self.horizontalLayout_3.addWidget(self.broadcast)
        self.removeBloodBankLabel = QtWidgets.QLabel(self.centralwidget)
        self.removeBloodBankLabel.setGeometry(QtCore.QRect(960, 370, 171, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeBloodBankLabel.sizePolicy().hasHeightForWidth())
        self.removeBloodBankLabel.setSizePolicy(sizePolicy)
        self.removeBloodBankLabel.setObjectName("removeBloodBankLabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 220, 1311, 171))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.addBloodBank = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addBloodBank.setMaximumSize(QtCore.QSize(120, 120))
        self.addBloodBank.setStyleSheet("border:none;")
        self.addBloodBank.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../MDTouch/Images/add_bloodBank.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addBloodBank.setIcon(icon4)
        self.addBloodBank.setIconSize(QtCore.QSize(100, 100))
        self.addBloodBank.setObjectName("addBloodBank")
        self.horizontalLayout_6.addWidget(self.addBloodBank)
        self.view_bloodBanks = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.view_bloodBanks.setMaximumSize(QtCore.QSize(120, 120))
        self.view_bloodBanks.setStyleSheet("border:none;")
        self.view_bloodBanks.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../MDTouch/Images/view_bloodBanks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.view_bloodBanks.setIcon(icon5)
        self.view_bloodBanks.setIconSize(QtCore.QSize(100, 100))
        self.view_bloodBanks.setObjectName("view_bloodBanks")
        self.horizontalLayout_6.addWidget(self.view_bloodBanks)
        self.removeBloodBank = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.removeBloodBank.setMaximumSize(QtCore.QSize(120, 120))
        self.removeBloodBank.setStyleSheet("border:none;")
        self.removeBloodBank.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../MDTouch/Images/remove_bloodBank.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeBloodBank.setIcon(icon6)
        self.removeBloodBank.setIconSize(QtCore.QSize(100, 100))
        self.removeBloodBank.setObjectName("removeBloodBank")
        self.horizontalLayout_6.addWidget(self.removeBloodBank)
        self.statisticsLabel = QtWidgets.QLabel(self.centralwidget)
        self.statisticsLabel.setGeometry(QtCore.QRect(610, 650, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statisticsLabel.sizePolicy().hasHeightForWidth())
        self.statisticsLabel.setSizePolicy(sizePolicy)
        self.statisticsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.statisticsLabel.setObjectName("statisticsLabel")
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(1240, 10, 101, 91))
        self.logout.setStyleSheet("border:none;")
        self.logout.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../MDTouch/Images/logout.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout.setIcon(icon7)
        self.logout.setIconSize(QtCore.QSize(80, 80))
        self.logout.setObjectName("logout")
        self.fraudLabel = QtWidgets.QLabel(self.centralwidget)
        self.fraudLabel.setGeometry(QtCore.QRect(240, 650, 161, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fraudLabel.sizePolicy().hasHeightForWidth())
        self.fraudLabel.setSizePolicy(sizePolicy)
        self.fraudLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.fraudLabel.setObjectName("fraudLabel")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 100, 1371, 80))
        self.frame.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(120, 0, 1131, 80))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.hospitals = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.hospitals.setMaximumSize(QtCore.QSize(80, 80))
        self.hospitals.setStyleSheet("border:none;")
        self.hospitals.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../MDTouch/Images/hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hospitals.setIcon(icon8)
        self.hospitals.setIconSize(QtCore.QSize(50, 50))
        self.hospitals.setObjectName("hospitals")
        self.horizontalLayout_5.addWidget(self.hospitals)
        self.events = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.events.setMaximumSize(QtCore.QSize(80, 80))
        self.events.setStyleSheet("border:none;")
        self.events.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../MDTouch/Images/event.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.events.setIcon(icon9)
        self.events.setIconSize(QtCore.QSize(50, 50))
        self.events.setObjectName("events")
        self.horizontalLayout_5.addWidget(self.events)
        self.bloodBank = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.bloodBank.setMaximumSize(QtCore.QSize(80, 80))
        self.bloodBank.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border:none;")
        self.bloodBank.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../MDTouch/Images/bloodbank.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bloodBank.setIcon(icon10)
        self.bloodBank.setIconSize(QtCore.QSize(50, 50))
        self.bloodBank.setObjectName("bloodBank")
        self.horizontalLayout_5.addWidget(self.bloodBank)
        self.testCenters = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.testCenters.setMaximumSize(QtCore.QSize(80, 80))
        self.testCenters.setStyleSheet("border:none;")
        self.testCenters.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../MDTouch/Images/test_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.testCenters.setIcon(icon11)
        self.testCenters.setIconSize(QtCore.QSize(50, 50))
        self.testCenters.setObjectName("testCenters")
        self.horizontalLayout_5.addWidget(self.testCenters)
        self.doctors = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.doctors.setMaximumSize(QtCore.QSize(80, 80))
        self.doctors.setStyleSheet("border:none;")
        self.doctors.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../MDTouch/Images/doctor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.doctors.setIcon(icon12)
        self.doctors.setIconSize(QtCore.QSize(50, 50))
        self.doctors.setObjectName("doctors")
        self.horizontalLayout_5.addWidget(self.doctors)
        self.dispensary = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.dispensary.setMaximumSize(QtCore.QSize(80, 80))
        self.dispensary.setStyleSheet("border:none;")
        self.dispensary.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("../MDTouch/Images/dispensary.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dispensary.setIcon(icon13)
        self.dispensary.setIconSize(QtCore.QSize(50, 50))
        self.dispensary.setObjectName("dispensary")
        self.horizontalLayout_5.addWidget(self.dispensary)
        self.emergency = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        self.emergency.setMaximumSize(QtCore.QSize(80, 80))
        self.emergency.setStyleSheet("border:none;")
        self.emergency.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("../MDTouch/Images/ambulance.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.emergency.setIcon(icon14)
        self.emergency.setIconSize(QtCore.QSize(50, 50))
        self.emergency.setObjectName("emergency")
        self.horizontalLayout_5.addWidget(self.emergency)
        self.inbox = QtWidgets.QPushButton(self.centralwidget)
        self.inbox.setGeometry(QtCore.QRect(1130, 0, 80, 80))
        self.inbox.setMaximumSize(QtCore.QSize(100, 100))
        self.inbox.setStyleSheet("border:none;")
        self.inbox.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("../MDTouch/Images/inbox.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.inbox.setIcon(icon15)
        self.inbox.setIconSize(QtCore.QSize(80, 80))
        self.inbox.setObjectName("inbox")
        bloodBank.setCentralWidget(self.centralwidget)

        self.retranslateUi(bloodBank, superadmin)
        QtCore.QMetaObject.connectSlotsByName(bloodBank)

    def retranslateUi(self, bloodBank, superadmin):
        _translate = QtCore.QCoreApplication.translate
        bloodBank.setWindowTitle(_translate("bloodBank", "MainWindow"))
        self.addDoctorLabel.setText(_translate("bloodBank", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Add</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Blood Bank</span></p></body></html>"))
        self.broadcastLabel.setText(_translate("bloodBank", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Broadcast</span></p></body></html>"))
        self.viewBloodBanksLabel.setText(_translate("bloodBank", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">View</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Blood Banks</span></p></body></html>"))
        self.title.setText(_translate("bloodBank", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; text-decoration: underline;\">MDTouch</span></p></body></html>"))
        self.removeBloodBankLabel.setText(_translate("bloodBank", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Remove</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Blood Bank</span></p><p align=\"center\"><br/></p></body></html>"))
        self.statisticsLabel.setText(_translate("bloodBank", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Statistics</span></p></body></html>"))
        self.fraudLabel.setText(_translate("bloodBank", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Fraud</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Inspection</span></p></body></html>"))

        self.clickEvents(bloodBank, superadmin)

    def clickEvents(self, parent, superadmin):
        self.hospitals.clicked.connect(lambda: self.clickOnHospital(parent, superadmin))
        self.events.clicked.connect(lambda: self.clickOnEvents(parent, superadmin))
        self.testCenters.clicked.connect(lambda: self.clickOnTestCenters(parent, superadmin))
        self.emergency.clicked.connect(lambda: self.clickOnEmergency(parent, superadmin))
        self.dispensary.clicked.connect(lambda: self.clickOnDispensary(parent, superadmin))
        self.doctors.clicked.connect(lambda: self.clickOnDoctors(parent, superadmin))
        self.inbox.clicked.connect(lambda: self.clickOnInbox(parent, superadmin))
        self.logout.clicked.connect(lambda: self.clickOnLogOut(parent, superadmin))
        self.back.clicked.connect(lambda: self.clickOnBack(parent, superadmin))


        self.addBloodBank.clicked.connect(lambda : self.clickOnAddBloodBank())
        self.removeBloodBank.clicked.connect(lambda : self.clickOnRemoveBloodBank())
        self.broadcast.clicked.connect(lambda: self.clickOnBroadcast())
        self.view_bloodBanks.clicked.connect(lambda : self.clickOnViewBloodBank())

    def clickOnHospital(self, parent, superadmin):
        superadmin.hospital_home.setup(parent, superadmin)

    def clickOnBloodBank(self, parent, superadmin):
        superadmin.bloodbank_home.setup(parent, superadmin)

    def clickOnEvents(self, parent, superadmin):
        superadmin.events_home.setup(parent, superadmin)

    def clickOnTestCenters(self, parent, superadmin):
        superadmin.testcenter_home.setup(parent, superadmin)

    def clickOnEmergency(self, parent, superadmin):
        superadmin.emergency_home.setup(parent, superadmin)

    def clickOnDispensary(self, parent, superadmin):
        superadmin.dispensary_home.setup(parent, superadmin)

    def clickOnDoctors(self, parent, superadmin):
        superadmin.doctor_home.setup(parent, superadmin)

    def clickOnInbox(self, parent, superadmin):
        self.window = QDialog()
        self.dialog = messageList()
        self.dialog.setup(self.window,superadmin.logindata)
        self.window.setModal(True)
        self.window.show()

    def clickOnLogOut(self, parent, superadmin):
        parent.loginpage.setup(parent)

    def clickOnBack(self, parent, superadmin):
        superadmin.setup(parent)

    def clickOnAddBloodBank(self):
        self.window = QDialog()
        self.dialog = addBloodBank()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()

    def clickOnRemoveBloodBank(self):
        self.window = QDialog()
        self.dialog = selectBloodBank()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()

    def clickOnBroadcast(self):
        self.window = QDialog()
        self.dialog = broadcast()
        self.dialog.setup(self.window, caller.BloodBank)
        self.window.setModal(True)
        self.window.show()

    def clickOnViewBloodBank(self):
        self.window = QDialog()
        self.dialog = viewBloodBankCenter()
        self.dialog.setup(self.window,'SA')
        self.window.setModal(True)
        self.window.show()