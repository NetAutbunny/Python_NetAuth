class NetworkDevices:
    def __init__(self, host, platform, username, password):
        self.host = host
        self.platform = platform
        self.username = username
        #Private attribute
        self._password = password

    #Adding @property to the password attribute
    @property
    def password(self):
        return '********'

    #Creating a setter for password
    @password.setter
    def password(self, new_password):
        if new_password == self._password:
            raise ValueError("New password cannot be the same as the old password.")
        self._password = new_password


    def __str__(self):
        return f"NetworkDevices: {self.host} ({self.platform})"

# Example usage:
Obj1 = NetworkDevices("host1.domain.com", "cisco_xe", "admin", "Cisco123")
Obj2 = NetworkDevices("host2.domain.com", "juniper_junos", "admin", "Juniper123")
print(Obj1)
print(Obj2)

# Changing the password
Obj1.password = "NewCisco123"
# Attempting to set the password to the same value should raise an error
try:
    Obj1.password = "NewCisco123"
except ValueError as e:
    print(f"Error: {e}")
# Accessing the password property
print(f"Obj1 Password: {Obj1.password}")
