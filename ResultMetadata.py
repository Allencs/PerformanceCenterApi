from PerformanceCenter import PerformanceCenter
from Authenticate import Authenticate
import requests
<<<<<<< HEAD
=======
from ResultMetadataParse import ParseResult
>>>>>>> PerfoermanceCenterApi


class ResultMetadata(PerformanceCenter):
    au_cookies = Authenticate().authenticate

    def __init__(self, run_id):
<<<<<<< HEAD
        self.run_id = str(run_id)

    def get_result_info_xml(self):
        url = "http://{}/LoadTest/rest/domains/{}/projects/{}/Runs/{}/Results".format(
            self.ip, self.domain, self.project_name, self.run_id)
        response = requests.get(url, cookies=self.au_cookies)
        return response.text
=======
        super().__init__()
        self.run_id = run_id

    def get_result_metadata_xml(self):
        url = "http://{}/LoadTest/rest/domains/{}/projects/{}/Runs/{}/Results".format(
            self.ip, self.domain, self.project_name, str(self.run_id))
        try:
            response = requests.get(url, cookies=self.au_cookies)
        except requests.exceptions.RequestException as error:
            print(error)
        else:
            return response.text

    @staticmethod
    def get_result_metadata():
        source = ResultMetadata(87).get_result_metadata_xml()
        result_metadata = ParseResult(source).get_metadata_info(0)
        return result_metadata


if __name__ == '__main__':
    print(ResultMetadata.get_result_metadata())


>>>>>>> PerfoermanceCenterApi
