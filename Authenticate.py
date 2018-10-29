import requests
from PerformanceCenter import PerformanceCenter


class Authenticate(PerformanceCenter):
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