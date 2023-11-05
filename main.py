#!/usr/bin/python
#    _____                 ____            _       
#   | ____|___ ___       / ___|___ _ __  | |_ ___ 
#  |  _|/ __/ _  \ _____| |  / _  \ '_ \| __/ __|
# | |__| (_| (_) |_____| |__|  __/ | | | |_\__ \
#|_____\___\___/       \____\___|_| |_|\__|___/
#                                             
# Please go through the README file before execution
# Visit https://github.com/tanishqru/9-EcoCents for the latest version and other info
# ---------------------------------------------------Import statements-------------------------------------------------- #

import sys
#pip install PyQt5
import random  
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QLineEdit, QWidget, QFileDialog, QLabel, QMessageBox, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from validate_email import validate_email
# pip install validate_email
import matplotlib.pyplot as plt
from io import BytesIO
import mysql.connector 
# pip install mysql-connector 
# pip install pandas 
from pandas.core.common import flatten
#Email libraries
import smtplib
from email.mime.multipart import MIMEMultipart

# ---------------------------------------------------Variables and misc---------------------------------------------------- #

global loginpage_details
loginpage_details = []
global lineEdit_username
lineEdit_username = ""
global in_username
in_username = ""
global lineEdit_email
lineEdit_email = ""
global lineEdit_phnumber
lineEdit_phnumber = ""
global lineEdit_password
lineEdit_password = ""
global lineEdit_repeatpassword
lineEdit_repeatpassword = ""

global db

try:
    db = mysql.connector.connect(host='localhost', user = 'admin_ecocents', passwd = 'admin@password@ecocents', database = 'ecocents')
    print("Successfully Connected To Local SQL Server") 
except:
    try: 
        db = mysql.connector.connect(host= 'archserver.ddns.net', user = 'ecocents', passwd = 'password@ecocents', database = 'ecocents')
        print("Successfully Connected Arch Server") 
    except: print("Error Connecting to SQL Server")

if (db) :
    print(r'''
 ____   ___  _        ____                            _           _
/ ___| / _ \| |      / ___|___  _ __  _ __   ___  ___| |_ ___  __| |
\___ \| | | | |     | |   / _ \| '_ \| '_ \ / _ \/ __| __/ _ \/ _` |
 ___) | |_| | |___  | |__| (_) | | | | | | |  __/ (__| ||  __/ (_| |
|____/ \__\_\_____|  \____\___/|_| |_|_| |_|\___|\___|\__\___|\__,_|
''')

else :
    print(r'''
 ____   ___  _       __  __                        _
/ ___| / _ \| |     |  \/  | ___  ___ ___  ___  __| |  _   _ _ __
\___ \| | | | |     | |\/| |/ _ \/ __/ __|/ _ \/ _` | | | | | '_ \
 ___) | |_| | |___  | |  | |  __/\__ \__ \  __/ (_| | | |_| | |_) |
|____/ \__\_\_____| |_|  |_|\___||___/___/\___|\__,_|  \__,_| .__/
                                                            |_|''')




try:
    global server
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('system.ecocents@gmail.com', 'ecocentspass')
except:
    print('Something went wrong with mail server')



global curs 
curs  = db.cursor()

def getLoginDetails():
    global loginpage_details
    curs.execute('select name, password from users')
    loginpage_details = curs.fetchall()
    loginpage_details = list(flatten(loginpage_details))

getLoginDetails()

# ----------------------------------------------------class declaration---------------------------------------------------- #

class loginregister(QMainWindow):
    def __init__(self):
        super(loginregister, self).__init__()
        loadUi("loginregister.ui", self)
        self.setWindowTitle("Eco-Cents")
        self.login_button.clicked.connect(self.gotologin_page)
        self.register_button.clicked.connect(self.gotoregister_page)
        #self.iconName = "logo.jpg"
    def gotologin_page(self):
        widget.setCurrentIndex(1)

    def gotoregister_page(self):
        widget.setCurrentIndex(2)

# ------------------------------------------------------login_page--------------------------------------------------------- #

