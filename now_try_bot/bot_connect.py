import vk_api
from vk_api.longpoll import VkLongPoll




# token_list = [
#     '0740fac27ff8a970964df25d0888295c6773ee48eb86ce9d23d4229fc8e86e8939b3fc4754f7b51d09c7c'
# ]




class attack(vk_api.VkApi):
    def __init__(self):
        self.token = '0740fac27ff8a970964df25d0888295c6773ee48eb86ce9d23d4229fc8e86e8939b3fc4754f7b51d09c7c'
        self.connect = None
        self.i = 0

    def write_msg(self, random_id):
        # self.connect.metgod('message_send', {'peer_id': 2557258913, 'message': 'attacked!'})
        self.connect.method('messages.send', {'user_id': 222196128, 'message': 'attacked!', 'random_id': random_id})


    def attack(self):
        self.connect = vk_api.VkApi(token=self.token)
        print('\n\t\t-----------------\n\t\t bot connected\n\t\t-----------------\n')

        print("""\t\t======================================\n
           \t\t\t!!!Attack started!!!\n\t\t
           ======================================""")
        while True:
            self.write_msg(self.i)
            self.i += 1
