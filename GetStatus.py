from PerformanceCenter import PerformanceCenter
import requests
import test_xml.etree.ElementTree as ET
from Authenticate import Authenticate
import json


class GetStatus(PerformanceCenter):
    au_cookies = Authenticate().authenticate

    def __init__(self, run_id):
        self.run_id = run_id

    @property
    def get_status_xml(self):
        print(self.au_cookies)
        url = "http://" + self.ip + "/LoadTest/rest/domains/{}/projects/{}/Runs/{}".format\
            (self.domain, self.project_name, self.run_id)
        response = requests.get(url, cookies=self.au_cookies)
        return response.text

    def status_info(self, args):
        run_info = {}
        tree = ET.fromstring(self.get_status_xml)
        count = 0
        for node in ['TestID', 'TestInstanceID', 'PostRunAction',
                     'TimeslotID', 'VudsMode', 'ID', 'Duration', 'RunState', 'RunSLAStatus']:
            run_info[node] = tree[count].text
            count += 1
        if args == 0:
            return json.load(run_info)
        else:
            return run_info[args]


if __name__ == '__main__':
    pass