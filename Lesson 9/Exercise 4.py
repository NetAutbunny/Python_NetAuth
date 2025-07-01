"""C:\My Drive\Study\Python\kirkbyers\venv>Scripts\activate

(venv) C:\My Drive\Study\Python\kirkbyers\venv>pip install Netmiko
Collecting Netmiko
  Downloading netmiko-4.5.0-py3-none-any.whl.metadata (7.5 kB)
Collecting ntc-templates>=3.1.0 (from Netmiko)
  Downloading ntc_templates-7.9.0-py3-none-any.whl.metadata (4.3 kB)
Collecting paramiko>=2.9.5 (from Netmiko)
  Using cached paramiko-3.5.1-py3-none-any.whl.metadata (4.6 kB)
Collecting pyserial>=3.3 (from Netmiko)
  Using cached pyserial-3.5-py2.py3-none-any.whl.metadata (1.6 kB)
Collecting pyyaml>=6.0.2 (from Netmiko)
  Using cached PyYAML-6.0.2-cp312-cp312-win_amd64.whl.metadata (2.1 kB)
Requirement already satisfied: rich>=13.8 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from Netmiko) (14.0.0)
Collecting ruamel.yaml>=0.17 (from Netmiko)
  Downloading ruamel.yaml-0.18.14-py3-none-any.whl.metadata (24 kB)
Collecting scp>=0.13.6 (from Netmiko)
  Using cached scp-0.15.0-py2.py3-none-any.whl.metadata (4.3 kB)
Collecting textfsm>=1.1.3 (from Netmiko)
  Downloading textfsm-2.1.0-py2.py3-none-any.whl.metadata (2.7 kB)
  Using cached textfsm-1.1.3-py2.py3-none-any.whl.metadata (2.6 kB)
Collecting six (from textfsm>=1.1.3->Netmiko)
  Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
Collecting future (from textfsm>=1.1.3->Netmiko)
  Using cached future-1.0.0-py3-none-any.whl.metadata (4.0 kB)
Collecting bcrypt>=3.2 (from paramiko>=2.9.5->Netmiko)
  Using cached bcrypt-4.3.0-cp39-abi3-win_amd64.whl.metadata (10 kB)
Collecting cryptography>=3.3 (from paramiko>=2.9.5->Netmiko)
  Downloading cryptography-45.0.4-cp311-abi3-win_amd64.whl.metadata (5.7 kB)
Collecting pynacl>=1.5 (from paramiko>=2.9.5->Netmiko)
  Using cached PyNaCl-1.5.0-cp36-abi3-win_amd64.whl.metadata (8.7 kB)
Collecting cffi>=1.14 (from cryptography>=3.3->paramiko>=2.9.5->Netmiko)
  Using cached cffi-1.17.1-cp312-cp312-win_amd64.whl.metadata (1.6 kB)
Collecting pycparser (from cffi>=1.14->cryptography>=3.3->paramiko>=2.9.5->Netmiko)
  Using cached pycparser-2.22-py3-none-any.whl.metadata (943 bytes)
Requirement already satisfied: markdown-it-py>=2.2.0 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from rich>=13.8->Netmiko) (3.0.0)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from rich>=13.8->Netmiko) (2.19.1)
Requirement already satisfied: mdurl~=0.1 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from markdown-it-py>=2.2.0->rich>=13.8->Netmiko) (0.1.2)
Collecting ruamel.yaml.clib>=0.2.7 (from ruamel.yaml>=0.17->Netmiko)
  Downloading ruamel.yaml.clib-0.2.12-cp312-cp312-win_amd64.whl.metadata (2.8 kB)
Downloading netmiko-4.5.0-py3-none-any.whl (244 kB)
Downloading ntc_templates-7.9.0-py3-none-any.whl (609 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 609.8/609.8 kB 10.9 MB/s eta 0:00:00
Using cached textfsm-1.1.3-py2.py3-none-any.whl (44 kB)
Using cached paramiko-3.5.1-py3-none-any.whl (227 kB)
Using cached bcrypt-4.3.0-cp39-abi3-win_amd64.whl (152 kB)
Downloading cryptography-45.0.4-cp311-abi3-win_amd64.whl (3.4 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 3.4/3.4 MB 16.8 MB/s eta 0:00:00
Using cached cffi-1.17.1-cp312-cp312-win_amd64.whl (181 kB)
Using cached PyNaCl-1.5.0-cp36-abi3-win_amd64.whl (212 kB)
Using cached pyserial-3.5-py2.py3-none-any.whl (90 kB)
Using cached PyYAML-6.0.2-cp312-cp312-win_amd64.whl (156 kB)
Downloading ruamel.yaml-0.18.14-py3-none-any.whl (118 kB)
Downloading ruamel.yaml.clib-0.2.12-cp312-cp312-win_amd64.whl (115 kB)
Using cached scp-0.15.0-py2.py3-none-any.whl (8.8 kB)
Using cached future-1.0.0-py3-none-any.whl (491 kB)
Using cached pycparser-2.22-py3-none-any.whl (117 kB)
Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: pyserial, six, ruamel.yaml.clib, pyyaml, pycparser, future, bcrypt, textfsm, ruamel.yaml, cffi, pynacl, ntc-templates, cryptography, paramiko, scp, Netmiko
Successfully installed Netmiko-4.5.0 bcrypt-4.3.0 cffi-1.17.1 cryptography-45.0.4 future-1.0.0 ntc-templates-7.9.0 paramiko-3.5.1 pycparser-2.22 pynacl-1.5.0 pyserial-3.5 pyyaml-6.0.2 ruamel.yaml-0.18.14 ruamel.yaml.clib-0.2.12 scp-0.15.0 six-1.17.0 textfsm-1.1.3

(venv) C:\My Drive\Study\Python\kirkbyers\venv>pip install git+https://github.com/ktbyers/netmiko
Collecting git+https://github.com/ktbyers/netmiko
  Cloning https://github.com/ktbyers/netmiko to c:\users\mahmoodpro6\appdata\local\temp\pip-req-build-_3p2ohz7
  Running command git clone --filter=blob:none --quiet https://github.com/ktbyers/netmiko 'C:\Users\MahmoodPro6\AppData\Local\Temp\pip-req-build-_3p2ohz7'
  Resolved https://github.com/ktbyers/netmiko to commit 8dc3ba428b5c9e4c097de5408bd04ebf53994b89
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: ntc-templates>=3.1.0 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.5.0) (7.9.0)
Requirement already satisfied: paramiko>=2.9.5 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.5.0) (3.5.1)
Requirement already satisfied: pyserial>=3.3 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.5.0) (3.5)
Requirement already satisfied: pyyaml>=6.0.2 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.5.0) (6.0.2)
Requirement already satisfied: rich>=13.8 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.5.0) (14.0.0)
Requirement already satisfied: ruamel.yaml>=0.17 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.5.0) (0.18.14)
Requirement already satisfied: scp>=0.13.6 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.5.0) (0.15.0)
Requirement already satisfied: textfsm>=1.1.3 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.5.0) (1.1.3)
Requirement already satisfied: six in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from textfsm>=1.1.3->netmiko==4.5.0) (1.17.0)
Requirement already satisfied: future in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from textfsm>=1.1.3->netmiko==4.5.0) (1.0.0)
Requirement already satisfied: bcrypt>=3.2 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from paramiko>=2.9.5->netmiko==4.5.0) (4.3.0)
Requirement already satisfied: cryptography>=3.3 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from paramiko>=2.9.5->netmiko==4.5.0) (45.0.4)
Requirement already satisfied: pynacl>=1.5 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from paramiko>=2.9.5->netmiko==4.5.0) (1.5.0)
Requirement already satisfied: cffi>=1.14 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from cryptography>=3.3->paramiko>=2.9.5->netmiko==4.5.0) (1.17.1)
Requirement already satisfied: pycparser in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from cffi>=1.14->cryptography>=3.3->paramiko>=2.9.5->netmiko==4.5.0) (2.22)
Requirement already satisfied: markdown-it-py>=2.2.0 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from rich>=13.8->netmiko==4.5.0) (3.0.0)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from rich>=13.8->netmiko==4.5.0) (2.19.1)
Requirement already satisfied: mdurl~=0.1 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from markdown-it-py>=2.2.0->rich>=13.8->netmiko==4.5.0) (0.1.2)
Requirement already satisfied: ruamel.yaml.clib>=0.2.7 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from ruamel.yaml>=0.17->netmiko==4.5.0) (0.2.12)

(venv) C:\My Drive\Study\Python\kirkbyers\venv>pip list | grep netmiko
'grep' is not recognized as an internal or external command,
operable program or batch file.

(venv) C:\My Drive\Study\Python\kirkbyers\venv>pip install grep
Collecting grep
  Downloading grep-0.3.2.tar.gz (3.2 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Building wheels for collected packages: grep
  Building wheel for grep (pyproject.toml) ... done
  Created wheel for grep: filename=grep-0.3.2-py3-none-any.whl size=2957 sha256=947291b6e28e5a53a9429d46f967129d287f66fb2ec57f05e4d43d043e4b3ac8
  Stored in directory: c:\users\mahmoodpro6\appdata\local\pip\cache\wheels\ac\63\0a\36e54c71cd4ec71f44911fc08126c0d91be2591bb842364a6a
Successfully built grep
Installing collected packages: grep
Successfully installed grep-0.3.2

(venv) C:\My Drive\Study\Python\kirkbyers\venv>pip list | grep netmiko
'grep' is not recognized as an internal or external command,
operable program or batch file.

(venv) C:\My Drive\Study\Python\kirkbyers\venv>pip install git+https://github.com/ktbyers/netmiko@master
Collecting git+https://github.com/ktbyers/netmiko@master
  Cloning https://github.com/ktbyers/netmiko (to revision master) to c:\users\mahmoodpro6\appdata\local\temp\pip-req-build-fld8ahez
  Running command git clone --filter=blob:none --quiet https://github.com/ktbyers/netmiko 'C:\Users\MahmoodPro6\AppData\Local\Temp\pip-req-build-fld8ahez'
  Running command git checkout -b master --track origin/master
  branch 'master' set up to track 'origin/master'.
  Switched to a new branch 'master'
  Resolved https://github.com/ktbyers/netmiko to commit 7ef6eff0175104e796ae9d97d31dc70a6ffca079
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: ntc-templates>=3.1.0 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.5.0) (7.9.0)
Requirement already satisfied: paramiko>=2.9.5 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.5.0) (3.5.1)
Requirement already satisfied: pyserial>=3.3 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.5.0) (3.5)
Requirement already satisfied: pyyaml>=6.0.2 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.5.0) (6.0.2)
Requirement already satisfied: rich>=13.8 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.5.0) (14.0.0)
Requirement already satisfied: ruamel.yaml>=0.17 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.5.0) (0.18.14)
Requirement already satisfied: scp>=0.13.6 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.5.0) (0.15.0)
Requirement already satisfied: textfsm>=1.1.3 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.5.0) (1.1.3)
Requirement already satisfied: six in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from textfsm>=1.1.3->netmiko==4.5.0) (1.17.0)
Requirement already satisfied: future in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from textfsm>=1.1.3->netmiko==4.5.0) (1.0.0)
Requirement already satisfied: bcrypt>=3.2 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from paramiko>=2.9.5->netmiko==4.5.0) (4.3.0)
Requirement already satisfied: cryptography>=3.3 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from paramiko>=2.9.5->netmiko==4.5.0) (45.0.4)
Requirement already satisfied: pynacl>=1.5 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from paramiko>=2.9.5->netmiko==4.5.0) (1.5.0)
Requirement already satisfied: cffi>=1.14 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from cryptography>=3.3->paramiko>=2.9.5->netmiko==4.5.0) (1.17.1)
Requirement already satisfied: pycparser in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from cffi>=1.14->cryptography>=3.3->paramiko>=2.9.5->netmiko==4.5.0) (2.22)
Requirement already satisfied: markdown-it-py>=2.2.0 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from rich>=13.8->netmiko==4.5.0) (3.0.0)
Requirement already satisfied: pygments<3.0.0,>=2.13.0 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from rich>=13.8->netmiko==4.5.0) (2.19.1)
Requirement already satisfied: mdurl~=0.1 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from markdown-it-py>=2.2.0->rich>=13.8->netmiko==4.5.0) (0.1.2)
Requirement already satisfied: ruamel.yaml.clib>=0.2.7 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from ruamel.yaml>=0.17->netmiko==4.5.0) (0.2.12)

(venv) C:\My Drive\Study\Python\kirkbyers\venv>pip install git+https://github.com/ktbyers/netmiko@v4.1.2
Collecting git+https://github.com/ktbyers/netmiko@v4.1.2
  Cloning https://github.com/ktbyers/netmiko (to revision v4.1.2) to c:\users\mahmoodpro6\appdata\local\temp\pip-req-build-htfudzsm
  Running command git clone --filter=blob:none --quiet https://github.com/ktbyers/netmiko 'C:\Users\MahmoodPro6\AppData\Local\Temp\pip-req-build-htfudzsm'
  Running command git checkout -q 89cd50990592a3f57c6acda1636f4adddc14fb8f
  Resolved https://github.com/ktbyers/netmiko to commit 89cd50990592a3f57c6acda1636f4adddc14fb8f
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: setuptools>=38.4.0 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.1.2) (80.9.0)
Requirement already satisfied: paramiko>=2.7.2 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.1.2) (3.5.1)
Requirement already satisfied: scp>=0.13.3 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.1.2) (0.15.0)
Collecting tenacity (from netmiko==4.1.2)
  Downloading tenacity-9.1.2-py3-none-any.whl.metadata (1.2 kB)
Requirement already satisfied: pyyaml>=5.3 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.1.2) (6.0.2)
Collecting textfsm==1.1.2 (from netmiko==4.1.2)
  Downloading textfsm-1.1.2-py2.py3-none-any.whl.metadata (2.5 kB)
Requirement already satisfied: ntc-templates>=2.0.0 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.1.2) (7.9.0)
Requirement already satisfied: pyserial in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.1.2) (3.5)
Requirement already satisfied: future in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from textfsm==1.1.2->netmiko==4.1.2) (1.0.0)
Requirement already satisfied: six in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from textfsm==1.1.2->netmiko==4.1.2) (1.17.0)
Requirement already satisfied: bcrypt>=3.2 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from paramiko>=2.7.2->netmiko==4.1.2) (4.3.0)
Requirement already satisfied: cryptography>=3.3 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from paramiko>=2.7.2->netmiko==4.1.2) (45.0.4)
Requirement already satisfied: pynacl>=1.5 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from paramiko>=2.7.2->netmiko==4.1.2) (1.5.0)
Requirement already satisfied: cffi>=1.14 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from cryptography>=3.3->paramiko>=2.7.2->netmiko==4.1.2) (1.17.1)
Requirement already satisfied: pycparser in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from cffi>=1.14->cryptography>=3.3->paramiko>=2.7.2->netmiko==4.1.2) (2.22)
Downloading textfsm-1.1.2-py2.py3-none-any.whl (44 kB)
Downloading tenacity-9.1.2-py3-none-any.whl (28 kB)
Building wheels for collected packages: netmiko
  Building wheel for netmiko (pyproject.toml) ... done
  Created wheel for netmiko: filename=netmiko-4.1.2-py3-none-any.whl size=198504 sha256=fa5c39f06792691e6448318ac347b74ddfe391e799c6d2a0eec3f1329e71fd31
  Stored in directory: C:\Users\MahmoodPro6\AppData\Local\Temp\pip-ephem-wheel-cache-vhf04rwu\wheels\ed\92\29\b584489dbbc311d9eb01cfc40964db3f8038d146d98ee749dd
Successfully built netmiko
Installing collected packages: textfsm, tenacity, netmiko
  Attempting uninstall: textfsm
    Found existing installation: textfsm 1.1.3
    Uninstalling textfsm-1.1.3:
      Successfully uninstalled textfsm-1.1.3
  Attempting uninstall: netmiko
    Found existing installation: netmiko 4.5.0
    Uninstalling netmiko-4.5.0:
      Successfully uninstalled netmiko-4.5.0
Successfully installed netmiko-4.1.2 tenacity-9.1.2 textfsm-1.1.2

(venv) C:\My Drive\Study\Python\kirkbyers\venv>pip install git+https://github.com/ktbyers/netmiko@679be2be58a975e874fd97616c7014f0726460c1
Collecting git+https://github.com/ktbyers/netmiko@679be2be58a975e874fd97616c7014f0726460c1
  Cloning https://github.com/ktbyers/netmiko (to revision 679be2be58a975e874fd97616c7014f0726460c1) to c:\users\mahmoodpro6\appdata\local\temp\pip-req-build-lmp12dnc
  Running command git clone --filter=blob:none --quiet https://github.com/ktbyers/netmiko 'C:\Users\MahmoodPro6\AppData\Local\Temp\pip-req-build-lmp12dnc'
  Running command git rev-parse -q --verify 'sha^679be2be58a975e874fd97616c7014f0726460c1'
  Running command git fetch -q https://github.com/ktbyers/netmiko 679be2be58a975e874fd97616c7014f0726460c1
  Running command git checkout -q 679be2be58a975e874fd97616c7014f0726460c1
  Resolved https://github.com/ktbyers/netmiko to commit 679be2be58a975e874fd97616c7014f0726460c1
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
Requirement already satisfied: ntc-templates>=2.0.0 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.2.0) (7.9.0)
Requirement already satisfied: paramiko>=2.9.5 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.2.0) (3.5.1)
Requirement already satisfied: pyserial>=3.3 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.2.0) (3.5)
Requirement already satisfied: pyyaml>=5.3 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.2.0) (6.0.2)
Requirement already satisfied: scp>=0.13.6 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from netmiko==4.2.0) (0.15.0)
Collecting textfsm>=1.1.3 (from netmiko==4.2.0)
  Using cached textfsm-2.1.0-py2.py3-none-any.whl.metadata (2.7 kB)
  Using cached textfsm-1.1.3-py2.py3-none-any.whl.metadata (2.6 kB)
Requirement already satisfied: six in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from textfsm>=1.1.3->netmiko==4.2.0) (1.17.0)
Requirement already satisfied: future in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from textfsm>=1.1.3->netmiko==4.2.0) (1.0.0)
Requirement already satisfied: bcrypt>=3.2 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from paramiko>=2.9.5->netmiko==4.2.0) (4.3.0)
Requirement already satisfied: cryptography>=3.3 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from paramiko>=2.9.5->netmiko==4.2.0) (45.0.4)
Requirement already satisfied: pynacl>=1.5 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from paramiko>=2.9.5->netmiko==4.2.0) (1.5.0)
Requirement already satisfied: cffi>=1.14 in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from cryptography>=3.3->paramiko>=2.9.5->netmiko==4.2.0) (1.17.1)
Requirement already satisfied: pycparser in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (from cffi>=1.14->cryptography>=3.3->paramiko>=2.9.5->netmiko==4.2.0) (2.22)
Using cached textfsm-1.1.3-py2.py3-none-any.whl (44 kB)
Building wheels for collected packages: netmiko
  Building wheel for netmiko (pyproject.toml) ... done
  Created wheel for netmiko: filename=netmiko-4.2.0-py3-none-any.whl size=217143 sha256=13e1a5076949d5673c9218de3191c7ebe9c409eb57bc548a6042204a1ee974dc
  Stored in directory: c:\users\mahmoodpro6\appdata\local\pip\cache\wheels\32\a4\e5\df446e87950d0b06c2ae1494270ad83eec8c0ec46fefed1cb0
Successfully built netmiko
Installing collected packages: textfsm, netmiko
  Attempting uninstall: textfsm
    Found existing installation: textfsm 1.1.2
    Uninstalling textfsm-1.1.2:
      Successfully uninstalled textfsm-1.1.2
  Attempting uninstall: netmiko
    Found existing installation: netmiko 4.1.2
    Uninstalling netmiko-4.1.2:
      Successfully uninstalled netmiko-4.1.2
Successfully installed netmiko-4.2.0 textfsm-1.1.3

(venv) C:\My Drive\Study\Python\kirkbyers\venv>pip freeze
bcrypt==4.3.0
cffi==1.17.1
cryptography==45.0.4
future==1.0.0
grep==0.3.2
markdown-it-py==3.0.0
mdurl==0.1.2
netmiko @ git+https://github.com/ktbyers/netmiko@679be2be58a975e874fd97616c7014f0726460c1
ntc_templates==7.9.0
paramiko==3.5.1
pycparser==2.22
Pygments==2.19.1
PyNaCl==1.5.0
pyserial==3.5
PyYAML==6.0.2
rich==14.0.0
ruamel.yaml==0.18.14
ruamel.yaml.clib==0.2.12
scp==0.15.0
setuptools==80.9.0
six==1.17.0
tenacity==9.1.2
textfsm==1.1.3

(venv) C:\My Drive\Study\Python\kirkbyers\venv>pip freeze> requirements.txt

(venv) C:\My Drive\Study\Python\kirkbyers\venv>"""