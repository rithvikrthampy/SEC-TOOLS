from icmplib import ping
import argparse

def send_request(url):
    destination_ip = url
    result = ping(destination_ip, count=4, interval=0.2, timeout=1)
    if result.is_alive:
        print(f"Host {destination_ip} is reachable, Average RTT: {result.avg_rtt}ms")
    else:
        print(f"Host {destination_ip} is unreachable.")

def main():
    parser = argparse.ArgumentParser(description="A ping clone")
    parser.add_argument("url", type=str, help = "Give url to scan")
    args = parser.parse_args()
    send_request(args.url)

main()