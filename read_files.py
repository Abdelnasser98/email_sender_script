import pandas as pd
class ReadFiles:

    def email_lists(self):

        data = pd.read_csv("emails.csv",)
        emails = list(data['emails'])

        return emails
