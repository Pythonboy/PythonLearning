import urllib.request

# urlopen打开对象为字符串
'''
response = urllib.request.urlopen("http://placekitten.com/g/500/600") #打开网址
img = response.read() #将二进制网址读取
with open('cat.png','wb') as f:
    f.write(img);  #将图片对象写入文件中

'''

# urlopen打开对象为Request对象
response = urllib.request.Request("http://placekitten.com/g/500/600")  
res = urllib.request.urlopen(response);
img = res.read()
with open('cat.jpg','wb') as f:
    f.write(img);
