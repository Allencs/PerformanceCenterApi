from PerformanceCenter import PerformanceCenter
import requests
<<<<<<< HEAD
import test_xml.etree.ElementTree as ET
=======
import xml.etree.ElementTree as ET
>>>>>>> PerfoermanceCenterApi
from Authenticate import Authenticate
import json


class GetStatus(PerformanceCenter):
    au_cookies = Authenticate().authenticate

    def __init__(self, run_id):
<<<<<<< HEAD
=======
        super().__init__()
>>>>>>> PerfoermanceCenterApi
        self.run_id = run_id

    @property
    def get_status_xml(self):
<<<<<<< HEAD
        print(self.au_cookies)
=======
>>>>>>> PerfoermanceCenterApi
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
<<<<<<< HEAD
            return json.load(run_info)
=======
            return json.dumps(run_info, sort_keys=False, indent=4)
>>>>>>> PerfoermanceCenterApi
        else:
            return run_info[args]


if __name__ == '__main__':
<<<<<<< HEAD
    pass
=======
    status = GetStatus(87).status_info(0)
    print(status)

>>>>>>> PerfoermanceCenterApi
