from __future__ import print_function

from gmail_auth import Gmail
from read_files import ReadFiles

def main():
    gm = Gmail()
    rf = ReadFiles()
    emails = rf.email_lists()

    for email in emails:
        gm.send_message(email)


if __name__ == '__main__':
    main()
