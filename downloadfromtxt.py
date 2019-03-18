#!/usr/bin/env python
# -*- coding: latin-1 -*-

'''
Download Urls From Txt File
(c) Benan Cetin - becetin AT gmail.com 
18.03.2019

NOTICE: You need to set the correct permissions to the folder before uploading.
'''

import os
import requests
import shutil

fileName= 'myfile.txt'
downDir = 'images/'

# check if the file exists.
if os.path.exists(fileName):
	print("File exist :"+fileName)
	print("Reading and Uploading")
	file = open(fileName, "r")
	for line in file:
			line = line.strip()
			req = requests.get(line,allow_redirects=False)
			open(line.split("/")[-1],'wb').write(req.content)
			shutil.move(line.split("/")[-1], downDir)
else:
	print("File does not exist :"+fileName);
