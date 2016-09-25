# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

sendersmtp = 'smtp.gmail.com'
senderemail = "dmtreeprod@gmail.com"
senderpassword = "doyourthing"

try:

    msg = MIMEMultipart()

    # Open a plain text file for reading.  For this example, assume that
    textfile = 'data.txt'
    # the text file contains only ASCII characters.
    with open(textfile) as fp:
        # Create a text/plain message
        msg.attach(MIMEText(fp.read()))

    attfile = open(textfile)

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attfile).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % textfile)

    msg.attach(part)

    # me == the sender's email address
    # you == the recipient's email address
    msg['Subject'] = 'The contents of %s' % textfile
    msg['From'] = 'dmtreeprog@gmail.com'
    msg['To'] = 'm.orlov@student.fontys.nl'

    # Send the message via our own SMTP server.
    s = smtplib.SMTP(sendersmtp,587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(senderemail, senderpassword)
    s.send_message(msg)
    s.quit()
    print("sent")
except Exception as ex:
    print(ex);