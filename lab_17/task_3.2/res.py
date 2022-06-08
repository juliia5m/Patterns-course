from chat import Chat
from users_groups import Groups
from users_groups import User1


def res():
    chat = Chat()

    admin1 = User1(name='Admin 1', username='a_1', group=Groups.Admin)
    admin2 = User1(name='Admin 2', username='a_2', group=Groups.Admin)
    chat.add_users([admin1, admin2])

    moderator1 = User1(name='Moderator 1', username='m_1', group=Groups.Moderator)
    moderator2 = User1(name='Moderator 2', username='m_2', group=Groups.Moderator)

    chat.add_users([moderator1, moderator2])

    user1 = User1(name='User 1', username='u-1')
    user2 = User1(name='User 2', username='u-2')

    chat.add_users([user1, user2])

    user1.send_message('Hi :)', 'u-2')
    moderator2.send_group(":)...", group=Groups.Admin.value)
    admin2.send_("I am an admin ! How can I help you ?")


if __name__ == '__main__':
    res()
