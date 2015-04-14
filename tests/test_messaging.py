import geopublisher.messaging
import unittest


class fake_SMTP:
    """
    A SMTP stub for unit tests
    Idea came from http://eradman.com/posts/python-test-doubles.html
    """
    calls = []

    def __init__(self, _server, _port):
        self.calls.append("__init__('%s')" % _server)

    def sendmail(self, _from, _to, _msg):
        self.calls.append("sendmail(%s, %s, <msg>)" % (_from, _to))

    def quit(self):
        self.calls.append("quit()")


class TestMessaging(unittest.TestCase):

    to = ['test@test.com']
    sub = 'test subject'
    body = 'test body'

    def setUp(self):
        """
        Create a emailer object
        """

        self.emailer = geopublisher.messaging.Emailer(self.to)

    def tearDown(self):
        """
        Remove the emailer object
        """

        self.emailer = None

    def test_sendEmail(self):
        """
        It should call the sendmail method of smtplib
        """

        geopublisher.messaging.SMTP = fake_SMTP
        self.emailer.sendEmail(self.sub, self.body)
        self.assertIn("sendmail(noreply@sanjuanco.com, {0}, <msg>)".format(self.to), fake_SMTP.calls)

    def test_quit(self):
        """
        It should quit the smtp connection after sending
        """

        pass

    def test_sendTestEmail(self):
        """
        It should not send the email when testing is true
        """

        geopublisher.messaging.smtplib = fake_SMTP
        emailerTest = geopublisher.messaging.Emailer('[fake@fake]', testing=True)
        emailerTest.sendEmail(self.sub, self.body)
        self.assertNotIn('fake@fake', fake_SMTP.calls)
