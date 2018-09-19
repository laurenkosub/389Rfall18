Writeup 3 - OSINT II, OpSec and RE
======

Name: Lauren Kosub
Section: 0102

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Lauren Kosub

## Assignment 3 Writeup

### Part 1 (100 pts)

One vulnerability Fred has was that his service had an exposed port (1337). 
He should instead used ssh (Secure shell, on port 22) to access his service. 
SSH provides a secure channel over an unsecured network in a client-server 
architecture, connecting an SSH client application with an SSH server. SSH would
also alow Fred's website to blacklist failed attempts to connect to his server,
which would overall make it more secure and prevent people without access from 
attempting to brute force their way into his website. 

Additionally, Fred should not have put anything you want to be kept secret in robots.txt.
This allows anybody to see what should have been kept hidden. Website owners
can use robots.txt to give instructions about their site to web robots. Robots
can ignore your robots.txt, but the robots.txt file is publically available to
anybody on the internet. That means that anybody can see what sections of your 
server you don't want the robots to use. In other words, you shouldn't use 
robots.txt to hide information because it won't actually be hidden.

Lastlty, Fred Krueger had a weak password: pokemon. Your password
should be a combination of uppercase letters, lowercase letters, numbers, and
symbols. You are not supposed to use passwords that are based on interests or
are found in a dictionary; however, pokemon is one of his interests and the word
itself was found in the rockyou.txt file, which contains common passwords
and words found in the dictionary that could be used as passwords. I would suggest
that Fred use a more secure password such as a randomly generated string of
numbers , letters, and symbols. He could check his password on howsecureismypassword.net
to see if it is worthy of protecting his server.
