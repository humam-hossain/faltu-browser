import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QLineEdit, QVBoxLayout, QWidget)
from PyQt5.QtWebEngineWidgets import QWebEngineView



class Browser(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon("icons/browser.png"))
        self.setWindowTitle("faltu browser")
        self.setGeometry(200, 50, 1000, 600)
        self.setStyleSheet(
            "QWidget {"
               "background-color: #fff;"
            "}"
        )

        # create the QWebEngineView
        self.view = QWebEngineView(self)
        self.view.load(QUrl("https://www.google.com"))

        # create the back, forward, and refresh buttons
        button_style = """QPushButton {
                background-color: #0d6efd;
                color: #fff;
                font-weight: 600;
                border-radius: 10px;
                border: 1px solid #0d6efd;
                padding: 5px 15px;
                margin-top: 10px;
                outline: 0px;
            }
            QPushButton:hover{
                background-color: #0b5ed7;
                border: 3px solid #9ac3fe;
            }
        """

        url_bar_style = """QLineEdit {
                border-radius: 8px;
                border: 1px solid #e0e4e7;
                padding: 5px 15px;
                margin-top: 10px;
            }

            QLineEdit:focus {
                border: 1px solid #d0e3ff;
            }

            QLineEdit::placeholder {
                color: #fff;
            }
        """

        self.back_button = QPushButton(self)
        self.back_button.setStyleSheet(button_style)
        self.back_button.setIcon(QIcon("icons/left.png"))

        self.forward_button = QPushButton(self)
        self.forward_button.setStyleSheet(button_style)
        self.forward_button.setIcon(QIcon("icons/right.png"))
        
        self.refresh_button = QPushButton(self)
        self.refresh_button.setStyleSheet(button_style)
        self.refresh_button.setIcon(QIcon("icons/reload.png"))
        

        # Connect the buttons to their respective slots
        self.back_button.clicked.connect(self.view.back)
        self.forward_button.clicked.connect(self.view.forward)
        self.refresh_button.clicked.connect(self.view.reload)

        # create the URL bar
        self.url_bar = QLineEdit(self)
        self.url_bar.setPlaceholderText("https://")
        self.url_bar.setStyleSheet(url_bar_style)

        self.url_bar.returnPressed.connect(self.navigate_to_url)

        # create the layout
        layout = QVBoxLayout()

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.back_button)
        button_layout.addWidget(self.forward_button)
        button_layout.addWidget(self.refresh_button)
        button_layout.addWidget(self.url_bar)

        layout.addLayout(button_layout)
        layout.addWidget(self.view)

        self.setLayout(layout)

    def navigate_to_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.view.setUrl(q)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = Browser()
    browser.show()
    sys.exit(app.exec_())