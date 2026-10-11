import sys
import pandas as pd
import requests

# lazy import pandas as pd
# lazy import requests


def main():
    if "--help" in sys.argv:
        print("usage: python cli.py URL")
        return
    data = requests.get(sys.argv[1]).json()
    print(pd.DataFrame(data).head())


main()