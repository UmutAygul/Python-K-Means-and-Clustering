

from PyQt5 import QtCore, QtWidgets


class Ui_spectralwindow(object):
    def setupUi(self, spectralwindow):
        spectralwindow.setObjectName("spectralwindow")
        spectralwindow.resize(387, 226)
        self.centralwidget = QtWidgets.QWidget(spectralwindow)
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.n_clusterline = QtWidgets.QLineEdit(self.centralwidget)
        self.n_clusterline.setObjectName("n_clusterline")
        self.verticalLayout_3.addWidget(self.n_clusterline)
        self.affbox = QtWidgets.QComboBox(self.centralwidget)
        self.affbox.setObjectName("algorithmbox")
        self.affbox.addItem("nearest_neighbors")
        self.affbox.addItem("rbf")
        self.affbox.addItem("precomputed")
        self.affbox.addItem("precomputed_nearest_neighbors")
        self.verticalLayout_3.addWidget(self.affbox)
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
        self.spectralwinb = QtWidgets.QPushButton(self.centralwidget)
        self.spectralwinb.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.spectralwinb)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.setStretch(0, 6)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spectralwindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(spectralwindow)
        self.statusbar.setObjectName("statusbar")
        spectralwindow.setStatusBar(self.statusbar)

        self.retranslateUi(spectralwindow)
        
        
        QtCore.QMetaObject.connectSlotsByName(spectralwindow)
        self.spectralwinb.clicked.connect(spectralwindow.close)
        
        
    def retranslateUi(self, spectralwindow):
        _translate = QtCore.QCoreApplication.translate
        spectralwindow.setWindowTitle(_translate("spectralwindow", "Spectral Clusterin"))
        self.label.setText(_translate("spectralwindow", "Number of cluster, int"))
        self.label_6.setText(_translate("spectralwindow", "Affinity"))
        
        self.spectralwinb.setText(_translate("spectralwindow", "Accept"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    spectralwindow = QtWidgets.QMainWindow()
    ui = Ui_spectralwindow()
    ui.setupUi(spectralwindow)
    spectralwindow.show()
    sys.exit(app.exec_())