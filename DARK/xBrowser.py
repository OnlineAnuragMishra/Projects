#!/usr/bin/env python
# coding: utf-8

import sys
import requests
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QFrame, QLineEdit, QHBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView

class BrowserApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SkyNav Privacy Browser")
        self.setGeometry(100, 100, 1280, 720)  # Adjust window size

        # Set the application icon
        self.setWindowIcon(QIcon("C:/Project DARK/ico/icons8-internet-100.png"))

        layout = QVBoxLayout()

        # Set the background image using a QLabel
        background_image = QPixmap("C:/Project DARK/Img/bg/ui_br_bg.jpg")
        background_label = QLabel(self)
        background_label.setPixmap(background_image)
        background_label.setGeometry(0, 0, 1280, 720)  # Adjust to the window size
        background_label.lower()

        # Title and Privacy labels with custom fonts
        title_layout = QHBoxLayout()
        title_label = QLabel("SkyNav Privacy Browser")
        title_font = title_label.font()
        title_font.setFamily("Pulpen Snowman")
        title_font.setPointSize(28)
        title_label.setFont(title_font)
        title_label.setStyleSheet("color: white;")
        title_layout.addWidget(title_label)

        layout.addLayout(title_layout)

        # Navigation buttons
        navigation_frame = QFrame()
        navigation_layout = QHBoxLayout()

        back_button = QPushButton("←")
        navigation_layout.addWidget(back_button)

        forward_button = QPushButton("→")
        navigation_layout.addWidget(forward_button)

        home_button = QPushButton("Home")
        navigation_layout.addWidget(home_button)

        refresh_button = QPushButton("Refresh")
        navigation_layout.addWidget(refresh_button)

        navigation_frame.setLayout(navigation_layout)
        layout.addWidget(navigation_frame)

        # Additional buttons
        buttons_layout = QHBoxLayout()

        news_button = QPushButton("News")
        buttons_layout.addWidget(news_button)

        email_button = QPushButton("Email")
        buttons_layout.addWidget(email_button)

        weather_button = QPushButton("Weather")
        buttons_layout.addWidget(weather_button)

        imdb_button = QPushButton("IMDb")
        buttons_layout.addWidget(imdb_button)

        facebook_button = QPushButton("Facebook")
        buttons_layout.addWidget(facebook_button)

        layout.addLayout(buttons_layout)

        # Search bar
        self.search_bar = QLineEdit()
        layout.addWidget(self.search_bar)

        # Location label
        self.location_label = QLabel("Loading location...")
        self.location_label.setStyleSheet("color: white;")
        layout.addWidget(self.location_label)

        # Web rendering widget
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.load_home()  # Load the home page on startup
        self.update_location()  # Update the location label

        # Connect buttons to their functions
        back_button.clicked.connect(self.web_view.back)
        forward_button.clicked.connect(self.web_view.forward)
        home_button.clicked.connect(self.load_home)
        refresh_button.clicked.connect(self.web_view.reload)

        # Connect additional buttons to their functions
        news_button.clicked.connect(self.open_news)
        email_button.clicked.connect(self.open_email)
        weather_button.clicked.connect(self.open_weather)
        imdb_button.clicked.connect(self.open_imdb)
        facebook_button.clicked.connect(self.open_facebook)

    def get_user_location(self):
        try:
            response = requests.get("http://ipinfo.io")
            data = response.json()
            location = f"{data['city']}, {data['region']}, {data['country']}"
            return location
        except Exception as e:
            print("Error retrieving location:", e)
            return "Location Not Available"

    def update_location(self):
        user_location = self.get_user_location()
        self.location_label.setText(user_location)

    def load_home(self):
        self.web_view.setUrl(QUrl("https://duckduckgo.com"))

    def open_news(self):
        self.web_view.setUrl(QUrl("https://news.sky.com/"))

    def open_email(self):
        self.web_view.setUrl(QUrl("https://mail.google.com/"))

    def open_weather(self):
        self.web_view.setUrl(QUrl("https://www.weather.com/"))

    def open_imdb(self):
        self.web_view.setUrl(QUrl("https://www.imdb.com/"))

    def open_facebook(self):
        self.web_view.setUrl(QUrl("https://www.facebook.com/"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser_app = BrowserApp()
    browser_app.show()
    sys.exit(app.exec_())
