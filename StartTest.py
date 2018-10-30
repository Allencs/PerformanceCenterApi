from PerformanceCenter import PerformanceCenter
import requests
from Authenticate import Authenticate
import json


class StartTest(PerformanceCenter):
    au_cookies = Authenticate().authenticate

    def __init__(self, test_id, instance_id, hours, minutes):
        super().__init__()
        self.test_id = test_id
        self.instance_id = instance_id
        self.hours = hours
        self.minutes = minutes

    def start(self):
        start_info = {}
        header = {'Content-Type': 'application/xml'}
        data = "<Run xmlns=\"http://www.hp.com/PC/REST/API\"><PostRunAction>Collate And Analyze</PostRunAction>" \
               "<TestID>{}</TestID><TestInstanceID>{}</TestInstanceID><TimeslotDuration>" \
               "<Hours>{}</Hours><Minutes>{}</Minutes></TimeslotDuration>" \
               "<VudsMode>false</VudsMode></Run>".format(self.test_id, self.instance_id, self.hours, self.minutes)

        url = "http://{}/LoadTest/rest/domains/{}/projects/{}/Runs".format(self.ip, self.domain, self.project_name)
        try:
            response = requests.post(url, data=data, headers=header, cookies=self.au_cookies)
        except requests.exceptions.RequestException as error:
            print(error)
        else:
            location = response.headers["Location"]
            run_id = location[-2:]
            start_info["RunID"] = run_id
            return json.dumps(start_info, sort_keys=False, indent=4)


if __name__ == '__main__':
    NEWTEST = StartTest(13, 6, 0, 30).start()
    print(NEWTEST)

