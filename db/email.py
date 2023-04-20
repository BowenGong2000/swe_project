import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header
import mimetypes

EMAIL = ''
PASSWORD = ''
RESUME_FILENAME = 'resume_filename'
RESUME_CONTENT = 'resume_content'
TRANSCRIPT_FILENAME = 'transcript_filename'
TRANSCRIPT_CONTENT = 'transcript_content'
COVERLETTER_FILENAME = 'coverletter_filename'
COVERLETTER_CONTENT = 'coverletter_content'
APPLICATION_NAME = 'application_name'


def email_send(reciver, application_dict):
    msg = MIMEMultipart()
    msg['From'] = Header("Project Matcher Team", 'utf-8')
    msg['To'] = Header(application_dict[APPLICATION_NAME], 'utf-8')
    msg['Subject'] = Header('Application Recieved from Project Matcher', 'utf-8')
    text = f"The project has recieve an application from" \
           f"{application_dict['application_name']}." \
           f"Files submitted by {application_dict['applicant_name']}"\
           f"is attached bellow."
    msg.attach(MIMEText(text, 'plain', 'utf-8'))
    if RESUME_FILENAME:
        attachment = MIMEApplication(application_dict[RESUME_CONTENT],
                                     _subtype=mimetypes.guess_type(application_dict[RESUME_FILENAME]))
        attachment.add_header('content-disposition',
                              'attachment',
                              filename=application_dict[RESUME_FILENAME])
        msg.attach(attachment)
    if TRANSCRIPT_FILENAME:
        attachment = MIMEApplication(application_dict[TRANSCRIPT_CONTENT],
                                     _subtype=mimetypes.guess_type(application_dict[TRANSCRIPT_FILENAME]))
        attachment.add_header('content-disposition',
                              'attachment',
                              filename=application_dict[TRANSCRIPT_FILENAME])
        msg.attach(attachment)
    if COVERLETTER_FILENAME:
        attachment = MIMEApplication(application_dict[COVERLETTER_CONTENT],
                                     _subtype=mimetypes.guess_type(application_dict[COVERLETTER_FILENAME]))
        attachment.add_header('content-disposition',
                              'attachment',
                              filename=application_dict[COVERLETTER_FILENAME])
        msg.attach(attachment)
    ret = True
    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.login(EMAIL, PASSWORD)
        smtpObj.sendmail(EMAIL, reciver, msg.as_string())
    except smtplib.SMTPException:
        ret = False
    finally:
        smtpObj.quit()
        return ret
