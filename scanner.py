# THIS IS THE CORE SCANNING ENGINE
import socket
import threading
from queue import Queue
from banner_grabber import grab_banner
from services import get_service
from utils import print_open_port

queue = Queue()

def scan_port(target, port):

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            service = get_service(port)
            banner = grab_banner(target, port)

            print_open_port(port, service, banner)

        s.close()

    except:
        pass


def worker(target):

    while not queue.empty():
        port = queue.get()
        scan_port(target, port)
        queue.task_done()


def scan_ports(target, start_port, end_port, threads):

    for port in range(start_port, end_port + 1):
        queue.put(port)

    for _ in range(threads):
        t = threading.Thread(target=worker, args=(target,))
        t.start()

    queue.join()

    print("\nScan Complete")