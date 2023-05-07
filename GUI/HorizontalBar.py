from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from Objects import *
import json


class HorizontalBar:
    def __init__(self, layout, browser):
        self.browser = browser

        self.horizontal = QHBoxLayout()
        self.urlBar = QLineEdit()
        self.urlBar.setMaximumHeight(30)

        self.go_button = QPushButton("Enter")
        self.go_button.setMinimumHeight(30)

        self.forwardbtn = QPushButton("->")
        self.forwardbtn.setMinimumHeight(20)

        self.backwardbtn = QPushButton("<-")
        self.backwardbtn.setMinimumHeight(20)

        self.homebtn = QPushButton("Home")
        self.homebtn.setMinimumHeight(20)

        self.historybtn = QPushButton("History")
        self.historybtn.setMinimumHeight(20)

        self.bookmarkbtn = QPushButton("Bookmark")
        self.bookmarkbtn.setMinimumHeight(20)

        self.refreshbtn = QPushButton("Refresh")
        self.refreshbtn.setMinimumHeight(20)

        self.horizontal.addWidget(self.historybtn)
        self.horizontal.addWidget(self.homebtn)
        self.horizontal.addWidget(self.bookmarkbtn)
        self.horizontal.addWidget(self.refreshbtn)
        self.horizontal.addWidget(self.backwardbtn)
        self.horizontal.addWidget(self.forwardbtn)
        self.horizontal.addWidget(self.urlBar)
        self.horizontal.addWidget(self.go_button)

        layout.addLayout(self.horizontal)

