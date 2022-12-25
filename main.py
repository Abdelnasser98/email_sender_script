from __future__ import print_function

from gmail_auth import Gmail
from read_files import ReadFiles

def main():
    gm = Gmail()
    rf = ReadFiles()

    email_list = rf.email_lists()

    for i in email_list:
        gm.send_message(i)
    print('Finished')

if __name__ == '__main__':
    main()
