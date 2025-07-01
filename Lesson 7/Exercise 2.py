class Interface:
    def __init__(self, intf_name, intf_mode='access', access_vlan='1', speed='1Gbps', duplex='full'):
        self.intf_name = intf_name
        self.intf_mode = intf_mode
        self.access_vlan = access_vlan
        self.speed = speed
        self.duplex = duplex


        if intf_mode not in ['access', 'trunk']:
           raise ValueError("Interface mode must be 'access' or 'trunk'")

        if intf_mode == 'trunk':
         self.access_vlan = None
        else:
         try:
             self.access_vlan = str(int(access_vlan))
         except ValueError:
                raise ValueError("Access VLAN must be a valid integer string")

    def __str__(self):
        return (f"Interface: {self.intf_name} ({self.speed}/{self.duplex},Mode: {self.intf_mode}, VLAN: {self.access_vlan})")



# Example usage:
eth1 = Interface(intf_name="Et1", intf_mode="access", access_vlan=1)
eth2 = Interface(intf_name="Et2", intf_mode="access", access_vlan=2)
eth3 = Interface(intf_name="Et3", intf_mode="access", access_vlan=3)
eth4 = Interface(intf_name="Et4", intf_mode="access", access_vlan=4)
eth5 = Interface(intf_name="Et5", intf_mode="access", access_vlan=5)
eth6 = Interface(intf_name="Et6", intf_mode="access", access_vlan=6)
eth7 = Interface(intf_name="Et7", intf_mode="trunk")

print(eth1,eth2,eth3,eth4,eth5,eth6,eth7,sep="\n")