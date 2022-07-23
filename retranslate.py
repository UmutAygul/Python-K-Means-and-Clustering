from PyQt5 import QtCore





class ret:
    def __init__(self):
        pass
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OOP_Lab Project"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Initial Solution"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Final Solution"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Heuristics"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Clustering"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Initial Solution"))
        self.groupBox_12.setTitle(_translate("MainWindow", "Final Solution"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Manual Solution"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Hubs"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Nodes"))
        self.runbutton.setText(_translate("MainWindow", "RUN"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Results"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Info Panel"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExport_As.setTitle(_translate("MainWindow", "Export As"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuClear.setTitle(_translate("MainWindow", "Clear"))
        self.menuUndo.setTitle(_translate("MainWindow", "Undo"))
        self.menuRedo.setTitle(_translate("MainWindow", "Redo"))
        self.menuClustering.setTitle(_translate("MainWindow", "Clustering"))
        self.menuHeuristics.setTitle(_translate("MainWindow", "Heuristics"))
        self.Open_Data.setText(_translate("MainWindow", "Open Data"))
        self.saveinitialsolution.setText(_translate("MainWindow", "Save Initial Solution"))
        self.savefinalsolution.setText(_translate("MainWindow", "Save Final Solution"))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.exportasinitial.setText(_translate("MainWindow", "Initial Solution"))
        self.exportasfinal.setText(_translate("MainWindow", "Final Solution"))
        self.clearinitial.setText(_translate("MainWindow", "Initial Solution"))
        self.undoinitial.setText(_translate("MainWindow", "Initial Solution"))
        self.redoinitial.setText(_translate("MainWindow", "Initial Solution"))
        self.clearfinal.setText(_translate("MainWindow", "Final Solution"))
        self.undofinal.setText(_translate("MainWindow", "Final Solution"))
        self.redofinal.setText(_translate("MainWindow", "Final Solution"))
        self.K_Means.setText(_translate("MainWindow", "K-Means"))
        self.Affinity_Propagation.setText(_translate("MainWindow", "Affinity Propagation"))
        self.Mean_Shift.setText(_translate("MainWindow", "Mean-Shift"))
        self.Spectral_Clustering.setText(_translate("MainWindow", "Spectral Clustering"))
        self.Hierarchical_Clustering.setText(_translate("MainWindow", "Hierarchical Clustering"))
        self.DBSCAN.setText(_translate("MainWindow", "DBSCAN"))
        self.Hill_Climbing.setText(_translate("MainWindow", "Hill Climbing"))
        self.Simulated_Anneling.setText(_translate("MainWindow", "Simulated Anneling"))

        self.savefinalb.setToolTip(_translate("MainWindow", 'Save Final Solution'))
        self.openfileb.setToolTip(_translate("MainWindow", 'Open File'))
        self.hillclimbingb.setToolTip(_translate("MainWindow", 'Click for "Hill Climbing"'))
        self.simulatedannealingb.setToolTip(_translate("MainWindow", 'Click for "Simulated Annealing"'))
        self.kmeanb.setToolTip(_translate("MainWindow", 'Click for "K-Means"'))
        self.affinitypb.setToolTip(_translate("MainWindow", 'Click for "Affinity Propagation"'))
        self.meanshiftb.setToolTip(_translate("MainWindow", 'Click for "Mean-Shift"'))
        self.spectralcb.setToolTip(_translate("MainWindow", 'Click for "Spectral Clustering"'))
        self.hierarchicalcb.setToolTip(_translate("MainWindow", 'Click for "Hierarchical_Clustering"'))
        self.dbscanb.setToolTip(_translate("MainWindow", 'Click for "DBSCAN"'))
        self.saveinitialb.setToolTip(_translate("MainWindow", "Click to save"))
        self.exportasinitialb.setToolTip(_translate("MainWindow", "Export As..."))
        self.clearinitialb.setToolTip(_translate("MainWindow", "Clear"))
        self.undoinitialb.setToolTip(_translate("MainWindow", "Undo"))
        self.redoinitialb.setToolTip(_translate("MainWindow", "Redo"))
        self.exportasfinalb.setToolTip(_translate("MainWindow", "Export As..."))
        self.clearfinalb.setToolTip(_translate("MainWindow", "Clear"))
        self.undofinalb.setToolTip(_translate("MainWindow", "Undo"))
        self.redofinalb.setToolTip(_translate("MainWindow", "Redo"))


        
        self.openfileb.setShortcut(_translate("MainWindow", "F5"))
        
        self.openfileb.clicked.connect(self.openfile)
        
        # self.kmeanb.clicked.connect(self.kmean)
        
        self.saveinitialb.clicked.connect(self.saveinit)
        self.saveinitialsolution.triggered.connect(self.saveinit)
        
        self.clearinitial.triggered.connect(self.clearinit)
        self.clearinitialb.clicked.connect(self.clearinit)
        
        self.kmeanb.clicked.connect(lambda: self.clustering("km"))
        self.K_Means.triggered.connect(lambda: self.clustering("km"))
        
        
        self.affinitypb.clicked.connect(lambda: self.clustering("aff"))
        self.Affinity_Propagation.triggered.connect(lambda: self.clustering("aff"))
        
        self.Mean_Shift.triggered.connect(lambda: self.clustering("ms"))
        self.meanshiftb.clicked.connect(lambda: self.clustering("ms"))
        
        # self.dbscanb.clicked.connect(self.dbscacn)
        # self.DBSCAN.triggered.connect(self.dbscacn)
        


        self.hierarchicalcb.clicked.connect(lambda: self.clustering("hw"))
        self.Hierarchical_Clustering.triggered.connect(lambda: self.clustering("hw"))
        
        
    
        self.Exit.triggered.connect(self.closeevent)
        
        self.spectralcb.clicked.connect(lambda: self.clustering("s"))
        self.Spectral_Clustering.triggered.connect(lambda: self.clustering("s"))
        
        self.exportasinitial.triggered.connect(self.exportis)
        self.exportasinitialb.clicked.connect(self.exportis)
        
        self.savefinalb.clicked.connect(self.exportfs)
        self.savefinalsolution.triggered.connect(self.exportfs)
        
        
        
        