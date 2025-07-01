from rich import print

with open('arubacx_show_vlan.txt') as f:
    vlan_int = {}
    for line in f:
        parts = line.split()
        if len(parts) > 1 and parts[0] != 'VLAN' and parts[0] != '----':
            try:
                vlan_id = int(parts[0])
                interfaces_str = parts[-1]
                interface_list = []
                for interface_range in interfaces_str.split(','):
                    if '-' in interface_range:
                        start, end = interface_range.split('-')
                        if '/' in start and '/' in end:
                            base = start.rsplit('/', 1)[0] + '/'
                            start_num = int(start.rsplit('/', 1)[1])
                            end_num = int(end.rsplit('/', 1)[1])
                            for i in range(start_num, end_num + 1):
                                interface_list.append(base + str(i))
                        elif 'lag' in start and 'lag' in end:
                            base = 'lag'
                            start_num = int(start.split('lag')[-1])
                            end_num = int(end.split('lag')[-1])
                            for i in range(start_num, end_num + 1):
                                interface_list.append(base + str(i))
                    else:
                        interface_list.append(interface_range)

                vlan_int[vlan_id] = interface_list
            except ValueError:
                pass

    print(vlan_int)