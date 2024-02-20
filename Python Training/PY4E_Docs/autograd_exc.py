# PY4E AUTOGRADER EXCERCISES
# By Roland Udvari
# 2024-02-14 (Happy Valentine's Day)


#===========PY4E AUTOGRADED TESTS==============

# def computepay(h, r):
#     if h > 40:
#         p = 40 * r + (h - 40) * r * 1.5
#     else:
#         p = h * r
#     return p
# ===================================================
# hrs = input("Enter Hours:")
# rate = input("Enter hourly rate: ")
# try:
#     h = float(hrs)
#     r = float(rate)
# except:
#     print('Invalid input. Use numbers only!')
# p = computepay(h, r)
# print(h, r)
# print("Pay", p)
#===========================================================
# largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#     if num == "done":
#         break
#     else:
#         try:
#             num = float(num)
#         except:
#             print('Invalid input')
#             continue
#     if largest == None or num > largest:
#         largest = num
#     elif smallest == None or num < smallest:
#         smallest = num
#     else:
#         continue
#
# print("Maximum", int(largest))
# print("Minimum", int(smallest))
#--------------------------------------------------------
# import re
# text = "X-DSPAM-Confidence:    0.8475"
# print(text[(-6):])
# num = re.findall('[0-9].\\S*', text)
# print(num)
# num2 = text.find('.')
# print(float(text[num2-1:]))
#============================================================
# Use the file name mbox-short.txt as the file name
# fname = input("Enter file name: ")
# fh = open(fname)
# count = 0
# total = 0
# for line in fh:
#     if not line.startswith("X-DSPAM-Confidence:"):
#         continue
#     else:
#         count += 1
#         sdline = line.strip()
#     # num = sdline[sdline.find(':')+1 : ]
#     # flnum = float(num.strip())
#     # num = float(line.strip()[line.strip().find(':') + 1 :])
#     total += float(line.strip()[line.strip().find(':') + 1 :])
# print('Average spam confidence:', total / count)

#============================================================
#fname = input("Enter file name: ")
# fh = open('romeo.txt')
# lst = list()
# for lines in fh:
#     lines.rstrip()
#     for word in lines.split() :
#         if not word in lst:
#             lst.append(word)
# print(sorted(lst))

#=========================================
# fname = input("Enter file name: ")
# if len(fname) < 1:
#     fname = "mbox-short.txt"
# fh = open(fname)
# count = 0
# for frmline in fh:
#     frmline = frmline.rstrip()
#     if frmline.startswith('From '):
#         count += 1
#         print(frmline.split()[1])
# print("There were", count, "lines in the file with From as the first word")
#======================================

# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)
# freq = dict()
# highval = 0
# for line in handle :
#     if line.rstrip().startswith('From ') :
#         text = line.split()
#         email = text[1]
#         if email not in freq :
#             freq[email] = 1
#         else :
#             freq[email] = freq.get(email, 0) + 1
# print(freq)
# for (key, maximum) in freq.items() :
#     if maximum > highval :
#         highval = maximum
#         highkey = key
# print(highkey, highval)

# =========================================
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)
# hrfrq = dict()
# lst = list()
# for frmline in handle :
#     if frmline.rstrip().startswith('From ') :
#         words = frmline.split()
#         for time in words :
#             if ':' in time :
#                 hrs = time.split(':')
#                 if hrs[0] not in hrfrq :
#                     hrfrq[hrs[0]] = 1
#                 else :
#                     hrfrq[hrs[0]] = hrfrq[hrs[0]] + 1
# for k, v in hrfrq.items() :
#     lst.append((k, v))
#     lst.sort()
# for frq in lst :
#     print(frq[0], frq[1])
#====================================================
import re
# name = input("Enter file:")
# if len(name) < 1:
#     name = "mbox-short.txt"
# handle = open(name)
# for line in handle :
#     words = line.rstrip()
#     if ':' in words :
#         frm = re.findall(':\\S', line)
#         print(frm)
#=====================================================

# import re
# handle = 'regex_sum_1974909.txt'
# file = open(handle).read()
# numbrs= [int(x) for x in re.findall('[0-9]+', file)]
# lstsum = sum(numbrs[:], 0)
# print(lstsum)
#
# ---------SAME AS----------
# print( sum( [ int(x) for x in re.findall('[0-9]+', open('regex_sum_1974909.txt').read())] ) )
#=======================================================

# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')
#
# mysock.close()
#==========================================================
# from urllib.request import urlopen
# #import urllib.request
# from bs4 import BeautifulSoup
#
# # Ignore SSL certificate errors
# import ssl
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = "http://py4e-data.dr-chuck.net/comments_1974911.html"
# html = urlopen(url, context=ctx).read()
# #html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, "html.parser")
#
# nbrs = 0
# for tag in soup('span'):
#     nbrs += int(tag.contents[0])
# print(nbrs)
#============================================================

# import  urllib.request, urllib.error, urllib.parse
# from bs4 import BeautifulSoup
# import ssl
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter URL: ')
# if len(url) < 1:
#     url = 'http://py4e-data.dr-chuck.net/known_by_Feden.html'
# cnt = input('Enter Count: ')
# pos = input('Enter Position: ')
# for x in range(int(cnt)) :
#     html = urllib.request.urlopen(url, context=ctx).read()
#     data = BeautifulSoup(html, 'html.parser')
#     tag = data('a')[int(pos) - 1]
#     url = tag.get('href', None)
#     print(tag)
# print(tag)
#===========================================================

