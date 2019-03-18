#!/usr/bin/env python
# -*- coding: latin-1 -*-

'''
Download Urls From Txt File
(c) Benan Cetin
18.03.2019

NOTICE: You need to set the correct permissions to the folder before downloading.
'''

import os
import requests
import shutil
import datetime

# File name that keeps urls to download
fileName= 'myfile.txt'
# The file to write logs.
fileLog = 'log.txt'
# Where the files will be downloaded.
downDir = 'images/'
i = 0
log = 'Number of downloaded file :'
if os.path.exists(fileName):
	print("File exist :"+fileName)
	print("Reading and Downloading")
	file = open(fileName, "r")
	for line in file:
			line = line.strip()
			req = requests.get(line,allow_redirects=False)
			open(line.split("/")[-1],'wb').write(req.content)
			shutil.move(line.split("/")[-1], downDir)
			i += 1
else:
	print("File does not exist :"+fileName);
	log = 'File does not exist. Downloaded :'
f = open(fileLog, "a")
time = datetime.datetime.now()
log = time.strftime("%Y-%m-%d %H:%M")+" "+fileName+": "+log+" "+str(i)+"\n"
print(log)
f.write(log)