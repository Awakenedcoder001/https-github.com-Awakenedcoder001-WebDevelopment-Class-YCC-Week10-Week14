import socket 
 
if __name__=='__main__': 
 try: 
  client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  print(f"SERVER SOCKET IS CREATED") 
 
  server_ipaddress='localhost' 
  port_no=9999 
  address=(server_ipaddress,port_no) 
  client_socket.connect(address) 
  print(f"CLIENT SOCKET IS CONNETED TO SERVER SOCKET WITH NAME : {server_ipaddress} PORT NO : {port_no}") 
 
  while True: 
   data=input("ENTER THE MESSAGE TO THE SERVER :").encode("utf-8") 
   client_socket.send(data) 
 
   bufsize=2048 
   server_data=client_socket.recv(bufsize).decode('utf-8') 
   print(f"MESSAGE FROM THE SERVER IS : {server_data}") 
 
 except socket.error as msg: 
  print(f"THE CAUSE OF THE EXCEPTON IS : {msg}") 
 
 except Exception as msg: 
  print(f"THE CAUSE OF THE EXCEPTON IS : {msg}") 
  
 else: 
  print(f"THE DATA IS SENT SUCCESSFULLY AND RECIEVED THE MSG FROM THE SERVER") 
 finally: 
  client_socket.close() 
  print(f"CLIENT SOCKET CLOSED SUCCESFULLY")