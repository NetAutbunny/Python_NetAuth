#creating a class hierarchy with NetworkDevices as parent class with host attribute in dunder-init method
from rich import print
class NetworkDevice:
    def __init__(self, host):
        self.host = host

#creating Router, Switch and AccessPoint child classes using dunder-init and dunder-repr method
class Router(NetworkDevice):
    def __init__(self, host):
     super().__init__(host)

    def __repr__(self):
        return f"Router(host={self.host})"

class Switch(NetworkDevice):
    def __init__(self, host):
        super().__init__(host)

    def __repr__(self):
        return f"Switch(host={self.host})"

class AccessPoint(NetworkDevice):
    def __init__(self, host):
        super().__init__(host)

    def __repr__(self):
        return f"AccessPoint(host={self.host})"

# Creating object for each child class printing host attributes and object itself
r1 = Router('r1')
s2 = Switch('s2')
a3 = AccessPoint('a3')

print(f"Router Host: {r1.host}")
print(f"Switch Host: {s2.host}")
print(f'Access Point Host: {a3.host}')

print()
print(r1)
print(s2)
print(a3)
print()