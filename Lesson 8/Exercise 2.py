from rich import print

# Creating a Router class with count initialized to 0 and all_hosts as a blank list.`
class Router:
    count = 0
    all_hosts = []

# Creating a router object that sets the host attribute and increments the count attribute that adds the
    # host to the all_hosts list.
    def __init__(self, host):
        self.host = host
        Router.count += 1
        Router.all_hosts.append(self.host)

# Creating four Router Objects
r1 = Router('rtr1')
r2 = Router('rtr2')
r3 = Router('rtr3')
r4 = Router('rtr4')

# Printing out count and all_hosts attributes
print(f"Total Routers: {Router.count}")
print(f"All Hosts: {Router.all_hosts}")



