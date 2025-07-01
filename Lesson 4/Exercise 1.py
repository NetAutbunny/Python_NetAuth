from rich import print
with open('show_ip_int_brief.txt') as f:
    interface_ip = {}
    for line in f:
        parts = line.split()
        if len(parts) > 1 and parts[1] != 'unassigned':
            interface = parts[0]
            ip_address = parts[1]
            interface_ip[interface] = ip_address

    print()
    print(interface_ip)
    print()