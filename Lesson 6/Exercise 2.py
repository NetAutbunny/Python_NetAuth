from telnetlib import Telnet
import time
import re

def read(telnet_conn,sleep=1.5):
    time.sleep(sleep)
    data = telnet_conn.read_very_eager().decode()
    return data

def write(telnet_conn, data):
    byte_data= data.encode()
    telnet_conn.write(byte_data)

host = "192.168.1.91"
username = "u1"
password = "Cisco"

tn = Telnet(host)
d = read(tn)

print(d)

if re.search(r"Username:", d):
    write(tn, "u1\n")
    d = read(tn)
    print(d)

    if re.search(r"Password", d):
        write(tn, "Cisco\n")
        d = read(tn)
        print(d)



