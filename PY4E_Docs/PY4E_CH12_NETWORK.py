# PY4E CHAPTER 12 NETWORK
# By Roland Udvari
# Created 1-30-2024

#==============SOCKET LIBRARY===============
# import socket
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')
#     print(len(data))
# mysock.close()

#==============URLIB LIBRARY==============

# import urllib.request, urllib.parse, urllib.error
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# header = fhand.getheaders()
# print(header)
# for line in fhand :
#     print(line.decode().strip())

#==========BEAUTIFULSOUP==============

# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import re
# url = input('Enter web address: ')
# html = urllib.request.urlopen(url).read().decode()
#
#soup = BeautifulSoup(html, 'html.parser')
# tags = soup('a')
# for tag in tags:
#     print(tag.get('href', None))
#
# words = html.split()
# #print(words)
# for href in words:
#     if href.startswith('href'):
#        print(href[6:(-1)])
#        hrefcln = re.findall('"(\\S*)"', href)
#        print(hrefcln)