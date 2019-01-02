from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Dialogs.superadmin.Doctors.addDoctor import *
from Dialogs.superadmin.Doctors.selectDoctor import *
from Dialogs.broadcast import *
from Dialogs.superadmin.Doctors.viewDoctors import *
from Dialogs.Message.messageList import *

class Doctor(object):
    def setup(self, doctor,superadmin):
        doctor.setObjectName("doctor")
        doctor.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(doctor)
        self.centralwidget.setObjectName("centralwidget")
        self.removeDoctorLabel = QtWidgets.QLabel(self.centralwidget)
        self.removeDoctorLabel.setGeometry(QtCore.QRect(990,370,125,80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeDoctorLabel.sizePolicy().hasHeightForWidth())
        self.removeDoctorLabel.setSizePolicy(sizePolicy)
        self.removeDoctorLabel.setObjectName("removeDoctorLabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 220, 1311, 171))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addDoctor = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addDoctor.setMaximumSize(QtCore.QSize(120, 120))
        self.addDoctor.setStyleSheet("border:none;")
        self.addDoctor.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../MDTouch/Images/add_doctor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addDoctor.setIcon(icon)
        self.addDoctor.setIconSize(QtCore.QSize(100, 100))
        self.addDoctor.setObjectName("addDoctor")
        self.horizontalLayout.addWidget(self.addDoctor)
        self.viewDoctors = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.viewDoctors.setMaximumSize(QtCore.QSize(120, 120))
        self.viewDoctors.setStyleSheet("border:none;")
        self.viewDoctors.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../MDTouch/Images/view_doctor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewDoctors.setIcon(icon1)
        self.viewDoctors.setIconSize(QtCore.QSize(100, 100))
        self.viewDoctors.setObjectName("viewDoctors")
        self.horizontalLayout.addWidget(self.viewDoctors)
        self.removeDoctor = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.removeDoctor.setMaximumSize(QtCore.QSize(120, 120))
        self.removeDoctor.setStyleSheet("border:none;")
        self.removeDoctor.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../MDTouch/Images/remove_doctor.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeDoctor.setIcon(icon2)
        self.removeDoctor.setIconSize(QtCore.QSize(100, 100))
        self.removeDoctor.setObjectName("removeDoctor")
        self.horizontalLayout.addWidget(self.removeDoctor)
        self.addDoctorLabel = QtWidgets.QLabel(self.centralwidget)
        self.addDoctorLabel.setGeometry(QtCore.QRect(250, 370, 126, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addDoctorLabel.sizePolicy().hasHeightForWidth())
        self.addDoctorLabel.setSizePolicy(sizePolicy)
        self.addDoctorLabel.setObjectName("addDoctorLabel")
        self.fraudLabel = QtWidgets.QLabel(self.centralwidget)
        self.fraudLabel.setGeometry(QtCore.QRect(240, 650, 161, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fraudLabel.sizePolicy().hasHeightForWidth())
        self.fraudLabel.setSizePolicy(sizePolicy)
        self.fraudLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.fraudLabel.setObjectName("fraudLabel")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 500, 1311, 161))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fraud = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.fraud.setMaximumSize(QtCore.QSize(120, 120))
        self.fraud.setMouseTracking(True)
        self.fraud.setStyleSheet("border:none;")
        self.fraud.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../MDTouch/Images/fraud.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fraud.setIcon(icon3)
        self.fraud.setIconSize(QtCore.QSize(100, 100))
        self.fraud.setCheckable(False)
        self.fraud.setObjectName("fraud")
        self.horizontalLayout_2.addWidget(self.fraud)
        self.statistics = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.statistics.setMaximumSize(QtCore.QSize(120, 120))
        self.statistics.setMouseTracking(True)
        self.statistics.setStyleSheet("border:none;")
        self.statistics.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../MDTouch/Images/statistics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.statistics.setIcon(icon4)
        self.statistics.setIconSize(QtCore.QSize(100, 100))
        self.statistics.setCheckable(False)
        self.statistics.setObjectName("statistics")
        self.horizontalLayout_2.addWidget(self.statistics)
        self.broadcast = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.broadcast.setMaximumSize(QtCore.QSize(120, 120))
        self.broadcast.setStyleSheet("border:none;\n"
"")
        self.broadcast.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../MDTouch/Images/broadcast.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.broadcast.setIcon(icon5)
        self.broadcast.setIconSize(QtCore.QSize(100, 100))
        self.broadcast.setObjectName("broadcast")
        self.horizontalLayout_2.addWidget(self.broadcast)
        self.statisticsLabel = QtWidgets.QLabel(self.centralwidget)
        self.statisticsLabel.setGeometry(QtCore.QRect(610, 650, 150, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statisticsLabel.sizePolicy().hasHeightForWidth())
        self.statisticsLabel.setSizePolicy(sizePolicy)
        self.statisticsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.statisticsLabel.setObjectName("statisticsLabel")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 100, 1371, 80))
        self.frame.setStyleSheet("background-color: rgb(85, 255, 127);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(120, 0, 1131, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.hospitals = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.hospitals.setMaximumSize(QtCore.QSize(80, 80))
        self.hospitals.setStyleSheet("border:none;")
        self.hospitals.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../MDTouch/Images/hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hospitals.setIcon(icon6)
        self.hospitals.setIconSize(QtCore.QSize(50, 50))
        self.hospitals.setObjectName("hospitals")
        self.horizontalLayout_4.addWidget(self.hospitals)
        self.events = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.events.setMaximumSize(QtCore.QSize(80, 80))
        self.events.setStyleSheet("border:none;")
        self.events.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../MDTouch/Images/event.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.events.setIcon(icon7)
        self.events.setIconSize(QtCore.QSize(50, 50))
        self.events.setObjectName("events")
        self.horizontalLayout_4.addWidget(self.events)
        self.bloodBank = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.bloodBank.setMaximumSize(QtCore.QSize(80, 80))
        self.bloodBank.setStyleSheet("border:none;")
        self.bloodBank.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../MDTouch/Images/bloodbank.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bloodBank.setIcon(icon8)
        self.bloodBank.setIconSize(QtCore.QSize(50, 50))
        self.bloodBank.setObjectName("bloodBank")
        self.horizontalLayout_4.addWidget(self.bloodBank)
        self.testCenters = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.testCenters.setMaximumSize(QtCore.QSize(80, 80))
        self.testCenters.setStyleSheet("border:none;")
        self.testCenters.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../MDTouch/Images/test_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.testCenters.setIcon(icon9)
        self.testCenters.setIconSize(QtCore.QSize(50, 50))
        self.testCenters.setObjectName("testCenters")
        self.horizontalLayout_4.addWidget(self.testCenters)
        self.doctors = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.doctors.setMaximumSize(QtCore.QSize(80, 80))
        self.doctors.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border:none;")
        self.doctors.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../MDTouch/Images/doctor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.doctors.setIcon(icon10)
        self.doctors.setIconSize(QtCore.QSize(50, 50))
        self.doctors.setObjectName("doctors")
        self.horizontalLayout_4.addWidget(self.doctors)
        self.dispensary = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.dispensary.setMaximumSize(QtCore.QSize(80, 80))
        self.dispensary.setStyleSheet("border:none;")
        self.dispensary.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../MDTouch/Images/dispensary.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dispensary.setIcon(icon11)
        self.dispensary.setIconSize(QtCore.QSize(50, 50))
        self.dispensary.setObjectName("dispensary")
        self.horizontalLayout_4.addWidget(self.dispensary)
        self.emergency = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.emergency.setMaximumSize(QtCore.QSize(80, 80))
        self.emergency.setStyleSheet("border:none;")
        self.emergency.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../MDTouch/Images/ambulance.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.emergency.setIcon(icon12)
        self.emergency.setIconSize(QtCore.QSize(50, 50))
        self.emergency.setObjectName("emergency")
        self.horizontalLayout_4.addWidget(self.emergency)
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(30, 0, 101, 100))
        self.back.setStyleSheet("border:none;")
        self.back.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("../MDTouch/Images/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon13)
        self.back.setIconSize(QtCore.QSize(80, 80))
        self.back.setObjectName("back")
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(1240, 10, 101, 91))
        self.logout.setStyleSheet("border:none;")
        self.logout.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("../MDTouch/Images/logout.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout.setIcon(icon14)
        self.logout.setIconSize(QtCore.QSize(80, 80))
        self.logout.setObjectName("logout")
        self.viewDoctorsLabel = QtWidgets.QLabel(self.centralwidget)
        self.viewDoctorsLabel.setGeometry(QtCore.QRect(620, 370, 126, 80))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewDoctorsLabel.sizePolicy().hasHeightForWidth())
        self.viewDoctorsLabel.setSizePolicy(sizePolicy)
        self.viewDoctorsLabel.setObjectName("viewDoctorsLabel")
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
        self.broadcastLabel = QtWidgets.QLabel(self.centralwidget)
        self.broadcastLabel.setGeometry(QtCore.QRect(960, 650, 161, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.broadcastLabel.sizePolicy().hasHeightForWidth())
        self.broadcastLabel.setSizePolicy(sizePolicy)
        self.broadcastLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.broadcastLabel.setObjectName("broadcastLabel")
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
        doctor.setCentralWidget(self.centralwidget)

        self.retranslateUi(doctor,superadmin)
        QtCore.QMetaObject.connectSlotsByName(doctor)

    def retranslateUi(self, doctor,superadmin):
        _translate = QtCore.QCoreApplication.translate
        doctor.setWindowTitle(_translate("doctor", "doctor"))
        self.removeDoctorLabel.setText(_translate("doctor", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Remove</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Doctor</span></p><p align=\"center\"><br/></p></body></html>"))
        self.addDoctorLabel.setText(_translate("doctor", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Add</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Doctor</span></p></body></html>"))
        self.fraudLabel.setText(_translate("doctor", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Fraud</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Inspection</span></p></body></html>"))
        self.statisticsLabel.setText(_translate("doctor", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Statistics</span></p></body></html>"))
        self.viewDoctorsLabel.setText(_translate("doctor", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">View</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Doctors</span></p></body></html>"))
        self.title.setText(_translate("doctor", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; text-decoration: underline;\">MDTouch</span></p></body></html>"))
        self.broadcastLabel.setText(_translate("doctor", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Broadcast</span></p></body></html>"))

        self.clickEvents(doctor,superadmin)

    def clickEvents(self, parent,superadmin):
        self.hospitals.clicked.connect(lambda: self.clickOnHospital(parent,superadmin))
        self.events.clicked.connect(lambda: self.clickOnEvents(parent,superadmin))
        self.bloodBank.clicked.connect(lambda: self.clickOnBloodBank(parent,superadmin))
        self.testCenters.clicked.connect(lambda: self.clickOnTestCenters(parent,superadmin))
        self.emergency.clicked.connect(lambda: self.clickOnEmergency(parent,superadmin))
        self.dispensary.clicked.connect(lambda: self.clickOnDispensary(parent,superadmin))
        self.inbox.clicked.connect(lambda: self.clickOnInbox(parent, superadmin))
        self.back.clicked.connect(lambda: self.clickOnBack(parent,superadmin))
        self.logout.clicked.connect(lambda: self.clickOnLogOut(parent, superadmin))

        self.addDoctor.clicked.connect(lambda: self.clickOnAddDoctor())
        self.removeDoctor.clicked.connect(lambda: self.clickOnRemoveDoctor())
        self.broadcast.clicked.connect(lambda: self.clickOnBroadcast())
        self.viewDoctors.clicked.connect(lambda : self.clickOnViewDoctors())

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


    def clickOnAddDoctor(self):
        self.window = QDialog()
        self.dialog = addDoctor()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()

    def clickOnRemoveDoctor(self):
        self.window = QDialog()
        self.dialog = selectDoctor()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()

    def clickOnBroadcast(self):
        self.window = QDialog()
        self.dialog = broadcast()
        self.dialog.setup(self.window, caller.Doctor)
        self.window.setModal(True)
        self.window.show()

    def clickOnViewDoctors(self):
        self.window = QDialog()
        self.dialog = viewDoctor()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()

