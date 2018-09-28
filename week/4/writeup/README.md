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
Fred's new solution is utilizing the command line, so I figured that I would be able to terminate his command he was executing (ping) with a semi colon, then append whatever commands I wanted after the semicolon, and those commands would execute in his system (instead of ping because ping was terminated by the semicolon).

After looking at the Fred's script (/opt/container_startup.sh), I think that to prevent this vulnerability fred could limit the input to one word (instead of just any string of input) or more precisely one ip-like string (no spaces, nothing besides numbers and periods). Fred could also just have a check in his script to see if the input was proper ping input. You shouldn't just arbitarily execute it.

Another way you can protect against malicious users is ensure that the input does not contain any semi-colons, back ticks, or other characters that serve the same function (to end a previous command or insert code into it). You can use black listing or you could escape bad character.

### Part 2 (55 pts)
My stub.py file was writen in python and can be run using python.

The task for part two was to implement an interactive shell that leverages the vulnerabilities discussed in part one. Mainly, the interactive shell levarages the open port (45) of cornerstoneairlines.co and after terminating the input for the ip with a semi colon runs a command and receives the output of said command. 

Due to the service only recieving one input on startup, the stub.py program needed to disconnect and reconnect for each command that the user entered into the interactive shell. The interactive shell displays as any other shell would (with a $), and it can conduct the following actions:

One input is "shell" which generates an interactive shell within this shell for users to enter bash commands within the cornerstone airlines system. For example, they could use this to access the flag stored by cornerstone airlines. Shell works by hitting the cornerstone airlines service and injecting each input to the newly spawned shell into the system using sockets. Since "shell" is simulating a real-time shell within the cornerstone airlines system, we need to track movement within the system even though we connect to the root directory each time we wish to execute a new command. To account for changing movement within the system the stub.py keeps track of what the current working directory is and before executing the command that the user input into the shell it moves to the directory that you were last in when you connected to the cornerstone airlines system in you last call to the service through the shell. If a user attempts to cd back to the system's home (root in this case), the user can simply enter "cd" in the shell, just as they would in a normal bash shell, and it will take them back to root. The shell also prevents users from cd ing to a directory that does not exist by checking that the directory exists before attempting to execute the command. If the directory does not exist then the cd will not execute and you will stay in whatever directory you were already in.

A second input option is "pull <remote-path> <local-path>" which
Downloads files (the remote path) onto your local machine (specifically the local path). Pull works by command injecting into the cornerstone airlines system. It only requires one socket connection (unlike shell), and the command injected take the following format: "; cat <remote-path>". This output is stored and then written to a file, specifically <local-path>. If the file does not exist, it needs to be created first.

A third input is "help", which will print a help menu that displays the four options for inputs to the interactive shell and the funcationality/purpose of each input. This help menu is simply a
string printed to stdout for the user to see.

The fourth and final input is "quit", which is the only way to exit the interactive shell.

If any other input (malinput) is entered into the interactive shell, then the shell will print "Invalid input. Use the help menu to see valid inputs", and it will prompt the user to enter a new correct input.

