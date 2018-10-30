from PerformanceCenter import PerformanceCenter
from Authenticate import Authenticate
import requests


class StopTest(PerformanceCenter):
    au_cookies = Authenticate().authenticate

    def __init__(self, run_id):
        super().__init__()
        self.run_id = run_id

    def stop(self):
        header = {'Content-Type': 'application/xml'}
        data = "<PostRunActions xmlns=\"http://www.hp.com/PC/REST/API\">" \
               "<PostRunAction>Collate And Analyze</PostRunAction>" \
               "<ReleaseTimeslot>true</ReleaseTimeslot></PostRunActions>"

        url = "http://{}/LoadTest/rest/domains/{}/projects/{}/Runs/{}/stop".format(
            self.ip, self.domain, self.project_name, self.run_id)
        try:
            response = requests.post(url, data=data, headers=header, cookies=self.au_cookies)
        except requests.exceptions.RequestException as error:
            print(error)
        else:
            print(response.status_code)
            print(response.headers)
            print(response.text)


if __name__ == '__main__':
    STOP = StopTest(93).stop()










