"""!
In this project, an interface was designed and the designed interface,
It is intended to work with the desired functions.

Hill Climbing is a heuristic search technique used in the field of Artificial Intelligence to solve
mathematical optimization issues.It seeks to discover a sufficiently excellent solution to the issue
given a broad number of inputs and a reasonable heuristic function. It's possible that this isn't 
the best option in the world.

Simulated Annealing is a global search optimization technique with a stochastic component.

This indicates that it employs chance as part of the search procedure. This makes the technique suitable for
 nonlinear objective functions, which are difficult to solve with standard local search algorithms.





"""



from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from sklearn.cluster import DBSCAN
import os
import itertools
import numpy as np
import matplotlib.pyplot as plt
import math

from sklearn.metrics import pairwise_distances
from clustering_class import Clustering

from retranslate import ret
from clusters import callfunctions

from kmean import Ui_SecondWindow
from aff2 import Ui_affWindow
from spectralwin import Ui_spectralwindow
from hierar import Ui_hierarc
from msp import Ui_meanshift


class Ui_MainWindow(object):
    """! The Main class.
    Opens all windows and connects buttons 'accept buttons'
    """
    
    def hiertrans(self):
        """! hieararch clustering transfer function
        """
        self.link=self.hs.linkbox.currentText()
        Clustering.hierarca(self, self.X)

    def spectrans(self):
        self.nc =int(self.sp.n_clusterline.text())
        self.affinitychoosen=self.sp.affbox.currentText()
        Clustering.spectralcluster(self,self.X)
    def meanstrans(self):
        self.quantile=float(self.means.quantilebox.currentText())
        Clustering.meanshift(self,self.X)

    def afftransfer(self):
        self.maxiter=int(self.aff.pref.text())
        self.convergenceiter=int(self.aff.convergence_iter.text())
        Clustering.affinity(self, self.X)

    def transfer(self):
        self.nc=int(self.ui.n_clusterline.text())
        self.mi=int(self.ui.max_iterline.text())
        self.initv=self.ui.initbox.currentText()
        self.algorit=self.ui.algorithmbox.currentText()

        Clustering.kmean(self,self.X)
    def meanshiftw(self):
        self.window=QtWidgets.QMainWindow()
        self.means= Ui_meanshift()
        self.means.setupUi(self.window)
        self.window.show()
        self.means.msbut.clicked.connect(self.meanstrans)

    def affWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.aff= Ui_affWindow()
        self.aff.setupUi(self.window)
        self.window.show()
        self.aff.affb.clicked.connect(self.afftransfer)
    
    def spectralw(self):
        self.window=QtWidgets.QMainWindow()
        self.sp=Ui_spectralwindow()
        self.sp.setupUi(self.window)
        self.window.show()
        self.sp.spectralwinb.clicked.connect(self.spectrans)   

    
    def hierarW(self):
        self.window=QtWidgets.QMainWindow()
        self.hs=Ui_hierarc()
        self.hs.setupUi(self.window)
        self.window.show()
        self.hs.hierbut.clicked.connect(self.hiertrans)

    
    
    def openWindow(self):
        self.window=QtWidgets.QMainWindow()
        self.ui= Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.accept.clicked.connect(self.transfer)
   
    
   
    def clustering(self,asdf):
        if asdf=="aff":
            callfunctions.affWindow(self)
        elif asdf=="hw":
            callfunctions.hierarW(self)
        elif asdf=="ms":
            callfunctions.meanshiftw(self)
        elif asdf=="s":
            callfunctions.spectralw(self)
        elif asdf=="km":
            callfunctions.openWindow(self)
    
    
    
    def setupUi(self, MainWindow):
        """! Main interface generating.
        and creating icons
        """
        self.center=list()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1122, 598)
        # MainWindow.resize(1295, 788)
        self.maxinit=int()
        self.quantile=float()
        self.affinitychoosen=''
        self.link=''
        self.nc=int()
        self.mi=int()
        self.initv=""
        self.algorit=""
        self.convergenceiter=int()
        self.affmaxiter=int()
        self.affchosen=""
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setContentsMargins(25, 6, 25, 6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.openfileb = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openfileb.sizePolicy().hasHeightForWidth())
        self.openfileb.setSizePolicy(sizePolicy)
        self.openfileb.setText("")
        self.openfileb.setObjectName("openfileb")
        self.horizontalLayout.addWidget(self.openfileb)
        self.savefinalb = QtWidgets.QPushButton(self.groupBox)
        self.savefinalb.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.savefinalb.sizePolicy().hasHeightForWidth())
        self.savefinalb.setSizePolicy(sizePolicy)
        self.savefinalb.setText("")
        self.savefinalb.setObjectName("savefinalb")
        self.horizontalLayout.addWidget(self.savefinalb)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setContentsMargins(15, -1, 15, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.saveinitialb = QtWidgets.QPushButton(self.groupBox_3)
        self.saveinitialb.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveinitialb.sizePolicy().hasHeightForWidth())
        self.saveinitialb.setSizePolicy(sizePolicy)
        self.saveinitialb.setText("")
        self.saveinitialb.setObjectName("saveinitialb")
        self.horizontalLayout_3.addWidget(self.saveinitialb)
        self.exportasinitialb = QtWidgets.QPushButton(self.groupBox_3)
        self.exportasinitialb.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exportasinitialb.sizePolicy().hasHeightForWidth())
        self.exportasinitialb.setSizePolicy(sizePolicy)
        self.exportasinitialb.setText("")
        self.exportasinitialb.setObjectName("exportasinitialb")
        self.horizontalLayout_3.addWidget(self.exportasinitialb)
        self.clearinitialb = QtWidgets.QPushButton(self.groupBox_3)
        self.clearinitialb.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearinitialb.sizePolicy().hasHeightForWidth())
        self.clearinitialb.setSizePolicy(sizePolicy)
        self.clearinitialb.setText("")
        self.clearinitialb.setObjectName("clearinitialb")
        self.horizontalLayout_3.addWidget(self.clearinitialb)
        self.undoinitialb = QtWidgets.QPushButton(self.groupBox_3)
        self.undoinitialb.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.undoinitialb.sizePolicy().hasHeightForWidth())
        self.undoinitialb.setSizePolicy(sizePolicy)
        self.undoinitialb.setText("")
        self.undoinitialb.setObjectName("undoinitialb")
        self.horizontalLayout_3.addWidget(self.undoinitialb)
        self.redoinitialb = QtWidgets.QPushButton(self.groupBox_3)
        self.redoinitialb.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.redoinitialb.sizePolicy().hasHeightForWidth())
        self.redoinitialb.setSizePolicy(sizePolicy)
        self.redoinitialb.setText("")
        self.redoinitialb.setObjectName("redoinitialb")
        self.horizontalLayout_3.addWidget(self.redoinitialb)
        self.horizontalLayout_4.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.exportasfinalb = QtWidgets.QPushButton(self.groupBox_2)
        self.exportasfinalb.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exportasfinalb.sizePolicy().hasHeightForWidth())
        self.exportasfinalb.setSizePolicy(sizePolicy)
        self.exportasfinalb.setText("")
        self.exportasfinalb.setObjectName("exportasfinalb")
        self.horizontalLayout_2.addWidget(self.exportasfinalb)
        self.clearfinalb = QtWidgets.QPushButton(self.groupBox_2)
        self.clearfinalb.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearfinalb.sizePolicy().hasHeightForWidth())
        self.clearfinalb.setSizePolicy(sizePolicy)
        self.clearfinalb.setText("")
        self.clearfinalb.setObjectName("clearfinalb")
        self.horizontalLayout_2.addWidget(self.clearfinalb)
        self.undofinalb = QtWidgets.QPushButton(self.groupBox_2)
        self.undofinalb.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.undofinalb.sizePolicy().hasHeightForWidth())
        self.undofinalb.setSizePolicy(sizePolicy)
        self.undofinalb.setText("")
        self.undofinalb.setObjectName("undofinalb")
        self.horizontalLayout_2.addWidget(self.undofinalb)
        self.redofinalb = QtWidgets.QPushButton(self.groupBox_2)
        self.redofinalb.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.redofinalb.sizePolicy().hasHeightForWidth())
        self.redofinalb.setSizePolicy(sizePolicy)
        self.redofinalb.setText("")
        self.redofinalb.setObjectName("redofinalb")
        self.horizontalLayout_2.addWidget(self.redofinalb)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 5)
        self.horizontalLayout_4.setStretch(2, 4)
        self.horizontalLayout_4.setStretch(3, 5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.hillclimbingb = QtWidgets.QPushButton(self.groupBox_4)
        self.hillclimbingb.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hillclimbingb.sizePolicy().hasHeightForWidth())
        self.hillclimbingb.setSizePolicy(sizePolicy)
        self.hillclimbingb.setText("")
        self.hillclimbingb.setObjectName("hillclimbingb")
        self.verticalLayout.addWidget(self.hillclimbingb)
        self.simulatedannealingb = QtWidgets.QPushButton(self.groupBox_4)
        self.simulatedannealingb.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.simulatedannealingb.sizePolicy().hasHeightForWidth())
        self.simulatedannealingb.setSizePolicy(sizePolicy)
        self.simulatedannealingb.setText("")
        self.simulatedannealingb.setObjectName("simulatedannealingb")
        self.verticalLayout.addWidget(self.simulatedannealingb)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.kmeanb = QtWidgets.QPushButton(self.groupBox_5)
        self.kmeanb.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kmeanb.sizePolicy().hasHeightForWidth())
        self.kmeanb.setSizePolicy(sizePolicy)
        self.kmeanb.setText("")
        self.kmeanb.setObjectName("kmeanb")
        self.verticalLayout_2.addWidget(self.kmeanb)
        self.affinitypb = QtWidgets.QPushButton(self.groupBox_5)
        self.affinitypb.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.affinitypb.sizePolicy().hasHeightForWidth())
        self.affinitypb.setSizePolicy(sizePolicy)
        self.affinitypb.setText("")
        self.affinitypb.setObjectName("affinitypb")
        self.verticalLayout_2.addWidget(self.affinitypb)
        self.meanshiftb = QtWidgets.QPushButton(self.groupBox_5)
        self.meanshiftb.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.meanshiftb.sizePolicy().hasHeightForWidth())
        self.meanshiftb.setSizePolicy(sizePolicy)
        self.meanshiftb.setText("")
        self.meanshiftb.setObjectName("meanshiftb")
        self.verticalLayout_2.addWidget(self.meanshiftb)
        self.spectralcb = QtWidgets.QPushButton(self.groupBox_5)
        self.spectralcb.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spectralcb.sizePolicy().hasHeightForWidth())
        self.spectralcb.setSizePolicy(sizePolicy)
        self.spectralcb.setText("")
        self.spectralcb.setObjectName("spectralcb")
        self.verticalLayout_2.addWidget(self.spectralcb)
        self.hierarchicalcb = QtWidgets.QPushButton(self.groupBox_5)
        self.hierarchicalcb.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hierarchicalcb.sizePolicy().hasHeightForWidth())
        self.hierarchicalcb.setSizePolicy(sizePolicy)
        self.hierarchicalcb.setText("")
        self.hierarchicalcb.setObjectName("hierarchicalcb")
        self.verticalLayout_2.addWidget(self.hierarchicalcb)
        self.dbscanb = QtWidgets.QPushButton(self.groupBox_5)
        self.dbscanb.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dbscanb.sizePolicy().hasHeightForWidth())
        self.dbscanb.setSizePolicy(sizePolicy)
        self.dbscanb.setText("")
        self.dbscanb.setObjectName("dbscanb")
        self.verticalLayout_2.addWidget(self.dbscanb)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        self.verticalLayout_3.setStretch(0, 4)
        self.verticalLayout_3.setStretch(1, 10)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox_11 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_11.setObjectName("groupBox_11")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.labelinput = QtWidgets.QLabel(self.groupBox_11)
        self.labelinput.setText("")
        self.labelinput.setObjectName("labelinput")
        self.horizontalLayout_13.addWidget(self.labelinput)
        self.horizontalLayout_5.addWidget(self.groupBox_11)
        self.groupBox_12 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_12.setObjectName("groupBox_12")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.labeloutput = QtWidgets.QLabel(self.groupBox_12)
        self.labeloutput.setText("")
        self.labeloutput.setObjectName("labeloutput")
        self.horizontalLayout_14.addWidget(self.labeloutput)
        self.horizontalLayout_5.addWidget(self.groupBox_12)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 9)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 6)
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.hubstext = QtWidgets.QTextEdit(self.groupBox_7)
        self.hubstext.setText("")
        self.hubstext.setObjectName("hubstext")
        self.horizontalLayout_7.addWidget(self.hubstext)
        self.verticalLayout_5.addWidget(self.groupBox_7)
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_8.setObjectName("groupBox_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.nodextext = QtWidgets.QTextEdit(self.groupBox_8)
        self.nodextext.setText("")
        self.nodextext.setObjectName("nodextext")
        self.horizontalLayout_8.addWidget(self.nodextext)
        self.verticalLayout_5.addWidget(self.groupBox_8)
        self.runbutton = QtWidgets.QPushButton(self.groupBox_6)
        self.runbutton.setEnabled(False)
        self.runbutton.setObjectName("runbutton")
        self.verticalLayout_5.addWidget(self.runbutton)
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_6)
        self.groupBox_9.setObjectName("groupBox_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.resulttext = QtWidgets.QTextEdit(self.groupBox_9)
        self.resulttext.setText("")
        self.resulttext.setObjectName("resulttext")
        self.horizontalLayout_9.addWidget(self.resulttext)
        self.verticalLayout_5.addWidget(self.groupBox_9)
        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 2)
        self.verticalLayout_5.setStretch(3, 3)
        self.horizontalLayout_11.addWidget(self.groupBox_6)
        self.horizontalLayout_11.setStretch(0, 8)
        self.horizontalLayout_11.setStretch(1, 2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.groupBox_10 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_10.sizePolicy().hasHeightForWidth())
        self.groupBox_10.setSizePolicy(sizePolicy)
        self.groupBox_10.setObjectName("groupBox_10")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_6 = QtWidgets.QTextEdit(self.groupBox_10)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_12.addWidget(self.label_6)
        self.verticalLayout_6.addWidget(self.groupBox_10)
        self.verticalLayout_6.setStretch(0, 7)
        self.verticalLayout_6.setStretch(1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExport_As = QtWidgets.QMenu(self.menuFile)
        self.menuExport_As.setEnabled(False)
        self.menuExport_As.setObjectName("menuExport_As")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuClear = QtWidgets.QMenu(self.menuEdit)
        self.menuClear.setEnabled(False)
        self.menuClear.setObjectName("menuClear")
        self.menuUndo = QtWidgets.QMenu(self.menuEdit)
        self.menuUndo.setEnabled(False)
        self.menuUndo.setObjectName("menuUndo")
        self.menuRedo = QtWidgets.QMenu(self.menuEdit)
        self.menuRedo.setEnabled(False)
        self.menuRedo.setObjectName("menuRedo")
        self.menuClustering = QtWidgets.QMenu(self.menubar)
        self.menuClustering.setObjectName("menuClustering")
        self.menuHeuristics = QtWidgets.QMenu(self.menubar)
        self.menuHeuristics.setObjectName("menuHeuristics")
        MainWindow.setMenuBar(self.menubar)
        self.Open_Data = QtWidgets.QAction(MainWindow)
        self.Open_Data.setObjectName("Open_Data")
        self.saveinitialsolution = QtWidgets.QAction(MainWindow)
        self.saveinitialsolution.setEnabled(False)
        self.saveinitialsolution.setObjectName("saveinitialsolution")
        self.savefinalsolution = QtWidgets.QAction(MainWindow)
        self.savefinalsolution.setEnabled(False)
        self.savefinalsolution.setObjectName("savefinalsolution")
        self.Exit = QtWidgets.QAction(MainWindow)
        self.Exit.setObjectName("Exit")
        self.exportasinitial = QtWidgets.QAction(MainWindow)
        self.exportasinitial.setObjectName("exportasinitial")
        self.exportasfinal = QtWidgets.QAction(MainWindow)
        self.exportasfinal.setObjectName("exportasfinal")
        self.clearinitial = QtWidgets.QAction(MainWindow)
        self.clearinitial.setObjectName("clearinitial")
        self.clearinitial.setEnabled(False)
        self.undoinitial = QtWidgets.QAction(MainWindow)
        self.undoinitial.setObjectName("undoinitial")
        self.redoinitial = QtWidgets.QAction(MainWindow)
        self.redoinitial.setObjectName("redoinitial")
        self.clearfinal = QtWidgets.QAction(MainWindow)
        self.clearfinal.setObjectName("clearfinal")
        self.clearfinal.setEnabled(False)
        self.undofinal = QtWidgets.QAction(MainWindow)
        self.undofinal.setObjectName("undofinal")
        self.redofinal = QtWidgets.QAction(MainWindow)
        self.redofinal.setObjectName("redofinal")
        self.K_Means = QtWidgets.QAction(MainWindow)
        self.K_Means.setEnabled(False)
        self.K_Means.setObjectName("K_Means")
        self.Affinity_Propagation = QtWidgets.QAction(MainWindow)
        self.Affinity_Propagation.setEnabled(False)
        self.Affinity_Propagation.setObjectName("Affinity_Propagation")
        self.Mean_Shift = QtWidgets.QAction(MainWindow)
        self.Mean_Shift.setEnabled(False)
        self.Mean_Shift.setObjectName("Mean_Shift")
        self.Spectral_Clustering = QtWidgets.QAction(MainWindow)
        self.Spectral_Clustering.setEnabled(False)
        self.Spectral_Clustering.setObjectName("Spectral_Clustering")
        self.Hierarchical_Clustering = QtWidgets.QAction(MainWindow)
        self.Hierarchical_Clustering.setEnabled(False)
        self.Hierarchical_Clustering.setObjectName("Hierarchical_Clustering")
        self.DBSCAN = QtWidgets.QAction(MainWindow)
        self.DBSCAN.setEnabled(False)
        self.DBSCAN.setObjectName("DBSCAN")
        self.Hill_Climbing = QtWidgets.QAction(MainWindow)
        self.Hill_Climbing.setObjectName("Hill_Climbing")
        self.Simulated_Anneling = QtWidgets.QAction(MainWindow)
        self.Simulated_Anneling.setObjectName("Simulated_Anneling")
        self.menuExport_As.addAction(self.exportasinitial)
        self.menuExport_As.addAction(self.exportasfinal)
        self.menuFile.addAction(self.Open_Data)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.saveinitialsolution)
        self.menuFile.addAction(self.savefinalsolution)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuExport_As.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.Exit)
        self.menuClear.addAction(self.clearinitial)
        self.menuClear.addAction(self.clearfinal)
        self.menuUndo.addAction(self.undoinitial)
        self.menuUndo.addAction(self.undofinal)
        self.menuRedo.addAction(self.redoinitial)
        self.menuRedo.addAction(self.redofinal)
        self.menuEdit.addAction(self.menuClear.menuAction())
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.menuUndo.menuAction())
        self.menuEdit.addAction(self.menuRedo.menuAction())
        self.menuClustering.addAction(self.K_Means)
        self.menuClustering.addAction(self.Affinity_Propagation)
        self.menuClustering.addAction(self.Mean_Shift)
        self.menuClustering.addAction(self.Spectral_Clustering)
        self.menuClustering.addAction(self.Hierarchical_Clustering)
        self.menuClustering.addAction(self.DBSCAN)
        self.menuHeuristics.addAction(self.Hill_Climbing)
        self.menuHeuristics.addAction(self.Simulated_Anneling)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuClustering.menuAction())
        self.menubar.addAction(self.menuHeuristics.menuAction())
        
        ret.retranslateUi(self, MainWindow)
        # self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
        self.Hill_Climbing.setEnabled(False)
        self.Simulated_Anneling.setEnabled(False)
        self.kmeanb.setText("K-\nMeans")
        self.affinitypb.setText("Affinity\nPropag.")
        self.meanshiftb.setText("Mean\nshift")
        self.spectralcb.setText("Spectral\nClusterin")
        self.hierarchicalcb.setText("Hierarc.\nClusterin")
        self.dbscanb.setText("DensityB\nScan")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/hillci2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hillclimbingb.setIcon(icon)
        self.hillclimbingb.setIconSize(QtCore.QSize(50, 25))
        icon2= QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/simi.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.simulatedannealingb.setIcon(icon2)
        self.simulatedannealingb.setIconSize(QtCore.QSize(50, 25))
        icon3=QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/undo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.undoinitialb.setIcon(icon3)
        self.undoinitialb.setIconSize(QtCore.QSize(40, 25))
        self.undofinalb.setIcon(icon3)
        self.undofinalb.setIconSize(QtCore.QSize(40, 25))
        self.openfileb.setStyleSheet("QPushButton::hover""{""background-color : lightgreen;""}")
        self.clearinitialb.setStyleSheet("QPushButton::hover""{""background-color : lightgreen;""}")
        self.clearfinalb.setStyleSheet("QPushButton::hover""{""background-color : lightgreen;""}")
        self.exportasinitialb.setStyleSheet("QPushButton::hover""{""background-color : lightgreen;""}")
        self.exportasfinalb.setStyleSheet("QPushButton::hover""{""background-color : lightgreen;""}")
        self.savefinalb.setStyleSheet("QPushButton::hover""{""background-color : lightgreen;""}")
        self.redoinitialb.setStyleSheet("QPushButton::hover""{""background-color : lightgreen;""}")
        self.redofinalb.setStyleSheet("QPushButton::hover""{""background-color : lightgreen;""}")
        self.undofinalb.setStyleSheet("QPushButton::hover""{""background-color : lightgreen;""}")
        self.saveinitialb.setStyleSheet("QPushButton::hover""{""background-color : lightgreen;""}")
        self.simulatedannealingb.setStyleSheet("QPushButton::hover""{""background-color : pink;""}")
        self.spectralcb.setStyleSheet("QPushButton::hover""{""background-color : pink;""}")
        self.meanshiftb.setStyleSheet("QPushButton::hover""{""background-color : pink;""}")
        self.hierarchicalcb.setStyleSheet("QPushButton::hover""{""background-color : pink;""}")
        self.affinitypb.setStyleSheet("QPushButton::hover""{""background-color : pink;""}")
        self.kmeanb.setStyleSheet("QPushButton::hover""{""background-color : pink;""}")
        self.dbscanb.setStyleSheet("QPushButton::hover""{""background-color : pink;""}")
        self.undoinitialb.setStyleSheet("QPushButton::hover""{""background-color : pink;""}")
        redo=QtGui.QIcon()
        redo.addPixmap(QtGui.QPixmap("icon/redo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.redoinitialb.setIcon(redo)
        self.redoinitialb.setIconSize(QtCore.QSize(40, 25))
        self.redofinalb.setIcon(redo)
        self.redofinalb.setIconSize(QtCore.QSize(40, 25))
        save=QtGui.QIcon()
        save.addPixmap(QtGui.QPixmap("icon/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.savefinalb.setIcon(save)
        self.savefinalb.setIconSize(QtCore.QSize(40, 25))
        self.saveinitialb.setIcon(save)
        self.saveinitialb.setIconSize(QtCore.QSize(40, 25))
        export=QtGui.QIcon()
        export.addPixmap(QtGui.QPixmap("icon/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exportasfinalb.setIcon(export)
        self.exportasfinalb.setIconSize(QtCore.QSize(40, 25))
        self.exportasinitialb.setIcon(export)
        self.exportasinitialb.setIconSize(QtCore.QSize(40, 25))
        clear=QtGui.QIcon()
        clear.addPixmap(QtGui.QPixmap("icon/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clearfinalb.setIcon(clear)
        self.clearfinalb.setIconSize(QtCore.QSize(40, 25))
        self.clearinitialb.setIcon(clear)
        self.clearinitialb.setIconSize(QtCore.QSize(40, 25))
        openf=QtGui.QIcon()
        openf.addPixmap(QtGui.QPixmap("icon/newfile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openfileb.setIcon(openf)
        self.openfileb.setIconSize(QtCore.QSize(40, 25))
        
    
        

    def ayni(self,n,uniql):
        """!
        @param n is the name of the picture that gonna be saved
        @param uniql is the center number for the title
        """
        
        plt.title('Estimated number of clusters: % d' % len(uniql))
        plt.savefig(n)  
        ##figure burada kaydediliyor
        plt.close()     
        ##ekstradan plota ihtiac duymuyruz
        self.labelpixmap(n)
        ##pixmap halinde basılıyor
        self.clusterenable(True)    

        

    def closeevent(self):
        """! Closing the executed system.
        If close button pressed, ask the user to really want to exit.
        If you click save it will save inputA
        """

        ret = QMessageBox.question(MainWindow, 'Quit form', " You really want to quit?", QMessageBox.Yes | QMessageBox.Cancel |QMessageBox.Save, QMessageBox.Cancel)
        if ret == QMessageBox.Yes:
        
            MainWindow.close()
        elif ret==QMessageBox.Cancel:
            pass
        elif ret==QMessageBox.Save:
            self.saveinit()  
    
    
        
    def max(self,center,xinnoktalari):
        """!
        @param center is the center cluster
        @param xinnoktalari aynı grubun noktaları
        """
        B = np.reshape(center, (-1, 2))
        distance=pairwise_distances(B,self.X)
        D =pairwise_distances(B,self.X[xinnoktalari]) #gelen center noktalarından center a olan uzaklılar
        sd=np.max(D)
        # print(D,"D")
        asd=np.where(distance==sd)
        i=sum(asd)
        # print(str(asd),"konum",i)
        return i
        
        
    def bos(self):
        """!
        ## this function just clear the labels
        """
        self.labelinput.clear()
        self.hubstext.setText("")
        self.nodextext.setText("")
        self.resulttext.setText("")
        self.label_6.setText("")

        
   

    
        
    def farthandpair(self,nc,labels):
        """!
        @param nc is the number of clusters
        @param labels is the number of labels
        @param  self.center is the center list to be appended
        @param sdf double pairs
        @param emp_lis
        """
        text=''
        x=''
        m=[]
        fhub=[]
        centers=''
        
        for i in range (nc-1,-1,-1):

            y=(self.ClusterIndicesNumpy(i,labels))
            # print(y,"y")#ayrı clusterler, ayrı gruplananlar belirleniyor
            ss = np.average(self.X[y], axis=0) #https://blog.finxter.com/numpy-average-along-axis/ #merkezleri bul
            #aynı gruplannaların ortalaası alınarak merkezleri belirleniyor.
            # print("Center",-i+nc-1,"is: ",ss)
            centers=centers+"Center"+str(-i+nc-1)+"->>"+str(ss)+"\t"
            self.center.append(ss)
            gelen=self.max(ss,y)
            
            
            gfarhesthub=self.farhesthub(ss,gelen,nc)    #maksimum uzak noktaların merkeze olan uzaklıkları
            # print(gfarhesthub,"gasdf")
            fhub.append(gfarhesthub)
            text=str(gelen)+text
            z='Cluster'+str(i)+"--->"
            x=z+' '+str(y)+"\n"+str(x)
        
        # print("farhesthubs:",fhub)
        centers=centers+"\n"+"Merkezlerine en uzak olanların uzaklığı:"+str(fhub)
        
        
        
        self.nodextext.setText(str(x))
        m = str(text)[1:-1]
        z = m.replace('[', '', len(self.X)) 
        y = z.replace(']', ' ', len(self.X))    #arrayı bozma işlemi
        
        new_str = y
        emp_lis = []
        for z in new_str.split():
            if z.isdigit():
               emp_lis.append(int(z))
        
        # print("Find number in string:",emp_lis)
        sdf=list(itertools.combinations((emp_lis), 2)) 

        # self.pairyolla(emp_lis)
        self.emp_lis=emp_lis
        
        return sdf,emp_lis,centers
    
    def farhesthub(self,center,maxindex,length):
        """!
        @param center ss center cluster
        @param maxindex is points in the same labels
        @param length is the number of clusters
        
        """
        point=self.X[maxindex]
        px=point[0][0]
        py=point[0][1]
        cx=center[0]
        cy=center[1]
                
        return (math.sqrt((px-cx)**2+(py-cy)**2))


        
    
    def objective_function(self):
        """! Function to be found objective valus
        objective function. and pair objects
        @param pair_obj is the pair objects
        """
        pair_obj=[]
        
        for i in range (len(self.pairs)):
                
            pair_obj.append(self.emp_lis[0]
                                +0.75*(abs(self.emp_lis[0]-self.emp_lis[1]))
                                        +self.emp_lis[1])
            
        self.objective_func=pair_obj[np.argmax(pair_obj)]

            
        return(self.objective_func)
            
            
 
        
        
    def dbscacn(self):

        self.bos()
        X=self.X
        

        db = DBSCAN(eps=0.5).fit(X)
        core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
        core_samples_mask[db.core_sample_indices_] = True
        labels = db.labels_
        print(labels)
        
        
        
        name="kmean.png"
        plt.savefig(name)
        plt.close()
        self.labelpixmap(name)
        self.clusterenable(True)
        
        
        

  

  
    def ClusterIndicesNumpy(self,clustNum, labels_array): #numpy 
        """!
        @return  The indice, where the exact node
        """
        return np.where(labels_array == clustNum)[0]
        
        

    
        
        
    def clearinit(self,check):
        self.bos()
        self.labelinput.clear()
        self.clearfin(False)
        self.enabling(False)
        self.clusterenable(False)
        
    def clearfin(self,check):
        #clear commands


        self.labeloutput.clear()
        self.clearfinal.setEnabled(check)
        self.clearfinalb.setEnabled(check)

        

        

    def enabling(self,check):     #enabling variables after loading a picture fron open source
        self.K_Means.setEnabled(check)
        self.Affinity_Propagation.setEnabled(check)
        self.Mean_Shift.setEnabled(check)
        self.Spectral_Clustering.setEnabled(check)
        self.Hierarchical_Clustering.setEnabled(check)
        self.DBSCAN.setEnabled(check)
        self.kmeanb.setEnabled(check)
        self.meanshiftb.setEnabled(check)
        self.spectralcb.setEnabled(check)
        self.hierarchicalcb.setEnabled(check)
        self.dbscanb.setEnabled(check)
        self.affinitypb.setEnabled(check)
        self.menuClear.setEnabled(check)
        self.clearinitial.setEnabled(check)
        self.clearinitialb.setEnabled(check)


    def clusterenable(self,check):
        self.saveinitialsolution.setEnabled(check)
        self.saveinitialb.setEnabled(check)
        self.exportasinitialb.setEnabled(check)
        self.exportasinitial.setEnabled(check)
        self.redoinitial.setEnabled(check)
        self.redoinitialb.setEnabled(check)
        self.undoinitial.setEnabled(check)
        self.undoinitialb.setEnabled(check)
        
        

    def heuristicenable(self,check):
        self.savefinalb.setEnabled(check)
        self.savefinalsolution.setEnabled(check)
        self.exportasfinal.setEnabled(check)
        self.exportasfinalb.setEnabled(check)
        
        
        
        
        
    def hillc(self):
        self.heuristicenable(True)
        
    def simul(self):
        self.heuristicenable(True)
        
    
    
    def exportis(self):
        """! Exports the input pixel.
        @param self.file   dosyayı ekstra uzantısıyla alıyor
        @param self.filesave   dosyanın tam olarak acılacak konumunu elde ettiriyor
        @param image   labeldaki pixmapı image e çeviriyor

        """

        # self.option=QFileDialog.Options()    
        self.file=QFileDialog.getSaveFileName(self.centralwidget,"Export As..","","jpg file \n *.jpg")
        self.filesave = self.file[0]
        image=Image.fromqimage(self.labelinput.pixmap())
        image.save(self.filesave)
        
        
    def saveinit(self):
        self.file=QFileDialog.getSaveFileName(filter="txt files (*.txt)")[0]
        np.savetxt(self.file,self.X)
        
        
        
        
   
    def exportfs(self):
        self.option=QFileDialog.Options()    
        self.file=QFileDialog.getSaveFileName(self.centralwidget,"Export As..","","jpg file (\n *.jpg",options=self.option)
        self.filesave = self.file[0]
        image=Image.fromqimage(self.labeloutput.pixmap())
        image.save(self.filesave)
    
    
    
    
    
    def openfile(self):
        self.filename = QFileDialog.getOpenFileName(filter="txt files (*.txt)")
        self.path = self.filename[0]
        if self.path:
            f = open(self.path,"r")
            with f:
                self.textfile = f.read()
                self.enabling(True)
                self.X=np.loadtxt(self.path)
        plt.scatter(self.X[:,0], self.X[:,1],c='black', picker=True)
        for i in range(len(self.X)):
            plt.text(self.X[i,0],self.X[i,1],str(i))

        name="emp.png"
        plt.savefig(name)
        plt.close()
        self.labelpixmap(name)

        
    
  
        
        
    def labelpixmap(self,n):
        self.ss=QtGui.QPixmap(n) 
        # self.ss=self.ss.scaled(400,400,Qt.KeepAspectRatio,Qt.SmoothTransformation)
        self.labelinput.setPixmap(self.ss)
        os.remove(n)
        










        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())