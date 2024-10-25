import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit, QApplication)
from subprocess import Popen, PIPE

class JobApplierClient(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # LinkedIn Credentials
        self.email_label = QLabel('LinkedIn Email', self)
        self.email_input = QLineEdit(self)

        self.password_label = QLabel('LinkedIn Password', self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        # Job Search Terms
        self.job_search_label = QLabel('Job Search Terms', self)
        self.job_search_input = QLineEdit(self)

        # Job Location
        self.location_label = QLabel('Job Location', self)
        self.location_input = QLineEdit(self)

        # Run Button
        self.run_button = QPushButton('Run Bot', self)
        self.run_button.clicked.connect(self.run_bot)

        # Log/Status Output
        self.log_output = QTextEdit(self)
        self.log_output.setReadOnly(True)

        # Layout Configuration
        layout = QVBoxLayout()
        
        # Add Input Fields
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.job_search_label)
        layout.addWidget(self.job_search_input)
        layout.addWidget(self.location_label)
        layout.addWidget(self.location_input)
        
        # Add Run Button and Log Output
        layout.addWidget(self.run_button)
        layout.addWidget(self.log_output)

        self.setLayout(layout)
        self.setWindowTitle('Auto Job Applier')
        self.show()

    def run_bot(self):
        # Capture inputs
        email = self.email_input.text()
        password = self.password_input.text()
        job_search = self.job_search_input.text()
        location = self.location_input.text()

        # Log credentials and parameters for testing
        self.log_output.append(f"Email: {email}")
        self.log_output.append(f"Password: {password}")
        self.log_output.append(f"Job Search Terms: {job_search}")
        self.log_output.append(f"Location: {location}")

        # Update config files (e.g., config/secrets.py) with the entered details
        self.update_configs(email, password, job_search, location)

        # Execute the bot using subprocess to run runAiBot.py
        process = Popen(['python', 'runAiBot.py'], stdout=PIPE, stderr=PIPE, universal_newlines=True)

        for line in iter(process.stdout.readline, ''):
            self.log_output.append(line)

        process.stdout.close()
        process.wait()

    def update_configs(self, email, password, job_search, location):
        # Update config/secrets.py and other config files as necessary
        secrets_content = f"""
username = '{email}'
password = '{password}'
"""
        with open('config/secrets.py', 'w') as secrets_file:
            secrets_file.write(secrets_content)

        search_content = f"""
search_terms = ['{job_search}']
search_location = '{location}'
"""
        with open('config/search.py', 'w') as search_file:
            search_file.write(search_content)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    client = JobApplierClient()
    sys.exit(app.exec_())
