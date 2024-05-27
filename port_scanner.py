import socket
import threading

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print( f"{target} - Port {port} - " + "\033[92m" + "open" + "\033[0m" )
    except Exception as e:
        pass
    finally:
        sock.close()

def scan_ports(domain_ip_lists):
    subdomain_list = set(domain_ip_lists.keys())
    print("\033[92m" + "✓ Port scanner started!" + "\033[0m")
    for domain in subdomain_list:
        print("\033[94m",domain,"\033[0m")
        for port in range(1024):
            threading.Thread(target=scan_port, args=(domain_ip_lists.get(domain), port)).start()


