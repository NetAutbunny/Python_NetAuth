from telnetlib import Telnet
import time
import re
from getpass import getpass


def read(telnet_conn, sleep=1.5):
    """
    Read data from the telnet connection.
    """
    time.sleep(sleep)
    data = telnet_conn.read_very_eager().decode()
    return data

def write(telnet_conn, data):
    """
    Write data to the telnet connection.
    """
    byte_data = data.encode()
    telnet_conn.write(byte_data)

def login(telnet_conn, username, password):
    """
    Perform login to the device using telnet.
    """
    d = read(telnet_conn)
    output = d

    if re.search(r"Username:", d):
        write(telnet_conn, f"{username}\n")
        d = read(telnet_conn)

        if re.search(r"Password", d):
            write(telnet_conn, f"{password}\n")
            d = read(telnet_conn)
            return d
    return None

if __name__ == "__main__":
    host = "192.168.1.91"
    username = "u1"
    password = getpass("Enter Password: ")

    tn = Telnet(host)
    output = login(tn, username, password)
    if output:
        print(output)
    else:
        print("Login failed or no output received.")

