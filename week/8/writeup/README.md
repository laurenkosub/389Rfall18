Writeup 8 - Forensics II, Network Analysis and File Carving/Parsing
=====

Name: Lauren Kosub
Section: 0102

I pledge on my honor that I have not given or received anyunauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Lauren Kosub

## Assignment 8 Writeup

### Part 1 (45 Pts)
1. Yes, Cornerstone Airlines's Website (cornerstoneairlines.co)

2. c0uchpot4doz and laz0rh4x

3. laz0rh4x has an IP of 104.248.224.85, which appears to be connecting from North Bergen, New Jersey. c0uchpot4doz has an IP of 206.189.113.189, which appears to be connecting from London England. Locations were found using www.iplocation.net.

4. 2749

5. Tomorrow at 1500

6. https://drive.google.com/file/d/1McOX5WjeVHNLyTBNXqbOde7l8SAQ3DoI/view?usp=sharing

7. Tomorrow

### Part 2 (55 Pts)

*Report your answers to the questions about parsing update.fpff below.*
1. 2018-10-24 20:40:07

2. laz0rh4x

3. It says in the header that there are only 9 sections; however, after parsing
   the file, 11 sections were found

4. SECTION 1: STYPE = ASCII (9)
   Call this number to get your flag: (422) 537 - 7946

   SECTION 2: STYPE = WORDS (5)
   3

   SECTION 3: STYPE = COORD (6)
   (38.991610, -77.027540)

   SECTION 4: STYPE = REFERENCE (7)
   1 

   SECTION 5: STYPE = ASCII (9)
   The imfamous security pr0s at CMSC389R will never find this!

   SECTION 6: STYPE = ASCII (9)
   The first recorded uses of steganography Can be traced back to 440 BC when Herodotus Mentions two exampleS in his Histories.[3] Histicaeus s3nt a message to his vassal, Arist8goras, by sha9ving the hRead of his most trusted servan-t, "marking" the message onto his scal{p, then sending him on his way once his hair had rePrown, withl the inastructIon, "WheN thou art come to Miletus, bid _Aristagoras shave thy head, and look thereon." Additionally, demaratus sent a warning about a forthcoming attack to Greece by wrIting it dirfectly on the wooden backing oF a wax tablet before applying i_ts beeswax surFace. Wax tablets were in common use then as reusabLe writing surfAces, sometimes used for shorthand. In his work Polygraphiae Johannes Trithemius developed his so-called "Ave-Maria-Cipher" that can hide information in a Latin praise of God. "Auctor Sapientissimus Conseruans Angelica Deferat Nobis Charitas Gotentissimi Creatoris" for example contains the concealed word VICIPEDIA.[4}

   SECTION 7: STYPE = COORD (6)
   (38.991094, -76.932802)

   SECTION 8: STYPE = PNG (1)
   The png data was written to a file as "pic1286.png"

   SECTION 9: STYPE = ASCII (9)
   AF(saSAdf1AD)Snz**asd1

   SECTION 10: STYPE = ASCII (9)
   Q01TQzM4OVIte2gxZGQzbi1zM2N0MTBuLTFuLWYxbDN9

   SECTION 11: STYPE = DWORDS (2)
   4


5. CMSC389R-{c0rners0ne_airlin3s_to_the_m00n}
   CMSC389R-{h1dd3n-s3ct10n-1n-f1l3}
   CMSC389R-{PlaIN_DIfF_FLAG}

