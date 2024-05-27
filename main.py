# 1. scan a given website and get metadata details of the domain
# 2. related sub-domains
# 3. get details of the ipaddresses and ports within the domain
import internet_check as IC
import meta_scrapper as MS
import subdomain_enum as sde
import IPresolve as IPR
import port_scanner as PS

# --------------------Main Section--------------------------------

site_addr = "http://" + (input("Enter website address: "))
# section for metadata scrapper
if IC.internet_check() != "iok":
    quit()
else: MS.scrap_site(site_addr)

#section for Subdomain Enumerator
subdomain_list = sde.Subdomain_enumerator(site_addr)

#section for IP address resolution
domain_IP_list = IPR.ipresolver(subdomain_list)

#setion for port scanning
PS.scan_ports(domain_IP_list)