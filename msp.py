

from PyQt5 import QtCore, QtWidgets


class Ui_meanshift(object):
    """! The Meanshift  class.
    Menu(interface) window sets up in this class
    @param self.label_6 holds the data of the hierarchical function
    @param self.msbut It is accept button
        
    """
    def setupUi(self, meanshift):
        meanshift.setObjectName("meanshift")
        meanshift.resize(365, 148)
        self.centralwidget = QtWidgets.QWidget(meanshift)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.quantilebox = QtWidgets.QComboBox(self.centralwidget)
        self.quantilebox.setObjectName("quantilebox")

        self.quantilebox.addItem("0.2")
        self.quantilebox.addItem("0.3")
        self.quantilebox.addItem("0.4")
        self.quantilebox.addItem("0.5")
        self.quantilebox.addItem("0.6")
        self.quantilebox.addItem("0.7")
        self.quantilebox.addItem("0.8")
        
        
        
        self.verticalLayout_3.addWidget(self.quantilebox)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.msbut = QtWidgets.QPushButton(self.centralwidget)
        self.msbut.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.msbut)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.setStretch(0, 6)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        meanshift.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(meanshift)
        self.statusbar.setObjectName("statusbar")
        meanshift.setStatusBar(self.statusbar)

        self.retranslateUi(meanshift)
        QtCore.QMetaObject.connectSlotsByName(meanshift)
        self.msbut.clicked.connect(meanshift.close)

    def retranslateUi(self, meanshift):
        _translate = QtCore.QCoreApplication.translate
        meanshift.setWindowTitle(_translate("meanshift", "MainWindow"))
        self.label_6.setText(_translate("meanshift", "Quantile,def=0.3"))
        self.msbut.setText(_translate("meanshift", "Accept"))






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    meanshift = QtWidgets.QMainWindow()
    ms = Ui_meanshift()
    ms.setupUi(meanshift)
    meanshift.show()
    sys.exit(app.exec_())