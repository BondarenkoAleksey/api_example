from utils.authorization import *

a = Authorization()


class TestAuthorization:
    def test_account_availability(self):
        a.checking_account_availability()

    def test_admin_account_availability(self):
        a.checking_admin_account_availability()

    def test_confirm_code(self):
        a.send_confirm_code()

    def test_login(self):
        a.login()

    def test_refresh_token(self):
        a.refresh_token()