class login_page(QMainWindow):
    def __init__(self):
        super(login_page, self).__init__()
        loadUi("login_page.ui", self)
        self.pushButton_back.clicked.connect(self.back_button_pressed)
        self.pushButton_login.clicked.connect(self.login_button_pressed)
        self.password_view.clicked.connect(self.pass_view_clicked)

    def pass_view_clicked(self):
        if self.password_view.isChecked():
            self.lineEdit_password.setEchoMode(QLineEdit.Normal)
        else:
            self.lineEdit_password.setEchoMode(QLineEdit.Password)

    def back_button_pressed(self):
        widget.setCurrentIndex(0)

    def login_button_pressed(self):
        getLoginDetails()
        if self.lineEdit_username.text() == "" or self.lineEdit_password.text() == "":
            print("empty")

            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.setWindowTitle('Empty Fields')
            error_dialog.showMessage("Please fill all the fields")
        else:
            if self.lineEdit_username.text() in loginpage_details:
                if self.lineEdit_password.text() == loginpage_details[loginpage_details.index(self.lineEdit_username.text()) + 1]:
                    login_page.logged_in_username = self.lineEdit_username.text()
                    global in_username
                    in_username = login_page.logged_in_username
                    login_page.logged_in_password = self.lineEdit_password.text()
                    self.lineEdit_username.setText("")
                    self.lineEdit_password.setText("")
                    error_dialog = QtWidgets.QErrorMessage(self)
                    error_dialog.setWindowTitle('Welcome')
                    error_dialog.showMessage(
                        f"Welcome back {login_page.logged_in_username}!")
                    widget.setCurrentIndex(3)
                else:
                    error_dialog = QtWidgets.QErrorMessage(self)
                    error_dialog.setWindowTitle('Password')
                    error_dialog.showMessage(
                        'Incorrect password, please try again')
                    self.lineEdit_password.setText("")
            else:
                error_dialog = QtWidgets.QErrorMessage(self)
                error_dialog.setWindowTitle('Account')
                error_dialog.showMessage('Please create an account')
                self.lineEdit_username.setText("")
                self.lineEdit_password.setText("")
                widget.setCurrentIndex(2)

# --------------------------------------------------------register_page---------------------------------------------------- #

class register_page(QMainWindow):
    def __init__(self):
        super(register_page, self).__init__()
        loadUi("registerpage.ui", self)
        self.pushButton_back.clicked.connect(self.backbutton_clicked)
        self.pushButton_register.clicked.connect(self.registerbutton_clicked)
        self.sp_view.clicked.connect(self.sp_view_clicked)
        self.cp_view.clicked.connect(self.cp_view_clicked)

    def sp_view_clicked(self):
        if self.sp_view.isChecked():
            self.lineEdit_password.setEchoMode(QLineEdit.Normal)
        else:
            self.lineEdit_password.setEchoMode(QLineEdit.Password)

    def cp_view_clicked(self):
        if self.cp_view.isChecked():
            self.lineEdit_repeatpassword.setEchoMode(QLineEdit.Normal)
        else:
            self.lineEdit_repeatpassword.setEchoMode(QLineEdit.Password)

    def backbutton_clicked(self):
        widget.setCurrentIndex(0)

    def registerbutton_clicked(self):

        if self.lineEdit_username.text() == "" or self.lineEdit_email.text() == "" or self.lineEdit_phnumber.text() == "" or self.lineEdit_password.text() == "" or self.lineEdit_repeatpassword.text() == "":
            print("empty")
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.setWindowTitle('Empty Fields')
            error_dialog.showMessage("Please fill all the fields")
        elif len(self.lineEdit_phnumber.text()) != 10:
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.setWindowTitle('Phone Number')
            error_dialog.showMessage('Please enter a valid phone number')
            self.lineEdit_phnumber.setText("")

        elif self.lineEdit_password.text() != self.lineEdit_repeatpassword.text():
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.setWindowTitle('Password')
            error_dialog.showMessage('Passwords are not matching, please try again.')
            self.lineEdit_password.setText("")
            self.lineEdit_repeatpassword.setText("")

        elif self.lineEdit_password.text() == self.lineEdit_repeatpassword.text():
            if validate_email(self.lineEdit_email.text()):
                if self.lineEdit_username.text() not in loginpage_details:

                    eight_digit_number = random.randint(10000000, 99999999)
                    print(eight_digit_number)
                    phone_number = self.lineEdit_phnumber.text()
                    print(phone_number)
                    curs.execute(f"insert into users values('{self.lineEdit_email.text()}', '{self.lineEdit_username.text()}', '{self.lineEdit_password.text()}', {phone_number})")  
                    db.commit()
                    getLoginDetails()
                    self.lineEdit_username.setText("")
                    self.lineEdit_email.setText("")
                    self.lineEdit_phnumber.setText("")
                    self.lineEdit_referal.setText("")
                    self.lineEdit_password.setText("")
                    self.lineEdit_repeatpassword.setText("")
                    error_dialog = QtWidgets.QErrorMessage(self)
                    error_dialog.setWindowTitle('Thank you')
                    error_dialog.showMessage('Creation of account is successful! Please login with the same credentials')
                    widget.setCurrentIndex(1)
                else:
                    error_dialog = QtWidgets.QErrorMessage(self)
                    error_dialog.setWindowTitle('Account')
                    error_dialog.showMessage('An account with these credentials is already registered, please try logging in.')
                    widget.setCurrentIndex(1)

            else:
                error_dialog = QtWidgets.QErrorMessage(self)
                error_dialog.setWindowTitle('Email')
                error_dialog.showMessage('Please enter a valid email ID')
                self.lineEdit_email.setText("")

