from dataclasses import dataclass
from typing import List
from rich import print


@dataclass
class RouterFacts:
    hostname: str
    vendor: str
    network_os: str
    model: str
    os_version: str
    interfaces: list
    uptime_sec: int
    serial_number: str

# Creating an instance of RouterFacts
rtr = RouterFacts(hostname='la-rtr1',
                   vendor='cisco',
                   network_os='iosxr',
                   model='8201-SYS',
                   os_version='7.0.12',
                   interfaces=['HundredGigE0/0/0/24',
                               'HundredGigE0/0/0/25',
                               'HundredGigE0/0/0/26',
                               'HundredGigE0/0/0/27',
                               'HundredGigE0/0/0/28',
                               'HundredGigE0/0/0/29',
                               'HundredGigE0/0/0/30',
                               'HundredGigE0/0/0/31',
                               'HundredGigE0/0/0/32',
                               'HundredGigE0/0/0/33',
                               'HundredGigE0/0/0/34',
                               'HundredGigE0/0/0/35',],
                   uptime_sec=93070,
                   serial_number='FOC2291AVYB')
# Function to print router facts

print()
print(rtr)
print()






