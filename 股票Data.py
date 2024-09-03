import codecs
import json
import os
import time

import requests as requests

from datetime import date


class Run():
    # region 获取所有板块
    def Get_All_HQNodes(self):
        """
        获取所有得板块代码
        :return:
        """
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Cookie': 'U_TRS1=00000080.686c48f.5fa56a8e.983b4018; SINAGLOBAL=113.57.54.128_1604676239.610652; UOR=www.baidu.com,finance.sina.com.cn,; SFA_version7.0.0=2023-07-28%2018%3A30; SFA_version7.0.0_click=1; SR_SEL=1_511; SFA_version7.1.0=2023-08-23%2012%3A27; Apache=61.242.128.86_1692765123.746747; ULV=1692765125391:4:2:2:61.242.128.86_1692765123.746747:1692765118136; MONEY-FINANCE-SINA-COM-CN-WEB5=; U_TRS2=00000056.ef964d25a.64e594c2.44e5d767; hqEtagMode=1; close_rightAppMsg=1; FIN_ALL_VISITED=sz301170%2Cbj430418%2Cbj836221%2Cbj830896%2Cbj834058; rotatecount=10; FINA_V_S_2=sz301170'
        }
        UrlDataListName = 'https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodes'
        _List_Name = requests.get(url=UrlDataListName, headers=headers)
        Jons_List_NameData = json.loads(_List_Name.text)

        # print(Jons_List_NameData[1][0][1])
        # print(Jons_List_NameData[1][0])
        IsTrue: bool = False
        for n in range(0, len(Jons_List_NameData)):
            for m in range(0, len(Jons_List_NameData[n])):
                for j in range(0, len(Jons_List_NameData[n][m])):
                    # print(Jons_List_NameData[n][m][j])
                    if IsTrue:
                        IsTrue = False
                        for k in range(0, len(Jons_List_NameData[n][m][j])):
                            for u in range(0, len(Jons_List_NameData[n][m][j][k])):
                                # print(Jons_List_NameData[n][m][j][k][u])
                                if Jons_List_NameData[n][m][j][k][u] == '申万行业':
                                    pass
                                if Jons_List_NameData[n][m][j][k][u] == '申万一级':
                                    pass
                                if Jons_List_NameData[n][m][j][k][u] == '申万二级':
                                    pass
                                if Jons_List_NameData[n][m][j][k][u] == '申万二级':
                                    申万二级: dict = {}
                                    for w in range(0, len(Jons_List_NameData[n][m][j][k][u + 1])):
                                        key_in = Jons_List_NameData[n][m][j][k][u + 1][w][0]
                                        value_in = Jons_List_NameData[n][m][j][k][u + 1][w][2]
                                        申万二级.update({key_in: value_in})
                                    JsonUrl = './申万二级.json'
                                    fp = open(JsonUrl, 'w', encoding='utf-8')
                                    json.dump(申万二级, fp=fp, ensure_ascii=False)
                                    pass
                                if Jons_List_NameData[n][m][j][k][u] == '申万三级':
                                    _申万三级: dict = {}
                                    for w in range(0, len(Jons_List_NameData[n][m][j][k][u + 1])):
                                        key_in = Jons_List_NameData[n][m][j][k][u + 1][w][0]
                                        value_in = Jons_List_NameData[n][m][j][k][u + 1][w][2]
                                        _申万三级.update({key_in: value_in})
                                    JsonUrl = './申万三级.json'
                                    fp = open(JsonUrl, 'w', encoding='utf-8')
                                    json.dump(_申万三级, fp=fp, ensure_ascii=False)

                                if Jons_List_NameData[n][m][j][k][u] == '热门概念':
                                    pass
                                if Jons_List_NameData[n][m][j][k][u] == '概念板块':
                                    pass
                    if Jons_List_NameData[n][m][j] == 'A股':
                        IsTrue = True

                        # endregion

                        # region 大单

    def GetIP(self):
        while True:
            Url = 'http://pandavip.xiongmaodaili.com/xiongmao-web/apiPlus/vgl?secret=d65a1cd5eda2252df5e4993d1cd2198f&orderNo=VGL20231221235617wLELQ3rf&count=1&isTxt=0&proxyType=1&validTime=0&removal=0&cityIds='
            IP_Black = requests.get(url=Url)
            IPJson = IP_Black.json()
            IP = f"{IPJson['obj'][0]['ip']}:{IPJson['obj'][0]['port']}"
            proxies = {
                'http': IP,  # HTTP 代理服务器
                'https': IP  # HTTPS 代理服务器
            }
            try:
                IP_Black = requests.get(url='https://www.baidu.com/', proxies=proxies)
                if IP_Black.status_code == 200:
                    return IPJson
            except:
                pass

    # endregion

    # region 获取指定股票大单信息
    def Big_Order(self, gopiaocode: str):
        """
        获取指定股票大单信息
        :param gopiaocode:股票代码
        :return:
        """
        while True:
            try:
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                    'Referer': f'https://vip.stock.finance.sina.com.cn/quotes_service/view/cn_bill.php?symbol={gopiaocode}',
                    'Cookie': 'U_TRS1=00000080.686c48f.5fa56a8e.983b4018; SINAGLOBAL=113.57.54.128_1604676239.610652; UOR=www.baidu.com,finance.sina.com.cn,; SFA_version7.0.0=2023-07-28%2018%3A30; SFA_version7.0.0_click=1; SR_SEL=1_511; SFA_version7.1.0=2023-08-23%2012%3A27; Apache=61.242.128.86_1692765123.746747; ULV=1692765125391:4:2:2:61.242.128.86_1692765123.746747:1692765118136; MONEY-FINANCE-SINA-COM-CN-WEB5=; U_TRS2=00000056.ef964d25a.64e594c2.44e5d767; hqEtagMode=1; close_rightAppMsg=1; FIN_ALL_VISITED=sz301170%2Cbj430418%2Cbj836221%2Cbj830896%2Cbj834058; rotatecount=10; FINA_V_S_2=sz301170'
                }
                Big_Order_url = f'https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_Bill.GetBillList?symbol={gopiaocode}&num=60&page=1&sort=ticktime&asc=0&volume=40000&amount=0&type=0&day={date.today()}'
                # Big_Order_url = f'https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/CN_Bill.GetBillList?symbol={gopiaocode}&num=60&page=1&sort=ticktime&asc=0&volume=40000&amount=0&type=0&day=2023-12-21'
                Big_Order_data = requests.get(url=Big_Order_url, headers=headers, proxies=self.proxies1)
                if Big_Order_data.status_code != 200:
                    self.Updata_proxies()
                else:
                    break
            except:
                self.Updata_proxies()
        Json_Big_Order = json.loads(Big_Order_data.text)
        print(Json_Big_Order)

    # endregion
    proxies1 = {}

    def Updata_proxies(self):
        IPJson = self.GetIP()
        IP = f"{IPJson['obj'][0]['ip']}:{IPJson['obj'][0]['port']}"
        self.proxies1 = {
            'http': IP,  # HTTP 代理服务器
            'https': IP  # HTTPS 代理服务器
        }

    # region 获取指定板块下所有得股票代码
    def Get_HQNodes_List(self, Node: str, page=1):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            'Cookie': 'U_TRS1=00000080.686c48f.5fa56a8e.983b4018; SINAGLOBAL=113.57.54.128_1604676239.610652; UOR=www.baidu.com,finance.sina.com.cn,; SFA_version7.0.0=2023-07-28%2018%3A30; SFA_version7.0.0_click=1; SR_SEL=1_511; SFA_version7.1.0=2023-08-23%2012%3A27; Apache=61.242.128.86_1692765123.746747; ULV=1692765125391:4:2:2:61.242.128.86_1692765123.746747:1692765118136; MONEY-FINANCE-SINA-COM-CN-WEB5=; U_TRS2=00000056.ef964d25a.64e594c2.44e5d767; hqEtagMode=1; close_rightAppMsg=1; FIN_ALL_VISITED=sz301170%2Cbj430418%2Cbj836221%2Cbj830896%2Cbj834058; rotatecount=10; FINA_V_S_2=sz301170'
        }
        url = f'https://vip.stock.finance.sina.com.cn/quotes_service/api/json_v2.php/Market_Center.getHQNodeData?page={page}&num=80&sort=symbol&asc=1&node={Node}&symbol=&_s_r_a=init'
        while True:
            try:
                _getHQNodeData = requests.get(url=url, headers=headers, proxies=self.proxies1)
                if _getHQNodeData.status_code != 200:
                    self.Updata_proxies()
                else:
                    break
            except:
                self.Updata_proxies()
        _getHQNodeData_json = json.loads(_getHQNodeData.text)
        return _getHQNodeData_json

    # endregion  sw2_730200
    def PrCode(self):
        JsonUrl = './申万二级.json'
        with open(JsonUrl, 'r', encoding='utf-8') as file:
            # 使用json.load()加载JSON文件内容并保存到变量data中
            line = file.readline()
            ThreeData_Json = json.loads(line)
            for ThreeKey, ThreeValue in ThreeData_Json.items():
                ThreeKey_dic = []
                print(ThreeKey)
                # print(ThreeValue)

    # region 分类保存所有股票代码
    def saveCode(self):
        """
        更新股票代码
        :return:
        """
        # JsonUrl_申万三级 = './申万三级.json'
        JsonUrl_申万二级 = './申万二级.json'
        级别字典 = {}
        # 级别字典['申万三级分类股票'] = JsonUrl_申万三级
        级别字典['申万二级分类股票'] = JsonUrl_申万二级
        for n in 级别字典.keys():
            JsonUrl_申万 = 级别字典[n]
            with open(JsonUrl_申万, 'r', encoding='utf-8') as file:
                # 使用json.load()加载JSON文件内容并保存到变量data中
                line = file.readline()
                ThreeData_Json = json.loads(line)
                for ThreeKey, ThreeValue in ThreeData_Json.items():
                    ThreeKey_dic = []
                    print(ThreeKey)
                    print(ThreeValue)
                    RunBool = True
                    Page = 1
                    while RunBool:
                        ThreeKey_dic_New = self.Get_HQNodes_List(ThreeValue, Page)
                        if len(ThreeKey_dic_New) < 1:
                            RunBool = False
                        else:
                            ThreeKey_dic.extend(ThreeKey_dic_New)
                        Page += 1
                        # time.sleep(2)
                    ThreeKey_dic_w: dict = {}
                    for ThreeKey_w in ThreeKey_dic:
                        ThreeKey_dic_w.update({ThreeKey_w["symbol"]: ThreeKey_w["name"]})
                    JsonUrl = f'./{n}/{ThreeKey}.json'
                    fp = open(JsonUrl, 'w', encoding='utf-8')
                    json.dump(ThreeKey_dic_w, fp=fp, ensure_ascii=False)

    def read_json_files(self, folder):
        json_files = [file for file in os.listdir(folder) if file.endswith('.json')]
        # 循环读取json文件
        for file_name in json_files:
            file_path = os.path.join(folder, file_name)
            with open(file_path) as file:
                data = json.load(file)
                # 打印或处理数据
                print(data)

    # endregion
    def Get_TheOne_Code(self, CodeName="", Code=""):
        folder = 'D:\A开发\python项目\股票分析\申万三级分类股票'
        json_files = [file for file in os.listdir(folder) if file.endswith('.json')]
        # 循环读取json文件
        for file_name in json_files:
            file_path = os.path.join(folder, file_name)
            with codecs.open(file_path, 'r', 'utf-8') as file:
                data = json.load(file)
                if Code!="":
                    for Keys in data.keys():
                        if Code in Keys:
                            print(f"{Keys}---{data[Keys]}")
                            break
                if CodeName != "":
                    for Keys in data.keys():
                        if CodeName in data[Keys]:
                            print(f"{Keys}---{data[Keys]}")
                            break


R = Run()
R.Get_TheOne_Code(Code='600711')
