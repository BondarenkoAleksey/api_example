import time
from assertion import *
from http_methods import HttpMethod
from utils.const.const_authorization import *


url = 'https://abc.ru'
path = '/api/v1/auth/'
url_auth = url + path


class Authorization(HttpMethod):

    """Проверка наличия аккаунта /api/v1/auth/check-login"""
    def checking_account_availability(self):
        print('\nPOST Проверка наличия аккаунта /api/v1/auth/check-login')
        response = self.post(url_auth + 'check-login',
                             post_json=json_for_check_email_for_login)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_params_in_json(
            response, expected_params_check_login)
        Assertions.assert_value_in_json(response, 'registrationRequired', False,
                                        response.json()['data'][
                                            'registrationRequired'])
        print("response_json = ", response.json())

    """Проверка наличия аккаунта администратора 
    /api/v1/auth/admin/check-login"""
    def checking_admin_account_availability(self):
        print('\nPOST Проверка наличия аккаунта администратора '
              '/api/v1/auth/check-login')
        response = self.post(url_auth + 'admin/check-login',
                             post_json=json_for_check_admin_acount)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_params_in_json(
            response, expected_params_check_admin_acount)
        Assertions.assert_value_in_json(response, 'registrationRequired', True,
                                        response.json()['data'][
                                            'registrationRequired'])
        print("response_json = ", response.json())

    """Отправка кода подтверждения /api/v1/auth/confirm-code/send"""
    def send_confirm_code(self):
        print('\nPOST Отправка кода подтверждения '
              '/api/v1/auth/confirm-code/send')
        response = self.post(url_auth + 'confirm-code/send',
                             post_json=json_for_send_confirm_code)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_params_in_json(
            response, list_of_expected_params_from_comfirm_code)
        Assertions.assert_value_in_json(response, 'status', 'ok',
                                        response.json()['data']['status'])
        print("response_json = ", response.json())

    """Авторизация /api/v1/auth/login"""
    def login(self):
        print('\nPOST Авторизация /api/v1/auth/login')
        response = self.post(url_auth + 'login',
                             post_json=json_for_login)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_params_in_json(
            response, expected_params_login)
        print("response_json = ", response.json())
        global refresh, access
        refresh = response.json()['data']['refresh']
        access = response.json()['data']['access']

    """Обновление токена /api/v1/auth/token/refresh"""
    def refresh_token(self):
        print('\nPOST Обновление токена /api/v1/auth/token/refresh')
        json_for_refresh = {"refresh": refresh}
        response = self.post(url_auth + 'token/refresh',
                             post_json=json_for_refresh)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_params_in_json(
            response, expected_params_resresh)
        Assertions.\
            assert_value_in_json_not_equal_to_actual(
                response, 'access', access, response.json()['data']['access'])
        Assertions.\
            assert_value_in_json_not_equal_to_actual(
                response, 'refresh', refresh, response.json()[
                    'data']['refresh'])
        Assertions.\
            assert_value_in_json_not_equal_to_actual(
                response, 'expire', round(time.time()),
                response.json()['data']['expire'])
        print("response_json = ", response.json())
