# Coded / Dev: ††#9999 | https://github.com/TT-Tutorials | https://github.com/TT-Tutorials/GANG-Nuker
# GANG Discord Nuker / Multi Tool©
# Copyright © 2022
########################################


import colorama
import random, json
import ctypes, os, sys
import time, threading
import string, pyautogui
import webbrowser, base64
from colorama import Fore
import requests, websocket
from selenium import webdriver

global useragent
def useragent():
    file = open('utilities/QR/useragent.txt','r')
    useragent = (random.choice(list(file)))
    useragent2 = []
    useragent2.append(useragent)
    useragent1 = []
def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text

optionsforpfp = print(f'''
[{Fore.LIGHTRED_EX}-{Fore.RESET}] These Options Can Lock Your Tokens!\n
[\x1b[95m1\x1b[95m\x1B[37m] Single PFP
[\x1b[95m2\x1b[95m\x1B[37m] Multiple PFP
[\x1b[95m3\x1b[95m\x1B[37m] GANG-Nuker PFP\n''')
optionsforpfp = int(input('[\x1b[95m>\x1b[95m\x1B[37m] Choice?: '))

if optionsforpfp == 1:
        image = input('[\x1b[95m>\x1b[95m\x1B[37m] Image Name?: ')
        with open(image,'rb') as f:
            byteform = base64.b64encode(f.read())
            imageurl1 = byteform.decode('utf-8')

        payload1 = {
            'avatar':f'data:image/png;base64,{imageurl1}'
        }

elif optionsforpfp == 2:
        path = input('[\x1b[95m>\x1b[95m\x1B[37m] Directory For All The Images?: ')
        path.replace(r'\\','\\\\')

        image1 = random.choice([
        x for x in os.listdir(path)
        if os.path.isfile(os.path.join(path, x))
    ])

        with open(image1,'rb') as e:
            byteform = base64.b64encode(e.read())
            imageurl2 = byteform.decode('utf-8')

        payload2 = {
            'avatar':f'data:image/png;base64,{imageurl2}'
        }

elif optionsforpfp == 3:
        image = "data:image/jpeg;base64,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"

        payload3 = {
            'avatar':image
        }

url = 'https://discord.com/api/v9/users/@me'
  
tokens = []
token = []

with open('tokens.txt','r') as f:
        for line in f:
            tokens.append(line)

        for element in tokens:
            token.append(element.strip())

        length = len(token)

for x in range(length):
        header = {
            "authority": "discord.com",
            "method": "POST",
            "path": "/api/v9/users/@me",
            "scheme": "https",
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US",
            "Authorization": f"{token[x]}",
            "content-length": "0",
            "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
            "origin": "https://discord.com",
            'referer': 'https://discord.com/channels/@me',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": useragent(),
            "x-context-properties": "eyJsb2NhdGlvbiI6Ikludml0ZSBCdXR0b24gRW1iZWQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijg3OTc4MjM4MDAxMTk0NjAyNCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4ODExMDg4MDc5NjE0MTk3OTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjAsImxvY2F0aW9uX21lc3NhZ2VfaWQiOiI4ODExOTkzOTI5MTExNTkzNTcifQ==",
            "x-debug-options": "bugReporterEnabled",
            "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJjYW5hcnkiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC42MDAiLCJvc192ZXJzaW9uIjoiMTAuMC4yMjAwMCIsIm9zX2FyY2giOiJ4NjQiLCJzeXN0ZW1fbG9jYWxlIjoic2siLCJjbGllbnRfYnVpbGRfbnVtYmVyIjo5NTM1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
        }

        if optionsforpfp == 1:
            r = requests.patch(url,headers=header,json=payload1)
            if r.status_code == 200:
                print(Fore.GREEN + f'Added | {token[x]}')
            else:
                print(r)
        elif optionsforpfp == 2:
            r = requests.patch(url,headers=header,json=payload2)
            if r.status_code == 200:
                print(Fore.GREEN + f'Added | {token[x]}')
            else:
                print(r)

        elif optionsforpfp == 3:
            r = requests.patch(url,headers=header,json=payload3)
            if r.status_code == 200:
                print(Fore.GREEN + f'Added | {token[x]}')
            else:
                print(r)

        else:
            print("Error")
