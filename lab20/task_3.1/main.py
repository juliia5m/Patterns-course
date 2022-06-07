from player import MediaPlayer


def music():
    media_player = MediaPlayer()
    media_player.add_track(track='Airplane')
    media_player.add_track(track='Fire_starter')
    media_player.add_track(track='Marching_on')
    media_player.add_track(track='Saints_of_violence_and_innuendo')
    media_player.add_track(track='Radioactive')
    media_player.add_track(track='Outlaw')

    media_player.play()
    media_player.pause()
    media_player.play()
    media_player.next()
    media_player.next()
    media_player.stop()
    media_player.play()
    media_player.next()
    media_player.next()
    media_player.play()
    media_player.next()
    media_player.stop()


if __name__ == '__main__':
    music()
