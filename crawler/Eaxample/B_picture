'''
时间：2018/9/26
作者：楼浩然
功能：爬虫爬取B站图片
'''

import requests
import json
import os
os.chdir("Graph");
URL = "https://api.vc.bilibili.com/link_draw/v1/doc/detail?doc_id="
start = 1245574;
a = [];
for i in range(10):
    start += i;
    url = URL + str(start);
    req = requests.get(url).json();
    try:
        t = req["data"]["item"]['pictures'];
        for item in t:
            a.append(item["img_src"]);
    except:
        continue;
for i in a:
    res = requests.get(i);
    with open(i[-10:-1],'wb') as f:
        f.write(res.content);
