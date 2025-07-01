class Interface:
    def __init__(self, intf_name, intf_mode='access', access_vlan='1', speed='1Gbps', duplex='full'):
        self.intf_name = intf_name
        self.speed = speed
        self.duplex = duplex
        # Private attributes
        self._intf_mode = intf_mode
        self._access_vlan = access_vlan

    # @property decorator for intf_mode and access_vlan
    @property
    def intf_mode(self):
        return self._intf_mode
    @property
    def access_vlan(self):
        return self._access_vlan

    # Setter for intf_mode
    @intf_mode.setter
    def intf_mode(self, mode):
        if mode not in ['access', 'trunk']:
            raise ValueError("Interface mode must be 'access' or 'trunk'")
        self._intf_mode = mode
        if mode == 'trunk':
            self._access_vlan = None  # Reset access_vlan for trunk mode

    # Setter for access_vlan
    @access_vlan.setter
    def access_vlan(self, vlan):
        if self._intf_mode == 'access':
            try:
                self._access_vlan = str(int(vlan))
            except ValueError:
                raise ValueError("Access VLAN must be a valid integer string")
        else:
            if self._intf_mode == 'trunk':
                self._access_vlan = None

    def __str__(self):
        return (f"Interface: {self.intf_name} ({self.speed}/{self.duplex}, Mode: {self._intf_mode}, VLAN: {self._access_vlan})")

# Example usage:
eth1 = Interface(intf_name="Et1", intf_mode="access", access_vlan=1)
eth2 = Interface(intf_name="Et2", intf_mode="access", access_vlan=2)
eth3 = Interface(intf_name="Et3", intf_mode="access", access_vlan=3)
eth4 = Interface(intf_name="Et4", intf_mode="access", access_vlan=4)
eth5 = Interface(intf_name="Et5", intf_mode="access", access_vlan=5)
eth6 = Interface(intf_name="Et6", intf_mode="access", access_vlan=6)
eth7 = Interface(intf_name="Et7", intf_mode="trunk")

print(eth1, eth2, eth3, eth4, eth5, eth6, eth7, sep="\n")

# Changing the interface mode and access VLAN
eth1.intf_mode = 'trunk'
# eth1.access_vlan = '10'  # This will raise an error since eth1 is now in trunk mode
try:
    eth1.access_vlan = '10'  # This will raise an error since eth1 is now in trunk mode
except ValueError as e:
    print(f"Error: {e}")
# Accessing the properties
print(f"Eth1 Mode: {eth1.intf_mode}, Eth1 VLAN: {eth1.access_vlan}")
# Changing the access VLAN in access mode
eth2.intf_mode = 'access'
eth2.access_vlan = '20'
# Accessing the properties after changes
print(f"Eth2 Mode: {eth2.intf_mode}, Eth2 VLAN: {eth2.access_vlan}")
# Attempting to set an invalid mode
try:
    eth3.intf_mode = 'invalid_mode'  # This will raise an error
except ValueError as e:
    print(f"Error: {e}")
# Attempting to set an invalid access VLAN in access mode
try:
    eth4.access_vlan = 'invalid_vlan'  # This will raise an error
except ValueError as e:
    print(f"Error: {e}")
# Attempting to set an access VLAN in trunk mode
try:
    eth7.access_vlan = '30'  # This will raise an error since eth7 is in trunk mode
except ValueError as e:
    print(f"Error: {e}")
# Attempting to set the mode to trunk and then access VLAN
try:
    eth7.intf_mode = 'access'  # This will raise an error since eth7 is in trunk mode
    eth7.access_vlan = '30'  # This will not execute due to the previous error
except ValueError as e:
    print(f"Error: {e}")
# Attempting to set the mode to access and then access VLAN
try:
    eth1.intf_mode = 'access'  # This will change eth1 to access mode
    eth1.access_vlan = '10'  # This will set the access VLAN
    print(f"Eth1 Mode after change: {eth1.intf_mode}, Eth1 VLAN after change: {eth1.access_vlan}")
except ValueError as e:
    print(f"Error: {e}")



