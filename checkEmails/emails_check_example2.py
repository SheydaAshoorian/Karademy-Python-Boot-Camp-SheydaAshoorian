class check_email_list:
    def __init__(self, file_name):
        self.file_name = file_name
        self._line_list = []

    def read_file(self):
        with open(self.file_name) as file:
            list_mail = file.readlines()
            yield list_mail

    def get_gmails_account_name_without_dot(self):
        for item in self.read_file():
            for email in item:
                if '@gmail' in email:
                    account_name = email.split('@')
                    account_name = account_name[0].replace('.', '')
                    self._line_list.append(account_name)
        return self._line_list

    def get_mails_account_name(self):
        for item in self.read_file():
            for email in item:
                self._line_list.append(email.split('@')[0])
        return self._line_list

    def get_emails_domains(self):
        for item in self.read_file():
            for email in item:
                self._line_list.append(email.split('@')[1])
        return self._line_list


obj = check_email_list('Book1.csv')
emails_list = obj.read_file()
print('list of gmail clean account_name without dot:',
      obj.get_gmails_account_name_without_dot())
print('list of account_name: ', obj.get_mails_account_name())
print('list of domains: ', obj.get_emails_domains())
