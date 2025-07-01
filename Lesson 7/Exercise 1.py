class NetworkDevices:
    def __init__(self, host, platform, username, password):
        self.host = host
        self.platform = platform
        self.username = username
        self.password = password

    def __str__(self):
        return f"Host: {self.host}, Platform: {self.platform}"

# Example usage:
Obj1 = NetworkDevices("host1.domain.com", "cisco_xe", "admin", "Cisco123")
Obj2 = NetworkDevices("host2.domain.com", "juniper_junos", "admin", "Juniper123")

print()
print(Obj1)
print(Obj2)
