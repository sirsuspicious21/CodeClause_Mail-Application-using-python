from tkinter import *
import smtplib
from tkinter import scrolledtext

# Create the main window
prompt = Tk()
prompt.title('Email Application')
Tk.resizable(prompt, 0, 0)

# Function to send the email
def send():
    try:
        username = temp_username.get()
        password = temp_password.get()
        to = temp_receiver.get()
        subject = temp_subject.get()
        body = subjectBody.get("1.0", "end-1c")
        
        if not all([username, password, to, subject, body]):
            notif.config(text="All fields are required", fg="red")
            return
        
        finalMessage = f'Subject: {subject}\n\n{body}'
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(username, password)
        server.sendmail(username, to, finalMessage)
        notif.config(text="Email sent successfully", fg="green")
    except:
        notif.config(text="Error sending email", fg="red")

# Function to reset the form
def reset():
    temp_username.set("")
    temp_password.set("")
    temp_receiver.set("")
    temp_subject.set("")
    subjectBody.delete("1.0", "end")
    notif.config(text="")

# Labels
Label(prompt, text="Email Application", font=('Calibri', 20)).grid(row=0, columnspan=2, pady=10)
# Label(prompt, text="Use the form below to send an email", font=('Calibri', 15)).grid(row=1, columnspan=2, sticky=W, padx=10, pady=(0, 10))
Label(prompt, text="Email:", font=('Calibri', 15)).grid(row=2, column=0, padx=10, pady=(0, 5), sticky=E)
Label(prompt, text="Password:", font=('Calibri', 15)).grid(row=3, column=0, padx=10, pady=(0, 5), sticky=E)
Label(prompt, text="To:", font=('Calibri', 15)).grid(row=4, column=0, padx=10, pady=(0, 5), sticky=E)
Label(prompt, text="Subject:", font=('Calibri', 15)).grid(row=5, column=0, padx=10, pady=(0, 5), sticky=E)
Label(prompt, text="Body:", font=('Calibri', 15)).grid(row=6, column=0, padx=10, pady=(0, 5), sticky=NE)

# Notification Label
notif = Label(prompt, text="", font=('Calibri', 15))
notif.grid(row=8, columnspan=2, pady=(10, 0))

# Storage
temp_username = StringVar()
temp_password = StringVar()
temp_receiver = StringVar()
temp_subject = StringVar()

# Entries
usernameEntry = Entry(prompt, textvariable=temp_username, font=('Calibri', 13), width=30)
usernameEntry.grid(row=2, column=1, padx=(0, 10), pady=(0, 5))
passwordEntry = Entry(prompt, show="*", textvariable=temp_password, font=('Calibri', 13), width=30)
passwordEntry.grid(row=3, column=1, padx=(0, 10), pady=(0, 5))
receiverEntry = Entry(prompt, textvariable=temp_receiver, font=('Calibri', 13), width=30)
receiverEntry.grid(row=4, column=1, padx=(0, 10), pady=(0, 5))
subjectEntry = Entry(prompt, textvariable=temp_subject, font=('Calibri', 13), width=30)
subjectEntry.grid(row=5, column=1, padx=(0, 10), pady=(0, 5))

# ScrolledText for Body
subjectBody = scrolledtext.ScrolledText(prompt, font=('Calibri', 13), width=40, height=10)
subjectBody.grid(row=6, column=1, padx=(0, 10), pady=(0, 5), sticky=NW)

# Buttons
send_button = Button(prompt, font=('Calibri', 15), text="Send", command=send)
send_button.grid(row=9, column=0, padx=10, pady=(20, 10), sticky=W)
reset_button = Button(prompt, font=('Calibri', 15), text="Reset", command=reset)
reset_button.grid(row=9, column=1, pady=(20, 10), padx=(0, 10), sticky=E)

# Main loop
prompt.mainloop()
