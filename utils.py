# Utility functions + colored output.
import socket
from colorama import Fore, Style

def resolve_target(target):

    try:
        return socket.gethostbyname(target)
    except:
        print("Unable to resolve target")
        exit()


def print_open_port(port, service, banner):

    print(
        f"{Fore.GREEN}[OPEN]{Style.RESET_ALL} "
        f"Port {port} | Service: {service} | Banner: {banner}"
    )