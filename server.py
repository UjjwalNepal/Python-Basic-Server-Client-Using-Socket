import socket

def main():
    host = '127.0.0.1'
    port = 5000
    s = socket.socket()
    s.bind((host,port))
    
    
    s.listen(1)
    print('server '+ str(host)+ 'is running at port: '+str(port))
    c,addr = s.accept()
    print("Connection from: "+ str(addr))
    while True:
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print("From Connected user: "+ data)
        data = data.upper()
        print("Sending: "+ data)
        c.send(data.encode('utf-8'))
    c.close()
    
if __name__ == "__main__":main()