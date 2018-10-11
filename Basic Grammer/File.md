# 读写文件
open()将会返回一个file对象，基本语法： **open(filename,mode)**  
```
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```
- filename : 是一个包含了访问的文件名称的路径字符串
- mode : 决定了打开文件的模式：只读，写入，追加等，默认文件访问模式为只读(r)
- buffering :设置缓冲
- encoding ： 一般为utf-8
- errors : 报错级别
- newline : 区分换行符
- colsefd : 传入的file参数类型

|mode|用途|
|:-:|:-:|
|r|以只读的方式打开文件，文件的指针将会放在文件的开头，为默认模式|
|rb|以二进制格式打开一个文件用于只读，文件指针会在文件的开头|
|r+|打开一个文件用于读写，文件指针将会在文件的开头|
|rb+|以二进制格式打开一个文件用于读写，文件指针会放在文件的开头|
|w|打开一个文件用于写入，如果该文件已存在则将会覆盖文件，如果不存在则创建新文件|
|wb|以二进制打开一个文件用于写入|
|w+|打开一个文件用于读写|
|wb+|以二进制格式打开一个文件用于读写，如果文件存在则覆盖，如果不存在则创建新文件|
|a|打开一个文件用于追加内容，如果文件已存在，文件指针会放在文件的结尾，如果不存在则创建新文件进行写入|
|ab|以二进制格式打开一个文件用于追加写入|
|a+|打开一个文件用于读写，如果该文件已存在，文件指针会放在结尾，文件打开时会是追加模式，该文件不存在则创建新文件|
|ab+|以二进制格式打开一个文件用于追加|

**Example**
```
>>> file = open('test1.py','w')  #以写模式打开文件
>>> file.write('hello python')
>>> file.flush()  #刷新文件内容
>>> file.read()   #文件不可读
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
io.UnsupportedOperation: not readable

>>> file = open('test1.py','r')  #以只读打开文件
>>> file.readline()  #读取一行文件内容
'hello python\n'
>>> file.readline()
'hello python\n'
>>> file.readline()
''
>>> file.close()   #关闭文件
```

# 文件对象的方法
**f.read() ： 读取一个文件的内容**
```
>>> f = open('/etc/passwd','r')
>>> f.read(5)  #指定字节数读取   
'root:'
>>> f.read()   #读取文件全部内容
"root:x:0:0:root:/root:/bin/bash\nbin:x:1:1:bin:/bin:/sbin/nologin\ndaemon:x:2:2:daemon:/sbin:/sbin/nologin\nadm:x:3:4:adm:/var/adm:/sbin/nologin\nlp:x:4:7:lp:/var/spool/lpd:/sbin/nologin\nsync:x:5:0:sync:/sbin:/bin/sync\nshutdown:x:6:0:shutdown:/sbin:/sbin/shutdown\nhalt:x:7:0:halt:/sbin:/sbin/halt\nmail:x:8:12:mail:/var/spool/mail:/sbin/nologin\nuucp:x:10:14:uucp:/var/spool/uucp:/sbin/nologin\noperator:x:11:0:operator:/root:/sbin/nologin\ngames:x:12:100:games:/usr/games:/sbin/nologin\ngopher:x:13:30:gopher:/var/gopher:/sbin/nologin\nftp:x:14:50:FTP User:/var/ftp:/sbin/nologin\nnobody:x:99:99:Nobody:/:/sbin/nologin\ndbus:x:81:81:System message bus:/:/sbin/nologin\nvcsa:x:69:69:virtual console memory owner:/dev:/sbin/nologin\nabrt:x:173:173::/etc/abrt:/sbin/nologin\nhaldaemon:x:68:68:HAL daemon:/:/sbin/nologin\nntp:x:38:38::/etc/ntp:/sbin/nologin\nsaslauth:x:499:76:Saslauthd user:/var/empty/saslauth:/sbin/nologin\npostfix:x:89:89::/var/spool/postfix:/sbin/nologin\nsshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin\ntcpdump:x:72:72::/:/sbin/nologin\nvmail:x:5000:5000::/home/vmail:/sbin/nologin\napache:x:48:48:Apache:/var/www:/sbin/nologin\nmysql:x:27:27:MySQL Server:/var/lib/mysql:/bin/bash\nilanni:x:5001:5001::/home/ilanni:/bin/bash\ndovecot:x:97:97:Dovecot IMAP server:/usr/libexec/dovecot:/sbin/nologin\ndovenull:x:498:499:Dovecot's unauthorized user:/usr/libexec/dovecot:/sbin/nologin\n"
>>> f.close()
```

