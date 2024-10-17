from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox, QRadioButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys
import json

class Register(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Register")
        self.setFixedSize(1000, 700)
        self.dark_mode = False

        self.txt = QLabel(""" Create Your GOOGLE Account
                          
     Enter  your  first  name
                          
     Enter  your  last  name""", self)
        self.font(self.txt, 120, 20)


        self.first_name_input = QLineEdit(self)
        self.first_name_input.setPlaceholderText("First name...")
        self.font(self.first_name_input, 220, 80)
        self.first_name_input.setFixedSize(450, 55)

        self.last_name_input = QLineEdit(self)
        self.last_name_input.setPlaceholderText("Last name...")
        self.font(self.last_name_input, 220, 196)
        self.last_name_input.setFixedSize(450, 55)

        self.month_combo = QComboBox(self)
        self.month_combo.addItems(["Month", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"])
        self.font(self.month_combo, 130, 320)

        self.day_input = QLineEdit(self)
        self.day_input.setPlaceholderText("Day")
        self.font(self.day_input, 443, 320)
        self.day_input.setFixedSize(130, 63)

        self.year_input = QLineEdit(self)
        self.year_input.setPlaceholderText("Year")
        self.font(self.year_input, 643, 320)
        self.year_input.setFixedSize(130, 63)

        self.gender_male = QRadioButton("Male", self)
        self.gender_female = QRadioButton("Female", self)
        self.gender_male.move(140, 440)
        self.gender_female.move(240, 440)

        self.font(self.gender_male, 220, 400)
        self.font(self.gender_female, 480, 400)

        self.gmail_text = QLabel("  Pick a Gmail address or create your own", self)
        self.gmail_text.setFont(QFont("Open Sans", 1))
        self.font(self.gmail_text, 45, 470)

        self.gmail_input = QLineEdit(self)
        self.gmail_input.setPlaceholderText("@gmail...")
        self.font(self.gmail_input, 120, 543)
        self.gmail_input.setFixedSize(364, 63)

        self.gmail_com_label = QLabel("@gmail.com", self)
        self.font(self.gmail_com_label, 489, 543)

        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("password...")
        self.font(self.password_input, 120, 615)
        self.password_input.setFixedSize(364, 63)

        self.submit_button = QPushButton("submit", self)
        self.font(self.submit_button, 640, 620)
        self.submit_button.setFixedWidth(364)
        self.submit_button.clicked.connect(self.register)

        self.mode_button = QPushButton("🌚", self)
        self.font(self.mode_button, 800, 20)
        self.mode_button.setFixedSize(200, 63)
        self.mode_button.clicked.connect(self.toggle_mode)

        self.setStyleSheet(self.light_mode_style())
        self.show()

    def font(self, obj, x, y):
        obj.setFont(QFont("Open Sans", 23))
        obj.move(x, y)

    def write_json(self, new_user):
        try:
            with open("users.json", "r") as file:
                users = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            users = []
        users.append(new_user)
        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)

    def register(self):
        firstname = self.first_name_input.text()
        lastname = self.last_name_input.text()
        gender = "Male" if self.gender_male.isChecked() else "Female"
        month = self.month_combo.currentText()
        day = self.day_input.text()
        year = self.year_input.text()
        email = self.gmail_input.text() + "@gmail.com"
        password = self.password_input.text()

        if not firstname:
            QMessageBox.warning(self, "Input Error", "First name is required.")
            return
        if not lastname:
            QMessageBox.warning(self, "Input Error", "Last name is required.")
            return
        if not day:
            QMessageBox.warning(self, "Input Error", "Day is required.")
            return
        if not year:
            QMessageBox.warning(self, "Input Error", "Year is required.")
            return
        if self.month_combo.currentIndex() == 0:
            QMessageBox.warning(self, "Input Error", "Please select a month.")
            return
        if not email:
            QMessageBox.warning(self, "Input Error", "Email is required.")
            return
        if not password:
            QMessageBox.warning(self, "Input Error", "Password is required.")
            return

        try:
            new_user = {
                "firstname": firstname,
                "lastname": lastname,
                "gender": gender,
                "month": month,
                "day": day,
                "year": year,
                "email": email,
                "password": password
            }
            self.write_json(new_user)
            QMessageBox.information(self, "Success", "Registration successful!")
        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def toggle_mode(self):
        self.dark_mode = not self.dark_mode
        if self.dark_mode:
            self.setStyleSheet(self.dark_mode_style())
            self.mode_button.setText("🌕")
        else:
            self.setStyleSheet(self.light_mode_style())
            self.mode_button.setText("🌚")

    def light_mode_style(self):
        return """
            QWidget {
                background-color: white;
                color: black;
            }
            QPushButton {
                background-color: white;  
                color: black;               
                border: 4px solid blue;  
                border-radius: 20px;      
            }
            QLabel {
                color: black;
                border: 4px solid blue;
                border-radius: 20px;
            }
            QLineEdit {
                background-color: white;
                color: black;
                border: 4px solid blue;
                border-radius: 20px;
            }
            QComboBox {
                background-color: white;
                color: black; 
                border: 4px solid blue;
                border-radius: 20px;
            }
            QRadioButton {
                color: black;
                border: 4px solid blue;
                border-radius: 20px;
            }
        """

    def dark_mode_style(self):
        return """
            QWidget {
                background-color: black;
                color: white;
            }
            QPushButton {
                background-color: black;  
                color: lightblue;               
                border: 4px solid blue;  
                border-radius: 20px;      
            }
            QLabel {
                color: lightblue;
                border: 4px solid blue;
                border-radius: 20px;
            }
            QLineEdit {
                background-color: black;
                color: lightblue;
                border: 4px solid blue;
                border-radius: 20px;
            }
            QComboBox {
                background-color: black;
                color: lightblue; 
                border: 4px solid blue;
                border-radius: 20px;
            }
            QRadioButton {
                color: lightblue;
            }
        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    application = Register()
    sys.exit(app.exec_())
