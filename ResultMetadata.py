from PerformanceCenter import PerformanceCenter
from Authenticate import Authenticate
import requests


class ResultMetadata(PerformanceCenter):
    au_cookies = Authenticate().authenticate

    def __init__(self, run_id):
        self.run_id = str(run_id)

    def get_result_info_xml(self):
        url = "http://{}/LoadTest/rest/domains/{}/projects/{}/Runs/{}/Results".format(
            self.ip, self.domain, self.project_name, self.run_id)
        response = requests.get(url, cookies=self.au_cookies)
        return response.text