**f.readline() : 会从文件中读取单独的一行，换行符为“\n”，如果返回一个空字符串说明已经读到最后一行**
```
>>> f = open('/etc/passwd','r')
>>> f.readline()   #读取一行的内容
'root:x:0:0:root:/root:/bin/bash\n'
>>> f.readline()
'bin:x:1:1:bin:/bin:/sbin/nologin\n'
>>> f.readline()
'daemon:x:2:2:daemon:/sbin:/sbin/nologin\n'
>>> f.close()
```

**f.readlines(): 将会以列表的形式返回该文件中包含的所有行**
```
>>> f = open('/etc/passwd','r')
>>> f.readlines()   #读取所有行
['root:x:0:0:root:/root:/bin/bash\n', 'bin:x:1:1:bin:/bin:/sbin/nologin\n', 'daemon:x:2:2:daemon:/sbin:/sbin/nologin\n', 'adm:x:3:4:adm:/var/adm:/sbin/nologin\n', 'lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin\n', 'sync:x:5:0:sync:/sbin:/bin/sync\n', 'shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown\n', 'halt:x:7:0:halt:/sbin:/sbin/halt\n', 'mail:x:8:12:mail:/var/spool/mail:/sbin/nologin\n', 'uucp:x:10:14:uucp:/var/spool/uucp:/sbin/nologin\n', 'operator:x:11:0:operator:/root:/sbin/nologin\n', 'games:x:12:100:games:/usr/games:/sbin/nologin\n', 'gopher:x:13:30:gopher:/var/gopher:/sbin/nologin\n', 'ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin\n', 'nobody:x:99:99:Nobody:/:/sbin/nologin\n', 'dbus:x:81:81:System message bus:/:/sbin/nologin\n', 'vcsa:x:69:69:virtual console memory owner:/dev:/sbin/nologin\n', 'abrt:x:173:173::/etc/abrt:/sbin/nologin\n', 'haldaemon:x:68:68:HAL daemon:/:/sbin/nologin\n', 'ntp:x:38:38::/etc/ntp:/sbin/nologin\n', 'saslauth:x:499:76:Saslauthd user:/var/empty/saslauth:/sbin/nologin\n', 'postfix:x:89:89::/var/spool/postfix:/sbin/nologin\n', 'sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin\n', 'tcpdump:x:72:72::/:/sbin/nologin\n', 'vmail:x:5000:5000::/home/vmail:/sbin/nologin\n', 'apache:x:48:48:Apache:/var/www:/sbin/nologin\n', 'mysql:x:27:27:MySQL Server:/var/lib/mysql:/bin/bash\n', 'ilanni:x:5001:5001::/home/ilanni:/bin/bash\n', 'dovecot:x:97:97:Dovecot IMAP server:/usr/libexec/dovecot:/sbin/nologin\n', "dovenull:x:498:499:Dovecot's unauthorized user:/usr/libexec/dovecot:/sbin/nologin\n"]
>>> f.seek(0)   #跳指针到开头
>>> f.readlines(9)  #指定参数读取行
['root:x:0:0:root:/root:/bin/bash\n']
>>> f.readlines(9)
['bin:x:1:1:bin:/bin:/sbin/nologin\n']
>>> f.readlines(9)
['daemon:x:2:2:daemon:/sbin:/sbin/nologin\n']
>>> f.readlines(10)
['adm:x:3:4:adm:/var/adm:/sbin/nologin\n']
>>> f.readlines(1)
['lp:x:4:7:lp:/var/spool/lpd:/sbin/nologin\n']
>>> f.readlines()
['sync:x:5:0:sync:/sbin:/bin/sync\n', 'shutdown:x:6:0:shutdown:/sbin:/sbin/shutdown\n', 'halt:x:7:0:halt:/sbin:/sbin/halt\n', 'mail:x:8:12:mail:/var/spool/mail:/sbin/nologin\n', 'uucp:x:10:14:uucp:/var/spool/uucp:/sbin/nologin\n', 'operator:x:11:0:operator:/root:/sbin/nologin\n', 'games:x:12:100:games:/usr/games:/sbin/nologin\n', 'gopher:x:13:30:gopher:/var/gopher:/sbin/nologin\n', 'ftp:x:14:50:FTP User:/var/ftp:/sbin/nologin\n', 'nobody:x:99:99:Nobody:/:/sbin/nologin\n', 'dbus:x:81:81:System message bus:/:/sbin/nologin\n', 'vcsa:x:69:69:virtual console memory owner:/dev:/sbin/nologin\n', 'abrt:x:173:173::/etc/abrt:/sbin/nologin\n', 'haldaemon:x:68:68:HAL daemon:/:/sbin/nologin\n', 'ntp:x:38:38::/etc/ntp:/sbin/nologin\n', 'saslauth:x:499:76:Saslauthd user:/var/empty/saslauth:/sbin/nologin\n', 'postfix:x:89:89::/var/spool/postfix:/sbin/nologin\n', 'sshd:x:74:74:Privilege-separated SSH:/var/empty/sshd:/sbin/nologin\n', 'tcpdump:x:72:72::/:/sbin/nologin\n', 'vmail:x:5000:5000::/home/vmail:/sbin/nologin\n', 'apache:x:48:48:Apache:/var/www:/sbin/nologin\n', 'mysql:x:27:27:MySQL Server:/var/lib/mysql:/bin/bash\n', 'ilanni:x:5001:5001::/home/ilanni:/bin/bash\n', 'dovecot:x:97:97:Dovecot IMAP server:/usr/libexec/dovecot:/sbin/nologin\n', "dovenull:x:498:499:Dovecot's unauthorized user:/usr/libexec/dovecot:/sbin/nologin\n"]
>>>
```

