from smtplib import SMTP, SMTPException
from email.mime.text import MIMEText


class Emailer:
    """
    toAddress: python list of addresses to send emails to
    testing: (optional) set to true to not actually send the email but print
    the email output to stdout instead
    """
    fromAddress = 'noreply@sanjuanco.com'
    toAddress = []
    server = 'mail.sanjuanco.com'
    port = 25

    def __init__(self, toAddress, testing=False):
        self.testing = testing

        if len(toAddress) > 0:
            self.toAddress = toAddress
        else:
            raise Exception('You must provide a toAddress')

        if testing:
            print('Emailer: Testing Only. No emails will be sent!')

    def sendEmail(self, subject, body, toAddress=False):
        """
        subject: subject of email
        body: text body of email
        toAddress: (optional) python list of email recipients instead of those
        already specified in the class definition

        Sends an email through the County email server
        """

        if not toAddress:
            toAddress = self.toAddress

        message = MIMEText(body)
        message['Subject'] = subject
        message['From'] = self.fromAddress
        message['To'] = ','.join(toAddress)

        if not self.testing:
            s = SMTP(self.server, self.port)
            try:
                s.sendmail(self.fromAddress, toAddress, message.as_string())
            except SMTPException:
                raise
            s.quit()
        else:
            print('*** Test Email Message to {0} ***'.format(toAddress))
            print(message)
            print('*** End Email Message ***')
