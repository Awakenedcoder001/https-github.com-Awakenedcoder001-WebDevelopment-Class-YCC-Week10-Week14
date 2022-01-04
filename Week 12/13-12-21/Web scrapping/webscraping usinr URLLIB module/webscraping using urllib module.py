import urllib.request 
 
if __name__== '__main__': 
 data=urllib.request.urlopen('http://data.pr4e.org/romeo-full.txt') 
 for i in data: 
  print(i.decode().strip())