from abc import ABC, abstractmethod
from users_groups import Groups


class Mediator(ABC):
    @abstractmethod
    def send_message(self, message, user_from, user_to):
        pass

    @abstractmethod
    def send_(self, message, user_from):
        pass

    @abstractmethod
    def send_group(self, message, user_from, group):
        pass


class Chat(Mediator):
    def __init__(self):
        self._users = {}
        self._groups_dict = { group.value: set() for group in Groups}

    def add_user(self, user):
        self._users.setdefault(user.username, user)
        self._groups_dict[user.group.value].add(user)
        user.set_chat(self)

    def add_users(self, users):
        for user in users:
            self.add_user(user)

    def send_message(self, message, user_from, user_to):
        if user_from != user_to:
            receiver = self._users.get(user_to)
            receiver.receive_message(message, user_from)

    def send_(self, message, user_from):
        for receiver in self._users.values():
            if receiver.username == user_from:
                continue
            receiver.receive_message(message, user_from)

    def send_group(self, message, user_from, group):
        for receiver in self._groups_dict[group]:
            if receiver.username == user_from:
                continue
            receiver.receive_message(message, user_from)
