'''
时间：2018/9/21
作者：楼浩然
功能：爬虫爬取百度翻译中英互译
'''

import urllib.request
import urllib.parse
import json
import time

language = {"English":"en","Chinese":"zh"};
print("请输入翻译的初始语言和预期语言:\n");
start = input("初始语言:\n");
end = input("预期语言：\n");
while True:
    url = "https://fanyi.baidu.com/transapi";

    # data内容直接复制过来，注意是字典格式，通过parse进行encode
    # 各种语言之间的翻译是通过"from" & "to"来控制的
    data = { };
    content = input("请输入翻译内容：\n");
    data["transtype"] = "translang";
    data["from"] = language[start];
    data["to"] = language[end];
    data["query"] = content;
    data["simple_means_flag"] = 3;
    data["sign"] = "384193.81904";
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