# ---------------------------------------------------------home_page------------------------------------------------------- #

class home_page(QMainWindow):
    def __init__(self) -> None :
        super(home_page, self).__init__()
        loadUi("home.ui", self)
        #menubar.self.menubar()
        #menubar.setNativeMenuBar(False)
        self.pushButton_logout.clicked.connect(self.are_you_sure)
#        self.pushButton_profile.clicked.connect(self.gotoprofile)

#        self.companies_button.clicked.connect(self.gotocompanies)
#        self.investments_button.clicked.connect(self.gotoinvestments)
#        self.courses_button.clicked.connect(self.gotocourses)
#        self.newsgroup_button.clicked.connect(self.gotonewsgroup)
#        self.transHistory_button.clicked.connect(self.gototransHistory)
#        self.refer_button.clicked.connect(self.gotorefer)

    def are_you_sure(self):
        msg = QMessageBox()
        msg.setWindowTitle("Logout")
        msg.setText("Are you sure?")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        msg.setDefaultButton(QMessageBox.No)
        msg.buttonClicked.connect(self.popup_button)
        x = msg.exec_()

    def popup_button(self, button):
        button_pressed = button.text()

        if button_pressed == '&Yes':
            widget.setCurrentIndex(0)

        else:
            pass

    def gotocompanies(self):
        widget.setCurrentIndex(5)
    
    def gotoinvestments(self):
        widget.setCurrentIndex(6)

    def gotocourses(self):
        widget.setCurrentIndex(9)

    def gotonewsgroup(self):
        widget.setCurrentIndex(7)

    def gototransHistory(self):
        widget.setCurrentIndex(11)

    def gotorefer(self):
        widget.setCurrentIndex(12)

# ---------------------------------------------------------companies_page------------------------------------------------------- #

class companies_page(QMainWindow):
    def __init__(self) -> None :
        super(companies_page, self).__init__()
        loadUi("explore_companies.ui", self)
        #menubar.self.menubar()
        #menubar.setNativeMenuBar(False)
        self.pushButton_back.clicked.connect(self.backbutton_clicked)
        self.pushButton_1.clicked.connect(self.gototransaction)
        self.pushButton_2.clicked.connect(self.gototransaction)
        self.pushButton_3.clicked.connect(self.gototransaction)
        self.pushButton_4.clicked.connect(self.gototransaction)
        self.pushButton_5.clicked.connect(self.gototransaction)
        self.pushButton_6.clicked.connect(self.gototransaction)
        self.pushButton_7.clicked.connect(self.gototransaction)
        self.pushButton_8.clicked.connect(self.gototransaction)
        self.pushButton_9.clicked.connect(self.gototransaction)
        self.pushButton_10.clicked.connect(self.gototransaction)
        self.pushButton_11.clicked.connect(self.gototransaction)
        self.pushButton_12.clicked.connect(self.gototransaction)
        self.pushButton_13.clicked.connect(self.gototransaction)
        self.pushButton_14.clicked.connect(self.gototransaction)
        self.pushButton_15.clicked.connect(self.gototransaction)
        self.pushButton_16.clicked.connect(self.gototransaction)

    def backbutton_clicked(self):
        widget.setCurrentIndex(0)

    def gototransaction(self):
        widget.setCurrentIndex(5)

# ---------------------------------------------------------investment_page------------------------------------------------------- #

class investment_page(QMainWindow):
    def __init__(self) -> None :
        super(investment_page, self).__init__()
        loadUi("investment_analysis.ui", self)
        #menubar.self.menubar()
        #menubar.setNativeMenuBar(False)
        self.pushButton_back.clicked.connect(self.backbutton_clicked)
#        self.pushButton_sell_shares.clicked.connect(self.gotoshares)

    def backbutton_clicked(self):
        widget.setCurrentIndex(0)

