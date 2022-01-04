import socket

if __name__ == '__main__':
 server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 print("SOCKET IS CREATED SUCCESSFULLY")

 ipaddress='localhost'
 port_no=9999
 address=(ipaddress,port_no)
 
 server_socket.bind(address)
 print(f"SERVER SORCTEK IS BINDED TO THE COMPUTER : {ipaddress}")
 print(f"THE PORT NO OF THE PROGRAM IS : {port_no}")