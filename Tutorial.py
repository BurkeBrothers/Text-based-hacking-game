import time
import os
import sys
import Mission1
import json

x = .5
files = ['email.txt']
addedFiles = []

with open("Directories.json", "r") as read_file:
    data = json.load(read_file)

commands = {
    1:{
        'name': 'ftpsploit',
        'desc': 'Use this to hack website FTP services\nuse: ftpsploit [port] [website]\n'
    },
    2:{
        'name': 'ssh',
        'desc': 'Connect remotely to computers\nuse:ssh [name]@[password]'
    }
}

sourceProgram = 'HydraHack'
ftpAdminPassword = 'Admin'

def tutorial():
    print('Your first task is a test. Using your skills you must hack website that contains important data.\nThe website you are hacking is',
          'www.testhack.com.\n')
    print('You must then take the data and log into Johns account and get his email.\n')

    print("To start of you must hack the website using the command 'ftpsploit [port] [url]'\n")
    CommandEnter = input(f'{sourceProgram}~$ ')
    if CommandEnter == 'help':
        print(commands[1]['name'])
        print(commands[1]['desc'])
        print(commands[2]['name'])
        print(commands[2]['desc'])

    CommandEnter = input(f'{sourceProgram}~$ ')

    if CommandEnter == 'ftpsploit 21 www.testhack.com':
        print(f"{sourceProgram}: Ftp Exploit Initiated...")
        time.sleep(x)
        print(f'{sourceProgram}: File Transfer Protocole requires Admin Password...')
        time.sleep(x)
        ftpPasswordInput = input("FTP Admin Password: ")
        os.system('cls')
        if ftpPasswordInput == ftpAdminPassword:
            for i in range(100):
                time.sleep(.1)
                sys.stdout.write("\r%d%%" % i)
                sys.stdout.flush()
            print(f"\n{sourceProgram}: FTP Hack Successful...")

            print('Data Found:')
            time.sleep(x)
            print('| ID |   Name    |                      Passowrd                 |')
            print('|----|-----------|-----------------------------------------------|')
            print('| 1  |   John    |   64F97E29B987532F13FC0DF6D4033A98A152C0B7    |')
            print('|----|-----------|-----------------------------------------------|')
            print('| 2  |   Jack    |   Jack123                                     |')
            print('|----|-----------|-----------------------------------------------|')
            print('| 3  |   Admin   |   Admin                                       |')
            print("\nLuanch the cracking consoole with 'KrackerConsole'\n")
            CommandEnter = input(f'{sourceProgram}~$ ')
            if CommandEnter == 'krackerconsole':
                print("Now you need to crack the hashed password with 'krackHash -f -h [hashed password] optional[username]'")
                CommandEnter = input("KrackerConsole~$ ")
                if CommandEnter == 'krackHash -f -h 64F97E29B987532F13FC0DF6D4033A98A152C0B7':
                    os.system('cls')
                    for i in range(100):
                        time.sleep(.1)
                        sys.stdout.write("\r%d%%" % i)
                        sys.stdout.flush()
                    os.system('cls')
                    print("\nPassword = johny12")
                    time.sleep(x)
                    hack()
def hack():
    os.system('color a')
    print("Connect to Johns computer using 'ssh [username]@[password]'\n")

    CommandEnter = input(f'{sourceProgram}~$ ')

    if CommandEnter == 'ssh john@johny12':

        print("List the directories in 'Johns-Computer' using the 'ls' command\n")
        CommandEnter = input('john@johny12~$ ')

        if CommandEnter == 'ls':
            print('\n'.join(data['directories']['Tutorial']['Johns-Computer']))

        print('Now you must change the directory so that you are in the Documents folder\n')
        CommandEnter = input('john@johny12/Home~$ ')

        if CommandEnter == 'cd Documents':
            print()
            CommandEnter = input('john@johny12/Documents~$ ')
            if CommandEnter == 'ls':
                print(data['directories']['Johns-Computer']['Documents']['Document-Contents'])

        user_input = input('Do you want to continue? Y/N: ')
        if user_input == 'Y':
            print("Now you must view the 'email.txt' file using the command 'cat'\n")

        CommandEnter = input('john@johny12~$ ')

        if CommandEnter == 'cat email.txt':
                print('johny123@hotmail.co.uk\n')

        print("You now need to copy the file using the command 'cp [file]'\n")
        CommandEnter = input('john@johny12~$ ')

        if CommandEnter == 'cp email.txt':
                addedFiles.append('email.txt\n')

        print("Now you need to disconnect from his computer using the 'dc' command\n")
        CommandEnter = input('john@johny12~$ ')

        if CommandEnter == 'dc':
            CommandEnter = input(f'\n{sourceProgram}~$ ')

            if CommandEnter == 'ls':
                print(''.join(addedFiles))

            print("Now you need to send the client the file using the 'send [file] command'\n")

            CommandEnter = input(f'{sourceProgram}~$ ')

            if CommandEnter == 'send email.txt':
                print('Sent Message')
                time.sleep(2)
                print('Well done you completed the tutorial.')
                Mission1.Start()
