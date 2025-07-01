from telnetlib import Telnet
import time

def read(telnet_conn,sleep=1.5):
    """
    Read data from the telnet connection.
    """
    time.sleep(sleep)
    data = telnet_conn.read_very_eager().decode()
    return data

host= "192.168.1.91"
username = "u1"

# Create telnet connection
tn = Telnet(host)
d = read(tn)
print(d)



