import subprocess
import sys
import os.path
from os import path
######## This script is only for educational purpose ########
######## use it on your own RISK ########
######## I'm not responsible for any loss or damage ########
######## caused to you using this script ########
######## Github Repo - https://github.com/Dark-Princ3/DTU-Alert-Bot/ ########


def install(name):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', name])


def main():

    my_packages = ['Pyrogram', 'TgCrypto', 'psycopg2-binary', 'python-dotenv',
                   'lxml', 'bs4', 'requests', 'urllib3', 'pymongo', 'dnspython']

    for package in my_packages:
        install(package)
        print('\n')

if __name__ == '__main__':
    main()
