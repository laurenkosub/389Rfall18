Writeup 7 - Forensics I
======

Name: Lauren Kosub
Section: 0102

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Lauren Kosub

## Assignment 7 writeup

### Part 1 (40 pts)

1. JPEG image

2. John Hancock Center 875 N Michigan Ave, Chicago, IL 60611 USA
   Long = 87 deg 37' 22.53" W 
   GPS Location = 41 deg 53' 54.87" N, 87 deg 37' 22.53" W

3. 2018:08:22 11:33:24

4. Apple iPhone 8 back camera 3.99mm f/1.8

5. 539.5 m Above Sea Level

6. CMSC389R-{look_I_f0und_a_string} 
   CMSC389R-{abr@cadabra}

### Part 2 (55 pts)

flag = CMSC389R-{dropping_files_is_fun}

First things first, I opened the binary in IDA to see what was going on in the
binary (see what it was doing and what data it had stored). The first thing I 
noticed was that there was data being first reveresed (probably to hide the 
data/prevent it from being readable via strings) then written to /tmp/.stego.
I then ran the binary (./binary) to see that it did indeed write something to a
file called .stego. By running the binary, I could not inspect the file via 
the command line.

After inspecting the file using file, strings, etc. I found nothing. Then
I did a hex dump of the file and it reminded me of the hex dump of the 
image file from part 1. I downloaded a random jpeg file to see if that too
had a simular hex dump and it did aside from the fact that the .stego file 
had an extra zero byte at the beginning of the file. There was an 
extraneous byte at the front of the .stego hex dump that needed to be removed!
I removed the 0 at the beginning of the .stego file and ran file on that to 
see that the .stego file was now a jpeg file! 

I opend the file to see that it was a picture of a stegosarus! (you can view 
the photo by opening the stego.jpg file in the writeup directory. I attempted 
to modify the saturation and coloring of the picture to see if I 
could find anything but I could not, After referring back to the notes, I 
decided to attempt to use steghide and guessed that the password was 
stegosarus because the picture itself was a jpeg of a stegosarous and I was
attempting to do steg, so I thought that it would be humorous for the 
oassword to be stegosaurus. Low and behold, the password was successful,
and the flag was written to a flag file. I was then able to cat said file
to find that the flag is CMSC389R-{dropping_files_is_fun}.
