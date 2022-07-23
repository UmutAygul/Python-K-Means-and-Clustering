

from PyQt5 import QtCore, QtWidgets


class Ui_affWindow(object):
    """! The Affinity  class.
    Menu(interface) window sets up in this class
    @param self.label_2 is input variables
    @param self.label is input variables
    @param self.affb is input variables
        
    """
    def setupUi(self, affWindow):
        affWindow.setObjectName("affWindow")
        affWindow.resize(387, 226)
        self.centralwidget = QtWidgets.QWidget(affWindow)
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)


  
    
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        
        self.pref = QtWidgets.QLineEdit(self.centralwidget)
        self.pref.setObjectName("preference")
        self.verticalLayout_3.addWidget(self.pref)
        
        self.convergence_iter = QtWidgets.QLineEdit(self.centralwidget)
        self.convergence_iter.setObjectName("convergence_iter")
        
        
        self.verticalLayout_3.addWidget(self.convergence_iter)
   
        
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
        self.affb = QtWidgets.QPushButton(self.centralwidget)
        self.affb.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.affb)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        affWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(affWindow)
        self.statusbar.setObjectName("statusbar")
        affWindow.setStatusBar(self.statusbar)

        self.retranslateUi(affWindow)
        QtCore.QMetaObject.connectSlotsByName(affWindow)

        self.affb.clicked.connect(affWindow.close)


    def retranslateUi(self, affWindow):
        _translate = QtCore.QCoreApplication.translate
        affWindow.setWindowTitle(_translate("affWindow", "Affinity Propagation"))
        self.label_2.setText(_translate("affWindow", "max_iter, def=200"))
        self.label.setText(_translate("affWindow", "convergence_iter, def=15"))

        
        self.affb.setText(_translate("affWindow", "Accept"))
        
        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    affWindow = QtWidgets.QMainWindow()
    ui = Ui_affWindow()
    ui.setupUi(affWindow)
    affWindow.show()
    sys.exit(app.exec_())