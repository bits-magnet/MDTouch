

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Dialogs.changePassword import *
from Dialogs.Notice.NoticeList import *

class emergencyServiceHome(object):
    def setup(self, emergencyServiceHome,loginData = None):
        self.logindata = loginData
        emergencyServiceHome.setObjectName("emergencyServiceHome")
        emergencyServiceHome.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(emergencyServiceHome)
        self.centralwidget.setObjectName("centralwidget")
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(1300, 10, 50, 50))
        self.logout.setMinimumSize(QtCore.QSize(50, 50))
        self.logout.setMaximumSize(QtCore.QSize(50, 50))
        self.logout.setStyleSheet("border:none;")
        self.logout.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../MDTouch/Images/LogoutIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout.setIcon(icon)
        self.logout.setIconSize(QtCore.QSize(50, 50))
        self.logout.setObjectName("logout")
        self.profileLabel = QtWidgets.QLabel(self.centralwidget)
        self.profileLabel.setGeometry(QtCore.QRect(560, 540, 221, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profileLabel.sizePolicy().hasHeightForWidth())
        self.profileLabel.setSizePolicy(sizePolicy)
        self.profileLabel.setMinimumSize(QtCore.QSize(100, 30))
        self.profileLabel.setMaximumSize(QtCore.QSize(400, 100))
        self.profileLabel.setStyleSheet("font-size:14pt;\n"
                                        "font-weight:bold;\n"
                                        "text-decoration: underline")
        self.profileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.profileLabel.setObjectName("profileLabel")
        self.changePasswordLabel = QtWidgets.QLabel(self.centralwidget)
        self.changePasswordLabel.setGeometry(QtCore.QRect(860, 545, 221, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.changePasswordLabel.sizePolicy().hasHeightForWidth())
        self.changePasswordLabel.setSizePolicy(sizePolicy)
        self.changePasswordLabel.setMinimumSize(QtCore.QSize(100, 30))
        self.changePasswordLabel.setMaximumSize(QtCore.QSize(400, 100))
        self.changePasswordLabel.setStyleSheet("font-size:14pt;\n"
                                               "font-weight:bold;\n"
                                               "text-decoration: underline")
        self.changePasswordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.changePasswordLabel.setObjectName("changePasswordLabel")
        self.addAmbulanceLabel = QtWidgets.QLabel(self.centralwidget)
        self.addAmbulanceLabel.setGeometry(QtCore.QRect(990, 280, 221, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addAmbulanceLabel.sizePolicy().hasHeightForWidth())
        self.addAmbulanceLabel.setSizePolicy(sizePolicy)
        self.addAmbulanceLabel.setMinimumSize(QtCore.QSize(100, 30))
        self.addAmbulanceLabel.setMaximumSize(QtCore.QSize(400, 100))
        self.addAmbulanceLabel.setStyleSheet("font-size:14pt;\n"
                                             "font-weight:bold;\n"
                                             "text-decoration: underline")
        self.addAmbulanceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.addAmbulanceLabel.setObjectName("addAmbulanceLabel")
        self.noticesLabel = QtWidgets.QLabel(self.centralwidget)
        self.noticesLabel.setGeometry(QtCore.QRect(270, 540, 221, 51))
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
        self.requestsLabel = QtWidgets.QLabel(self.centralwidget)
        self.requestsLabel.setGeometry(QtCore.QRect(160, 280, 221, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.requestsLabel.sizePolicy().hasHeightForWidth())
        self.requestsLabel.setSizePolicy(sizePolicy)
        self.requestsLabel.setMinimumSize(QtCore.QSize(100, 30))
        self.requestsLabel.setMaximumSize(QtCore.QSize(400, 100))
        self.requestsLabel.setStyleSheet("font-size:14pt;\n"
                                         "font-weight:bold;\n"
                                         "text-decoration: underline")
        self.requestsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.requestsLabel.setObjectName("requestsLabel")
        self.inbox = QtWidgets.QPushButton(self.centralwidget)
        self.inbox.setGeometry(QtCore.QRect(1230, 10, 50, 50))
        self.inbox.setMinimumSize(QtCore.QSize(50, 50))
        self.inbox.setMaximumSize(QtCore.QSize(50, 50))
        self.inbox.setStyleSheet("border:none;")
        self.inbox.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../MDTouch/Images/inbox_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.inbox.setIcon(icon1)
        self.inbox.setIconSize(QtCore.QSize(50, 50))
        self.inbox.setObjectName("inbox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 150, 1291, 141))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.requests = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.requests.setMinimumSize(QtCore.QSize(100, 100))
        self.requests.setMaximumSize(QtCore.QSize(100, 100))
        self.requests.setStyleSheet("border:none;")
        self.requests.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../MDTouch/Images/test_requests.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.requests.setIcon(icon2)
        self.requests.setIconSize(QtCore.QSize(100, 100))
        self.requests.setObjectName("requests")
        self.horizontalLayout.addWidget(self.requests)
        self.records = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.records.setMinimumSize(QtCore.QSize(100, 100))
        self.records.setMaximumSize(QtCore.QSize(100, 100))
        self.records.setStyleSheet("border:none;")
        self.records.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../MDTouch/Images/medical_records.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.records.setIcon(icon3)
        self.records.setIconSize(QtCore.QSize(100, 100))
        self.records.setObjectName("records")
        self.horizontalLayout.addWidget(self.records)
        self.viewAmbulances = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.viewAmbulances.setMinimumSize(QtCore.QSize(100, 100))
        self.viewAmbulances.setMaximumSize(QtCore.QSize(100, 100))
        self.viewAmbulances.setStyleSheet("border:none;")
        self.viewAmbulances.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../MDTouch/Images/remove_ambulance.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewAmbulances.setIcon(icon4)
        self.viewAmbulances.setIconSize(QtCore.QSize(100, 100))
        self.viewAmbulances.setObjectName("viewAmbulances")
        self.horizontalLayout.addWidget(self.viewAmbulances)
        self.addAmbulance = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addAmbulance.setMinimumSize(QtCore.QSize(100, 100))
        self.addAmbulance.setMaximumSize(QtCore.QSize(100, 100))
        self.addAmbulance.setStyleSheet("border:none;")
        self.addAmbulance.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../MDTouch/Images/ambulance.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addAmbulance.setIcon(icon5)
        self.addAmbulance.setIconSize(QtCore.QSize(100, 100))
        self.addAmbulance.setObjectName("addAmbulance")
        self.horizontalLayout.addWidget(self.addAmbulance)
        self.viewAmbulancesLabel = QtWidgets.QLabel(self.centralwidget)
        self.viewAmbulancesLabel.setGeometry(QtCore.QRect(700, 280, 231, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewAmbulancesLabel.sizePolicy().hasHeightForWidth())
        self.viewAmbulancesLabel.setSizePolicy(sizePolicy)
        self.viewAmbulancesLabel.setMinimumSize(QtCore.QSize(100, 30))
        self.viewAmbulancesLabel.setMaximumSize(QtCore.QSize(400, 100))
        self.viewAmbulancesLabel.setStyleSheet("font-size:14pt;\n"
                                               "font-weight:bold;\n"
                                               "text-decoration: underline")
        self.viewAmbulancesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.viewAmbulancesLabel.setObjectName("viewAmbulancesLabel")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(550, 10, 281, 70))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        self.title.setMinimumSize(QtCore.QSize(0, 50))
        self.title.setMaximumSize(QtCore.QSize(400, 70))
        self.title.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.title.setObjectName("title")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(150, 430, 1051, 121))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.notices = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.notices.setMinimumSize(QtCore.QSize(100, 100))
        self.notices.setMaximumSize(QtCore.QSize(100, 100))
        self.notices.setStyleSheet("border:none;")
        self.notices.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../MDTouch/Images/notices.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notices.setIcon(icon6)
        self.notices.setIconSize(QtCore.QSize(100, 100))
        self.notices.setObjectName("notices")
        self.horizontalLayout_2.addWidget(self.notices)
        self.profile = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.profile.setMinimumSize(QtCore.QSize(100, 100))
        self.profile.setMaximumSize(QtCore.QSize(100, 100))
        self.profile.setStyleSheet("border:none;")
        self.profile.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../MDTouch/Images/profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.profile.setIcon(icon7)
        self.profile.setIconSize(QtCore.QSize(100, 100))
        self.profile.setObjectName("profile")
        self.horizontalLayout_2.addWidget(self.profile)
        self.changePassword = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.changePassword.setMinimumSize(QtCore.QSize(100, 100))
        self.changePassword.setMaximumSize(QtCore.QSize(100, 100))
        self.changePassword.setStyleSheet("border:none;")
        self.changePassword.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../MDTouch/Images/change_password.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.changePassword.setIcon(icon8)
        self.changePassword.setIconSize(QtCore.QSize(100, 100))
        self.changePassword.setObjectName("changePassword")
        self.horizontalLayout_2.addWidget(self.changePassword)
        self.emergencyServiceName = QtWidgets.QLabel(self.centralwidget)
        self.emergencyServiceName.setGeometry(QtCore.QRect(30, 20, 400, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emergencyServiceName.sizePolicy().hasHeightForWidth())
        self.emergencyServiceName.setSizePolicy(sizePolicy)
        self.emergencyServiceName.setMinimumSize(QtCore.QSize(100, 30))
        self.emergencyServiceName.setMaximumSize(QtCore.QSize(400, 100))
        self.emergencyServiceName.setStyleSheet("font-size:20pt;\n"
                                                "font-weight:bold;\n"
                                                "text-decoration: underline")
        self.emergencyServiceName.setObjectName("emergencyServiceName")
        self.recordsLabel = QtWidgets.QLabel(self.centralwidget)
        self.recordsLabel.setGeometry(QtCore.QRect(420, 280, 221, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recordsLabel.sizePolicy().hasHeightForWidth())
        self.recordsLabel.setSizePolicy(sizePolicy)
        self.recordsLabel.setMinimumSize(QtCore.QSize(100, 30))
        self.recordsLabel.setMaximumSize(QtCore.QSize(400, 100))
        self.recordsLabel.setStyleSheet("font-size:14pt;\n"
                                        "font-weight:bold;\n"
                                        "text-decoration: underline")
        self.recordsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.recordsLabel.setObjectName("recordsLabel")
        emergencyServiceHome.setCentralWidget(self.centralwidget)

        self.retranslateUi(emergencyServiceHome)
        QtCore.QMetaObject.connectSlotsByName(emergencyServiceHome)

    def retranslateUi(self, emergencyServiceHome):
        _translate = QtCore.QCoreApplication.translate
        emergencyServiceHome.setWindowTitle(_translate("emergencyServiceHome", "MainWindow"))
        self.profileLabel.setText(_translate("emergencyServiceHome", "<html><head/><body><p><span style=\" font-size:16pt;\">Profile</span></p></body></html>"))
        self.changePasswordLabel.setText(_translate("emergencyServiceHome", "<html><head/><body><p><span style=\" font-size:16pt;\">Change<br>Password</span></p></body></html>"))
        self.addAmbulanceLabel.setText(_translate("emergencyServiceHome", "<html><head/><body><p><span style=\" font-size:16pt;\">Add Ambulance</span></p></body></html>"))
        self.noticesLabel.setText(_translate("emergencyServiceHome", "<html><head/><body><p><span style=\" font-size:16pt;\">Notices</span></p></body></html>"))
        self.requestsLabel.setText(_translate("emergencyServiceHome", "<html><head/><body><p><span style=\" font-size:16pt;\">Requests</span></p></body></html>"))
        self.viewAmbulancesLabel.setText(_translate("emergencyServiceHome", "<html><head/><body><p><span style=\" font-size:16pt;\">View Ambulances</span></p></body></html>"))
        self.title.setText(_translate("emergencyServiceHome", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                              "p, li { white-space: pre-wrap; }\n"
                                                              "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
                                                              "<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; text-decoration: underline;\">MDTouch</span></p></body></html>"))
        self.emergencyServiceName.setText(_translate("emergencyServiceHome", "emergency_service_name"))
        self.recordsLabel.setText(_translate("emergencyServiceHome", "<html><head/><body><p><span style=\" font-size:16pt;\">Records</span></p></body></html>"))

        self.clickEvents(emergencyServiceHome)

    def clickEvents(self,parent):
        self.logout.clicked.connect(lambda : self.clickOnLogoutButton(parent))
        self.changePassword.clicked.connect(lambda : self.clickOnChangePassword(parent))
        self.notices.clicked.connect(lambda : self.clickOnNotice())

    def clickOnLogoutButton(self,parent):
        parent.loginpage.setup(parent)

    def clickOnChangePassword(self,parent):
        self.window = QDialog()
        self.dialog = changePassword()
        self.dialog.setup(self.window,self.logindata,self)
        self.window.setModal(True)
        self.window.show()

    def clickOnNotice(self):
        self.window = QDialog()
        self.dialog = noticeList()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()