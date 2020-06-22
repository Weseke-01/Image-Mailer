import smtplib
import os
from email.message import EmailMessage
import tkinter as tk
from tkinter import filedialog
import imghdr


def run():
    select_attachment()
    send()

    restart = input("Do you want to send more images? If so, typ 'yes': ").lower()

    if restart == "yes":
        run()
    else:
        exit()



def select_attachment():
    frame = tk.Tk()
    frame.withdraw()

    file_path = filedialog.askopenfilename()

    files = list()
    for f in file_path:
        with open(file_path, 'rb') as file:
            file_data = file.read()
            file_type = imghdr.what(file.name)
            file_sort = file.name
            a = attachment(file_data, file_type, file_sort)
            files.append(a)

    return files


def send():
    EMAIL_ADRRESS = os.environ.get('GMAIL_BC_USER')
    EMAIL_PASSWORD = os.environ.get('GMAIL_BC_PASS')

    msg = EmailMessage()
    msg['Subject'] = 'test'
    msg['From'] = EMAIL_ADRRESS
    msg['To'] = 'wes.kikken@outlook.com'
    msg.set_content('Image attached...')

    files = select_attachment()
    for a in files:
        msg.add_attachment(a.file_d, maintype='image', subtype=a.file_t, filename=a.file_s)


    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as mail:
        mail.login(EMAIL_ADRRESS, EMAIL_PASSWORD)
        mail.send_message(msg)


class attachment:
    def __init__(self, file_d, file_t, file_s):
        self.file_d = file_d
        self.file_t = file_t
        self.file_s = file_s

run()