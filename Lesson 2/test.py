base_addr = "192.168.254."
last_octet = 0

prefix_length = int(input("\nEnter a subnet prefix length(25-30): "))
subnet_size_bin = 32 - prefix_length
subnet_size = 2**subnet_size_bin
lost_hosts = 2  # network_number and broadcast
number_of_hosts = subnet_size - lost_hosts
first_address = f"{base_addr}1"
last_address = f"{base_addr}{number_of_hosts}"
first_subnet = f"{base_addr}0"
second_subnet = f"{base_addr}{subnet_size}"

print(f"Number of hosts: {number_of_hosts}")
print("\nSubnets:")
print(f" First subnet: {first_subnet}")
print(f" Second subnet: {second_subnet}")

print(f"\nFirst subnet: {first_subnet}")
print(f" First Host Address: {first_address}")
print(f" Last Host Address: {last_address}")