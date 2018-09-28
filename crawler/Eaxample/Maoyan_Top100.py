'''
时间：2018/9/28
作者：楼浩然
功能：通过requests & re 实现爬取猫眼电影top100榜单信息
'''

import re
import requests
import numpy as np
import pandas as pd
pattern = re.compile('<p.*?name.*?title="(.*?)".*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?score.*?integer">(.*?)</i>.*?fraction">(.*?)</i>',re.S);
header = {"Uesr-Agent" : "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
         "Host" : "maoyan.com"};
res = [];
for i in range(10):
    offset = 10*i;
    payload = {"offset":str(offset)}
    html = requests.get("http://maoyan.com/board/4",params = payload,headers = header).text;
    info = re.findall(pattern,html);
    for item in info:
        temp = [];
        for i in item:
            temp.append(i.strip());
        res.append(temp);
df = pd.DataFrame(res,index = np.arange(1,101),columns = ["title","star","releasetime","score","faction"]);
df["score"] = df["score"] + df["faction"];
df.pop("faction")
print(df.head())
