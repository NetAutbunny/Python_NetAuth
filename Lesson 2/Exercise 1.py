base_addr = '192.168.254.'
prefix_Length = int(input('\nEnter a prefix length between 25 to 30: '))
subnet_size = 2 ** (32 - prefix_Length)
host_allowed = subnet_size -2
First_subnet = base_addr + '0'
Second_subnet = base_addr + str(subnet_size)
First_addr = f"{base_addr}1"
Last_addr = f"{base_addr}{host_allowed}"
print(f'\nHosts in the subnet : {host_allowed}')
print(f'\nThe first subnet is : {First_subnet}')
print(f'\nThe second subnet is : {Second_subnet}')
print(f'\nFirst Host Address: {First_addr}')
print(f'\nLast Host Address: {Last_addr}')


