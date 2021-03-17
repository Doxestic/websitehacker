from time import sleep
from random import randint

a = '''
welcome to my fake website hacker
this panel made by Doxestic
note: its not real just for fun ;)
contact me:
github: github.com/doxestic
telegram: @doxestic
'''
print(a)
print("pls enter your targets name:")
tname = input("target name:")
haveIp = input("do you have targets IP/Domin? (y/n)")
if haveIp == "y":
    print("pls enter targets IP/Domin:")
    tip = input("enter target IP/Domin:")
else:
    print("finding targets IP/domin from Google pls wait...")
    sleep(1)
    print("Progress: [||                  ] 10%")
    sleep(2)
    print("Progress: [||||                ] 20%")
    sleep(2)
    print("Progress: [||||||||||          ] 50%")
    sleep(2)
    print("Progress: [||||||||||||||||    ] 80%")
    print("Domin found")
    print("domin has set to " + tname + ".com")
    print("starting...")
    sleep(4)
    tip = tname + ".com"
print("hacking started...")
print("progress: [|                   ] 5%")
sleep(5)
print("progress: [|||                 ] 15%")
sleep(2)
print("progress: [||||                ] 20%")
sleep(5)
print("progress: [|||||||             ] 35%")
sleep(3)
print("progress: [||||||||||||        ] 60%")
sleep(2)
print("progress: [||||||||||||||||||  ] 90%")
sleep(5)
print("panel has found")
print("location: " + tname + ".com/cpanel")
print("starting to hack UserName and Password")
sleep(1)
print("starting to hack username...")
print("progress: [|                   ] 5%")
sleep(5)
print("progress: [|||                 ] 15%")
sleep(2)
print("progress: [||||                ] 20%")
print("connected to database")
sleep(5)
print("progress: [|||||||             ] 35%")
sleep(3)
print("progress: [||||||||||||        ] 60%")
sleep(2)
print("progress: [||||||||||||||||||  ] 90%")
num = randint(1, 5)
if num > 2:
    user = "admin" + tname
    print("user is " + user)
elif num > 5:
    user = "main" + tname
    print("user is " + user)
else:
    user = tname
    print("user is " + user)
sleep(1)
print("starting to hack password")
print("progress: [|                   ] 5%")
sleep(5)
print("progress: [|||                 ] 15%")
sleep(2)
print("progress: [||||                ] 20%")
print("connected to database")
sleep(5)
print("progress: [|||||||             ] 35%")
print("something went wrogn trying again...")
sleep(7)
print("starting to hack password")
print("progress: [|                   ] 5%")
sleep(5)
print("progress: [|||                 ] 15%")
sleep(2)
print("progress: [||||                ] 20%")
print("connected to database")
sleep(5)
print("progress: [|||||||             ] 35%")
sleep(2)
print("progress: [||||||||||||        ] 60%")
sleep(2)
print("progress: [||||||||||||||||||  ] 90%")
num = randint(1, 5)
if num > 2:
    passw = "12@pass" + tname
    print("password is " + passw)
elif num > 5:
    passw = "mainPassword@!" + tname
    print("password is " + passw)
else:
    passw = tname + "#$1179544"
    print("password is " + passw)
print("website haccked :)!")
print("login in " + tname + "/cpanel")
print("username: " + user + " Password: " + passw)
input("press enter to exit panel")