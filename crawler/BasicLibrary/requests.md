# Python3 requests模块详解

## requests库的七个主要方法
|方法|解释|
|:-:|:-:|
|request.request()|构造一个请求，支持以下各种方法|
|requests.get()|获取html的主要方法|
|requests.head()|获取html头部信息的主要方法|
|requests.post()|向html网页提交post请求的方法|
|requests.put()|向html网页提交put请求的方法|
|requests.patch()|向html提交局部修改的请求|
|requests.delete()|向html提交删除请求|
### requests.get()
```
r=requests.get(url,params,**kwargs)
```
- params : 字典或字节序列， 作为参数增加到url中,使用这个参数可以把一些键值对以?key1=value1&key2=value2的模式增加到url中
- data : 字典，字节序或文件对象，重点作为向服务器提供或提交资源是提交，，作为request的内容，与params不同的是，data提交的数据并不放在
url链接里， 而是放在url链接对应位置的地方作为数据来存储。，它也可以接受一个字符串对象
- headers : 字典是http的相关语，对应了向某个url访问时所发起的http的头i字段， 可以用这个字段来定义http的访问的http头，可以用来模拟任何
我们想模拟的浏览器来对url发起访问。
```
hd = {‘user-agent’: ‘Chrome/10’} 
r = requests.request(‘POST’, ‘http://python123.io/ws‘, headers=hd)
```
- timeout : 用于设定超时时间， 单位为秒，当发起一个get请求时可以设置一个timeout时间， 如果在timeout时间内请求内容没有返回， 将产生一
个timeout的异常
- proxies : 字典， 用来设置访问代理服务器

**response对象有以下属性**
|属性|说明|
|:-:|:-:|
|r.status_code|http请求的返回状态，若为200则表示请求成功|
|r.text|http响应内容的字符串形式，即返回的页面内容|
|r.encoding|从http header 中猜测的相应内容编码方式|
|r.apparent_encoding|从内容中分析出的响应内容编码方式（备选编码方式）|
|r.content|http响应内容的二进制形式|
```
>>> import requests
>>> r=requests.get("http://www.baidu.com")
>>> r.status_code
200
>>>  r.encoding
'ISO-8859-1'
>>> r.apparent_encoding
'utf-8'
>>> r.text
'<!DOCTYPE html>\r\n<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8>ipt> <a href=//www.baidu.com/more/ name=tj_briicon class=bri style="display: block;">æ\x9b´å¤\x9aäº§å\x93\x81</a> </div> </div> </div> <div id=ftCon> <div id=ftConw> <p id=lh> <a com/ class=cp-feedback>æ\x84\x8fè§\x81å\x8f\x8dé¦\x88</a>&nbsp;äº¬ICPè¯\x81030173å\x8f·&nbsp; <img src=//www.baidu.com/img/gs.gif> </p> </div> </div> </div> </body> </html>\r\n'
>>> r.encoding='utf-8'
>>> r.text
'<!DOCTYPE html>\r\n<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta chref=http://s1.bdstatic.com/r/www/cache/bdorz/baidu.min.css="h读</a>&nbsp; <a href=http://jianyi.baidu.com/ class=cp-feedback>意见反馈</a>&nbsp;京ICP证030173号&nbsp; <img src=//www.baidu.com/img/gs.gif> </p> </div> </div> </div> </body> </html>\r\n'

```
**requests库的异常**
注意requests库有时会产生异常，比如网络连接错误、http错误异常、重定向异常、请求url超时异常等等。所以我们需要判断r.status_codes是否是
200，在这里我们怎么样去捕捉异常呢？

这里我们可以利用r.raise_for_status() 语句去捕捉异常，该语句在方法内部判断r.status_code是否等于200，如果不等于，则抛出异常。

***通用框架***
```
try:
    r=requests.get(url,timeout=30)#请求超时时间为30秒
    r.raise_for_status()#如果状态不是200，则引发异常
    r.encoding=r.apparent_encoding #配置编码
    return r.text
except:
    return"产生异常" 

```

### requests.head()
```
>>> r=requests.head("http://httpbin.org/get")
 >>>r.headers
 {'Connection': 'keep-alive', 'Server': 'meinheld/0.6.1', 'Date': 'Mon, 20 Nov 2017 08:08:46 GMT', 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true', 'X-Powered-By': 'Flask', 'X-Processed-Time': '0.000658988952637', 'Content-Length': '268', 'Via': '1.1 vegur'}
 >>>r.text
 ""
```

### requests.post()
- 向url post一个字典
```
>>> payload={"key1":"value1","key2":"value2"}
>>> r=requests.post("http://httpbin.org/post",data=payload)
>>> print(r.text)
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "23", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.18.4"
  }, 
  "json": null, 
  "origin": "218.197.153.150", 
  "url": "http://httpbin.org/post"
}

```
- 向url post一个字符串，自动编码为data
```
>>>r=requests.post("http://httpbin.org/post",data='helloworld')
>>>print(r.text)
{
  "args": {}, 
  "data": "helloworld", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "10", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.18.4"
  }, 
  "json": null, 
  "origin": "218.197.153.150", 
  "url": "http://httpbin.org/post"
}

```

### requests.put()
```
>>> payload={"key1":"value1","key2":"value2"}
>>> r=requests.put("http://httpbin.org/put",data=payload)
>>> print(r.text)
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "key1": "value1", 
    "key2": "value2"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "23", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.18.4"
  }, 
  "json": null, 
  "origin": "218.197.153.150", 
  "url": "http://httpbin.org/put"
+
```

### requests.request()
requests.request()支持其他所有方法
requests.request(method,url,**kwargs)
- method : "GET" "HEAD" "POST" "PUT" "PATCH"
- url : 请求的网址
- kwarg : 控制访问的参数

















































