import argparse
import socket
import shlex
import subprocess
import sys
import textwrap
import threading

def executeCommand(command) :
    cmd = command.strip()
    if not cmd :
        return
    output = subprocess.check_output(shlex.split(cmd),stderr=subprocess.STDOUT)
    return output.decode()

class NetCat(object):
    def __init__(self,args,buffer=None):
        pass
    def run(self):
        pass

def main():
    parser = argparse.ArgumentParser(
        description="BHP Net Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent(
            '''  Example:
            netcat.py -t 192.168.1.108 -p 7777 -l -c # command shell
            netcat.py -t 192.168.1.108 -p 7777 -l -u=mytest.txt # upload to file
            netcat.py -t 192.168.1.108 -p 7777 -l -e=\"cat /etc/passwd\" # excute command
            echo 'ABC' | ./netcat.py -t 192.168.1.108 -p 135 # echo text to server port 135
            netcat.py -t 192.168.1.108 -p 7777 # connect to server
            '''
            
        )
    )
    parser.add_argument('-c' , '--command' , action='store_true' , help='command shell')
    parser.add_argument('-e' , '--execution' , help='excute specified command')
    parser.add_argument('-l' , '--listen' , action='store_true' , help='listen')
    parser.add_argument('-p' , '--port' , type=int,default=7777 , help='specified port')
    parser.add_argument('-t' , '--target' , default='192.168.1.108' , help='specified IP')
    parser.add_argument('-u' , '--upload' , help = 'upload file')
    args = parser.parse_args()
    if args.listen:
        buffer = ''
    else:
        buffer = sys.stdin.read()
        
    nc = NetCat(args,buffer.encode())
    
    nc.run()
    
if __name__ == "__main__":
    main()