from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Dialogs.superadmin.TestCenters.addTestCenter import *
from Dialogs.superadmin.TestCenters.selectTestCenter import *
from Dialogs.broadcast import *

class TestCenter(object):
    def setup(self, TestCenter, superadmin):
        TestCenter.setObjectName("TestCenter")
        TestCenter.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(TestCenter)
        self.centralwidget.setObjectName("centralwidget")
        self.logout = QtWidgets.QPushButton(self.centralwidget)
        self.logout.setGeometry(QtCore.QRect(1240, 10, 101, 91))
        self.logout.setStyleSheet("border:none;")
        self.logout.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../MDTouch/Images/logout.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logout.setIcon(icon)
        self.logout.setIconSize(QtCore.QSize(80, 80))
        self.logout.setObjectName("logout")
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setGeometry(QtCore.QRect(30, 0, 101, 100))
        self.back.setStyleSheet("border:none;")
        self.back.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../MDTouch/Images/back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back.setIcon(icon1)
        self.back.setIconSize(QtCore.QSize(80, 80))
        self.back.setObjectName("back")
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
        self.addTestCenterLabel = QtWidgets.QLabel(self.centralwidget)
        self.addTestCenterLabel.setGeometry(QtCore.QRect(240, 360, 180, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addTestCenterLabel.sizePolicy().hasHeightForWidth())
        self.addTestCenterLabel.setSizePolicy(sizePolicy)
        self.addTestCenterLabel.setObjectName("addTestCenterLabel")
        self.broadcastLabel = QtWidgets.QLabel(self.centralwidget)
        self.broadcastLabel.setGeometry(QtCore.QRect(960, 660, 161, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.broadcastLabel.sizePolicy().hasHeightForWidth())
        self.broadcastLabel.setSizePolicy(sizePolicy)
        self.broadcastLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.broadcastLabel.setObjectName("broadcastLabel")
        self.removeTestCentersLabel = QtWidgets.QLabel(self.centralwidget)
        self.removeTestCentersLabel.setGeometry(QtCore.QRect(940, 360, 200, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.removeTestCentersLabel.sizePolicy().hasHeightForWidth())
        self.removeTestCentersLabel.setSizePolicy(sizePolicy)
        self.removeTestCentersLabel.setObjectName("removeTestCentersLabel")
        self.viewTestCentersLabel = QtWidgets.QLabel(self.centralwidget)
        self.viewTestCentersLabel.setGeometry(QtCore.QRect(580, 360, 200, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewTestCentersLabel.sizePolicy().hasHeightForWidth())
        self.viewTestCentersLabel.setSizePolicy(sizePolicy)
        self.viewTestCentersLabel.setObjectName("viewTestCentersLabel")
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../MDTouch/Images/hospital.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hospitals.setIcon(icon2)
        self.hospitals.setIconSize(QtCore.QSize(50, 50))
        self.hospitals.setObjectName("hospitals")
        self.horizontalLayout_4.addWidget(self.hospitals)
        self.events = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.events.setMaximumSize(QtCore.QSize(80, 80))
        self.events.setStyleSheet("border:none;")
        self.events.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../MDTouch/Images/event.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.events.setIcon(icon3)
        self.events.setIconSize(QtCore.QSize(50, 50))
        self.events.setObjectName("events")
        self.horizontalLayout_4.addWidget(self.events)
        self.bloodBank = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.bloodBank.setMaximumSize(QtCore.QSize(80, 80))
        self.bloodBank.setStyleSheet("border:none;")
        self.bloodBank.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../MDTouch/Images/bloodbank.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bloodBank.setIcon(icon4)
        self.bloodBank.setIconSize(QtCore.QSize(50, 50))
        self.bloodBank.setObjectName("bloodBank")
        self.horizontalLayout_4.addWidget(self.bloodBank)
        self.testCenters = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.testCenters.setMaximumSize(QtCore.QSize(80, 80))
        self.testCenters.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"border:none;")
        self.testCenters.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("../MDTouch/Images/test_2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.testCenters.setIcon(icon5)
        self.testCenters.setIconSize(QtCore.QSize(50, 50))
        self.testCenters.setObjectName("testCenters")
        self.horizontalLayout_4.addWidget(self.testCenters)
        self.doctors = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.doctors.setMaximumSize(QtCore.QSize(80, 80))
        self.doctors.setStyleSheet("border:none;")
        self.doctors.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("../MDTouch/Images/doctor.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.doctors.setIcon(icon6)
        self.doctors.setIconSize(QtCore.QSize(50, 50))
        self.doctors.setObjectName("doctors")
        self.horizontalLayout_4.addWidget(self.doctors)
        self.dispensary = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.dispensary.setMaximumSize(QtCore.QSize(80, 80))
        self.dispensary.setStyleSheet("border:none;")
        self.dispensary.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("../MDTouch/Images/dispensary.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.dispensary.setIcon(icon7)
        self.dispensary.setIconSize(QtCore.QSize(50, 50))
        self.dispensary.setObjectName("dispensary")
        self.horizontalLayout_4.addWidget(self.dispensary)
        self.emergency = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.emergency.setMaximumSize(QtCore.QSize(80, 80))
        self.emergency.setStyleSheet("border:none;")
        self.emergency.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("../MDTouch/Images/ambulance.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.emergency.setIcon(icon8)
        self.emergency.setIconSize(QtCore.QSize(50, 50))
        self.emergency.setObjectName("emergency")
        self.horizontalLayout_4.addWidget(self.emergency)
        self.searchTestsLabel = QtWidgets.QLabel(self.centralwidget)
        self.searchTestsLabel.setGeometry(QtCore.QRect(250, 660, 150, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchTestsLabel.sizePolicy().hasHeightForWidth())
        self.searchTestsLabel.setSizePolicy(sizePolicy)
        self.searchTestsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.searchTestsLabel.setObjectName("searchTestsLabel")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 230, 1291, 151))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addTestCenter = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.addTestCenter.setMaximumSize(QtCore.QSize(120, 120))
        self.addTestCenter.setStyleSheet("border:none;")
        self.addTestCenter.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("../MDTouch/Images/add_testCenter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addTestCenter.setIcon(icon9)
        self.addTestCenter.setIconSize(QtCore.QSize(100, 100))
        self.addTestCenter.setObjectName("addTestCenter")
        self.horizontalLayout.addWidget(self.addTestCenter)
        self.viewTestCenter = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewTestCenter.sizePolicy().hasHeightForWidth())
        self.viewTestCenter.setSizePolicy(sizePolicy)
        self.viewTestCenter.setMaximumSize(QtCore.QSize(120, 120))
        self.viewTestCenter.setStyleSheet("border:none;")
        self.viewTestCenter.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("../MDTouch/Images/search_testCenters.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.viewTestCenter.setIcon(icon10)
        self.viewTestCenter.setIconSize(QtCore.QSize(100, 100))
        self.viewTestCenter.setObjectName("viewTestCenter")
        self.horizontalLayout.addWidget(self.viewTestCenter)
        self.removeTestCenter = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.removeTestCenter.setMaximumSize(QtCore.QSize(120, 120))
        self.removeTestCenter.setStyleSheet("border:none;")
        self.removeTestCenter.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("../MDTouch/Images/remove_testCenters.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeTestCenter.setIcon(icon11)
        self.removeTestCenter.setIconSize(QtCore.QSize(125, 125))
        self.removeTestCenter.setObjectName("removeTestCenter")
        self.horizontalLayout.addWidget(self.removeTestCenter)
        self.statisticsLabel = QtWidgets.QLabel(self.centralwidget)
        self.statisticsLabel.setGeometry(QtCore.QRect(620, 660, 150, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statisticsLabel.sizePolicy().hasHeightForWidth())
        self.statisticsLabel.setSizePolicy(sizePolicy)
        self.statisticsLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.statisticsLabel.setObjectName("statisticsLabel")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 520, 1291, 161))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.searchTests = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchTests.sizePolicy().hasHeightForWidth())
        self.searchTests.setSizePolicy(sizePolicy)
        self.searchTests.setMaximumSize(QtCore.QSize(120, 120))
        self.searchTests.setStyleSheet("border:none;")
        self.searchTests.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("../MDTouch/Images/search_test.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchTests.setIcon(icon12)
        self.searchTests.setIconSize(QtCore.QSize(100, 100))
        self.searchTests.setObjectName("searchTests")
        self.horizontalLayout_2.addWidget(self.searchTests)
        self.statistics = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statistics.sizePolicy().hasHeightForWidth())
        self.statistics.setSizePolicy(sizePolicy)
        self.statistics.setMaximumSize(QtCore.QSize(120, 120))
        self.statistics.setStyleSheet("border:none;")
        self.statistics.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("../MDTouch/Images/statistics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.statistics.setIcon(icon13)
        self.statistics.setIconSize(QtCore.QSize(100, 100))
        self.statistics.setObjectName("statistics")
        self.horizontalLayout_2.addWidget(self.statistics)
        self.broadcast = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.broadcast.sizePolicy().hasHeightForWidth())
        self.broadcast.setSizePolicy(sizePolicy)
        self.broadcast.setMaximumSize(QtCore.QSize(120, 120))
        self.broadcast.setStyleSheet("border:none;")
        self.broadcast.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("../MDTouch/Images/broadcast.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.broadcast.setIcon(icon14)
        self.broadcast.setIconSize(QtCore.QSize(100, 100))
        self.broadcast.setObjectName("broadcast")
        self.horizontalLayout_2.addWidget(self.broadcast)
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
        TestCenter.setCentralWidget(self.centralwidget)

        self.retranslateUi(TestCenter, superadmin)
        QtCore.QMetaObject.connectSlotsByName(TestCenter)

    def retranslateUi(self, TestCenter, superadmin):
        _translate = QtCore.QCoreApplication.translate
        TestCenter.setWindowTitle(_translate("TestCenter", "MainWindow"))
        self.title.setText(_translate("TestCenter", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; font-weight:600; text-decoration: underline;\">MDTouch</span></p></body></html>"))
        self.addTestCenterLabel.setText(_translate("TestCenter", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Add</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Test Center</span></p></body></html>"))
        self.broadcastLabel.setText(_translate("TestCenter", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Broadcast</span></p></body></html>"))
        self.removeTestCentersLabel.setText(_translate("TestCenter", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Remove</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Test Centers</span></p></body></html>"))
        self.viewTestCentersLabel.setText(_translate("TestCenter", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">View</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Test Centers</span></p></body></html>"))
        self.searchTestsLabel.setText(_translate("TestCenter", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Search</span></p><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Tests</span></p></body></html>"))
        self.statisticsLabel.setText(_translate("TestCenter", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Statistics</span></p></body></html>"))

        self.clickEvents(TestCenter, superadmin)

    def clickEvents(self, parent, superadmin):
        self.hospitals.clicked.connect(lambda: self.clickOnHospital(parent, superadmin))
        self.bloodBank.clicked.connect(lambda: self.clickOnBloodBank(parent, superadmin))
        self.testCenters.clicked.connect(lambda: self.clickOnTestCenters(parent, superadmin))
        self.emergency.clicked.connect(lambda: self.clickOnEmergency(parent, superadmin))
        self.dispensary.clicked.connect(lambda: self.clickOnDispensary(parent, superadmin))
        self.doctors.clicked.connect(lambda: self.clickOnDoctors(parent, superadmin))
        self.logout.clicked.connect(lambda: self.clickOnLogOut(parent, superadmin))
        self.inbox.clicked.connect(lambda: self.clickOnInbox(parent, superadmin))
        self.back.clicked.connect(lambda: self.clickOnBack(parent, superadmin))
        self.events.clicked.connect(lambda : self.clickOnEvents(parent,superadmin))

        self.addTestCenter.clicked.connect(lambda: self.clickOnAddTestCenter())
        self.removeTestCenter.clicked.connect(lambda: self.clickOnRemoveTestCenter())
        self.broadcast.clicked.connect(lambda: self.clickOnBroadcast())

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
        pass

    def clickOnLogOut(self, parent, superadmin):
        parent.loginpage.setup(parent)

    def clickOnBack(self, parent, superadmin):
        superadmin.setup(parent)


    def clickOnAddTestCenter(self):
        self.window = QDialog()
        self.dialog = addTestCenter()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()

    def clickOnRemoveTestCenter(self):
        self.window = QDialog()
        self.dialog = selectTestCenter()
        self.dialog.setup(self.window)
        self.window.setModal(True)
        self.window.show()

    def clickOnBroadcast(self):
        self.window = QDialog()
        self.dialog = broadcast()
        self.dialog.setup(self.window, caller.TestCenter)
        self.window.setModal(True)
        self.window.show()