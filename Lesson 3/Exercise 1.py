base_addr = '192.168.254'
first_octet = '192.168.254.0'
prefix_length = int(input('Enter any length between 25 to 30: '))
subnet = 32 - prefix_length
subnet_size = 2 ** subnet
hosts = subnet_size - 2
number_of_subnets = 256 // subnet_size
print(f'Number of hosts : {hosts}')
for x in base_addr:
    subnet_numbers = base_addr
