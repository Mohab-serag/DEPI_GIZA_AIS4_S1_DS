from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys
import time
import psycopg2


class Main(QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi("std.ui", self)
    
    def InitUI(self):
        self.setWindowTitle("Student system")
        print("hello")
    
    
    def handle_db_conn(self):
        self.db = psycopg2.connect(
            host="localhost",
            database="std_mng",
            user="postgres",
            password="Mohab_@123"
        )

        self.curr = self.db.cursor()
        print("connection is done!")
  

    def handle_btn(self):
        self.std_add_btn.clicked.connect(self.std_add_btn)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())