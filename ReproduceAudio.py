import pathlib
import vlc
import os, random
import time
import Main

main = Main
vlc_instance = vlc.Instance()

def get_random_audio_file_to_reproduce():
     randomfile = random.choice(os.listdir(str(pathlib.Path().absolute()) + '/audio files'))
     play_audio_file(randomfile)
    
def play_audio_file(file_name):
    file_path = str(pathlib.Path().absolute()) + '/audio files/' + file_name
    print ("Playing audio: " + file_path)
    audio_to_play = vlc.MediaPlayer(file_path)
    audio_to_play.play()

def play_audio_file_online(file_id,file_name):
    print("playing: " + str(file_name))
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new("http://docs.google.com/uc?export=open&id="+file_id)
    player.set_media(media)
    player.play()
    time.sleep(1)
    duration = player.get_length() / 1000
    print("audio duration: " + str(duration))
    time.sleep(duration)
    main.check_if_someone_is_in_front_and_reproduce()