**f.write() : 将内容写入到文件中，然后返回写入的字符数**
```
>>> f = open('test2.py','w')
>>> f.write('hello python')   #写入内容
>>> libex = 'hhhhhhhhhhhhhh'
>>> f.write(libex)   #按变量写入内容
>>> f.close()  #关闭文件
>>> 
[root@python day7]# cat test2.py   #内容没有换行符
hello pythonhhhhhhhhhhhhhh[root@python day7]#
```

**f.tell() : 返回文件对象当前所处的位置，它是从文件开头开始算起的字节数。**
```
>>> f = open('test2.py','r')
>>> f.tell()   #指针当前位置
>>> f.readline()   #读取一行文件后
'hello pythonhhhhhhhhhhhhhh'
>>> f.tell()   #指针移动26字节数处
>>> f.close()  #关闭文件
```

**f.seek() : 改变当前文件指针的位置，f.seek(offset,from_what)**
- from_what的值，如果是0表示开头，如果是1表示当前位置，2表示文件的结尾
1. seek(x,0):从文件首行首字符开始移动x个字符
2. seek(x,1):从当前为往后移动x个字符
3. seek(-x,2):从文件的结尾往前移动x个字符

```
>>> f = open('test3.py','a+')
>>> f.readlines()
[]
>>> f.seek(0)  #开头
>>> f.readlines()
['aaa\n', 'bbb\n', 'ccc\n', 'ddd\n', 'eee\n']
>>> f.tell()
```

**f.close() : 关闭文件并释放系统的资源**

**f.writelines() : 向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符**

**f.next() : 返回文件下一行**

**f.flush() : 刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入**




