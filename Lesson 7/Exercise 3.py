from rich import print

class OSPFRouter:
    def __init__(self, instance_id,area_id, router_id, is_dr= False, is_bdr= False):
        self.instance_id = instance_id
        self.area_id = area_id
        self.router_id = router_id
        self.is_dr = is_dr
        self.is_bdr = is_bdr
        # private attributes
        self._neighbors = set()

    def __str__(self):
     return f'''
                OSPF Router Instance ID: {self.instance_id}
                Area ID: {self.area_id}
                Router ID: {self.router_id}
                DR: {self.is_dr}
                BDR: {self.is_bdr}
                
Neighbors: {self._neighbors}
        '''

    def add_neighbor(self,  neighbor_id):
        self._neighbors = self._neighbors.union({neighbor_id})

    def remove_neighbor(self,  neighbor_id):
        self._neighbors = self._neighbors.difference({neighbor_id})

#Example Usage:
ospf_router = OSPFRouter(42, '0.0.0.0','10.220.88.29', is_dr = True)
ospf_router.add_neighbor('10.220.88.28')
ospf_router.add_neighbor('10.220.88.30')
ospf_router.add_neighbor('10.220.88.32')
ospf_router.add_neighbor('10.220.88.34')
ospf_router.add_neighbor('10.220.88.31')
ospf_router.add_neighbor('10.220.88.33')
ospf_router.add_neighbor('10.220.88.29')
ospf_router.add_neighbor('10.220.88.35')

# Add a fictional neighbor
ospf_router.add_neighbor('10.220.88.36')
# Remove the fictional neighbor as a test
ospf_router.remove_neighbor('10.220.88.36')

print(ospf_router)





