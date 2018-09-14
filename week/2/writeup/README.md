Writeup 2 - OSINT (Open Source Intelligence)
======

Name: Lauren Kosub
Section: 0102

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Lauren Kosub

## Assignment 2 writeup

### Part 1 (45 pts)

1.  Fred Krueger 

2.  Twitter handle is @kruegster1990 ->  Discovered by googling his username
    Has a reddit account -> Discovered by googling his username
    email is kruegster@tutanota.com -> found off of his website cornerstoneairlines.co

3.  142.93.118.186 -> Discovered by putting the cornerstoneairlines.co domain in this website: https://centralops.net/co/DomainDossier.aspx

4.  The /secret directory contains the flag CMSC389R-{fly_th3_sk1es_w1th_u5} (found by inspecting page source)
    The main page contagins the flag CMSC389R-{h1dden_fl4g_in_s0urce} (found by inspecting page source)
    I found the .git directory that has a COMMIT_EDITMSG that contain the flag CMSC389R-{y0u_found_th3_g1t_repo}

5.  142.93.117.193 links to the admin page, and I found this by going clicking on the admin tab

6.  142.93.118.186 has Apache httpd 2.4.18 and OpenSSH 7.2p2. Located in New York City, New York -> found on https://censys.io/ipv4/142.93.118.186
    142.93.117.193 has Apache httpd 2.4.18. Located in New York City, New York -> found on https://censys.io/ipv4/142.93.117.193

7. Ubuntu -> found on https://censys.io/ipv4/142.93.118.186

8.  CMSC389R-{y0u_found_th3_g1t_repo} -> .git/COMMIT_EDITMSG (got here using nmap on 142.93.118.186)
    CMSC389R-{c0rn3rstone-air-27670} -> after getting into the system with the 
        username and password, I found the /home/flight_records directory that 
        is full of files with flags in them. From OSINT, I found Fred's instagram, 
        and after a few pokemon photots I found three pictures that when put 
        together compromised this flight ticket from his bad malaysian flight 
        experience (which he tweeted about)

### Part 2 (55 pts)

Username: kruegster
Password: pokemon

After using nmap to find the port to be 1337, I determined 2 possible usernames
that fred could use in a professional setting: kruegster (from his work email) or admin
(a generic work username for someone with admin privledges). Then, I iterated through
rockyou.txt line by line and attempted both usernames with the line from the file (the
password). If the received data was not a "Fail!\n", then I printed the recieved data 
and the username and password I tried and I quit the function. From here I found the 
username to be kruegster and the password to be pokemon because eventually stub.py
printed "Success!\n" with the username and password that was used to yield that
success.

Something I tried after I found the user name and password was filtering the rockyou.txt file
by greping "poke", "pup", "dog" (based on his interests that I found by googling his twitter 
handle online) and funneling those results into a new password file to use in stub.py. This
approach was must faster than my previous approach and it yeield the same username and 
password.

