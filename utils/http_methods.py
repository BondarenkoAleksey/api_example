import requests

headers = {
    'Authorization': 'Bearer onlyfortesttoken',
    'Cookie': '_csrf=1FeffghG3Jg54H'
}

cookies = ""


class HttpMethod:

    @staticmethod
    def get(url, query_params=None):
        response = requests.get(url, headers=headers,
                                cookies=cookies, params=query_params)
        return response

    @staticmethod
    def post(url, payload=None, post_json=None, files=None):
        response = requests.post(url, json=post_json, data=payload,
                                 headers=headers, cookies=cookies, files=files)
        return response

    @staticmethod
    def patch(url, payload=None, patch_json=None, files=None):
        response = requests.patch(url, json=patch_json, data=payload,
                                  headers=headers, cookies=cookies, files=files)
        return response

    @staticmethod
    def delete(url):
        response = requests.delete(url, headers=headers, cookies=cookies)
        return response
