import re
from rich import print
with open("aruba_cx_show_ipv6_intf.txt") as f:
    output = f.read()
    match = re.search(r"^Interface\s(\S+) is\s(\S+)\nAdmin state is\s?(\S+)\nIPv6 address:\n\s+([\w:/]+)", output, flags=re.M)
    if match:
        print(f"intf_name: {match.group(1)}")
        print(f"intf _state : {match.group(2)}")
        print(f"Admin state: {match.group(3)}")
        print(f"ipv6_addr: {match.group(4)}")

