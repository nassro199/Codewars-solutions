import re

def domain_name(url):
    # Matches the domain name without www. or http(s)://
    pattern = re.compile(r'(https?://)?(www\.)?([a-zA-Z0-9-]+)\.')
    matches = pattern.search(url)
    return matches.group(3)
