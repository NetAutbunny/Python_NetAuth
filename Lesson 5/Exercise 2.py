import re
from rich import print
with open('show_ip_bgp_neighbors.txt') as f:
    output = f.read()
match1 = re.search(r'^BGP neighbor is (?P<bgp_neighbor_ip>\d+\.\d+\.\d+\.\d+)', output)
match2 = re.search(r'\sremote AS\s(?P<remote_as>\d\d)', output, re.MULTILINE)
match3 = re.search(r"^\s+BGP version\s(?P<bgp_version>\d)", output, re.MULTILINE)
match4 = re.search(r"\sremote router ID\s(?P<router_id>[\d\.]+)", output, re.MULTILINE)
match5 = re.search(r"^\s+BGP state = (?P<bgp_state>\S+),", output, re.MULTILINE)

BGP_Neighbor_IP = match1.group("bgp_neighbor_ip")
Remote_AS = match2.group("remote_as")
BGP_Version = match3.group("bgp_version")
Router_ID = match4.group("router_id")
BGP_State = match5.group("bgp_state")


print(f"BGP Neighbor IP: {BGP_Neighbor_IP}")
print(f"Remote AS: {Remote_AS}")
print(f"BGP Version: {BGP_Version}")
print(f"Router ID: {Router_ID}")
print(f"BGP State: {BGP_State}")

