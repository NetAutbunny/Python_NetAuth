with open("show_ip_int_brief.txt") as f:
    for line in f:
        if "10.220" in line:
            fields = line.split()
            intf_name = fields[0]
            ip_addr = fields[1]

print(f"Interface_name: {intf_name}")
print(f"IP_address: {ip_addr}")


