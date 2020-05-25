from FileDialog import FileDialog
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = FileDialog()
    ui.show()
    sys.exit(app.exec_())
