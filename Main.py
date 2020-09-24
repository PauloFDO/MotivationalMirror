from __future__ import print_function
import pickle
import os.path
import pathlib
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.http import MediaIoBaseDownload
import auth
import io
import UltrasonicRanging
import ReproduceAudio
import random

ultra_sonic_measurement = UltrasonicRanging
reproduce_audio = ReproduceAudio
authentification_instance = auth.auth()
credentials = authentification_instance.get_credentials()
drive_service = build('drive', 'v3', credentials=credentials)

    
def list_files(numberOfFiles):
    # Call the Drive v3 API
    results = drive_service.files().list(
        pageSize=numberOfFiles, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            print(u'{0} ({1})'.format(item['name'], item['id']))

def download_file(file_id, file_name):
	
    file_path = str(pathlib.Path().absolute()) + '/audio files/' + file_name
    
    if (file_name.endswith('.mp3') or file_name.endswith('.m4a') or file_name.endswith('.wav')) and not os.path.isfile(filepath):
       print('download path: '  + file_path)
    
       request = drive_service.files().get_media(fileId=file_id)
       fh = io.BytesIO()
       downloader = MediaIoBaseDownload(fh, request)
       done = False
       
       while done is False:
         status, done = downloader.next_chunk()
         print("Download %d%%." % int(status.progress() * 100))
       with io.open(file_path,'wb') as f:
         fh.seek(0)
         f.write(fh.read())
    else:
        print('Nothing to download')

def get_a_single_random_file_from_cloud(number_of_files):
    # Call the Drive v3 API
    results = drive_service.files().list(
    page_size=number_of_files, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    while(True):
         random_item = random.choice(items)
        
         if random_item['name'].endswith('.mp3'):
                 reproduce_audio.play_audio_file_online(random_item['id'], random_item['name'])
                 break

def check_if_someone_is_in_front_and_reproduce():
    is_someone_in_front = ultra_sonic_measurement.start_distance_measurement()
    
    if is_someone_in_front:
       get_a_single_random_file_from_cloud(500)
            
if __name__ == '__main__':
    check_if_someone_is_in_front_and_reproduce()
