import sys
from PyQt5 import QtWidgets
from views.frmGiris import frmGiris
from views.frmArkaplan import frmArkaplan


def app():
    print("Program Calıstırıldı...")
    app = QtWidgets.QApplication(sys.argv)
    win_bg = frmArkaplan()
    win = frmGiris()
    win_bg.show()
    win.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    app()