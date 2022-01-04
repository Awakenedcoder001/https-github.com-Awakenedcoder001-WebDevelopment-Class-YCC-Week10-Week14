import urllib.request 
 
if __name__== '__main__': 
 data=urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read() 
 with open('copy.jpg','wb') as file_write: 
  file_write.write(data)