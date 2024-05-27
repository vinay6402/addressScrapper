import socket
from tqdm import tqdm


def url_to_ip(url):
    ip_address = socket.gethostbyname(url)
    return ip_address



def ipresolver(subdomain_list):
    print("\033[92m" + "✓ Domain to ip resolving started!" + "\033[0m")
    url_ip_pair = {}
    for f_url in tqdm(subdomain_list):
        url_ip_pair[f_url] = url_to_ip(str(f_url))
    for k,l in url_ip_pair.items():
        print("\033[92m" + "[✓] " + "\033[94m"+ f"{k}: {l}" + "\033[0m")
    return url_ip_pair