import vk_api
import connect
from vk_api.longpoll import VkLongPoll, VkEventType


def clear(rows):
    row = 0
    while row < rows:
        print('\n')
        row += 1

def hello():
    clear(25)
    print('\n=======================================\n')
    print("\t\tVkSpamBot")
    print('\n=======================================\n')
    print("   Write --help for open help list\n\n")

def attack():
    id = input("Input target id:  ")
    text = input("Input attack message: ")
    count = int(input("Input count of messages:  "))
    attck = connect.Attack()
    attck.attck(text, id, count)


hello()

commands = [
    '--help',
    '--start-attack',
    '--clear',
    '--exit'
]

helper_list = [
    '  ' + commands[0] + '    open helper-list\n',
    '  ' + commands[1] + '    start spam-attack on target\n',
    '  ' + commands[2] + '    clear console\n',
    '  ' + commands[3] + '    exit from VkSpammer',
]


command = None

while command != '--exit':
    command = input('>>\t ')

    if command == commands[0]:
        clear(15)
        for i in helper_list:
            print(i)

    if command == commands[1]:
        try:
            attack()

        except:
            print('\n Attack krashed! Try now!\n\n')

    if command == commands[2]:
        clear(25)

    if command not in commands:
        print('\n>>   Write --help fo view all commands\n\n')

clear(25)
