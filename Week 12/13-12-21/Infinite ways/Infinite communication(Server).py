if __name__== '__main__': 
 try: 
  server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  print(f"SERVER SOCKET IS CREATED") 
 
  server_ipaddress='localhost' 
  port_no=9999 
  address=(server_ipaddress,port_no) 
  server_socket.bind(address) 
  print(f"SERVER SOCKET IS BINDED TO PORT NO : {port_no}") 
 
  backlog=5 
  server_socket.listen(backlog) 
  print(f"SERVER SOCKET IS LISTENING TO : {backlog} REQUETS") 
   
  client_access,(client_ipaddress,client_portno)=server_socket.accept() 
  print(f"THE CLIENT INFO IS :") 
  print(f"{client_access}") 
  print(f"THE CLIENT COMPUTER NAME IS : {client_ipaddress} WITH PORT NO : {client_portno}") 
 
  bufsize=2048 
  while True: 
   client_data=client_access.recv(bufsize).decode('utf-8') 
   print(f"THE MSG FORM THE CLIENT IS : {client_data}") 
 
   data=input(f"ENTER THE MESSAGE TO THE CLIENT :").encode('utf-8') 
   client_access.send(data) 
 
 except socket.error as msg: 
  print(f"THE CAUSE OF THE EXCEPTON IS : {msg}") 
 
 except Exception as msg: 
  print(f"THE CAUSE OF THE EXCEPTON IS : {msg}") 
  
 else: 
  print(f"DATA IS RECIEVD AND SENT SUCESSFULLY") 
 
 finally: 
  client_access.close() 
  print(f"CLIENT ACCESS CLOSED SUCCESFULLY")