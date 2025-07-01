import re
from rich import print
filename = "show_lldp.txt"
with open(filename) as f:
    lldp_data = f.read()

nbr_info = r"^Chassis id:.*?Vlan ID:\s+\w+\s+\w+"
match = re.findall(nbr_info, lldp_data, flags=re.DOTALL | re.M)
#print(match)

for line in match:
 m = re.search(r"System Name:\s+(.+)", line, flags = re.M)
 if m:
  print(f"System_Name: {m.group(1)}")

 m = re.search(r"Port id: (\S+)", line, flags=re.M)
 if m:
  print(f'Port_ID: {m.group(1)}')

 m = re.search(r"Local Port id:\s+(\S+)", line, flags=re.M)
 if m:
    print(f'Local_Port_ID: {m.group(1)}')