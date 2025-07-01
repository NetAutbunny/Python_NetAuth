intf = "GigabitEthernet1       10.0.2.15       YES DHCP   up            up"
intf_fields = intf.split()
intf_name = intf_fields[0]
intf_ip_addr = intf_fields[1]
intf_status = intf_fields[4]
intf_protocol = intf_fields[5]

print("-" * 80)
print(f"intf_name: {intf_name}")
print(f"intf_ip_addr: {intf_ip_addr}")
print(f"intf_status: {intf_status}")
print(f"intf_protocol: {intf_protocol}")
print("-" * 80)

status_is_up = intf_status == "up"
protocol_is_up = intf_protocol == "up"
print()
print("-" * 80)
print(f"{status_is_up=}")
print(f"{protocol_is_up=}")
print("-" * 80)
print()