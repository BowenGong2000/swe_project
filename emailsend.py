import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 465  # For SSL
sender_email = "yw4177@nyu.edu"
password = input("Type your password and press enter: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    #todo send email