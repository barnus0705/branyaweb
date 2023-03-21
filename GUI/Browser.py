from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from Functions.Search import *

import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)

        self.window = QWidget()
        self.window.setWindowTitle("BranyaWeb")

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.urlbar = QTextEdit()
        self.urlbar.setMaximumHeight(30)

        self.go_button = QPushButton("Enter")
        self.go_button.setMinimumHeight(30)

        self.go_button.clicked.connect(lambda: self.searchByURL(self.urlbar.toPlainText()))

        self.forwardbtn  = QPushButton("->")
        self.forwardbtn.setMinimumHeight(30)


        self.backwardbtn = QPushButton("<-")
        self.backwardbtn.setMinimumHeight(30)


        self.horizontal.addWidget(self.backwardbtn)
        self.horizontal.addWidget(self.forwardbtn)
        self.horizontal.addWidget(self.urlbar)
        self.horizontal.addWidget(self.go_button)

        self.browser = QWebEngineView()
        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://google.com"))

        self.window.setLayout(self.layout)
        self.window.show()

        self.browser.urlChanged.connect(lambda url: self.urlbar.setText(url.toString()))

        self.backwardbtn.clicked.connect(self.browser.back)
        self.forwardbtn.clicked.connect(self.browser.forward)

    def searchByURL(self, url):
        if "." in url:
            if not url.startswith("https") and not url.startswith("http"):
                url = "https://"+url
                self.urlbar.setText(url)
                self.browser.setUrl(QUrl(url))
            else:
                self.browser.setUrl(QUrl(url))
        else:
            self.browser.setUrl(QUrl("https://www.google.com/search?q="+url))









app = QApplication([])
window = MainWindow()
app.exec_()


