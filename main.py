from __future__ import print_function

from gmail_auth import Gmail
from read_files import ReadFiles


def main():
    message = input('Please Enter your message.\n')
    gm = Gmail()
    rf = ReadFiles()
    emails = rf.email_lists()

    for email in emails:
        gm.send_message(email, message)


if __name__ == '__main__':
    main()
