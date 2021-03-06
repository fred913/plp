# coding: utf-8
import waitress
import webapp
import socket

# ip = socket.gethostbyname(socket.gethostname())

print("服务启动，请在浏览器打开：")
for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
    print("http://%s/" % (ip, ))

try:
    waitress.serve(webapp.app, host="0.0.0.0", port=80, threads=9)
except PermissionError:
    print("检测到权限错误，运行在8080端口。请在浏览器打开：")
    for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
        print("http://%s:8080/" % (ip, ))
    waitress.serve(webapp.app, host="0.0.0.0", port=8080, threads=9)