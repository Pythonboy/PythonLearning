'''
时间：2018/9/26
作者：楼浩然
功能：爬取B站视频信息
'''

import requests
import json
import pandas as pd
import numpy as np
URL = "https://api.bilibili.com/x/web-interface/archive/stat?aid=";
start = 32143134;
vedio = {};

for i in range(100):
    u = start + i;
    url = URL + str(u);
    header = {};
    header["User-Agent"] = "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
    try:
        req = requests.get(url,headers = header,timeout = 10).json();
        for item in req['data'].keys():
            if item not in vedio:
                vedio[item] = [];
            vedio[item].append(req['data'][item]);
    except:
        continue;
data = pd.DataFrame(data = vedio);
d = data.sort_values(by="coin",ascending = False)
print(d.head())
