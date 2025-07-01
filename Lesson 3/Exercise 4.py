
with open('show_ip_int_brief.txt') as f:
    ip_addresses = []
    interfaces = []
    for line in f:
      if '10' in line:
       line = line.strip()
       intf_name,ip_addr, *fields = line.split()
       ip_addresses.append(ip_addr)
       interfaces.append(intf_name)

print(f"Interface_name: {interfaces}")
print(f"IP_addresses: {ip_addresses}")




