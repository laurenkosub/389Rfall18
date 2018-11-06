#!/usr/bin/env python
#-*- coding:utf-8 -*-

# importing a useful library -- feel free to add any others you find necessary
import hashlib
import string

# this will work if you place this script in your writeup folder
wordlist = open("../probable-v2-top1575.txt", 'r')

# a string equal to 'abcdefghijklmnopqrstuvwxyz'.
salts = string.ascii_lowercase

for word in wordlist:
    word = word.strip()
    for salt in salts:
        # do stuff
        password = salt + word
        pass_hash = hashlib.sha512(password.encode('utf-8')).hexdigest()
        for line in open("../hashes", 'r'):
            line = line.strip()
            if line == pass_hash:
                print("Salt: " + salt + ", Password: " + word)