# import  urllib.request, urllib.error, urllib.parse
# import ssl
# import xml.etree.ElementTree as ET
#
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter location: ')
# if len(url) < 1 :
#     url = "http://py4e-data.dr-chuck.net/comments_1974913.xml"
# print('Retreiving:', url)
# urlread = urllib.request.urlopen(url, context=ctx).read()
# print('Retreived', len(urlread), 'characters.')
# xmldata = ET.fromstring(urlread)
# count = xmldata.findall('comments/comment')
# cnt = 0
# for item in count :
#     cnt += int(item.find('count').text)
# print('Count:', len(count))
# print(cnt)
#===============================================================

# import  urllib.request, urllib.error, urllib.parse
# import ssl
# import json
#
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# url = input('Enter location: ')
# if len(url) < 1 :
#     url = "http://py4e-data.dr-chuck.net/comments_1974914.json "
# print('Retreiving:', url)
# urlread = urllib.request.urlopen(url, context=ctx).read()
# print('Retreived', len(urlread), 'characters.')
# xmldata = json.loads(urlread)
# cnt = 0
# for count in xmldata['comments'] :
#     cnt += count['count']
# print(cnt)
#======================================================================
#
# import urllib.request, urllib.parse
# import json
# import ssl
#
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'
# parms = dict()
# while True :
#     address = input('Enter location: ')
#     if not address or address == 'done' :
#         break
#     parms['q'] = address.strip()
#     url = serviceurl + urllib.parse.urlencode(parms)
#     print('Retreiving:', url)
#     uh = urllib.request.urlopen(url, context=ctx).read()
#     print('Retreived', len(uh), 'characters')
#     jsn = json.loads(uh)
#     print('Plus code:', jsn['features'][0]['properties']['plus_code'])
#=====================================================

# import sqlite3
#
# conn = sqlite3.connect('PY4E_CH15autograd.sqlite')
# cur = conn.cursor()
#
# cur.execute('DROP TABLE IF EXISTS Counts')
#
# cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
#
# fname = input('Enter file name: ')
# if (len(fname) < 1): fname = 'mbox.txt'
# fh = open(fname)
# for line in fh:
#     if not line.startswith('From:'): continue
#     pieces = line.split()
#     email = pieces[1]
#     org = email.split('@')[1]
#     cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
#     row = cur.fetchone()
#     if row is None:
#         cur.execute('''INSERT INTO Counts (org, count)
#                 VALUES (?, 1)''', (org,))
#     else:
#         cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
#                     (org,))
# conn.commit()
#
# sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC'
#
# for row in cur.execute(sqlstr):
#     print(str(row[1]), row[0])
#
# cur.close()
#=========================================================
#
# import sqlite3
#
# conn = sqlite3.connect('PY4E_CH15agrad2.sqlite')
# cur = conn.cursor()
#
# cur.executescript('''
# DROP TABLE IF EXISTS Artist;
# DROP TABLE IF EXISTS Album;
# DROP TABLE IF EXISTS Genre;
# DROP TABLE IF EXISTS Track;
#
# CREATE TABLE Artist (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );
#
# CREATE TABLE Genre (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );
#
# CREATE TABLE Album (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     artist_id  INTEGER,
#     title   TEXT UNIQUE
# );
#
# CREATE TABLE Track (
#     id  INTEGER NOT NULL PRIMARY KEY
#         AUTOINCREMENT UNIQUE,
#     title TEXT  UNIQUE,
#     album_id  INTEGER,
#     genre_id  INTEGER,
#     len INTEGER, rating INTEGER, count INTEGER
# );''')
#
# handle = open('tracks CH15/tracks/tracks.csv')
#
# # Beauty School Dropout,Various,Grease,48,100,239960,Soundtrack
# #   0                      1       2    3  4    5       6
#
# for line in handle:
#     line = line.strip();
#     pieces = line.split(',')
#     if len(pieces) < 5 : continue
#
#     name = pieces[0]
#     artist = pieces[1]
#     album = pieces[2]
#     count = pieces[3]
#     rating = pieces[4]
#     length = pieces[5]
#     genre = pieces[6]
#
#     # print(name, artist, album, count, rating, length, genre)
#
#     cur.execute('''INSERT OR IGNORE INTO Artist (name)
#         VALUES ( ? )''', ( artist, ) )
#     cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
#     artist_id = cur.fetchone()[0]
#
#     cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
#         VALUES ( ?, ? )''', ( album, artist_id ) )
#     cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
#     album_id = cur.fetchone()[0]
#
#     cur.execute('''INSERT OR IGNORE INTO Genre (name)
#         VALUES ( ? )''', (genre, ))
#     cur.execute('SELECT ID FROM Genre WHERE name = ? ', (genre, ))
#     genre_id = cur.fetchone()[0]
#
#     cur.execute('''INSERT OR REPLACE INTO Track
#         (title, album_id, len, rating, count, genre_id)
#         VALUES ( ?, ?, ?, ?, ?, ? )''',
#         ( name, album_id, length, rating, count, genre_id ) )
#     cur.execute('SELECT * FROM Track ORDER BY title')
#
# conn.commit()
#
# cur.execute('''
#     SELECT Track.title, Artist.name, Album.title, Genre.name
#     FROM Track JOIN Genre JOIN Album JOIN Artist
#     ON Track.genre_id = Genre.ID and Track.album_id = Album.id
#         AND Album.artist_id = Artist.id
#     ORDER BY Artist.name LIMIT 3
#             ''')
# ================================================================

