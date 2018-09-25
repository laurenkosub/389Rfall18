Writeup 3 - Pentesting I
======

Name: Lauren Kosub
Section: 0102

I pledge on my honor that I havie not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: Lauren Kosub

## Assignment 4 Writeup

### Part 1 (45 pts)
flag = CMSC389R-{p1ng_as_a_$erv1c3}
input = ; cat /home/flag.txt

thought process = Fred's new solution is utilizing the command line, so I figured that I would be able to
terminate his command he was executing (ping) with a semi colon, then append whatever commands I wanted
after the semicolon, and those commands would execute in his system (instead of ping because ping was
terminated by the semicolon).

After looking at the Fred's script (/opt/container_startup.sh), I think that to prevent this vulnerability fred
could limit the input to one word (instead of just any string of input) or more precisely one ip-like string
(no spaces, nothing besides numbers and periods). Fred could also just have a check in his script to see if the input was proper ping input. You shouldn't just arbitarily execute it.

Another way you can protect against malicious users is ensure that the input does not contain any semi-colons, back ticks, or other characters that serve the same function (to end a previous command or insert code into it). You can use black listing or you could escape bad character.

### Part 2 (55 pts)
see my stub.py for the interactive shell

