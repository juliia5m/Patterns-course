from abc import ABC, abstractmethod
from enum import Enum


class Groups(Enum):
    User = 'user'
    Admin = 'administrator'
    Moderator = 'moderator'


class User(ABC):
    @abstractmethod
    def send_message(self, message, to):
        pass

    @abstractmethod
    def send_(self, message):
        pass

    @abstractmethod
    def send_group(self, message, group):
        pass

    @abstractmethod
    def receive_message(self, message, fromm):
        pass


class User1(User):
    def __init__(self, name, username, group = Groups.User):

        self._name = name
        self._username = username
        self._group = group
        self._chat = None


    def set_chat(self, chat):
        self._chat = chat

    @property
    def username(self):
        return self._username

    @property
    def name(self):
        return self._name

    @property
    def group(self):
        return self._group

    def send_message(self, message, user_to):
        self._chat.send_message(message, self._username, user_to)

    def send_(self, message):
        self._chat.send_(message, self._username)

    def send_group(self, message, group):
        self._chat.send_group(message, self._username, group)

    def receive_message(self, message, user_from):
        print(f'{str(self)} from {user_from}:"{message}"')

    def __str__(self):
        return f'{self._username} in ({self._group})'