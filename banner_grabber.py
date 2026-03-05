# This file Detects service banner
import socket

def grab_banner(target, port):

    try:
        s = socket.socket()
        s.settimeout(2)
        s.connect((target, port))

        banner = s.recv(1024).decode().strip()

        return banner

    except:
        return None