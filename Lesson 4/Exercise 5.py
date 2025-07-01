from rich import print

with open('arubacx_show_vlan.txt') as f:
    vlan_int = {}
    for line in f:
        parts = line.split()
        if len(parts) > 1 and parts[0] != 'VLAN' and parts[0] != '----':
            try:
                vlan_id = int(parts[0])
                interfaces_str = parts[-1]
                interface_set = set()
                for interface_range in interfaces_str.split(','):
                    interface_range = interface_range.strip()
                    if '-' in interface_range:
                        start, end = interface_range.split('-')
                        if '/' in start and '/' in end:
                            base = start.rsplit('/', 1)[0] + '/'
                            start_num = int(start.rsplit('/', 1)[1])
                            end_num = int(end.rsplit('/', 1)[1])
                            for i in range(start_num, end_num + 1):
                                interface_set.add(base + str(i))
                        elif 'lag' in start and 'lag' in end:
                            base = 'lag'
                            start_num = int(start.split('lag')[-1])
                            end_num = int(end.split('lag')[-1])
                            for i in range(start_num, end_num + 1):
                                interface_set.add(base + str(i))
                    else:
                        interface_set.add(interface_range)

                vlan_int[vlan_id] = interface_set
            except ValueError:
                pass

    print(vlan_int)

    print()
    print("Section a: ")
    common_intf = vlan_int[1] & vlan_int[2] & vlan_int[3]
    print(f"Common interfaces in VLAN 1, 2, and 3: {common_intf}")
    print()

    print()
    print("Section b: ")
    all_interfaces = set.union(*vlan_int.values())
    print(f"All interfaces in all VLANs: {all_interfaces}")
    print()

    print()
    print("Section c: ")
    interface_12_13 = vlan_int[12] | vlan_int[13]
    print(f"Interfaces in VLAN 12 or 13: {interface_12_13}")
    print()
