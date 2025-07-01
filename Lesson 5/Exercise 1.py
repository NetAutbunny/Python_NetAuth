import re
from rich import print
with open("show_version.txt") as f:
    output = f.read()
    match1 = re.search(r'(cisco\s\w\d\d\d+?.4P)', output)
    match2 = re.search(r'(FG.+)', output)
    print(f'Model Number: {match1.group(1)}')
    print(f'Serial Number: {match2.group(1)}')
