from mainwindows import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog, QMainWindow
import pandas as pd
import re


class FileDialog(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(FileDialog, self).__init__()
        self.setupUi(self)
        self.btn_browse.clicked.connect(self.browse__open_file)  # browse按钮与browse_file建立联系

    def browse__open_file(self):
        file = QFileDialog(self)
        file_name, file_type = file.getOpenFileName(self, "选取文件",
                                                    "./",
                                                    "Python Files (*.py);;"
                                                    "Json Files (*.json);;"
                                                    "Text Files (*.txt);;"
                                                    "Excel Files (*.xls , *.xlsx);;"
                                                    "Csv Files (*.csv );;"
                                                    "All Files (*)")
        if file_type.strip():  # 判断用户取消操作
            self.file_name_text.setPlainText(file_name)  # 写文件名
            '''在下面进行文件读写及判断'''
            try:
                if re.findall('.xls|.xlsx', file_name):
                    self.file_text.setPlainText(str(pd.read_excel(file_name, encoding='utf8')))
                elif re.findall('.csv', file_name):

                    self.file_text.setPlainText(str(pd.read_csv(file_name), encoding='utf8'))
                else:
                    with open(file_name, 'r', encoding='utf8') as f:
                        self.file_text.setPlainText(f.read())
            except Exception as e:
                self.file_text.setPlainText(str(e))
