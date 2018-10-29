import requests
import xml.etree.ElementTree as ET
import json


class PerformanceCenter(object):
    domain = "default"
    project_name = "PC"
    ip = "10.203.64.188"


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


class GetStatus(PerformanceCenter):
    au_cookies = Authenticate().authenticate

    def __init__(self, domain_name, project_name, run_id):
        self.domain_name = domain_name
        self.project_name = project_name
        self.run_id = run_id


    @property
    def get_status_xml(self):
        print(self.au_cookies)
        url = "http://" + self.ip + "/LoadTest/rest/domains/{}/projects/{}/Runs/{}".format\
            (self.domain_name, self.project_name, self.run_id)
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
        if args is None:
            return json.load(run_info)
        else:
            return run_info[args]


# status = GetStatus("default", "PC", "89")
# statusInfo = status.status_info("TestID")
# print(statusInfo)


class ResultMetadata(PerformanceCenter):
    au_cookies = Authenticate().authenticate

    def __init__(self, run_id):
        self.run_id = str(run_id)

    def get_result_info_xml(self):
        url = "http://{}/LoadTest/rest/domains/{}/projects/{}/Runs/{}/Results".format(
            self.ip, self.domain, self.project_name, self.run_id)
        response = requests.get(url, cookies=self.au_cookies)
        return response.text


class Result(PerformanceCenter):

    au_cookies = Authenticate().authenticate

    def __init__(self, run_id, result_id):
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


# result = Result(87, 1317).get_result

if __name__ == '__main__':
    # result = Result(87, 1317).get_data
    result_info = ResultMetadata(87).get_result_info_xml()
    print(result_info)









