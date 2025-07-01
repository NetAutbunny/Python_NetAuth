with open('junos_show_arp.txt') as f:
    bindings = [line.strip().split() for line in f if '0' in line]
    print(bindings)
    mac = [binding[0].replace(':', '_') for binding in bindings]
    ip = [binding[1] for binding in bindings]

    for ip, mac in zip(ip, mac):
        print(f'{ip} --> {mac}')