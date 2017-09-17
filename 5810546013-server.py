import socket
import datetime
import re
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('10.2.21.75',12345))
s.listen(1)
regex = re.compile(r'\d+, \d+, \W\r\n$')

while(True):
    sock,info = s.accept() 
    msg=sock.recv(1024) 
    print(msg)
    if(msg.decode()== 'LocalTime\r\n'):
        localt = datetime.datetime.fromtimestamp(time.time()).strftime('%I : %M %p') + "\n"
        sock.send(localt.encode())
    
    elif(regex.match(msg.decode())):
        operation = msg.decode().split()
        num1 = int(operation[0].replace(',', ''))
        num2 = int(operation[1].replace(',', ''))
        if(operation[2]=='+'):
            sock.send('{} + {} = {}\r\n'.format(num1,num2,num1+num2).encode())
        elif(operation[2]=='-'):
            sock.send('{} - {} = {}\r\n'.format(num1,num2,num1-num2).encode())
        else:
            sock.send(b'No Answer\r\n') 

    elif(msg.decode()=='Quit\r\n'):
        sock.send(b'Thank you and good bye\r\n') 
    else:
        sock.send(b'No Answer\r\n') 

time.sleep(0.3)

