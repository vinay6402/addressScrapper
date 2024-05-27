import requests, re

def scrap_site(addr):
    print("\033[92m" + "✓ Metadata Scrapper started!" + "\033[0m")
    response = requests.get(addr, timeout=5)
    # list of all metadata
    meta_tags = re.findall(r'<meta\s+([^>]+)>', response.text)
    meta_tags_list = []
    for tag in meta_tags:
        meta_dict = {}  # initialise dict for each meta for extraction of attribute value pairs
        # Extract attributes and values from each metadata
        each_meta = re.findall(r'(\S+)=["\']?((?:.(?!["\']?\s+(?:\S+)=|[>"\']))+.)["\']?', tag)
        # attributes and values to dict
        for attribute, value in each_meta:
            meta_dict[attribute] = value
        # Append the dictionary to the list
        meta_tags_list.append(meta_dict)
    print("\033[93m"+f"Metadata of {addr}: "+"\033[0m")
    for meta_dict in meta_tags_list:
        # Print each dictionary in the desired format
        for key, value in meta_dict.items():
            print("\033[91m" + f"{key}: " + "\033[92m" + f"{value}" + "\033[0m")
        print()  # Add an empty line after each meta tag
