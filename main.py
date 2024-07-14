import requests
from bs4 import BeautifulSoup
import pandas as pd
import sys
from colorama import Fore
import pyfiglet
import socket
def path():
    proj_name = pyfiglet.figlet_format("Subdomain-Checker", font='rev')
    print(Fore.GREEN + proj_name)
    
    enter_path = ""
    while not enter_path:
        enter_path = input(Fore.WHITE + r"Enter path -> ")
        if not enter_path:
            print(Fore.RED + "Path cannot be empty. Please enter a valid path.")
        elif not enter_path.endswith('.txt'):
            print(Fore.RED + "Invalid file type. Please enter a path to a .txt file.")
            enter_path = ""

    def check(file_path):
        try:
            with open(file_path, 'r') as file:
                subdomains = file.read().splitlines()
                
            for subdomain in subdomains:
                url = f"http://{subdomain}"
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
                        print(Fore.BLUE + f'[🔎] {url}')
                        print(Fore.GREEN + f"[✅] URL: "+ Fore.WHITE + f"{url}" + Fore.GREEN + " is Active")
                        print('-' * 40)
                    else:
                        print(Fore.BLUE + f'[🔎] {url}')
                        print(f"[❌] URL: " + f"{url} is "+ Fore.RED +" not active." +"Status code: {response.status_code}")
                        print('-' * 40)
                except requests.ConnectionError:
                    print(Fore.BLUE + f'[🔎] {url}')
                    print(f'[❗] URL: ' + Fore.LIGHTYELLOW_EX+ f"{url} is not reachable.")
                    print('-' * 40)
        except FileNotFoundError:
            print('[❌]'+ Fore.RED + "File not found. Please enter a valid path.")

    check(enter_path)

path()
