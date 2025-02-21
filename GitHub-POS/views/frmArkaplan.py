from forms.frmArkaPlanUi import Ui_frmArkaPlan
from PyQt5 import QtWidgets



class frmArkaplan(QtWidgets.QWidget):
    def __init__(self):
        super(frmArkaplan, self).__init__()
        self.ui = Ui_frmArkaPlan()
        self.ui.setupUi(self)
        self.showFullScreen()