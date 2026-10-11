# Python 3.15 lazy imports: one word, faster startup

Watch the Short: [youtube.com/shorts/UpZWB-XVvu0](https://youtube.com/shorts/UpZWB-XVvu0)

Code from the SnakeByte Short "Python 3.15: one word, 16x faster startup".

`cli.py` is a tiny CLI: it downloads JSON from a URL and prints it as a table with pandas.
Its `--help` needs neither pandas nor requests, but a normal `import` loads both anyway.

## Run it

Requires Python 3.15 or newer.

```powershell
py -3.15 -m pip install pandas requests
py -3.15 cli.py https://jsonplaceholder.typicode.com/users
```

## Measure the startup (PowerShell)

```powershell
(Measure-Command { py -3.15 cli.py --help }).TotalMilliseconds
```

Now put the new keyword in front of the two imports:

```python
lazy import pandas as pd
lazy import requests
```

Run the same command again. On my Windows laptop it went from 1708 ms to 106 ms.

To try it on an old project without editing any files, make every import lazy with a flag:

```powershell
(Measure-Command { py -3.15 -X lazy_imports=all cli.py --help }).TotalMilliseconds
```

## Two rules

- `lazy` works only at the top level of a file, not inside functions, classes or `try` blocks.
- A broken import fails on first use, not on the import line.

More: [PEP 810](https://peps.python.org/pep-0810/) · [What's New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)
