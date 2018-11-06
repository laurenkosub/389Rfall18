#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing useful libraries -- feel free to add any others you find necessary
import socket
import hashlib

host = "142.93.117.193"   # IP address or URL
port = 7331  # port

# use these to connect to the service
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# receive some data
data = s.recv(1024).decode("utf-8")

while "CMSC389R" not in data:
    data_arr = data.split()
    sha = data_arr[-5]
    new_data = data_arr[-2]
    if sha == "sha512":
        data_hash = hashlib.sha512(new_data.encode("utf-8")).hexdigest()
    elif sha == "sha384": 
        data_hash = hashlib.sha384(new_data.encode("utf-8")).hexdigest()
    elif sha == "sha224":
        data_hash = hashlib.sha224(new_data.encode("utf-8")).hexdigest()
    elif sha == "sha256":
        data_hash = hashlib.sha256(new_data.encode("utf-8")).hexdigest()
    elif sha == "sha1":
        data_hash = hashlib.sha1(new_data.encode("utf-8")).hexdigest()
    elif sha == "md5":
        data_hash = hashlib.md5(new_data.encode("utf-8")).hexdigest()
    s.send(bytes(data_hash + '\n', 'utf-8'))
    data = s.recv(1024).decode("utf-8")    
print(data)

# close the connection
s.close()
