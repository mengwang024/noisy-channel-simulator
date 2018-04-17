import os

from PyQt4 import *
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QFileDialog, QStringListModel
import errno
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)





class Ui_Home(object):
    def setupUi(self, Dialog):
        self.openedlist = []
        Dialog.setObjectName(_fromUtf8("Dialog"))
        self.dialog = Dialog
        self.dialog.setWindowIcon(QtGui.QIcon('ico.png'))
        Dialog.resize(635, 342)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)




    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Wetspa_Urban", None))


def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def main():
    sys.setrecursionlimit(10 ** 6)

    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Home()
    ui.setupUi(Dialog)
    Dialog.show()
    (app.exec_())


if __name__ == "__main__":
    main()
