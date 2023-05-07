from json import JSONDecodeError

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import json


def bookmarks_load():
    with open("bookmark.json", "r") as infile:
        try:
            data = json.load(infile)
        except JSONDecodeError:
            return []
        return data


class Bookmarks:
    def __init__(self, main_window):
        self.bookmark_bar = QHBoxLayout()

        self.main_window = main_window
        self.bookmarks = bookmarks_load()

        for item in self.bookmarks:
            self.add_bookmark_to_bar(item)

    def bookmarks_save(self):
        url = self.main_window.browser.page().url().toString()
        for item in self.bookmarks:
            if item['url'] == url:
                return

        with open("bookmark.json", "w") as outfile:

            bookmark = {
                'title': self.main_window.browser.page().title(),
                'id': len(self.bookmarks),
                'url': url
            }

            self.bookmarks.append(bookmark)
            self.add_bookmark_to_bar(bookmark)
            obj = json.dumps(self.bookmarks, indent=2)
            outfile.write(obj)

    def add_bookmark_to_bar(self, item):
        bookmark_button = QPushButton(item['title'])
        bookmark_button.setMinimumHeight(20)
        bookmark_button.setMaximumWidth(400)
        bookmark_button.clicked.connect(lambda: self.main_window.search_by_url(item['url']))
        self.bookmark_bar.addWidget(bookmark_button)
