import socket
import threading

def connHandler(info, newsock):
    print(f"New connection: {src}")
    data = newsock.recv(4096)
    print(data.decode())
    
    # 2. Modify the line below to send the string across the socket newsock.
    # Be sure to encode that string. You do not need to change anything inside of the quotation marks.
    
    # "HTTP/1.1 200 OK\r\n\r\n<html>Hello <b> World </b></html>\r\n"

    # 3. What can you say about HTTP traffic, html, and all other layer-7 network traffic?

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 5555))
    s.listen(5)
    while True:
        conn, src = s.accept()
        
        # 1. Uncomment and modify the line below to create a threat t which spawns a new thread to run the connHandler function.
        # Be sure to pass in the arguments in the correct order
        
        # t = threading.Thread(target = , args=( , ))
        
        t.start()
