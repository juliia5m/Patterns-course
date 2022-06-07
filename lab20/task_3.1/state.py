from __future__ import annotations
from abc import ABC, abstractmethod



class State(ABC):
    @abstractmethod
    def play(self, media_player):
        pass

    @abstractmethod
    def pause(self, media_player):
        pass

    @abstractmethod
    def stop(self, media_player):
        pass

    @staticmethod
    def next(media_player):

        if media_player.cur_track_num() < len(media_player.get_tracks()) - 1:
            media_player.set_state(PlayingState())
            media_player.set_cur_track_num(media_player.cur_track_num() + 1)
            curr = media_player.cur_track()
            print(f'next: {curr}')
        else:
            print('it"s a final track')

    @staticmethod
    def prev(media_player):

        if media_player.cur_track_num() > 0:
            media_player.set_state(PlayingState())
            media_player.set_cur_track_num(media_player.cur_track_num() - 1)
            curr = media_player.cur_track()
            print(f'Play previous: {curr}')
        else:
            print('It"s the first track')


class PauseState(State):
    def play(self, media_player):
        media_player.set_state(PlayingState())
        curr = media_player.cur_track()
        print(f'continue: {curr}')

    def pause(self, media_player):
        pass

    def stop(self, media_player):
        media_player.set_state(StoppedState())
        curr = media_player.cur_track()
        print(f'Stop: {curr}')


class PlayingState(State):
    def play(self, media_player):
        pass

    def pause(self, media_player):
        media_player.set_state(PauseState())
        curr = media_player.cur_track()
        print(f'Pause: {curr}')

    def stop(self, media_player):
        media_player.set_state(StoppedState())
        curr = media_player.cur_track()
        print(f'Stop: {curr}')


class StoppedState(State):
    def play(self, media_player):
        media_player.set_state(PlayingState())
        curr = media_player.cur_track()
        print(f'Play: {curr}')

    def pause(self, media_player):
        pass

    def stop(self, media_player):
        pass