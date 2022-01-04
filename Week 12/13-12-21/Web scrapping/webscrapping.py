# http://data.pr4e.org/ 
# http://data.pr4e.org/romeo-full.txt 
import socket 
 
if __name__== '__main__': 
 try: 
  client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  print(f"CLIENT SOCKET IS CREATED") 
 
  server_ipaddress='data.pr4e.org' 
  port_no=80 
  address=(server_ipaddress,port_no) 
  client_socket.connect(address) 
  print(f"CLIENT GOT CONNECTED TO THE SERVER") 
 
  client_socket.send("GET http://data.pr4e.org/romeo-full.txt HTTP/1.0\r\n\r\n".encode()) 
  print(f"CLIENT HAS SENT THE REQUEST TO THE SERVER") 
 
  bufsize=2048 
 
  while True: 
   data=client_socket.recv(bufsize) 
 
   if len(data)<1: 
    break; 
 
   print(data.decode()) 
 
 except socket.error as msg: 
  print(f"THE CAUSE OF THE EXCEPTON IS : {msg}") 
 
 except socket.gaierror as msg: 
  print(f"THE CAUSE OF THE EXCEPTON IS : {msg}") 
 
 except Exception as msg: 
  print(f"THE CAUSE OF THE EXCEPTON IS : {msg}") 
 
 
 else: 
  print(f"INFORMATION IS GATHERED FROM THE SERVER") 
 
 finally: 
  client_socket.close() 
  print(f"CLIENT SOCKET IS CLOSED SUCCESSFULLY!!")