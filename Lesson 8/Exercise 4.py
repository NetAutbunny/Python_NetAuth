from rich import print
class NetworkDevices:
    def __init__(self,host):
        self.host = host

class Router(NetworkDevices):
    def __init__(self, host, model='None'):
        super().__init__(host)
        self.model = model

    def __repr__(self):
        return f"Router host = {self.host}, model = {self.model}"

    def print_model(self):
        if self.model is not None:
            print(f"Router Model: {self.model}")

r1= Router('r1.com', 'Cisco 8500')

print(r1.host)
print(r1.model)
print(r1)
r1.print_model()


