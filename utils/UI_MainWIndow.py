# This UI was designed using QT Designer and PySide2, recompiled for Python 

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide2.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        # Setting up Main Window & Styling
        MainWindow.setEnabled(True)
        MainWindow.resize(920, 565)
        MainWindow.setMinimumSize(QSize(920, 550))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	width: 100%;\n"
" 	height: 100%;\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #242533, stop:1 #343641);\n"
"\n"
"\n"
"\n"
" 	background-position:  center;\n"
" 	background-repeat: no-repeat;\n"
"	position: absolute;\n"
"  	border-radius: 6px;\n"
"  	left: 0;\n"
"  	top: 0;\n"
"}")
        self.centralwidget = QWidget(MainWindow)


        # Centeral Widget Main Container
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.main_frame = QFrame(self.centralwidget)


        # Main Frame for responsiveness and alignment
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setMinimumSize(QSize(900, 520))
        self.main_frame.setMaximumSize(QSize(16777215, 16777215))
        self.main_frame.setMouseTracking(False)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.main_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.controllers_frame = QFrame(self.main_frame)


        # Controllers From For Labels & Input Fields
        self.controllers_frame.setObjectName(u"controllers_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.controllers_frame.sizePolicy().hasHeightForWidth())
        self.controllers_frame.setSizePolicy(sizePolicy1)
        self.controllers_frame.setMinimumSize(QSize(257, 500))
        self.controllers_frame.setMaximumSize(QSize(500, 16777215))
        self.controllers_frame.setFrameShape(QFrame.StyledPanel)
        self.controllers_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.controllers_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(self.controllers_frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 200, 73);\n"
"	margin-right:5%;\n"
"	margin-left:5%;\n"
"\n"
"}")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.function_label = QLabel(self.controllers_frame)
        self.function_label.setObjectName(u"function_label")
        self.function_label.setStyleSheet(u"/* Styling for the input field label */\n"
"QLabel {\n"
"  color: rgb(255, 255, 255); /* Label text color */\n"
"  font-size: 14px; /* Label font size */\n"
"  padding-bottom: 2px; /* Bottom padding for label */\n"
"	font-weight: bold;\n"
"	margin-left: 10%;\n"
"	margin-right:10%;\n"
"\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.function_label)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.function_input = QLineEdit(self.controllers_frame)
        self.function_input.setObjectName(u"function_input")
        font1 = QFont()
        self.function_input.setFont(font1)
        self.function_input.setStyleSheet(u"/* Styling for the input field */\n"
"QLineEdit {\n"
"  padding: 6px; /* Padding around the input field */\n"
"  border: 2px solid rgb(203, 203, 203);\n"
"  border-radius: 10px; \n"
"  font-size: 13px; \n"
"  color: rgb(0, 0, 0);\n"
"	margin-left: 10%;\n"
"	margin-right:10%;\n"
"margin-bottom: 5%;\n"
"\n"
"}\n"
"\n"
"/* Styling for the input field when it has focus */\n"
"QLineEdit:focus {\n"
"  border-color:rgb(255, 200, 73); /* Border color when focused */\n"
"  outline: none; /* Remove the default focus outline */\n"
"}\n"
"\n"
"/* Styling for the input field placeholder text */\n"
"QLineEdit::placeholder {\n"
"  color: rgb(199, 199, 199); /* Placeholder text color */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.function_input)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.min_label = QLabel(self.controllers_frame)
        self.min_label.setObjectName(u"min_label")
        self.min_label.setStyleSheet(u"/* Styling for the input field label */\n"
"QLabel {\n"
"  color: rgb(255, 255, 255); /* Label text color */\n"
"  font-size: 14px; /* Label font size */\n"
"  padding-bottom: 2px; /* Bottom padding for label */\n"
"	font-weight: bold;\n"
"	margin-left: 10%;\n"
"	margin-right:10%;\n"
"\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.min_label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.min_input = QLineEdit(self.controllers_frame)
        self.min_input.setObjectName(u"min_input")
        self.min_input.setFont(font1)
        self.min_input.setStyleSheet(u"/* Styling for the input field */\n"
"QLineEdit {\n"
"  padding: 6px; /* Padding around the input field */\n"
"  border: 2px solid rgb(203, 203, 203);\n"
"  border-radius: 10px; \n"
"  font-size: 13px; \n"
"  color: rgb(0, 0, 0);\n"
"	margin-left: 10%;\n"
"	margin-right:10%;\n"
"margin-bottom: 5%;\n"
"\n"
"}\n"
"\n"
"/* Styling for the input field when it has focus */\n"
"QLineEdit:focus {\n"
"  border-color:rgb(255, 200, 73); /* Border color when focused */\n"
"  outline: none; /* Remove the default focus outline */\n"
"}\n"
"\n"
"/* Styling for the input field placeholder text */\n"
"QLineEdit::placeholder {\n"
"  color: rgb(199, 199, 199); /* Placeholder text color */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.min_input)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.max_label = QLabel(self.controllers_frame)
        self.max_label.setObjectName(u"max_label")
        self.max_label.setStyleSheet(u"/* Styling for the input field label */\n"
"QLabel {\n"
"  color: rgb(255, 255, 255); /* Label text color */\n"
"  font-size: 14px; /* Label font size */\n"
"  padding-bottom: 2px; /* Bottom padding for label */\n"
"	font-weight: bold;\n"
"	margin-left: 10%;\n"
"	margin-right:10%;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.max_label)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.max_input = QLineEdit(self.controllers_frame)
        self.max_input.setObjectName(u"max_input")
        self.max_input.setFont(font1)
        self.max_input.setStyleSheet(u"/* Styling for the input field */\n"
"QLineEdit {\n"
"  padding: 6px; /* Padding around the input field */\n"
"  border: 2px solid rgb(203, 203, 203);\n"
"  border-radius: 10px; \n"
"  font-size: 13px; \n"
"  color: rgb(0, 0, 0);\n"
"	margin-left: 10%;\n"
"	margin-right:10%;\n"
"margin-bottom: 5%;\n"
"\n"
"}\n"
"\n"
"/* Styling for the input field when it has focus */\n"
"QLineEdit:focus {\n"
"  border-color:rgb(255, 200, 73); /* Border color when focused */\n"
"  outline: none; /* Remove the default focus outline */\n"
"}\n"
"\n"
"/* Styling for the input field placeholder text */\n"
"QLineEdit::placeholder {\n"
"  color: rgb(199, 199, 199); /* Placeholder text color */\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.max_input)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.plot_button = QPushButton(self.controllers_frame)
        self.plot_button.setObjectName(u"plot_button")
        self.plot_button.setStyleSheet(u"QPushButton {\n"
"  border-radius: 10px;\n"
"  height: 44px;\n"
"  font-size: 13px;\n"
"  font-weight: 600;\n"
"  text-transform: uppercase;\n"
"  padding: 0 30px;\n"
"  text-align: center;\n"
"  border: none;\n"
"  background-color: #ffeba7;\n"
"  color: #102770;\n"
"  outline: none; /* Remove the outline when button is focused */\n"
"	font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color:rgb(255, 255, 255);\n"
"  color: #000000;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"  background-color: rgb(111, 111, 111);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.plot_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.info_label = QLabel(self.controllers_frame)
        self.info_label.setObjectName(u"info_label")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.info_label.setFont(font2)
        self.info_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	margin-left:10%;\n"
"	margin-right:10%;\n"
"}")
        self.info_label.setTextFormat(Qt.AutoText)
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.info_label)

        self.example_label = QLabel(self.controllers_frame)
        self.example_label.setObjectName(u"example_label")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(True)
        self.example_label.setFont(font3)
        self.example_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	margin-left:10%;\n"
"	margin-right:10%;\n"
"}")
        self.example_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.example_label)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.controllers_frame, 0, 0, 1, 1)


        # Widget Frame to show plotted Function using a Matplot Figure
        self.widget_frame = QFrame(self.main_frame)
        self.widget_frame.setObjectName(u"widget_frame")
        self.widget_frame.setMaximumSize(QSize(16777215, 16777215))
        self.widget_frame.setFrameShape(QFrame.StyledPanel)
        self.widget_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.widget_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.canvas_widget = QWidget(self.widget_frame)
        self.canvas_widget.setObjectName(u"canvas_widget")
        self.canvas_widget.setMinimumSize(QSize(600, 490))
        self.canvas_widget.setMaximumSize(QSize(16777215, 16777215))
        self.canvas_widget.setStyleSheet(u"border-radius: 10px;")

        self.gridLayout_3.addWidget(self.canvas_widget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_frame, 0, 1, 1, 1)
        self.horizontalLayout_5.addWidget(self.main_frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Python Function Plotter", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Python Function Plotter", None))
        self.function_label.setText(QCoreApplication.translate("MainWindow", u"Function", None))
        self.function_input.setText("")
        self.function_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"e.g. 5*x^3 + 2*x", None))
        self.min_label.setText(QCoreApplication.translate("MainWindow", u"Minimum Value for X", None))
        self.min_input.setText("")
        self.min_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a min value for x, e.g. -10", None))
        self.max_label.setText(QCoreApplication.translate("MainWindow", u"Maximum Value for X", None))
        self.max_input.setText("")
        self.max_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"enter a max value for x, e.g. 10", None))
        self.plot_button.setText(QCoreApplication.translate("MainWindow", u"Plot", None))
        self.info_label.setText(QCoreApplication.translate("MainWindow", u"Function Plotter is an app to plot\n1-variable mathematical function.", None))
        self.example_label.setText(QCoreApplication.translate("MainWindow", u"e.g.  5*x^3 + 2*x.", None))
    # retranslateUi

