import socket
if __name__== '__main__': 
 try: 
  server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  print(f"SERVER SOCKET IS CREATED") 
 
  server_ipaddress='localhost' 
  port_no=9999 
 
  address=(server_ipaddress,port_no) 
  server_socket.bind(address) 
  print(f"SERVER SOCKET IS CREATED AND BINDED TO PORT NO : {port_no}") 
 
  backlog=5 
  server_socket.listen(backlog) 
  print(f"SERVER IS LISTENING TO {backlog} requests") 
 
  client_access,(client_ipaddress,client_portno)=server_socket.accept() 
  print(f"THE CLIENT INFORMATION IS : ") 
  print(f"{client_access}") 
 
  print(f"THE CLIENT COMPUTER NAME IS : {client_ipaddress} AND PORT NO IS : {client_portno}") 
 
  data="Hi!! Thazay How Are You !!".encode('utf-8') 
  client_access.send(data) 
 
 except socket.error as msg: 
  print(f"THE CAUSE OF THE EXCEPTON IS : {msg}") 
 
 except Exception as msg: 
  print(f"CAUSE OF THE EXCEPTON IS : {msg}") 
 
 else: 
  print(f"SERVER HAS SENT THE INFORMATION SUCESSFULLY!!") 
 
 finally: 
  client_access.close() 
  print(f"CLIENT ACCESS IS CLOSED !!")