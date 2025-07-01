from rich import print
import re
with open("arista_show_ip_arp.txt") as file:
    output = file.read()
ip_addr = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
mac_addr = r"[\w.]*"
pattern = rf"^({ip_addr})\s+\S+\s+({mac_addr})\s+"
match = re.findall(pattern, output, flags=re.M)
output_dict = dict(match)
print(output_dict)