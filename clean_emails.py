import webbrowser
import sys
import email
import imaplib
import time
import urllib2

username, password = "test@email.com", "Password"


def delete_all__event_summary_emails(username, password):
    try:
        connection = imaplib.IMAP4_SSL('imap.gmail.com')
        try:
            connection.login(username, password)
            print "Success"
        except imaplib.IMAP4.error:
            print "Login Fail - Exception When Deleting Emails"
            raise Exception

        # ----- Delete From Inbox

        connection.select("inbox")
        typ, data = connection.search(None, '(FROM "your_delete@mail.com")')
        for num in data[0].split():
            connection.store(num, '+FLAGS', '\\Deleted')
        connection.expunge()

        # ----- Delete From Trash

        connection.select("[Gmail]/Trash")
        typ, data = connection.search(None, '(FROM "your_delete@mail.com")')
        for num in data[0].split():
            connection.store(num, '+FLAGS', '\\Deleted')
        connection.expunge()
    except imaplib.IMAP4_SSL.error:
        print "Exception While Deleting Emails"
        raise Exception


if __name__ == "__main__":
    delete_all__event_summary_emails(username, password)
