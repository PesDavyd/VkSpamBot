import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


connect = vk_api.VkApi(login='89998403102', password='censured', scope='messages')
connect.auth()

longpoll = VkLongPoll(connect)
connect.method('message.send', {'user_id': '222196128', 'message': 'spam'})