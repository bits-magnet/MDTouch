# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'superadminHospitals.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_superadminHospitals(object):
    def setupUi(self, superadminHospitals):
        superadminHospitals.setObjectName("superadminHospitals")
        superadminHospitals.resize(1368, 768)
        superadminHospitals.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(superadminHospitals)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(550, 20, 241, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setMinimumSize(QtCore.QSize(0, 50))
        self.title.setMaximumSize(QtCore.QSize(400, 70))
        self.title.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.title.setObjectName("title")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(50, 220, 1291, 171))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addHospital = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addHospital.setMaximumSize(QtCore.QSize(120, 120))
        self.addHospital.setStyleSheet("border:none;")
        self.addHospital.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../MdTouch/Images/add_hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addHospital.setIcon(icon)
        self.addHospital.setIconSize(QtCore.QSize(100, 100))
        self.addHospital.setObjectName("addHospital")
        self.horizontalLayout.addWidget(self.addHospital)
        self.viewHospitals = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.viewHospitals.setMaximumSize(QtCore.QSize(120, 120))
        self.viewHospitals.setStyleSheet("border:none;")
        self.viewHospitals.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../MdTouch/Images/search_hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewHospitals.setIcon(icon1)
        self.viewHospitals.setIconSize(QtCore.QSize(100, 100))
        self.viewHospitals.setObjectName("viewHospitals")
        self.horizontalLayout.addWidget(self.viewHospitals)
        self.removeHospital = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.removeHospital.setMaximumSize(QtCore.QSize(120, 120))
        self.removeHospital.setStyleSheet("border:none;")
        self.removeHospital.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../MdTouch/Images/remove_hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeHospital.setIcon(icon2)
        self.removeHospital.setIconSize(QtCore.QSize(100, 100))
        self.removeHospital.setObjectName("removeHospital")
        self.horizontalLayout.addWidget(self.removeHospital)
        self.addAdmin = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addAdmin.setMaximumSize(QtCore.QSize(120, 120))
        self.addAdmin.setStyleSheet("border:none;")
        self.addAdmin.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../MdTouch/Images/add_admin.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addAdmin.setIcon(icon3)
        self.addAdmin.setIconSize(QtCore.QSize(100, 100))
        self.addAdmin.setObjectName("addAdmin")
        self.horizontalLayout.addWidget(self.addAdmin)
        self.removeAdmin = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.removeAdmin.setMaximumSize(QtCore.QSize(120, 120))
        self.removeAdmin.setStyleSheet("border:none;")
        self.removeAdmin.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../MdTouch/Images/remove_admin.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeAdmin.setIcon(icon4)
        self.removeAdmin.setIconSize(QtCore.QSize(100, 100))
        self.removeAdmin.setObjectName("removeAdmin")
        self.horizontalLayout.addWidget(self.removeAdmin)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 500, 1281, 161))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fraud = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.fraud.setMaximumSize(QtCore.QSize(120, 120))
        self.fraud.setMouseTracking(True)
        self.fraud.setStyleSheet("border:none;")
        self.fraud.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../MdTouch/Images/fraud.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fraud.setIcon(icon5)
        self.fraud.setIconSize(QtCore.QSize(100, 100))
        self.fraud.setCheckable(False)
        self.fraud.setObjectName("fraud")
        self.horizontalLayout_2.addWidget(self.fraud)
        self.users = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.users.setMaximumSize(QtCore.QSize(120, 120))
        self.users.setStyleSheet("border:none;")
        self.users.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../MdTouch/Images/users.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.users.setIcon(icon6)
        self.users.setIconSize(QtCore.QSize(100, 100))
        self.users.setObjectName("users")
        self.horizontalLayout_2.addWidget(self.users)
        self.analytics = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.analytics.setMaximumSize(QtCore.QSize(120, 120))
        self.analytics.setMouseTracking(True)
        self.analytics.setStyleSheet("border:none;")
        self.analytics.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../MdTouch/Images/statistics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.analytics.setIcon(icon7)
        self.analytics.setIconSize(QtCore.QSize(100, 100))
        self.analytics.setCheckable(False)
        self.analytics.setObjectName("analytics")
        self.horizontalLayout_2.addWidget(self.analytics)
        self.broadcast = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.broadcast.setMaximumSize(QtCore.QSize(120, 120))
        self.broadcast.setStyleSheet("border:none;\n"
"")
        self.broadcast.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../MdTouch/Images/broadcast.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.broadcast.setIcon(icon8)
        self.broadcast.setIconSize(QtCore.QSize(100, 100))
        self.broadcast.setObjectName("broadcast")
        self.horizontalLayout_2.addWidget(self.broadcast)
        self.beds = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.beds.setMaximumSize(QtCore.QSize(120, 120))
        self.beds.setMouseTracking(True)
        self.beds.setStyleSheet("border:none;")
        self.beds.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../MdTouch/Images/hospital_beds.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.beds.setIcon(icon9)
        self.beds.setIconSize(QtCore.QSize(100, 100))
        self.beds.setCheckable(False)
        self.beds.setObjectName("beds")
        self.horizontalLayout_2.addWidget(self.beds)
        self.addHospitalLabel = QtWidgets.QLabel(self.centralwidget)
        self.addHospitalLabel.setGeometry(QtCore.QRect(160, 370, 126, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addHospitalLabel.sizePolicy().hasHeightForWidth())
        self.addHospitalLabel.setSizePolicy(sizePolicy)
        self.addHospitalLabel.setObjectName("addHospitalLabel")
        self.userLabel = QtWidgets.QLabel(self.centralwidget)
        self.userLabel.setGeometry(QtCore.QRect(370, 650, 161, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userLabel.sizePolicy().hasHeightForWidth())
        self.userLabel.setSizePolicy(sizePolicy)
        self.userLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.userLabel.setObjectName("userLabel")
        self.analyticsLabel = QtWidgets.QLabel(self.centralwidget)
        self.analyticsLabel.setGeometry(QtCore.QRect(620, 650, 141, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analyticsLabel.sizePolicy().hasHeightForWidth())
        self.analyticsLabel.setSizePolicy(sizePolicy)
        self.analyticsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.analyticsLabel.setObjectName("analyticsLabel")
        self.broadcastLabel = QtWidgets.QLabel(self.centralwidget)
        self.broadcastLabel.setGeometry(QtCore.QRect(850, 650, 161, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.broadcastLabel.sizePolicy().hasHeightForWidth())
        self.broadcastLabel.setSizePolicy(sizePolicy)
        self.broadcastLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.broadcastLabel.setObjectName("broadcastLabel")
        self.bedsLabel = QtWidgets.QLabel(self.centralwidget)
        self.bedsLabel.setGeometry(QtCore.QRect(1090, 650, 151, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bedsLabel.sizePolicy().hasHeightForWidth())
        self.bedsLabel.setSizePolicy(sizePolicy)
        self.bedsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.bedsLabel.setObjectName("bedsLabel")
        self.fraudLabel = QtWidgets.QLabel(self.centralwidget)
        self.fraudLabel.setGeometry(QtCore.QRect(140, 650, 161, 81))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fraudLabel.sizePolicy().hasHeightForWidth())
        self.fraudLabel.setSizePolicy(sizePolicy)
        self.fraudLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.fraudLabel.setObjectName("fraudLabel")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(30, 0, 101, 100))
        self.back.setStyleSheet("border:none;")
        self.back.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../MdTouch/Images/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon10)
        self.back.setIconSize(QtCore.QSize(80, 80))
        self.back.setObjectName("back")
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(1240, 10, 101, 91))
        self.logout.setStyleSheet("border:none;")
        self.logout.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../MdTouch/Images/logout.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout.setIcon(icon11)
        self.logout.setIconSize(QtCore.QSize(80, 80))
        self.logout.setObjectName("logout")
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
        self.hospitals.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border:none;")
        self.hospitals.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../MdTouch/Images/hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hospitals.setIcon(icon12)
        self.hospitals.setIconSize(QtCore.QSize(50, 50))
        self.hospitals.setObjectName("hospitals")
        self.horizontalLayout_4.addWidget(self.hospitals)
        self.events = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.events.setMaximumSize(QtCore.QSize(80, 80))
        self.events.setStyleSheet("border:none;")
        self.events.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("../MdTouch/Images/event.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.events.setIcon(icon13)
        self.events.setIconSize(QtCore.QSize(50, 50))
        self.events.setObjectName("events")
        self.horizontalLayout_4.addWidget(self.events)
        self.bloodBank = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.bloodBank.setMaximumSize(QtCore.QSize(80, 80))
        self.bloodBank.setStyleSheet("border:none;")
        self.bloodBank.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("../MdTouch/Images/bloodbank.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bloodBank.setIcon(icon14)
        self.bloodBank.setIconSize(QtCore.QSize(50, 50))
        self.bloodBank.setObjectName("bloodBank")
        self.horizontalLayout_4.addWidget(self.bloodBank)
        self.testCenters = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.testCenters.setMaximumSize(QtCore.QSize(80, 80))
        self.testCenters.setStyleSheet("border:none;")
        self.testCenters.setText("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("../MdTouch/Images/test_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.testCenters.setIcon(icon15)
        self.testCenters.setIconSize(QtCore.QSize(50, 50))
        self.testCenters.setObjectName("testCenters")
        self.horizontalLayout_4.addWidget(self.testCenters)
        self.doctors = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.doctors.setMaximumSize(QtCore.QSize(80, 80))
        self.doctors.setStyleSheet("border:none;")
        self.doctors.setText("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("../MdTouch/Images/doctor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.doctors.setIcon(icon16)
        self.doctors.setIconSize(QtCore.QSize(50, 50))
        self.doctors.setObjectName("doctors")
        self.horizontalLayout_4.addWidget(self.doctors)
        self.dispensary = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.dispensary.setMaximumSize(QtCore.QSize(80, 80))
        self.dispensary.setStyleSheet("border:none;")
        self.dispensary.setText("")
        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("../MdTouch/Images/dispensary.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dispensary.setIcon(icon17)
        self.dispensary.setIconSize(QtCore.QSize(50, 50))
        self.dispensary.setObjectName("dispensary")
        self.horizontalLayout_4.addWidget(self.dispensary)
        self.emergency = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.emergency.setMaximumSize(QtCore.QSize(80, 80))
        self.emergency.setStyleSheet("border:none;")
        self.emergency.setText("")
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("../MdTouch/Images/ambulance.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.emergency.setIcon(icon18)
        self.emergency.setIconSize(QtCore.QSize(50, 50))
        self.emergency.setObjectName("emergency")
        self.horizontalLayout_4.addWidget(self.emergency)
        self.removeHospitalLabel = QtWidgets.QLabel(self.centralwidget)
        self.removeHospitalLabel.setGeometry(QtCore.QRect(640, 370, 112, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeHospitalLabel.sizePolicy().hasHeightForWidth())
        self.removeHospitalLabel.setSizePolicy(sizePolicy)
        self.removeHospitalLabel.setObjectName("removeHospitalLabel")
        self.addAdminLabel = QtWidgets.QLabel(self.centralwidget)
        self.addAdminLabel.setGeometry(QtCore.QRect(890, 370, 86, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addAdminLabel.sizePolicy().hasHeightForWidth())
        self.addAdminLabel.setSizePolicy(sizePolicy)
        self.addAdminLabel.setObjectName("addAdminLabel")
        self.removeAdminLabel = QtWidgets.QLabel(self.centralwidget)
        self.removeAdminLabel.setGeometry(QtCore.QRect(1110, 370, 111, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeAdminLabel.sizePolicy().hasHeightForWidth())
        self.removeAdminLabel.setSizePolicy(sizePolicy)
        self.removeAdminLabel.setObjectName("removeAdminLabel")
        self.viewHospitalsLabel = QtWidgets.QLabel(self.centralwidget)
        self.viewHospitalsLabel.setGeometry(QtCore.QRect(390, 370, 126, 78))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewHospitalsLabel.sizePolicy().hasHeightForWidth())
        self.viewHospitalsLabel.setSizePolicy(sizePolicy)
        self.viewHospitalsLabel.setObjectName("viewHospitalsLabel")
        superadminHospitals.setCentralWidget(self.centralwidget)

        self.retranslateUi(superadminHospitals)
        QtCore.QMetaObject.connectSlotsByName(superadminHospitals)

    def retranslateUi(self, superadminHospitals):
        _translate = QtCore.QCoreApplication.translate
        superadminHospitals.setWindowTitle(_translate("superadminHospitals", "MainWindow"))
        self.title.setText(_translate("superadminHospitals", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; text-decoration: underline;\">MDTouch</span></p></body></html>"))
        self.addHospitalLabel.setText(_translate("superadminHospitals", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Add</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Hospital</span></p></body></html>"))
        self.userLabel.setText(_translate("superadminHospitals", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">User</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Statistics</span></p></body></html>"))
        self.analyticsLabel.setText(_translate("superadminHospitals", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Analytics</span></p></body></html>"))
        self.broadcastLabel.setText(_translate("superadminHospitals", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Broadcast</span></p></body></html>"))
        self.bedsLabel.setText(_translate("superadminHospitals", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Beddings</span></p></body></html>"))
        self.fraudLabel.setText(_translate("superadminHospitals", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Fraud</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Inspection</span></p></body></html>"))
        self.removeHospitalLabel.setText(_translate("superadminHospitals", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Remove</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Hospital</span></p></body></html>"))
        self.addAdminLabel.setText(_translate("superadminHospitals", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Add</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Admin</span></p></body></html>"))
        self.removeAdminLabel.setText(_translate("superadminHospitals", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Remove</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Admin</span></p></body></html>"))
        self.viewHospitalsLabel.setText(_translate("superadminHospitals", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">View</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Hospitals</span></p></body></html>"))

