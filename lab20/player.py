from __future__ import annotations
from state import StoppedState


class MediaPlayer:
    def __init__(self):
        self._state = StoppedState()
        self._tracks = []
        self._cur_track = 0

    def cur_track(self):
        cur = self._tracks[self._cur_track]
        return cur

    def set_cur_track_num(self, track_num):
        if track_num >= 0 and track_num < len(self._tracks):
            self._cur_track = track_num
        else:
            print('wrong ranges')

    def cur_track_num(self):
        return self._cur_track

    def get_tracks(self):
        return self._tracks

    def add_track(self, track):
        self._tracks.append(track)

    def set_state(self, state):
        self._state = state

    def get_state(self):
        return self._state

    def play(self):
        self._state.play(self)

    def pause(self):
        self._state.pause(self)

    def stop(self):
        self._state.stop(self)

    def next(self):
        self._state.next(self)

    def prev(self):
        self._state.prev(self)