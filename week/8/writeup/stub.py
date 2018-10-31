#!/usr/bin/env python2

import sys
import struct
import datetime

# You can use this method to exit on failure conditions.
def bork(msg):
    sys.exit(msg)

# helper method
def is_ascii(char_arr):
    ret = True
    for c in char_arr:
        if c < 0 and c > 127:
            return False
    return ret

# Some constants. You shouldn't need to change these.
MAGIC = 0xdeadbeef
VERSION = 1
PNGSIG = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'

if len(sys.argv) < 2:
    sys.exit("Usage: python2 stub.py input_file.fpff")

# Normally we'd parse a stream to save memory, but the FPFF files in this
# assignment are relatively small.
with open(sys.argv[1], 'rb') as fpff:
    data = fpff.read()

# Hint: struct.unpack will be VERY useful.
# Hint: you might find it easier to use an index/offset variable than
# hardcoding ranges like 0:8
magic, version = struct.unpack("<LL", data[0:8])

if magic != MAGIC:
    bork("Bad magic! Got %s, expected %s" % (hex(magic), hex(MAGIC)))

if version != VERSION:
    bork("Bad version! Got %d, expected %d" % (int(version), int(VERSION)))

timestamp = (struct.unpack("<L", data[8:12]))[0]
author = (data[12:20].decode("ascii"))
section = (struct.unpack("<L", data[20:24]))[0]

if int(section)<= 0:
    bork("Bad section! Got %d, expected number > 0", int(section))

print("------- HEADER -------")
print("MAGIC: %s" % hex(magic))
print("VERSION: %d" % int(version))
print("TIMESTAMP: " + str(datetime.datetime.fromtimestamp(int(timestamp))))
print("AUTHOR: " + str(author))
print("SECTION: %d" % int(section))

loc = 24
end = len(data)
i = 1

print("-------  BODY  -------")

while ((loc+8) <= end):
    stype, slen = struct.unpack("<LL", data[loc:(loc+8)])
    loc += 8
    slen_num = int(slen)
    
    if (slen_num > 0):
        t = int(stype)
        
        # PNG
        if t == 1:
            print("SECTION %d: STYPE = PNG (1)" % i)
            # dump png data to a file
            file_name = "pic" + str(loc) + ".png"
            with open(file_name, "wb") as binary_file:
                binary_file.write(PNGSIG)
                binary_file.write(data[loc:(loc+slen_num)])

            print("The png data was written to a file as \"%s\"" % file_name)
        
        #DWORDS
        elif t == 2:
            print("SECTION %d: STYPE = DWORDS (2)" % i)
            if ((slen_num % 8) == 0):
                svalue = struct.unpack("<" + "Q"*(slen_num/8), data[loc:(loc+(slen_num))])[0]
                print(str(int(svalue)))
        
        #UTF8
        elif t == 3:
            print("SECTION %d: STYPE = UTF8 (3)" % i)
            svalue = data[loc:(loc+slen_num)]
            try:
                print(svalue.decode('utf-8'))
            except UnicodeError:
                bork("Bad UTF8! Got %s but expected UTF-8 encoded text" % svalue)
        
        #DOUBLES
        elif t == 4:                    
            print("SECTION %d: STYPE = DOUBLES (4)" % i)
            if ((slen_num % 8) == 0):
                svalue = struct.unpack("<" +"d"*(slen_num/8), data[loc:(loc+slen_num)])[0]
                print(str(int(svalue)))
        
        #WORDS
        elif t == 5:         
            print("SECTION %d: STYPE = WORDS (5)" % i)
            if ((slen_num % 4) == 0):
                svalue = struct.unpack("<" + "L"*(slen_num/4), data[loc:(loc+slen_num)])[0]
                print(str(int(svalue)))
        
        #COORD
        elif t == 6 and slen_num == 16:  
            print("SECTION %d: STYPE = COORD (6)" % i)
            lng, lat = struct.unpack("<dd", data[loc:(loc+slen_num)])
            print("(%f, %f)" % (float(lng), float(lat)))

        #REFERENCE
        elif t == 7 and slen_num == 4:   
            print("SECTION %d: STYPE = REFERENCE (7)" % i)
            svalue = struct.unpack("<L", data[loc:(loc+slen_num)])[0]
            if (svalue < 0 or svalue > int(section)):
                bork("Bad Reference! %d was not within [0, nsects - 1]" % word)
            else:
                print(str(int(svalue)))
        
        #ASCII
        elif t == 9:
            print("SECTION %d: STYPE = ASCII (9)" % i)
            svalue = data[loc:(loc+slen_num)]
            if (is_ascii(svalue)):
                print(svalue.decode("ascii"))
            else:
                bork("Bad ASCII!")
        else:
            print("INVALID STYPE!")
        
        i += 1

    loc += slen_num
    print("\n")
    
