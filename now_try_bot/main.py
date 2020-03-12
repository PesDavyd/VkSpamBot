import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import bot_connect


def clear(rows):
    row = 0
    while row < rows:
        print('\n')
        row += 1


def vk_spammer_hello():
    clear(20)
    print('\t\t\t\tVkSpammer')
    clear(5)
    print('\t\t\t Write --help for open helper-list')
    clear(4)


def attack():
    start = bot_connect.attack()
    start.attack()


_help_ = '\t Write --help for open helper-list'

commands = [
    '--help',
    '--start-attack',
    '--stop',
    '--clear',
    '--exit',
]

helper_list = [
    '\t' + commands[0] + '\topen helper-list\n',
    '\t' + commands[1] + '\tstart spam-attack on target\n',
    '\t' + commands[2] + '\tstop attack\n',
    '\t' + commands[3] + '\tclear console\n',
    '\t' + commands[4] + '\texit from VkSpammer',
]

vk_spammer_hello()

command = ''

while command != '--exit':
    command = input('>>\t')
    while command not in commands:
        print(_help_)
        command = input('>>\t')

    if command == commands[0]:
        for i in helper_list:
            print(i)


    if command == commands[1]:
        # target_id = input('>>\t', 'input target id')
        attack()

    if command == commands[2]:
        None

    if command == commands[3]:
        vk_spammer_hello()

    # clear(10)



clear(20)
