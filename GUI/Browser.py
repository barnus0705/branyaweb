from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

from GUI.HorizontalBar import HorizontalBar
from GUI.Bookmarks import Bookmarks
from Objects import *
import json


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.window = QWidget()
        self.window.setWindowTitle("BranyaWeb")

        self.browser = QWebEngineView()

        self.layout = QVBoxLayout()
        self.horizontal_bar = HorizontalBar(self.layout, self.browser)
        self.bookmarks = Bookmarks(self)

        self.layout.addLayout(self.bookmarks.bookmark_bar)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://google.com"))

        self.window.setLayout(self.layout)
        self.window.show()

        self.browser.urlChanged.connect(lambda url: self.horizontal_bar.urlBar.setText(url.toString()))

        self.horizontal_bar.go_button.clicked.connect(lambda: self.search_by_url(self.horizontal_bar.urlBar.text()))
        self.horizontal_bar.urlBar.returnPressed.connect(lambda: self.search_by_url(self.horizontal_bar.urlBar.text()))
        self.horizontal_bar.bookmarkbtn.clicked.connect(lambda: self.bookmarks.bookmarks_save())
        self.horizontal_bar.backwardbtn.clicked.connect(self.browser.back)
        self.horizontal_bar.refreshbtn.clicked.connect(lambda: self.browser.reload())
        self.horizontal_bar.forwardbtn.clicked.connect(self.browser.forward)
        self.horizontal_bar.homebtn.clicked.connect(lambda: self.browser.setUrl(QUrl("http://google.com")))
        self.horizontal_bar.historybtn.clicked.connect(lambda: self.open_new_window())

    def search_by_url(self, url):
        if "." in url:
            if not url.startswith("https") and not url.startswith("http"):
                url = "https://" + url
                self.horizontal_bar.urlBar.setText(url)
                self.browser.setUrl(QUrl(url))
            else:
                self.browser.setUrl(QUrl(url))
        else:
            self.browser.setUrl(QUrl("https://www.google.com/search?q=" + url))

    def history_list(self):
        browser_history = self.browser.history().items()
        history_list = []
        for item in browser_history:
            url = item.url().toString()
            visited = item.lastVisited().toString()
            obj = Histroy(url, visited)
            history_list.append(obj)
        return history_list

    def open_new_window(self):
        dialog = QDialog(self)
        dialog.setWindowTitle('Browser History')
        dialog.setGeometry(200, 200, 400, 300)
        browser_history_list = QListWidget(self)

        for items in self.history_list():
            item = QListWidgetItem(f'{items.link} '+items.date, browser_history_list)
            item.setData(Qt.UserRole, QUrl(f'{items.link}'))

        browser_history_list.itemClicked.connect(self.ConnecToLink)

        layout = QVBoxLayout(dialog)
        layout.addWidget(browser_history_list)
        dialog.exec_()

    def ConnecToLink(self, item):

        url = item.data(Qt.UserRole)
        self.browser.setUrl(url)



app = QApplication([])
window = MainWindow()
app.exec_()
