import re
from rich import print
with open("aruba_cx_show_ipv6_intf.txt") as f:
    output = f.read()
    # Explanation of regex components:
    # ?\s
    #   ?   : Makes the preceding token (in your pattern, a character or group) optional, matching zero or one occurrence.
    #   \s  : Matches any whitespace character (space, tab, newline, etc.).
    #   Used together (e.g., ',?\s') it means "an optional comma followed by a whitespace".
    #
    # [\w:/]+
    #   [\w:/] : Character class that matches any word character (\w: [a-zA-Z0-9_]), colon (:), or slash (/).
    #   +      : One or more of the preceding character class.
    #   This allows matching the full IPv6 address, which may contain hexadecimal digits, colons, and possibly a slash (for prefix length).
    match = re.search(
        r"^Interface\s(\S+) is\s(\S+)?\sAdmin state is\s+(\S+)?\sIPv6 address:\n\s+([\w:/]+)",
        output,
        flags=re.M
    )
    if match:
        print(f"intf_name: {match.group(1)}")
        print(f"intf _state : {match.group(2)}")
        print(f"Admin state: {match.group(3)}")
        print(f"ipv6_addr: {match.group(4)}")