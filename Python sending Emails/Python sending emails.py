
#!/usr/bin/python3

import smtplib

sender_mail = 'ahmadalisurani360@gmail.com'
receivers_mail = ['70177681@student.uol.edu.pk']

message = """From: Ahmad Ali
To: UOL Student
Subject: Sending SMTP E-mail

Hello!
This is a test email from Ahmad Ali.
"""

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender_mail, receivers_mail, message)
    print("Successfully sent email")

except Exception as e:
    print("Error: unable to send email:", e)



import smtplib
import ssl

sender_mail = 'ahmadalisurani360@gmail.com'
receivers_mail = ['70177681@student.uol.edu.pk']

message = """From: Ahmad Ali
To: UOL Student
Subject: Sending SMTP E-mail

Hello!
This is a test email from Ahmad Ali.
"""

try:
    context = ssl.create_default_context()

    with smtplib.SMTP('smtp.gmail.com', 587) as smtpObj:
        smtpObj.starttls(context=context)

        smtpObj.login(sender_mail, 'YOUR_APP_PASSWORD')

        smtpObj.sendmail(
            sender_mail,
            receivers_mail,
            message
        )

    print("Successfully sent email")

except Exception as e:
    print("Error:", e)
