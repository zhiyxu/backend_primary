# coding: utf-8

import socket

# socket 是操作系统用来进行网络通信的底层方案
# 简而言之, 就是发送 / 接收数据

# 创建一个 socket 对象
# 参数 socket.AF_INET 表示是 ipv4 协议
# 参数 socket.SOCK_STREAM 表示是 tcp 协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 这两个其实是默认值, 所以你可以不写, 如下
# s = socket.socket()
# s = ssl.wrap_socket(socket.socket())

# 主机(域名或者ip)和端口
# Here, host is only domain name, without port & address & https://
# so, http://movie.douban.com/top250 should only be movie.douban.com
host = 'movie.douban.com'
port = 80
# 用 connect 函数连接上主机, 参数是一个 tuple
s.connect((host, port))

# 连接上后, 可以通过这个函数得到本机的 ip 和端口
ip, port = s.getsockname()
print('本机 ip 和 port {} {}'.format(ip, port))
# 本机 ip 和 port 192.168.0.102 4961

# 构造一个 HTTP 请求
http_request = 'GET / HTTP/1.1\r\nhost:{}\r\n\r\n'.format(host)
# 发送 HTTP 请求给服务器
# send 函数只接受 bytes 作为参数
# str.encode 把 str 转换为 bytes, 编码是 utf-8
request = http_request.encode('utf-8')
print('request', request)
s.send(request)

# 接受服务器的响应数据
# 参数是长度, 这里为 1023 字节
# 所以这里如果服务器返回的数据中超过 1023 的部分你就得不到了
response = s.recv(1023)

# 输出响应的数据, bytes 类型
print('response', response)

# 转成 str 再输出
print('str format of response', response.decode('utf-8'))

'''
### example of response
'HTTP/1.1 301 Moved Permanently\r\n
Location: http://www.google.cn/\r\n
Date: Sat, 02 Dec 2017 07:33:03 GMT\r\n
Expires: Sat, 02 Dec 2017 07:33:03 GMT\r\n
Cache-Control: private, max-age=2592000\r\n
Content-Type: text/html; charset=UTF-8\r\n
Server: gws\r\n
Content-Length: 218\r\n
X-XSS-Protection: 1; mode=block\r\n
X-Frame-Options: SAMEORIGIN\r\n\r\n

<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">\n<TITLE>301 Moved</TITLE></HEAD><BODY>\n<H1>301 Moved</H1>\nThe document has moved\n<A HREF="http://www.google.cn/">here</A>.\r\n</BODY></HTML>\r\n')
'''