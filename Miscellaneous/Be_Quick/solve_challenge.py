#!/usr/bin/python
import socket as so
import re
s = so.socket()
host='127.0.0.1'
port=4444
s.connect((host, port))
banner = s.recv(1024)
print(banner)
pat1 = re.compile("'[A-Z]'")
chars = pat1.findall(banner)
pat2 = re.compile("[\w][\d]+")
times = pat2.findall(banner)
for i in range(len(chars)):
	chars[i] = chars[i].replace("'","")
	times[i] = int(times[i])
payload = (chars[0]*times[0]+chars[1]*times[1])
s.send(payload)
print(s.recv(1024))
s.close()
