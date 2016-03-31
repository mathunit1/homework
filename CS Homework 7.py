#Socket client example in python

import socket	#for sockets
import sys	#for exit

#create an INET, STREAMing socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print 'Failed to create socket'
	sys.exit()
	
print 'Socket Created'

host = 'gnarlygno.me';
port = 8888;

try:
	remote_ip = socket.gethostbyname( host )

except socket.gaierror:
	#could not resolve
	print 'Hostname could not be resolved. Exiting'
	sys.exit()

#Connect to remote server
s.connect((remote_ip , port))

print 'Socket Connected to ' + host + ' on ip ' + remote_ip

#Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n\r\n"

try :
	#Set the whole string
	s.sendall(message)
except socket.error:
	#Send failed
	print 'Send failed'
	sys.exit()

print 'Message test send successfully'

#Now receive data

advisory = s.recv(4096)

#find two dynamic numbers in “Convert (234) from base 10 to base (16)”

int firstParanOpenIndex = advisory.index('(', beg=0, end=len(string));

int firstParanCloseIndex = advisory.index(')',beg=0, end=len(string));

	string numberTxt = advisory.Substring(firstParanOpenIndex, firstParanCloseIndex - firstParanOpenIndex);

	int firstNum = int.Parse(numberTxt);

	advisory = advisory.replace(firstParanOpenIndex, '' [,1]);

	advisory = advisory.replace(firstParanCloseIndex, ''[,1]);

int secondParanOpenIndex = advisory.index('(', beg=0, end=len(string));

int secondParanCloseIndex = advisory.index(')',beg=0, end=len(string));

string numberTxtSecond = advisory.Substring(secondParanOpenIndex, secondParanCloseIndex - secondParanOpenIndex);

int secondNum = int.Parse(numberTxtSecond);
if secondNum = 16 reply == hex(firstNum)
				s.sendall(replay)
		eslf secondNum = 2 reply == bin(firstNum)
				s.sendall(replay)
					esle reply == firstNum;
if advisor ="How to spell head TA name???" 
		s.sendall("Salsaman")
			elif advisor ="Yuh dunz it!!"
print(" I get it ")

s.close()

