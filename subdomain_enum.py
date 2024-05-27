import requests
import tldextract
def Subdomain_enumerator(addr):
    print("\033[92m" + "✓ Subdomain enumerator started!" + "\033[0m")
    addr_extracted = tldextract.extract(addr)
    sld = addr_extracted.registered_domain #ex: google.com
    subdomain_list = []

    with open('sub_domain_names.txt', 'r') as file:
        lines = file.readlines()

    for line in lines:
        n_sd = "http://" + line.strip()+"."+sld
        try:
            response = requests.get(n_sd)
            if response.status_code == 200:
                subdomain_list.append(line.strip()+"."+sld)
                print("\033[92m" + "[✓] " + "\033[94m"+ n_sd + "\033[0m")
        except:
            pass
    return subdomain_list