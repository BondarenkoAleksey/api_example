from requests import Response


class Assertions:

    """Проверка статус-кода"""

    def assert_status_code(self: Response, expected_status_code):
        assert self.status_code == expected_status_code, \
            f'FAIL! Статус-код {self.status_code}.' \
            f'{self.json()}'
        print(f'Успешно! Статус-код запроса ниже: {self.status_code}')
        print(self.url)

    """Проверка параметров в JSON"""

    def assert_params_in_json(self: Response, expected_params):
        if type(self.json()['data']) == dict:
            if list((self.json()['data']).keys()) == ['user']:
                json_params = list((self.json()['data']['user']).keys())
                not_matches = [i for i in json_params if i
                               not in expected_params]
                not_matches2 = [i for i in expected_params if i
                                not in json_params]
                assert not_matches == not_matches2 == [], \
                    f'FAIL! Ожидаемые параметры и фактические' \
                    f'не совпали на {not_matches}'
                print(f"Полученные в JSON названия параметров совпали с "
                      f"ожидаемыми "
                      f"{expected_params}")

            else:
                json_params = list((self.json()['data']).keys())
                not_matches = [i for i in json_params if i
                               not in expected_params]
                assert not_matches == [], f'FAIL! Ожидаемые параметры и ' \
                                          f'фактические не совпали на ' \
                                          f'{not_matches}'
                print(f"Полученные в JSON названия параметров совпали с "
                      f"ожидаемыми "
                      f"{expected_params}")
                print('1g')

        if type(self.json()['data']) == list:
            if len(self.json()['data']) == 0:
                print("Пустой массив - параметров нет")
            elif list((self.json()['data'][0]).keys()) == ['role', 'company']:
                json_params = list((self.json()['data'][0]).keys())
                not_matches = [i for i in json_params if i
                               not in expected_params]
                not_matches2 = [i for i in expected_params if i
                                not in json_params]
                assert not_matches == not_matches2 == [], \
                    f'FAIL! Ожидаемые параметры и фактические' \
                    f'не совпали на {not_matches}'
                print(f"Полученные в JSON названия параметров совпали с "
                      f"ожидаемыми "
                      f"{expected_params}")

            else:
                print("Случая нет в проверяльщике assertion, ДОБАВИТЬ!!!")

    """Проверка соответствия фактического значения параметра ожидаемому"""

    def assert_value_in_json(
            self: Response, expected_param, expected_value, fact_value):
        assert fact_value == expected_value, \
            f'FAIL! Ожидаемое и фактическое значения' \
            f' параметра {expected_param} не совпали' \
            f' fact_value = {fact_value}, expected_value = {expected_value}'
        print(f"Полученное значение параметра {expected_param},"
              f" равное {fact_value}, совпадает с ожидаемым")

    """Проверка, что фактическое значение параметра не равно ожидаемому"""

    def assert_value_in_json_not_equal_to_actual(
            self: Response, expected_param, expected_value, fact_value):
        assert fact_value != expected_value, \
            f'FAIL! Ожидаемое и фактическое значения' \
            f' параметра {expected_param} совпали' \
            f' fact_value = {fact_value}, expected_value = {expected_value}'
        print(f"Полученное значение параметра {expected_param},"
              f" равное {fact_value}, не совпадает с ожидаемым")

