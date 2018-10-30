import xml.sax
import json


class ResultMetaHandler(xml.sax.ContentHandler):
    run_info = {}
    count = 0

    def __init__(self):
        super().__init__()
        self.__content = ""
        self.__tag = ""

    def startElement(self, tag, attributes):
        self.__tag = tag

        if tag == "RunResult":
            # print("*******************")
            self.count += 1
            self.run_info["RunResult_{}".format(self.count)] = {}  # 创建多层字典，避免重复字段被覆盖

    def endElement(self, tag):  # 当到达指定节点是，打印相应的值
        if self.__tag == "ID":
            self.run_info["RunResult_{}".format(self.count)]['ID'] = self.__content

        elif self.__tag == "Name":
            self.run_info["RunResult_{}".format(self.count)]['Name'] = self.__content

        elif self.__tag == "RunID":
            self.run_info["RunResult_{}".format(self.count)]['RunID'] = self.__content

        elif self.__tag == "Type":
            self.run_info["RunResult_{}".format(self.count)]['Type'] = self.__content

        self.__tag = None

    def characters(self, content):  # 获取节点值
        self.__content = content

    @staticmethod
    def show_info():
        return ResultMetaHandler.run_info


class ParseResult(object):

    def __init__(self, source):
        self.source = source

    def get_metadata_info(self, args):
        # source = "D:\\sgmuserprofile\pt543f\\Desktop\\RunTest.xml"
        handler = ResultMetaHandler()
        # xml.sax.parse(self.source, handler)
        xml.sax.parseString(self.source, handler)
        if args == 0:
            return json.dumps(ResultMetaHandler.show_info(), sort_keys=False, indent=4)
        else:
            return ResultMetaHandler.show_info()[args]


if __name__ == '__main__':
    pass
