import os, time, urllib, socket
from urllib.error import URLError, HTTPError
from urllib import request
from modules import *

netcheck()

clear()


def choise1():
    target_url = input(Yesil+"URL ==>")

    dosya = open("link.txt","r")
    sayac = 0
    while True:
        adminpanel = dosya.readline()
        try:
            request.urlopen(target_url+adminpanel)
        except URLError:
            print(Kirmizi+"Denied "+adminpanel)
            sayac += 1
            if sayac == 293:
                print(Kirmizi+"Admin Panel Not Found")
                exit()
            continue
        except HTTPError:
            print(Kirmizi+"Denied "+adminpanel)
            sayac+=1
            if sayac == 293:
                print(Kirmizi+"Admin Panel Not Found")
                exit()
            continue
        else:
            print(Yesil+"OK "+adminpanel)
            continue





def choise2():
    target_url = input(Yesil+"URL ==>")
    target_file = input(Yesil+"File Path ==>")

    dosya = open(target_file,"r")
    sayac = 0
    while True:
        adminpanel = dosya.readline()
        try:
            request.urlopen(target_url+adminpanel)
        except URLError:
            print(Kirmizi+"Denied "+adminpanel)
            sayac += 1
            if sayac == 293:
                print(Kirmizi+"Admin Panel Not Found")
                exit()
            continue
        except HTTPError:
            print(Kirmizi+"Denied "+adminpanel)
            sayac+=1
            if sayac == 293:
                print(Kirmizi+"Admin Panel Not Found")
                exit()
            continue
        else:
            print(Yesil+"OK "+adminpanel)
            continue


banner = Kirmizi+"""
 █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗██████╗  █████╗ ███╗   ██╗███████╗██╗     
██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██╔══██╗████╗  ██║██╔════╝██║     
███████║██║  ██║██╔████╔██║██║██╔██╗ ██║██████╔╝███████║██╔██╗ ██║█████╗  ██║     
██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║██╔═══╝ ██╔══██║██║╚██╗██║██╔══╝  ██║     
██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║██║     ██║  ██║██║ ╚████║███████╗███████╗
╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝╚══════╝
                                                                                  
                        [1]Defult Wordlist          [2]Custom Wordlist
"""
print(banner)

choise = input(Mavi+"Choise A Option ==>")

if choise == "1":
    choise1()
elif choise == "2":
    choise2()

