Writeup 9 - Crypto I
=====

Name: Lauren Kosub
Section: 0102

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Lauren Kosub

## Assignment 9 Writeup

### Part 1 (60 Pts)
To bruteforce the hashes, I iterated through the wordlist, appended a salt to 
the the front of the word I was currently on (in the wordlist), hashed it and 
iterated through the hash file to see if the hashes matched up. If they did, 
I printed out the salt and password used and continued onward. For each word in
the wordlist I attempted salts a-z, hashed, and checked it. After doing so, I
discovered the four passwords in the hash file to be:

Salt: m, Password: jordan
Salt: u, Password: loveyou
Salt: k, Password: neptune
Salt: p, Password: pizza

Note: Make sure to run part1.py from the writeup folder. also, run part1.py 
using python3

### Part 2 (40 Pts)
CMSC389R-{H4sh-5l!ngInG-h@sH3r}

Seeing as the service kept asking for different hashing methods (sha512, md5, 
etc.), I needed a way to differentiate what hashing method to use, because the
python hashlib library has a different method call for each hashing algorithm.
To do this I pulled the hashing algorithm name from the initial output, then 
used a series of if elses to use the correct hashlib method. After submiting
one hash, I did the same for the next hash. I continued until CMSC389R (the 
beginning of the flag) was in the received data. From that, I got the flag.

Note: Use python3 to run part2.py
