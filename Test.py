import sys
import time
import os
import sys
import json

# bank_acc = 0
# bank_acc = bank_acc + 500
# print(bank_acc)

with open("Directories.json", "r") as read_file:
    data = json.load(read_file)

print('\n'.join(data['directories']['Mission1']['Jacks-Computer']['Documents']['Bin']['Bin-Contents']))


#
# x = .5
# files = ['email.txt']
# addedFiles = []
#
# directories = {
#   "Johns-Computer":{
#     'Documents':{
#         "Document-Contents": "Email.txt"
#     },
#     "Downloads": "",
#     "Desktop":{
#         "Desktop-Contents":{
#             "README.txt"
#         }
#     }
#   }
# }
#
# CommandEnter = input('john@johny12/Home~$ ')
#
# if CommandEnter == 'ls':
#     print('\n'.join(directories['Johns-Computer']))
#
# print('Now you must change the directory so that you are in the Documents folder\n')
#
# CommandEnter = input('john@johny12/Home~$ ')
#
# if CommandEnter == 'cd Documents':
#     print()
#     CommandEnter = input('john@johny12/Documents~$ ')
#     if CommandEnter == 'ls':
#         print(''.join(directories['Johns-Computer']['Documents']['Document-Contents']), '\n')
# elif CommandEnter == 'cd ..':
#     CommandEnter = input('john@johny12/Home~$ ')
#     if CommandEnter == 'cd Desktop':
#         print()
#         CommandEnter = input('john@johny12/Desktop~$ ')
#         if CommandEnter == 'ls':
#             print(''.join(directories['Johns-Computer']['Desktop']['Desktop-Contents']), '\n')
