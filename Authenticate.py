import requests
from PerformanceCenter import PerformanceCenter


class Authenticate(PerformanceCenter):
<<<<<<< HEAD
    url = "http://" + PerformanceCenter.ip + "/LoadTest/rest/authentication-point/authenticate"
    login_info = "cHQ1NDNmOkNzY3NjczIy"

    @property
    def authenticate(self):
        header = {
            'Authorization': 'Basic ' + self.login_info
        }
        req = requests.get(self.url, headers=header)
        qc_cookies = req.cookies
        return qc_cookies
=======
    def __init__(self):
        super().__init__()

    @property
    def authenticate(self):
        url = "http://" + self.ip + "/LoadTest/rest/authentication-point/authenticate"
        login_info = "cHQ1NDNmOkNzY3NjczIy"
        header = {
            'Authorization': 'Basic ' + login_info
        }
        req = requests.get(url, headers=header)
        qc_cookies = req.cookies
        return qc_cookies


if __name__ == '__main__':
    au = Authenticate().authenticate
    print(au)
>>>>>>> PerfoermanceCenterApi
