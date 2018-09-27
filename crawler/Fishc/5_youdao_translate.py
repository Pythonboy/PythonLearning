import requests
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
header = {"User-Agent":"Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
         "Host":"fanyi.youdao.com"}
response = requests.post("http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule",data = data,headers = header)   #data是post的时候需要传送的数据，只需要为字典格式即可
t = response.json();
print(t["translateResult"][0][0]['tgt'])
