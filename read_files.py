import csv


class ReadFiles:

    @staticmethod
    def email_lists():
        email_list =[]
        with open('emails.csv', newline='') as i:
            reader = csv.reader(i)
            for row in reader:

                if row[1] != 'emails':
                    email_list.append(row[1])
            return email_list

# rf = ReadFiles()
# rf.email_lists()
