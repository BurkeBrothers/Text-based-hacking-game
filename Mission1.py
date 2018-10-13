import time
import os
import sys
import CommandErrors
import Tutorial
import json

bank_acc = [0]
x = .5
addedFiles = []

operatingSystem = 'HydraOS'
defaultPassword = 'HYDRA'
idNumber = '1'
sourceProgram = 'HydraHack'

with open("Directories.json", "r") as read_file:
    data = json.load(read_file)

def Main():
    print('Your first real mission is to hack a small company that has thousands of pounds worth of tools used in\n')
    time.sleep(x)
    print("hacking, which you will unlock later in the Game\n")
    time.sleep(x)
    print('Completing this mission will reward you $500, which you can use on new tools, storage or new hardware.')
    time.sleep(x)
    print("The company you are hacking is called 'Aroura Penetration Testing'")
    time.sleep(x)
    print("To start of the hack you must modify the admin password to their website at the url: 'www.ArouraTesting.com'")
    print("This will be done using your port cracking tools.")
    time.sleep(x)
    print("Note: The computer you hack will depend on what tools you get!")
    hack()

def hack():
    CommandEnter = input(f'{sourceProgram}~$ ')
    if CommandEnter == 'netstat -l --all' or 'netstat --listen':
        print("PORT     STATE       Service")
        time.sleep(x)
        print("21/tcp   closed      FTP")
        time.sleep(x)
        print("22/tcp   closed      SSH  ")
        time.sleep(x)
    CommandEnter = input(f'{sourceProgram}~$ ')
    if CommandEnter == 'ftpsploit 21 www.ArouraTesting.com':
        print("Cracking FTP port 21: ")
        for i in range(101):
            time.sleep(.1)
            sys.stdout.write("\r%d%%" % i)
            sys.stdout.flush()
        os.system('cls')
        print("FTP port 21 Cracked...")
        CommandEnter = input(f'{sourceProgram}/Ftpsploit~$ ')
        if CommandEnter == 'NetTraffic -t --listen':
            print('Proto  Local Address          Foreign Address        State')
            time.sleep(x)
            print('TCP    245.57.95.118:57010    DESKTOP-SERVER:18272   ESTABLISHED')
            time.sleep(x)
            print('TCP    245.57.95.118:57011    DESKTOP-SERVER:18273   ESTABLISHED')
            time.sleep(x)
        CommandEnter = input(f'{sourceProgram}/Ftpsploit~$ ')
        if CommandEnter == 'FtpTabels -t -ftp':
            print('| ID |   Name    |                      Passowrd                 |')
            print('|----|-----------|-----------------------------------------------|')
            print('| 1  |   Jack    |   BFE8D279ADD6BDD82A8E8F346398A44971BF0BE6    |')
            print('|----|-----------|-----------------------------------------------|')
            print('| 2  |   Adam    |   FCC390AC4202457F8DBFA3B8C44FE2A04B3F443B    |')
            print('|----|-----------|-----------------------------------------------|')
            print('| 3  |   Admin   |   Admin                                       |')
        CommandEnter = input(f'{sourceProgram}/Ftpsploit~$ ')
        if CommandEnter == 'exit ftpsploit':
            CommandEnter = input(f'{sourceProgram}~$ ')
            if CommandEnter == 'krackerconsole':
                CommandEnter = input("KrackerConsole~$ ")
                if CommandEnter == 'krackHash -SHA -f -h BFE8D279ADD6BDD82A8E8F346398A44971BF0BE6':
                    os.system('cls')
                    for i in range(100):
                        time.sleep(.1)
                        sys.stdout.write("\r%d%%" % i)
                        sys.stdout.flush()
                    os.system('cls')
                    print("\nPassword = JackDodger123")
                    time.sleep(x)
                    CommandEnter = input("KrackerConsole~$ ")
                    if CommandEnter == 'exit krackerconsole':
                        CommandEnter = input(f'{sourceProgram}~$ ')
                        if CommandEnter == 'ssh jack@JackDodger123':
                            ssh_jack()

                elif CommandEnter == 'krackHash -SHA -f -h FCC390AC4202457F8DBFA3B8C44FE2A04B3F443B':
                    os.system('cls')
                    for i in range(100):
                        time.sleep(.1)
                        sys.stdout.write("\r%d%%" % i)
                        sys.stdout.flush()
                    os.system('cls')
                    print("\nPassword = Adam123")
                    time.sleep(x)
                    CommandEnter = input("KrackerConsole~$ ")
                    if CommandEnter == 'exit krackerconsole':
                        CommandEnter = input(f'{sourceProgram}~$ ')
                        if CommandEnter == 'ssh adam@adam123':
                            ssh_adam()
def ssh_jack():
    CommandEnter = input('Jack@ArouraTesting~$ ')
    if CommandEnter == 'cd Bin':
        CommandEnter = input('Jack@ArouraTesting/Bin~$ ')
        if CommandEnter == 'ls':
            print('\n'.join(data['directories']['Mission1']['Jacks-Computer']['Documents']['Bin']['Bin-Contents']))
        if CommandEnter == 'cp AdminTracker.exe':
            for i in range(100):
                time.sleep(.1)
                sys.stdout.write("\r%d%%" % i)
                sys.stdout.flush()
                print('Copying file...')
            time.sleep(x)
            for i in range(100):
                time.sleep(.1)
                sys.stdout.write("\r%d%%" % i)
                sys.stdout.flush()
                print('Pasting file...')
            addedFiles.append('AdminTracker.exe\n')
        CommandEnter = input('Jack@ArouraTesting/Bin~$ ')
        if CommandEnter == 'cp FirewallCracker.exe':
            for i in range(100):
                time.sleep(.1)
                sys.stdout.write("\r%d%%" % i)
                sys.stdout.flush()
                print('Copying file...')
            time.sleep(x)
            for i in range(100):
                time.sleep(.1)
                sys.stdout.write("\r%d%%" % i)
                sys.stdout.flush()
                print('Pasting file...')
            addedFiles.append('FirewallCracker.exe\n')

            CommandEnter = input('Jack@ArouraTesting/Bin~$ ')
            if CommandEnter == 'dc':
                CommandEnter = input(f'{sourceProgram}~$ ')
                if CommandEnter == 'Mail':
                    print("Yo, have you got the software ive asked for?")
                    CommandEnter = input(f'{sourceProgram}~$ ')
                    if CommandEnter == 'reply -file':
                        email_reply = input('Enter the first file: ')
                        if email_reply == 'AdminTracker.exe':
                            print('File added')
                        email_reply = input('Enter the second file: ')
                        if email_reply == 'FirewallCracker.exe':
                            print('File added')
                            time.sleep(2)
                        print('Yo, thanks for the files, ive added £500 to you bank account')
                        bank_account.append(500)

    elif CommandEnter == 'cd Documents':
        CommandEnter = input('Jack@ArouraTesting/Documents~$ ')
        if CommandEnter == 'ls':
            print(data['directories']['Mission1']['Document-Contents'])
        CommandEnter = input('Jack@ArouraTesting/Documents~$ ')
        if CommandEnter == 'cat README.txt':
            print("Stop Snooping Around Hacker!")
            #create system corrupt

def ssh_adam():
    pass

Main()
