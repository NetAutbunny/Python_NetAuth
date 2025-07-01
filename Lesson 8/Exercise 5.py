#Creating Channel with four methods dunder-init(), connect(), read() and write()
class Channel:
    def __init__(self,host,username, password):
        self.host = host
        self.username = username
        self.password = password

    def connect(self):
        pass

    def read(self):
        print(f"Reading data from {self.host}")

    def write(self, data):
        print(f"Writing data to {self.host}: {data}")

#Creating 2 child classes of Channel: SSHChannel and TelnetChannel

class SSHChannel(Channel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.transport = 'ssh'
        # Additional initialization for SSHChannel if needed
    def connect(self):
        print(f"Fictional SSH connection to {self.host}")

class TelnetChannel(Channel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.transport = 'telnet'
        # Additional initialization for TelnetChannel if needed
    def connect(self):
        print(f"Fictional Telnet connection to {self.host}")

class Router:
    def __init__(self, host,device_type,username, password, transport='ssh'):
        self.host = host
        self.device_type = device_type

        if transport == 'ssh':
            self.channel = SSHChannel(host, username, password)
            self.channel.connect()
        elif transport == 'telnet':
            self.channel = TelnetChannel(host, username, password)
            self.channel.connect()

    def read(self):
        self.channel.read()
    def write(self, data):
        self.channel.write(data)

# Example usage
r1 = Router('r1.domain.com', 'router', 'admin', 'password', transport='ssh')
r1.write("show ip interface brief")
r1.read()


