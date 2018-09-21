'''
时间： 2018/9/21
作者： 楼浩然
功能： 有道翻译
'''


import urllib.request
import urllib.parse
import json
import time

while True:
    #网址
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule";

    # 从Form data中直接获取的，直接copy的
    # data 是一个字典，之后需要通过urlencode进行编码
    # 添加data是为了将从“Get”转化为“Post”
    data = {};
    a = input("请输入需要翻译的内容：\n");
    data['i'] = a;
    data["from"] = "Auto";
    data["to"] = "Auto";
    data["smartresult"] = "0dict";
    data["client"] = "fanyideskweb";
    data["salt"] = "1537507121137";
    data["sign"] = "acaef0fbff86661570a5493dc3c868e1";
    data["doctype"] = "json";
    data["version"] = "2.1";
    data["keyfrom"] = "fanyi.web";
    data["action"] = "FY_BY_REALTIME";
    data["typoResult"] = "true";
    data = urllib.parse.urlencode(data).encode('utf-8');
    res = urllib.request.Request(url,data);

    # 目的是为了隐藏id，防止被黑
    # 直接复制黏贴User-Agent的内容
    res.add_header("Ueser-Agent","Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36");

    response = urllib.request.urlopen(res);

    # 输出json格式内容
    html = response.read().decode('utf-8');  # json格式，需要再处理
    target = json.loads(html);
    print("翻译结果：\n%s" % (target["translateResult"][0][0]["tgt"]));  #为了得到这个形式，可以提前print(html看看json输出格式

    t = input("是否继续：yes or no :\n");
    if t == 'no':
        break;
    time.sleep(1);  # 延迟5秒钟
