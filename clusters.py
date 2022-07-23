from PyQt5 import QtWidgets
from kmean import Ui_SecondWindow
from aff2 import Ui_affWindow
from spectralwin import Ui_spectralwindow
from hierar import Ui_hierarc
from msp import Ui_meanshift





class callfunctions:
    """! The All Clusters' class.
    
        
    """
    def __init__(self):
        pass
    
    def meanshiftw(self):
        """! The Mean-shift  function.
        Mean shift window opens
        (As a second window)
        
        """
        self.window=QtWidgets.QMainWindow()
        self.means= Ui_meanshift()
        self.means.setupUi(self.window)
        self.window.show()
        self.means.msbut.clicked.connect(self.meanstrans)
        """
        @param self.means.msbut is the accept button of aff.c
        """

    def affWindow(self):
        """! The Affinity Propagation function.
        Affinity Propagation window opens
        (As a second window)
        
        """
        self.window=QtWidgets.QMainWindow()
        self.aff= Ui_affWindow()
        self.aff.setupUi(self.window)
        self.window.show()
        self.aff.affb.clicked.connect(self.afftransfer)
        """
        @param self.aff.affb is the accept button of aff.c
        """
    
    def spectralw(self):
        """! The Spectral-Clustering  function.
        Spectral Clustering window opens
        (As a second window)
        
        """
        self.window=QtWidgets.QMainWindow()
        self.sp=Ui_spectralwindow()
        self.sp.setupUi(self.window)
        self.window.show()
        self.sp.spectralwinb.clicked.connect(self.spectrans)   
        """
        @param self.sp.spectralwinb is the accept button of spectral.c
        """
    
    def hierarW(self):
        """! The Hierarchical-Clustering  function.
        Hierarchical Clustering window opens
        (As a second window)
        
        """
        self.window=QtWidgets.QMainWindow()
        self.hs=Ui_hierarc()
        self.hs.setupUi(self.window)
        self.window.show()
        self.hs.hierbut.clicked.connect(self.hiertrans)
        """
        @param self.hs.hierbut is the accept button of H.s
        """
    
    
    def openWindow(self):
        """! The K-Means  function.
        K shift Means opens
        (As a second window)
        
        """
        self.window=QtWidgets.QMainWindow()
        self.ui= Ui_SecondWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.accept.clicked.connect(self.transfer)
        """
        @param self.ui.accept is the accept button of K-means
        """
 