from rich import print

with open('show_ip_int_brief.txt') as f:
    interfaces = {}
    for line in f:
        parts = line.split()
        if len(parts) > 1 and parts[0] != 'Interface':
            interface = parts[0]
            ip_addr = parts[1]
            line_status = parts[-2]
            line_protocol = parts[-1]
            interfaces[interface] = {
                'ip_addr': ip_addr,
                'line_status': line_status,
                'line_protocol': line_protocol
            }
print(interfaces)


