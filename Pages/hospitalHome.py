from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Dialogs.messageBox import *
from Dialogs.changePassword import *
from Dialogs.superadmin.Hospitals.viewHospitals import *
from Dialogs.superadmin.BloodBanks.viewBloodBanks import *
from Dialogs.superadmin.Dispensaries.viewDispensaries import *
from Dialogs.superadmin.EmergencyServices.viewEs import *
from Dialogs.superadmin.TestCenters.viewTestCenters import *
from Dialogs.events import *
from Dialogs.hospital.hospitalMyProfileOption import *
from Dialogs.billsDialog import *
from Dialogs.Notice.NoticeList import *

class hospitalHome(object):
    def setup(self, hospitalHome,loginData = None):
        self.logindata = loginData
        self.admindata = {}
        self.hospitaldata = {}
        URL = "https://mdtouch.herokuapp.com/api/administrator/"
        params = {
            "username" : int(self.logindata["id"])
        }
        import requests
        r = requests.get(url=URL,params=params)
        l = r.json()
        self.admindata = l[0]
        print("admindata : ", self.admindata)

        URL = "https://mdtouch.herokuapp.com/api/hospital/" + str(self.admindata["workplace"])
        r = requests.get(URL)
        self.hospitaldata = r.json()
        print("hospitaldata  : ",self.hospitaldata)
        hospitalHome.setObjectName("hospitalHome")
        hospitalHome.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(hospitalHome)
        self.centralwidget.setObjectName("centralwidget")
        self.searchBloodBanksLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchBloodBanksLabel.setGeometry(QtCore.QRect(440, 590, 240, 71))
        self.searchBloodBanksLabel.setMinimumSize(QtCore.QSize(240, 40))
        self.searchBloodBanksLabel.setMaximumSize(QtCore.QSize(240, 80))
        self.searchBloodBanksLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.searchBloodBanksLabel.setObjectName("searchBloodBanksLabel")
        self.searchDispensariesLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchDispensariesLabel.setGeometry(QtCore.QRect(930, 590, 240, 80))
        self.searchDispensariesLabel.setMinimumSize(QtCore.QSize(240, 80))
        self.searchDispensariesLabel.setMaximumSize(QtCore.QSize(240, 80))
        self.searchDispensariesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.searchDispensariesLabel.setObjectName("searchDispensariesLabel")
        self.inbox = QtWidgets.QPushButton(self.centralwidget)
        self.inbox.setGeometry(QtCore.QRect(1230, 10, 50, 50))
        self.inbox.setMinimumSize(QtCore.QSize(50, 50))
        self.inbox.setMaximumSize(QtCore.QSize(50, 50))
        self.inbox.setStyleSheet("border:none;")
        self.inbox.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../MDTouch/Images/inbox_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.inbox.setIcon(icon)
        self.inbox.setIconSize(QtCore.QSize(50, 50))
        self.inbox.setObjectName("inbox")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 290, 1331, 111))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bills = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.bills.setMinimumSize(QtCore.QSize(100, 100))
        self.bills.setMaximumSize(QtCore.QSize(100, 100))
        self.bills.setStyleSheet("border:none;")
        self.bills.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../MDTouch/Images/medical_bills.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bills.setIcon(icon1)
        self.bills.setIconSize(QtCore.QSize(100, 100))
        self.bills.setObjectName("bills")
        self.horizontalLayout_2.addWidget(self.bills)
        self.changePassword = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.changePassword.setMinimumSize(QtCore.QSize(100, 100))
        self.changePassword.setMaximumSize(QtCore.QSize(100, 100))
        self.changePassword.setStyleSheet("border:none;")
        self.changePassword.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../MDTouch/Images/change_password.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changePassword.setIcon(icon2)
        self.changePassword.setIconSize(QtCore.QSize(100, 100))
        self.changePassword.setObjectName("changePassword")
        self.horizontalLayout_2.addWidget(self.changePassword)
        self.beds = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.beds.setMinimumSize(QtCore.QSize(100, 100))
        self.beds.setMaximumSize(QtCore.QSize(100, 100))
        self.beds.setStyleSheet("border:none;")
        self.beds.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../MDTouch/Images/hospital_bed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.beds.setIcon(icon3)
        self.beds.setIconSize(QtCore.QSize(100, 100))
        self.beds.setObjectName("beds")
        self.horizontalLayout_2.addWidget(self.beds)
        self.events = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.events.setMinimumSize(QtCore.QSize(100, 100))
        self.events.setMaximumSize(QtCore.QSize(100, 100))
        self.events.setStyleSheet("border:none;")
        self.events.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../MDTouch/Images/event.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.events.setIcon(icon4)
        self.events.setIconSize(QtCore.QSize(100, 100))
        self.events.setObjectName("events")
        self.horizontalLayout_2.addWidget(self.events)
        self.statistics = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.statistics.setMinimumSize(QtCore.QSize(100, 100))
        self.statistics.setMaximumSize(QtCore.QSize(100, 100))
        self.statistics.setStyleSheet("border:none;")
        self.statistics.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../MDTouch/Images/statistics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.statistics.setIcon(icon5)
        self.statistics.setIconSize(QtCore.QSize(100, 100))
        self.statistics.setObjectName("statistics")
        self.horizontalLayout_2.addWidget(self.statistics)
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(560, 10, 281, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setMinimumSize(QtCore.QSize(0, 50))
        self.title.setMaximumSize(QtCore.QSize(400, 70))
        self.title.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.title.setObjectName("title")
        self.appointmentsLabel = QtWidgets.QLabel(self.centralwidget)
        self.appointmentsLabel.setGeometry(QtCore.QRect(840, 220, 180, 40))
        self.appointmentsLabel.setMinimumSize(QtCore.QSize(180, 40))
        self.appointmentsLabel.setMaximumSize(QtCore.QSize(180, 40))
        self.appointmentsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.appointmentsLabel.setObjectName("appointmentsLabel")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(150, 480, 1071, 111))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.searchEmergencyServices = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.searchEmergencyServices.setMinimumSize(QtCore.QSize(100, 100))
        self.searchEmergencyServices.setMaximumSize(QtCore.QSize(100, 100))
        self.searchEmergencyServices.setStyleSheet("border:none;")
        self.searchEmergencyServices.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../MDTouch/Images/emergency.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchEmergencyServices.setIcon(icon6)
        self.searchEmergencyServices.setIconSize(QtCore.QSize(100, 100))
        self.searchEmergencyServices.setObjectName("searchEmergencyServices")
        self.horizontalLayout_3.addWidget(self.searchEmergencyServices)
        self.searchBloodBankCenters = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.searchBloodBankCenters.setMinimumSize(QtCore.QSize(100, 100))
        self.searchBloodBankCenters.setMaximumSize(QtCore.QSize(100, 100))
        self.searchBloodBankCenters.setStyleSheet("border:none;")
        self.searchBloodBankCenters.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../MDTouch/Images/view_bloodBanks.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchBloodBankCenters.setIcon(icon7)
        self.searchBloodBankCenters.setIconSize(QtCore.QSize(100, 100))
        self.searchBloodBankCenters.setObjectName("searchBloodBankCenters")
        self.horizontalLayout_3.addWidget(self.searchBloodBankCenters)
        self.searchTestCenters = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.searchTestCenters.setMinimumSize(QtCore.QSize(100, 100))
        self.searchTestCenters.setMaximumSize(QtCore.QSize(100, 100))
        self.searchTestCenters.setStyleSheet("border:none;")
        self.searchTestCenters.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../MDTouch/Images/search_testCenters.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchTestCenters.setIcon(icon8)
        self.searchTestCenters.setIconSize(QtCore.QSize(100, 100))
        self.searchTestCenters.setObjectName("searchTestCenters")
        self.horizontalLayout_3.addWidget(self.searchTestCenters)
        self.searchDispensaries = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.searchDispensaries.setMinimumSize(QtCore.QSize(100, 100))
        self.searchDispensaries.setMaximumSize(QtCore.QSize(100, 100))
        self.searchDispensaries.setStyleSheet("border:none;")
        self.searchDispensaries.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../MDTouch/Images/search_medicines.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchDispensaries.setIcon(icon9)
        self.searchDispensaries.setIconSize(QtCore.QSize(100, 100))
        self.searchDispensaries.setObjectName("searchDispensaries")
        self.horizontalLayout_3.addWidget(self.searchDispensaries)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 110, 1331, 109))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.profile = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.profile.setMinimumSize(QtCore.QSize(100, 100))
        self.profile.setMaximumSize(QtCore.QSize(100, 100))
        self.profile.setStyleSheet("border:none;")
        self.profile.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../MDTouch/Images/edit_profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.profile.setIcon(icon10)
        self.profile.setIconSize(QtCore.QSize(100, 100))
        self.profile.setObjectName("profile")
        self.horizontalLayout.addWidget(self.profile)
        self.doctors = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.doctors.setMinimumSize(QtCore.QSize(100, 100))
        self.doctors.setMaximumSize(QtCore.QSize(100, 100))
        self.doctors.setStyleSheet("border:none;")
        self.doctors.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../MDTouch/Images/doc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.doctors.setIcon(icon11)
        self.doctors.setIconSize(QtCore.QSize(100, 100))
        self.doctors.setObjectName("doctors")
        self.horizontalLayout.addWidget(self.doctors)
        self.patients = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.patients.setMinimumSize(QtCore.QSize(100, 100))
        self.patients.setMaximumSize(QtCore.QSize(100, 100))
        self.patients.setStyleSheet("border:none;")
        self.patients.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../MDTouch/Images/patients.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.patients.setIcon(icon12)
        self.patients.setIconSize(QtCore.QSize(100, 100))
        self.patients.setObjectName("patients")
        self.horizontalLayout.addWidget(self.patients)
        self.appointments = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.appointments.setMinimumSize(QtCore.QSize(100, 100))
        self.appointments.setMaximumSize(QtCore.QSize(100, 100))
        self.appointments.setStyleSheet("border:none;")
        self.appointments.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("../MDTouch/Images/appointments.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.appointments.setIcon(icon13)
        self.appointments.setIconSize(QtCore.QSize(100, 100))
        self.appointments.setObjectName("appointments")
        self.horizontalLayout.addWidget(self.appointments)
        self.notices = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.notices.setMinimumSize(QtCore.QSize(100, 100))
        self.notices.setMaximumSize(QtCore.QSize(100, 100))
        self.notices.setStyleSheet("border:none;")
        self.notices.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("../MDTouch/Images/notices.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notices.setIcon(icon14)
        self.notices.setIconSize(QtCore.QSize(100, 100))
        self.notices.setObjectName("notices")
        self.horizontalLayout.addWidget(self.notices)
        self.billsLabel = QtWidgets.QLabel(self.centralwidget)
        self.billsLabel.setGeometry(QtCore.QRect(90, 400, 240, 40))
        self.billsLabel.setMinimumSize(QtCore.QSize(240, 40))
        self.billsLabel.setMaximumSize(QtCore.QSize(240, 40))
        self.billsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.billsLabel.setObjectName("billsLabel")
        self.noticesLabel = QtWidgets.QLabel(self.centralwidget)
        self.noticesLabel.setGeometry(QtCore.QRect(1090, 220, 150, 40))
        self.noticesLabel.setMinimumSize(QtCore.QSize(150, 40))
        self.noticesLabel.setMaximumSize(QtCore.QSize(150, 40))
        self.noticesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.noticesLabel.setObjectName("noticesLabel")
        self.searchTestCentersLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchTestCentersLabel.setGeometry(QtCore.QRect(690, 590, 240, 71))
        self.searchTestCentersLabel.setMinimumSize(QtCore.QSize(240, 40))
        self.searchTestCentersLabel.setMaximumSize(QtCore.QSize(240, 80))
        self.searchTestCentersLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.searchTestCentersLabel.setObjectName("searchTestCentersLabel")
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(1300, 10, 50, 50))
        self.logout.setMinimumSize(QtCore.QSize(50, 50))
        self.logout.setMaximumSize(QtCore.QSize(50, 50))
        self.logout.setStyleSheet("border:none;")
        self.logout.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("../MDTouch/Images/LogoutIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout.setIcon(icon15)
        self.logout.setIconSize(QtCore.QSize(50, 50))
        self.logout.setObjectName("logout")
        self.patientsLabel = QtWidgets.QLabel(self.centralwidget)
        self.patientsLabel.setGeometry(QtCore.QRect(610, 220, 150, 40))
        self.patientsLabel.setMinimumSize(QtCore.QSize(150, 40))
        self.patientsLabel.setMaximumSize(QtCore.QSize(150, 40))
        self.patientsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.patientsLabel.setObjectName("patientsLabel")
        self.profileLabel = QtWidgets.QLabel(self.centralwidget)
        self.profileLabel.setGeometry(QtCore.QRect(130, 220, 150, 40))
        self.profileLabel.setMinimumSize(QtCore.QSize(150, 40))
        self.profileLabel.setMaximumSize(QtCore.QSize(150, 40))
        self.profileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.profileLabel.setObjectName("profileLabel")
        self.consultsLabel = QtWidgets.QLabel(self.centralwidget)
        self.consultsLabel.setGeometry(QtCore.QRect(370, 220, 150, 40))
        self.consultsLabel.setMinimumSize(QtCore.QSize(150, 40))
        self.consultsLabel.setMaximumSize(QtCore.QSize(150, 40))
        self.consultsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.consultsLabel.setObjectName("consultsLabel")
        self.searchHospitalsLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchHospitalsLabel.setGeometry(QtCore.QRect(200, 590, 250, 80))
        self.searchHospitalsLabel.setMinimumSize(QtCore.QSize(250, 80))
        self.searchHospitalsLabel.setMaximumSize(QtCore.QSize(250, 80))
        self.searchHospitalsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.searchHospitalsLabel.setObjectName("searchHospitalsLabel")
        self.changePasswordLabel = QtWidgets.QLabel(self.centralwidget)
        self.changePasswordLabel.setGeometry(QtCore.QRect(340, 400, 240, 40))
        self.changePasswordLabel.setMinimumSize(QtCore.QSize(240, 40))
        self.changePasswordLabel.setMaximumSize(QtCore.QSize(240, 40))
        self.changePasswordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.changePasswordLabel.setObjectName("changePasswordLabel")
        self.hospitalName = QtWidgets.QLabel(self.centralwidget)
        self.hospitalName.setGeometry(QtCore.QRect(170, 20, 400, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hospitalName.sizePolicy().hasHeightForWidth())
        self.hospitalName.setSizePolicy(sizePolicy)
        self.hospitalName.setMinimumSize(QtCore.QSize(100, 30))
        self.hospitalName.setMaximumSize(QtCore.QSize(400, 100))
        self.hospitalName.setStyleSheet("font-size:20pt;\n"
"font-weight:bold;\n"
"text-decoration: underline")
        self.hospitalName.setObjectName("hospitalName")
        self.bedsLabel = QtWidgets.QLabel(self.centralwidget)
        self.bedsLabel.setGeometry(QtCore.QRect(570, 400, 240, 40))
        self.bedsLabel.setMinimumSize(QtCore.QSize(240, 40))
        self.bedsLabel.setMaximumSize(QtCore.QSize(240, 40))
        self.bedsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bedsLabel.setObjectName("bedsLabel")
        self.eventsLabel = QtWidgets.QLabel(self.centralwidget)
        self.eventsLabel.setGeometry(QtCore.QRect(810, 400, 240, 40))
        self.eventsLabel.setMinimumSize(QtCore.QSize(240, 40))
        self.eventsLabel.setMaximumSize(QtCore.QSize(240, 40))
        self.eventsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.eventsLabel.setObjectName("eventsLabel")
        self.statisticsLabel = QtWidgets.QLabel(self.centralwidget)
        self.statisticsLabel.setGeometry(QtCore.QRect(1050, 400, 240, 40))
        self.statisticsLabel.setMinimumSize(QtCore.QSize(240, 40))
        self.statisticsLabel.setMaximumSize(QtCore.QSize(240, 40))
        self.statisticsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statisticsLabel.setObjectName("statisticsLabel")
        hospitalHome.setCentralWidget(self.centralwidget)

        self.retranslateUi(hospitalHome,loginData)
        QtCore.QMetaObject.connectSlotsByName(hospitalHome)

    def retranslateUi(self, hospitalHome,loginData):
        _translate = QtCore.QCoreApplication.translate
        hospitalHome.setWindowTitle(_translate("hospitalHome", "MainWindow"))
        self.searchBloodBanksLabel.setText(_translate("hospitalHome", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Search </span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Blood Banks</span></p></body></html>"))
        self.searchDispensariesLabel.setText(_translate("hospitalHome", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Search<br>Dispensaries</span></p></body></html>"))
        self.title.setText(_translate("hospitalHome", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; text-decoration: underline;\">MDTouch</span></p></body></html>"))
        self.appointmentsLabel.setText(_translate("hospitalHome", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Appointments</span></p></body></html>"))
        self.billsLabel.setText(_translate("hospitalHome", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Bills</span></p></body></html>"))
        self.noticesLabel.setText(_translate("hospitalHome", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Notices</span></p></body></html>"))
        self.searchTestCentersLabel.setText(_translate("hospitalHome", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Search </span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Test Centers</span></p></body></html>"))
        self.patientsLabel.setText(_translate("hospitalHome", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Patients</span></p></body></html>"))
        self.profileLabel.setText(_translate("hospitalHome", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Profile</span></p></body></html>"))
        self.consultsLabel.setText(_translate("hospitalHome", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Doctors</span></p></body></html>"))
        self.searchHospitalsLabel.setText(_translate("hospitalHome", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Search<br>Emergency Services</span></p></body></html>"))
        self.changePasswordLabel.setText(_translate("hospitalHome", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Change Password</span></p></body></html>"))
        self.hospitalName.setText(_translate("hospitalHome", "hospital_name"))
        self.bedsLabel.setText(_translate("hospitalHome", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Beds</span></p></body></html>"))
        self.eventsLabel.setText(_translate("hospitalHome", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Events</span></p></body></html>"))
        self.statisticsLabel.setText(_translate("hospitalHome", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; text-decoration: underline;\">Statistics</span></p></body></html>"))

        self.clickEvents(hospitalHome,loginData)

    def clickEvents(self, parent,loginData):
        self.hospitalName.setText(str(self.hospitaldata["name"]))
        self.logout.clicked.connect(lambda : self.clickOnLogoutButton(parent))
        self.changePassword.clicked.connect(lambda : self.clickOnChangePassword(parent))
        self.searchTestCenters.clicked.connect(lambda : self.clickOnTestCenter())
        self.searchDispensaries.clicked.connect(lambda : self.clickOnDispenary())
        self.searchBloodBankCenters.clicked.connect(lambda : self.clickOnBloodBank())
        self.searchEmergencyServices.clicked.connect(lambda : self.clickOnEs())
        self.events.clicked.connect(lambda : self.clickOnEvents())
        self.profile.clicked.connect(lambda : self.clickOnProfile(parent))
        self.bills.clicked.connect(lambda : self.clickOnBills(parent))
        self.notices.clicked.connect(lambda : self.clickOnNotice())

    def clickOnBills(self,parent):
        self.window = QDialog()
        self.dialog = billsDialog()
        self.dialog.setup(self.window,self.hospitaldata)
        self.window.setModal(True)
        self.window.show()


    def clickOnProfile(self,parent):
        self.window = QDialog()
        self.dialog = hospitalMyProfileDialog()
        self.dialog.setup(self.window,self.admindata,self.hospitaldata)
        self.window.setModal(True)
        self.window.show()


    def clickOnLogoutButton(self,parent):
        parent.loginpage.setup(parent)

    def clickOnChangePassword(self,parent):
        self.window = QDialog()
        self.dialog = changePassword()
        self.dialog.setup(self.window,self.logindata,self)
        self.window.setModal(True)
        self.window.show()

    def clickOnEvents(self):
        self.window = QDialog()
        self.dialog = eventsDialog()
        self.dialog.setup(self.window,'H',self.hospitaldata)
        self.window.setModal(True)
        self.window.show()


    def clickOnTestCenter(self):
        self.window = QDialog()
        self.dialog = viewTestCenter()
        self.dialog.setup(self.window,)
        self.window.setModal(True)
        self.window.show()

    def clickOnBloodBank(self):
        self.window = QDialog()
        self.dialog = viewBloodBankCenter()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()
    def clickOnDispenary(self):
        self.window = QDialog()
        self.dialog = viewDispensary()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()

    def clickOnEs(self):
        self.window = QDialog()
        self.dialog = viewEs()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()

    def clickOnNotice(self):
        self.window = QDialog()
        self.dialog = noticeList()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()
