# Python 3.15: UTF-8 by default

Code from the SnakeByte Short "Python 3.15 fixes UnicodeDecodeError on Windows".

`notes.txt` is a UTF-8 file with one emoji. `read.py` opens it without an `encoding` argument.

## Run it (Windows)

```powershell
py -3.14 read.py   # UnicodeDecodeError: 'charmap' codec can't decode byte ...
py -3.15 read.py   # Hello, world 😁
```

Before 3.15, `open()` on Windows used the system code page: cp1252, cp1250, cp1251 and so on.
Those encodings have no emoji, so reading this file crashes.
Python 3.15 uses UTF-8 by default ([PEP 686](https://peps.python.org/pep-0686/)).

## On older Python

Pass the encoding explicitly. It works on every version and every OS:

```python
f = open("notes.txt", encoding="utf-8")
```

## Want the old behaviour on 3.15?

```powershell
py -3.15 -X utf8=0 read.py
```

More: [What's New in Python 3.15](https://docs.python.org/3.15/whatsnew/3.15.html)