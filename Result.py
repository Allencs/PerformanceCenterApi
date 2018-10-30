from PerformanceCenter import PerformanceCenter
from Authenticate import Authenticate
import requests


class Result(PerformanceCenter):

    au_cookies = Authenticate().authenticate

    def __init__(self, run_id, result_id):
<<<<<<< HEAD
        self.run_id = str(run_id)
        self.result_id = str(result_id)

    @property
    def get_data(self):
        url = "http://{}/LoadTest/rest/domains/{}/projects/{}/Runs/{}/Results/{}/data".format(
            self.ip, self.domain, self.project_name, self.run_id, self.result_id)

        response = requests.get(url, cookies=self.au_cookies)
        file_path = "D:\\sgmuserprofile\\pt543f\\Desktop\\result\\result.zip"
        with open(file_path, 'wb') as f:
            f.write(response.content)
            f.close()
        return None
=======
        super().__init__()
        self.run_id = str(run_id)
        self.result_id = str(result_id)

    def download_result(self):
        url = "http://{}/LoadTest/rest/domains/{}/projects/{}/Runs/{}/Results/{}/data".format(
            self.ip, self.domain, self.project_name, self.run_id, self.result_id)
        try:
            response = requests.get(url, cookies=self.au_cookies)
        except requests.exceptions.RequestException as error:
            print(error)
        else:
            file_path = "D:\\sgmuserprofile\\pt543f\\Desktop\\result\\result.zip"
            with open(file_path, 'wb') as f:
                f.write(response.content)
                f.close()


>>>>>>> PerfoermanceCenterApi
