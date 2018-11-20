Writeup 10 - Crypto II
=====

Name: *PUT YOUR NAME HERE*
Section: *PUT YOUR SECTION HERE*

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *PUT YOUR NAME HERE*

## Assignment 10 Writeup

### Part 1 (70 Pts)
CMSC389R-{i_still_put_the_M_between_the_DV}
message = 'deadbeef', malicious = 'SURPRISE'
Run python stub.py to get the flag above.

I used sockets to automate the sending and receiving from the server because it
decreased the back and forth between me, my code, and the server. To use this
I imported the socket library.

In step 1, one can calculate the forged hash by receiving the legit hash after
sending in the message (since every time you sign new data, you will regenerate
a new secret). Then I used the stub code provided to generate the fake_hash.

In step 2, I iterated through the potential lengths/sizes for secret, calulated
the number of zeros using the math in the provided slides. Then using this number
of zeros, I was able to construct the padding, which starts with '\x80', is followed
by the calculated number of zeros, as well as the message data. Then calculate the
payload and send it off to the server, checking to see if the server returned a
positive message and  flag with the format CMSC.

### Part 2 (30 Pts)
1. pgp --gen-key --> pub   rsa2048 2018-11-20 [SC] [expires: 2020-11-19]
      D077579C4AC5ECF1DC01204E9A933494176EDD9C
uid                      laurenkosub <lkosub@umd.edu>
sub   rsa2048 2018-11-20 [E] [expires: 2020-11-19]

2. gpg --import pgpassignment.key --> 
            gpg: key 9665C74E448C470E: public key "UMD Cybersecurity Club <president@csec.umiacs.umd.edu>" imported
            gpg: Total number processed: 1
            gpg:               imported: 1
3. gpg --sign-key president@csec.umiacs.umd.edu
4. gpg --encrypt --sign --armor -r lkosub@umd.edu msg.txt --> the ouput file is
   called msg.txt.asc
5. rename the msg.txt.asc file to be message.private as stated in the part 2
   description



