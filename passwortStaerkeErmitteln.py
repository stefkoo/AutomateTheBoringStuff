#!python 3
# Anhand eines String soll die Passwortstärke ermittelt werden

import re


def checkRegex():
    while True:
        passWord: str = input('Bitte geben Sie ein Passwort ein: ')
        if re.match(r'\w{8,}', passWord):
            print('!!Your Password is strong!!')
            break
        else:
            print('your Password is not strong, please try again ')
        continue



checkRegex()