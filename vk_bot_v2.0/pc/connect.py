import vk_api
from vk_api.longpoll import VkLongPoll



class Attack(vk_api.VkApi):
    def __init__(self):
        self.token = '0740fac27ff8a970964df25d0888295c6773ee48eb86ce9d23d4229fc8e86e8939b3fc4754f7b51d09c7c'
        self.connect = None
        self.text = None
        self.id = None
        self.count = None
        self.i = 0

    def write_msg(self, random_id, text, id):
        self.connect.method('messages.send', {'user_id': id, 'message': text, 'random_id': random_id})


    def attack(self, text, id, count):
        self.connect = vk_api.VkApi(token=self.token)

        print("""\t\t======================================\n
           \t\t!!!Attack started!!!\n\t\t
                ======================================""")
        while self.i < count:
            self.write_msg(self.i, text, id)
            self.i += 1
            
            print("""
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n             
===================================
||                   ||          
||  text of message  || """ + str(text) + """ 
||                   ||          
===================================
||                   ||          
|| writed messages   ||  """ + str(self.i) + """ / """ + str(count) + """
||                   ||          
===================================
\n\n\n\n
""")

        print('\n\nAttack complite!\n\n')