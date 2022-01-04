import socket 
if __name__== '__main__': 
 try: 
  client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
  print(f"CLIENT SOCKET IS CREATED") 
 
  client_ipaddress='localhost' 
  port_no=9999 
 
  address=(client_ipaddress,port_no) 
  client_socket.connect(address) 
  print(f"CLIENT GOT CONNECTED TO THE SERVER COMPUTER WITH NAME : {client_ipaddress} AND PORT NO : {port_no}") 
 
  bufsize=2048 
  data=client_socket.recv(bufsize).decode('utf-8') 
  print(f"THE DATA SENT FROM THE SERVER IS :{data}") 
 
 except socket.error as msg: 
  print(f"THE CAUISE OF THE EXCEPTION IS : {msg}") 
 
 except Exception as msg: 
  print(f"THE CAUSE OF THE EXCEPTON IS : {msg}") 
 
 else: 
  print(f"DATA RECIEVED FROM THE SERVER SUCCESSFULLY!!") 
 
 finally: 
  client_socket.close()