#    def gotoshares(self):
#        widget.setCurrentIndex(5)

    # Load your .ui file
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = loadUi('your_ui_file.ui', baseinstance=window)

    # Create a simple line graph with matplotlib
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]

    plt.plot(x, y)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Sample Line Plot")

    # Save the matplotlib plot to a QPixmap
    buf = BytesIO()
    plt.savefig(buf, format='png')
    pixmap = QPixmap()
    pixmap.loadFromData(buf.getvalue())

    # Set the QPixmap as the label's pixmap in the .ui file
    ui.graphLabel.setPixmap(pixmap)

    # Show the main window
    window.show()

# ---------------------------------------------------------courses_page------------------------------------------------------- #

class courses_page(QMainWindow):
    def __init__(self) -> None :
        super(courses_page, self).__init__()
        loadUi("courses.ui", self)
        #menubar.self.menubar()
        #menubar.setNativeMenuBar(False)
        self.pushButton_back.clicked.connect(self.backbutton_clicked)
        self.pushButton_1.clicked.connect(self.gototransaction)
        self.pushButton_2.clicked.connect(self.gototransaction)
        self.pushButton_3.clicked.connect(self.gototransaction)
        self.pushButton_4.clicked.connect(self.gototransaction)
        
    def backbutton_clicked(self):
        widget.setCurrentIndex(0)

    def gototransaction(self):
        widget.setCurrentIndex(5)

# ------------------------------------------------------transactions_page-------------------------------------------------- #

class transaction_page(QMainWindow):
    def __init__(self) -> None :
        super(transaction_page, self).__init__()
        loadUi("transaction_page.ui", self)
        self.pushButton_back.clicked.connect(self.backbutton_clicked)
#        self.pushButton_paytm.clicked.connect(self.paytmbutton_clicked)
#        self.pushButton_upi.clicked.connect(self.upibutton_clicked)
#        self.pushButton_netbank.clicked.connect(self.netbankbutton_clicked)

    def backbutton_clicked(self):
        widget.setCurrentIndex(4)

#    def paytmbutton_clicked(self):
#        widget.setCurrentIndex(16)

#    def upibutton_clicked(self):
#        widget.setCurrentIndex(17)

#    def netbankbutton_clicked(self):
#        widget.setCurrentIndex(18)

# ---------------------------------------------------transactions_paytm_page----------------------------------------------- #

#class transaction_paytm_page(QMainWindow):
#    def __init__(self) -> None :
#        super(transaction_paytm_page, self).__init__()
#        loadUi("transaction_paytm.ui", self)
#        self.pushButton_pay.clicked.connect(self.paybutton_clicked)
#       self.pushButton_cancel.clicked.connect(self.cancelbutton_clicked)
#
#    def paybutton_clicked(self):
#        error_dialog = QtWidgets.QErrorMessage(self)
#        error_dialog.setWindowTitle('Booking')
#        error_dialog.showMessage('Your booking has been placed.')
#        global in_username
#        curs.execute(f"select email_or_fcbk from login_details where username = '{in_username}'")
#        send_to_email = curs.fetchone()
#        send_to_email = str(send_to_email[0])
#        msg = "\r\n".join([
#                "From: syedhasubhana2004@gmail.com",
#                f"To: {send_to_email}",
#                f"Subject: Booking Confirmed [NO REPLY]",
#                "",
#                f'''Dear Customer, 
#This is to confirm that we have received your booking. We pledge to provide you with the best possible at-home service experience. 
#Thank you again for making it possible.
#
#Regards
#Team SWEEP  '''
#                ])
#        server.sendmail('syedhasubhana2004@gmail.com', send_to_email, msg)
#        widget.setCurrentIndex(4)

#    def cancelbutton_clicked(self):
#        widget.setCurrentIndex(4)

# -----------------------------------------------indexing for stacked widget----------------------------------------------- #

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
widget.setMaximumHeight(600)
widget.setMaximumWidth(800)
widget.setMinimumHeight(600)
widget.setMinimumWidth(800)

login_register = loginregister()
login = login_page()
register = register_page()
home = home_page()
explore_companies = companies_page()
investment_analysis = investment_page()
courses = courses_page()
transactions = transaction_page()

widget.addWidget(login_register)                #00
widget.addWidget(login)                         #01
widget.addWidget(register)                      #02
widget.addWidget(home)                          #03
widget.addWidget(explore_companies)             #04
widget.addWidget(investment_analysis)           #05
widget.addWidget(courses)                       #06
widget.addWidget(transactions)                  #07

widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
