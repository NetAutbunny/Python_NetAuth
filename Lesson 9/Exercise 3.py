'''C:\My Drive\Study\Python\kirkbyers>python -m venv venv

C:\My Drive\Study\Python\kirkbyers>cd venv

C:\My Drive\Study\Python\kirkbyers\venv>Scripts\activate

(venv) C:\My Drive\Study\Python\kirkbyers\venv>pip list
Package Version
------- -------
pip     23.2.1

[notice] A new release of pip is available: 23.2.1 -> 25.1.1
[notice] To update, run: python.exe -m pip install --upgrade pip

(venv) C:\My Drive\Study\Python\kirkbyers\venv>pip install --upgrade pip
Requirement already satisfied: pip in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (23.2.1)
Collecting pip
  Obtaining dependency information for pip from https://files.pythonhosted.org/packages/29/a2/d40fb2460e883eca5199c62cfc2463fd261f760556ae6290f88488c362c0/pip-25.1.1-py3-none-any.whl.metadata
  Downloading pip-25.1.1-py3-none-any.whl.metadata (3.6 kB)
Downloading pip-25.1.1-py3-none-any.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 3.1 MB/s eta 0:00:00
ERROR: To modify pip, please run the following command:
C:\My Drive\Study\Python\kirkbyers\venv\Scripts\python.exe -m pip install --upgrade pip

[notice] A new release of pip is available: 23.2.1 -> 25.1.1
[notice] To update, run: python.exe -m pip install --upgrade pip

(venv) C:\My Drive\Study\Python\kirkbyers\venv>pip list
Package Version
------- -------
pip     23.2.1

[notice] A new release of pip is available: 23.2.1 -> 25.1.1
[notice] To update, run: python.exe -m pip install --upgrade pip

(venv) C:\My Drive\Study\Python\kirkbyers\venv> python.exe -m pip install --upgrade pip
Requirement already satisfied: pip in c:\my drive\study\python\kirkbyers\venv\lib\site-packages (23.2.1)
Collecting pip
  Obtaining dependency information for pip from https://files.pythonhosted.org/packages/29/a2/d40fb2460e883eca5199c62cfc2463fd261f760556ae6290f88488c362c0/pip-25.1.1-py3-none-any.whl.metadata
  Using cached pip-25.1.1-py3-none-any.whl.metadata (3.6 kB)
Using cached pip-25.1.1-py3-none-any.whl (1.8 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 23.2.1
    Uninstalling pip-23.2.1:
      Successfully uninstalled pip-23.2.1
Successfully installed pip-25.1.1

(venv) C:\My Drive\Study\Python\kirkbyers\venv>pip list
Package Version
------- -------
pip     25.1.1

(venv) C:\My Drive\Study\Python\kirkbyers\venv>pip install setuptools
Collecting setuptools
  Downloading setuptools-80.9.0-py3-none-any.whl.metadata (6.6 kB)
Downloading setuptools-80.9.0-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 5.0 MB/s eta 0:00:00
Installing collected packages: setuptools
Successfully installed setuptools-80.9.0

(venv) C:\My Drive\Study\Python\kirkbyers\venv>pip list
Package    Version
---------- -------
pip        25.1.1
setuptools 80.9.0

(venv) C:\My Drive\Study\Python\kirkbyers\venv>pip install rich
Collecting rich
  Downloading rich-14.0.0-py3-none-any.whl.metadata (18 kB)
Collecting markdown-it-py>=2.2.0 (from rich)
  Downloading markdown_it_py-3.0.0-py3-none-any.whl.metadata (6.9 kB)
Collecting pygments<3.0.0,>=2.13.0 (from rich)
  Using cached pygments-2.19.1-py3-none-any.whl.metadata (2.5 kB)
Collecting mdurl~=0.1 (from markdown-it-py>=2.2.0->rich)
  Using cached mdurl-0.1.2-py3-none-any.whl.metadata (1.6 kB)
Downloading rich-14.0.0-py3-none-any.whl (243 kB)
Using cached pygments-2.19.1-py3-none-any.whl (1.2 MB)
Downloading markdown_it_py-3.0.0-py3-none-any.whl (87 kB)
Using cached mdurl-0.1.2-py3-none-any.whl (10.0 kB)
Installing collected packages: pygments, mdurl, markdown-it-py, rich
Successfully installed markdown-it-py-3.0.0 mdurl-0.1.2 pygments-2.19.1 rich-14.0.0

(venv) C:\My Drive\Study\Python\kirkbyers\venv>pip list
Package        Version
-------------- -------
markdown-it-py 3.0.0
mdurl          0.1.2
pip            25.1.1
Pygments       2.19.1
rich           14.0.0
setuptools     80.9.0

(venv) C:\My Drive\Study\Python\kirkbyers\venv>pip freeze
markdown-it-py==3.0.0
mdurl==0.1.2
Pygments==2.19.1
rich==14.0.0
setuptools==80.9.0

(venv) C:\My Drive\Study\Python\kirkbyers\venv>deactivate
C:\My Drive\Study\Python\kirkbyers\venv>'''