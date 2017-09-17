import socket 
import time

server_check = True

while(server_check):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('10.2.21.75',12345)) 
    # stringTosend = (str(input()))
    # s.send(stringTosend.encode())
    s.send('{}\r\n'.format(input()).encode())
    time.sleep(0.5) 
    msg=s.recv(1024)

    print(msg) 
    
    if(msg.decode()=='Thank you and good bye'):
        server_check = False

    s.close()
