#  THIS HANDLES CLI ARGUMENTS AND STARTS THE SCAN
import argparse
from scanner import scan_ports
from utils import resolve_target

parser = argparse.ArgumentParser(description="Python Multithreaded Port Scanner")

parser.add_argument("-t", "--target", required=True, help="Target IP or domain")
parser.add_argument("-p", "--ports", default="1-1000", help="Port range (example: 1-1000)")
parser.add_argument("-th", "--threads", default=100, type=int, help="Number of threads")

args = parser.parse_args()

target = resolve_target(args.target)

start_port, end_port = map(int, args.ports.split("-"))

print(f"\nScanning {target} from port {start_port} to {end_port}\n")

scan_ports(target, start_port, end_port, args.threads)