import sys
import subprocess
import re
from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QApplication,
    QTabWidget, QCheckBox, QComboBox, QTextEdit, QSpinBox
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont, QColor, QPalette
from PyQt5.QtWidgets import QGraphicsDropShadowEffect

def update_config_file(file_path, updates):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.readlines()
    for i, line in enumerate(content):
        for key, value in updates.items():
            value_str = "True" if value is True else "False" if value is False else f"{value}" if isinstance(value, list) else f"'{value}'"
            if re.match(rf"^\s*{key}\s*=", line):
                content[i] = f"{key} = {value_str}\n"
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(content)

class BotRunnerThread(QThread):
    output_signal = pyqtSignal(str)
    error_signal = pyqtSignal(str)

    def run(self):
        args = [
            "C:/Users/ASUS/Desktop/Auto_job_applier_linkedIn/.venv/Scripts/python.exe",
            "runAiBot.py"
        ]
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd="C:/Users/ASUS/Desktop/Auto_job_applier_linkedIn")
        stdout, stderr = process.communicate()
        self.output_signal.emit(stdout.decode("utf-8", errors="replace") if stdout else "")
        self.error_signal.emit(stderr.decode("utf-8", errors="replace") if stderr else "")

class JobApplierClient(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(self.get_stylesheet())
        self.initUI()

    def get_stylesheet(self):
        return """
            QWidget {
                background-color: #FFFFFF;
                font-family: Arial;
                color: #333333;
            }
            QLabel {
                font-size: 13pt;
                color: #333333;
                padding: 6px;
            }
            QLineEdit, QComboBox, QSpinBox {
                font-size: 12pt;
                background-color: #F5F5F5;
                color: #333333;
                padding: 8px;
                border: 1px solid #DADADA;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #1E90FF;
                font-size: 12pt;
                padding: 10px 16px;
                color: #FFFFFF;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #1C86EE;
            }
            QTextEdit {
                background-color: #F5F5F5;
                border: 1px solid #DADADA;
                color: #333333;
                padding: 8px;
                border-radius: 5px;
            }
            QTabWidget::pane {
                border: 1px solid #DADADA;
                border-radius: 4px;
            }
            QTabBar::tab {
                font-size: 12pt;
                background: #E0E0E0;
                padding: 10px 20px;  /* Adjusted padding for better fit */
                margin: 1px;
                min-width: 150px;   /* Increased tab width */
            }
            QTabBar::tab:selected {
                background: #1E90FF;
                color: white;
            }
        """

    def initUI(self):
        self.tabs = QTabWidget()
        self.tabs.setTabPosition(QTabWidget.North)
        self.tabs.addTab(self.createLoginTab(), "Login Credentials")
        self.tabs.addTab(self.createPersonalInfoTab(), "Personal Information")
        self.tabs.addTab(self.createJobSearchTab(), "Job Search Settings")
        self.tabs.addTab(self.createJobApplicationTab(), "Job Application Filters")

        # Run Button
        self.run_button = QPushButton('Run Bot')
        self.run_button.clicked.connect(self.run_bot)
        self.run_button.setGraphicsEffect(self.add_shadow())

        # Logs
        self.logs = QTextEdit(self)
        self.logs.setReadOnly(True)

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tabs)
        main_layout.addWidget(self.run_button)
        main_layout.addWidget(self.logs)

        self.setLayout(main_layout)
        self.setWindowTitle('Auto Job Applier IDE')
        self.setGeometry(300, 100, 800, 600)
        self.show()

    def add_shadow(self):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setXOffset(0)
        shadow.setYOffset(0)
        shadow.setColor(QColor(0, 0, 0, 100))
        return shadow

    def createLoginTab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        self.username_input = QLineEdit("amir.lehmam@gmail.com")
        layout.addWidget(QLabel('LinkedIn Username'))
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit("Gdze_94400")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(QLabel('LinkedIn Password'))
        layout.addWidget(self.password_input)

        tab.setLayout(layout)
        return tab

    def createPersonalInfoTab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        self.first_name_input = QLineEdit("Amir")
        layout.addWidget(QLabel('First Name'))
        layout.addWidget(self.first_name_input)

        self.middle_name_input = QLineEdit()
        layout.addWidget(QLabel('Middle Name (Optional)'))
        layout.addWidget(self.middle_name_input)

        self.last_name_input = QLineEdit("Lehmam")
        layout.addWidget(QLabel('Last Name'))
        layout.addWidget(self.last_name_input)

        self.phone_number_input = QLineEdit("0787323996")
        layout.addWidget(QLabel('Phone Number'))
        layout.addWidget(self.phone_number_input)

        self.current_city_input = QLineEdit("Vitry-sur-Seine")
        layout.addWidget(QLabel('Current City'))
        layout.addWidget(self.current_city_input)

        self.linkedin_profile_input = QLineEdit("https://www.linkedin.com/in/amirlehmam/")
        layout.addWidget(QLabel('LinkedIn Profile URL'))
        layout.addWidget(self.linkedin_profile_input)

        self.website_input = QLineEdit("https://github.com/amirlehmam")
        layout.addWidget(QLabel('Website / Portfolio'))
        layout.addWidget(self.website_input)

        tab.setLayout(layout)
        return tab

    def createJobSearchTab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        self.search_terms_input = QLineEdit("Data")
        layout.addWidget(QLabel('Job Search Terms (comma-separated)'))
        layout.addWidget(self.search_terms_input)

        self.search_location_input = QLineEdit("London")
        layout.addWidget(QLabel('Search Location'))
        layout.addWidget(self.search_location_input)

        self.sort_by_combo = QComboBox()
        self.sort_by_combo.addItems(["Most recent", "Most relevant"])
        layout.addWidget(QLabel('Sort By'))
        layout.addWidget(self.sort_by_combo)

        self.date_posted_combo = QComboBox()
        self.date_posted_combo.addItems(["Any time", "Past month", "Past week", "Past 24 hours"])
        self.date_posted_combo.setCurrentText("Past week")
        layout.addWidget(QLabel('Date Posted'))
        layout.addWidget(self.date_posted_combo)

        tab.setLayout(layout)
        return tab

    def createJobApplicationTab(self):
        tab = QWidget()
        layout = QVBoxLayout()
        self.experience_level_combo = QComboBox()
        self.experience_level_combo.addItems(["Internship", "Entry level", "Associate", "Mid-Senior level", "Director", "Executive"])
        layout.addWidget(QLabel('Experience Level'))
        layout.addWidget(self.experience_level_combo)

        self.job_type_combo = QComboBox()
        self.job_type_combo.addItems(["Full-time", "Part-time", "Contract", "Temporary", "Volunteer", "Internship"])
        layout.addWidget(QLabel('Job Type'))
        layout.addWidget(self.job_type_combo)

        self.work_site_combo = QComboBox()
        self.work_site_combo.addItems(["On-site", "Remote", "Hybrid"])
        layout.addWidget(QLabel('Work Site'))
        layout.addWidget(self.work_site_combo)

        self.years_of_experience_input = QSpinBox()
        self.years_of_experience_input.setRange(0, 50)
        layout.addWidget(QLabel('Years of Experience'))
        layout.addWidget(self.years_of_experience_input)

        self.easy_apply_checkbox = QCheckBox("Easy Apply Only")
        self.easy_apply_checkbox.setChecked(True)
        layout.addWidget(self.easy_apply_checkbox)

        tab.setLayout(layout)
        return tab

    def run_bot(self):
        personals_updates = {
            "first_name": self.first_name_input.text(),
            "middle_name": self.middle_name_input.text(),
            "last_name": self.last_name_input.text(),
            "phone_number": self.phone_number_input.text(),
            "current_city": self.current_city_input.text(),
            "linkedIn": self.linkedin_profile_input.text(),
            "website": self.website_input.text()
        }
        search_updates = {
            "search_terms": self.search_terms_input.text(),
            "search_location": self.search_location_input.text(),
            "sort_by": self.sort_by_combo.currentText(),
            "date_posted": self.date_posted_combo.currentText()
        }
        settings_updates = {
            "search_location": self.search_location_input.text(),
            "experience_level": ["Entry level", "Associate", "Mid-Senior level", "Director", "Executive"],
            "job_type": [self.job_type_combo.currentText()] if self.job_type_combo.currentText() else [],
            "work_site": [self.work_site_combo.currentText()] if self.work_site_combo.currentText() else [],
            "years_of_experience": self.years_of_experience_input.value(),
            "easy_apply_only": self.easy_apply_checkbox.isChecked()
        }

        update_config_file("config/personals.py", personals_updates)
        update_config_file("config/search.py", search_updates)
        update_config_file("config/settings.py", settings_updates)

        self.bot_thread = BotRunnerThread()
        self.bot_thread.output_signal.connect(lambda output: self.logs.append("Output:\n" + output))
        self.bot_thread.error_signal.connect(lambda error: self.logs.append("Errors:\n" + error))
        self.bot_thread.start()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = JobApplierClient()
    sys.exit(app.exec_())
