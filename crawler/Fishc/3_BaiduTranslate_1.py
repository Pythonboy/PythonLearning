'''
时间：2018/9/21
作者：楼浩然
功能：爬虫爬取百度翻译中译英
'''

import urllib.request
import urllib.parse
import json
import time

print("爬虫爬取百度翻译中译英:\n")
while True:
    url = "https://fanyi.baidu.com/transapi";
    data = { };
    content = input("请输入翻译内容：\n");
    data["transtype"] = "translang";
    data["from"] = "zh";
    data["to"] = "en";
    data["query"] = content;
    data["simple_means_flag"] = 3;
    data["sign"] = "821806.551199";
    data["token"] = "9515995ea87b6e3381d030413da0b485";
    data = urllib.parse.urlencode(data).encode('utf-8');
    req = urllib.request.Request(url,data);
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36")
    response = urllib.request.urlopen(req);
    html = response.read().decode('utf-8');
    res = json.loads(html);
    print("翻译结果：\n%s"%(res["data"][0]["dst"]));
    t = input("是否继续:yes or no:\n");
    if t == 'no':
        break;
    time.sleep(1);
