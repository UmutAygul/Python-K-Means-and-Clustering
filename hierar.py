

from PyQt5 import QtCore, QtWidgets


class Ui_hierarc(object):
    """! The Hierarchical Clustering  class.
    Menu(interface) window sets up in this class
    @param self.label_6 holds the data of the hierarchical function
    @param self.hierbut It is accept button
        
    """
    def setupUi(self, hierarc):
        hierarc.setObjectName("hierarc")
        hierarc.resize(365, 148)
        self.centralwidget = QtWidgets.QWidget(hierarc)
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
        self.linkbox = QtWidgets.QComboBox(self.centralwidget)
        self.linkbox.setObjectName("linkbox")
        self.linkbox.addItem("ward")
        self.linkbox.addItem("complete")
        self.linkbox.addItem("average")
        self.linkbox.addItem("single")
        
        self.verticalLayout_3.addWidget(self.linkbox)
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
        self.hierbut = QtWidgets.QPushButton(self.centralwidget)
        self.hierbut.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.hierbut)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.setStretch(0, 6)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        hierarc.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(hierarc)
        self.statusbar.setObjectName("statusbar")
        hierarc.setStatusBar(self.statusbar)

        self.hierbut.clicked.connect(hierarc.close)
        self.retranslateUi(hierarc)
        QtCore.QMetaObject.connectSlotsByName(hierarc)

    def retranslateUi(self, hierarc):
        _translate = QtCore.QCoreApplication.translate
        hierarc.setWindowTitle(_translate("hierarc", "Hierarchical Clustering"))
        self.label_6.setText(_translate("hierarc", "Linkage criterion "))
        
        self.hierbut.setText(_translate("hierarc", "Accept"))
        ## It is accept button




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hierarc = QtWidgets.QMainWindow()
    hier = Ui_hierarc()
    hier.setupUi(hierarc)
    hierarc.show()
    sys.exit(app.exec_())