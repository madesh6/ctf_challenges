#!/usr/bin/python
import socket
import sys
import random
s = socket.socket()
port = 1337
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('',port))
s.listen(5)
while True:
	try:
		con, addr = s.accept()
		print("received a connection form : {0}:{1}".format(addr[0], addr[1]))
		chal=b"send '{0}' {1} times and '{2}' {3} times.\n"
		ch1 , ch2 = chr(random.randint(65, 90)), chr(random.randint(65, 90))
		n1 = random.randint(500, 700)
		n2 = random.randint(500, 700)
		chal =  chal.format(ch1, n1, ch2, n2)
		exp = ch1*n1+ch2*n2
		con.settimeout(4)
		con.send(chal)
		rep =  con.recv(1500)
		if (rep == exp):
			con.send(b"you won the challenge, here is the flag : DH{sKriPtiNg_iS_Funn} \n")
		else:
			con.send(b"try next time")
		con.close()
	except Exception as e:
		if (e == 'KeyboardInterrupt'):
			sys.exit(0)
		else:
			con.send(b"\nTimed out!!\n")
			con.close()
		pass
