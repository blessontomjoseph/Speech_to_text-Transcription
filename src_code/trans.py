import pytube
from pytube import YouTube
import os
import requests
import time

auth_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzE0NzU5NjAxLCJkYXRhIjp7ImVtYWlsIjoiYmxlc3NvbnRvbWpvc2VwaEBnbWFpbC5jb20iLCJyb2xlIjoicHJvdmlkZXIiLCJhcGlrZXkiOiIzYzM3MmViMi04MTNiLTQ5ZGQtYWYyZS02ODFhMDFkYzhmMWQiLCJyZWZlcmVuY2VLZXkiOiIzYzM3MmViMi04MTNiLTQ5ZGQtYWYyZS02ODFhMDFkYzhmMWQiLCJwbGFuVHlwZSI6ImRlZmF1bHQiLCJjb3VudHJ5IjoiSW5kaWEifSwiaWF0IjoxNjcxNDc1NjAwfQ.yknkfcje_WgDOIk588JyFXtoRLgyMKC6LA9jY0ztd0E"

def transcribe(url):
    video = YouTube(url)
    yt = video.streams.get_audio_only()
    yt.download()
    current_dir = os.getcwd()
    for file in os.listdir(current_dir):
        if file.endswith(".mp4"):
            name = file.split(' ')[0]
            file_path = os.path.join(current_dir, file)
            os.rename(file_path, os.path.join(current_dir, name+'.mp3'))
    file_name = name+".mp3"
    return file_name


def fileId(file_name):
    url = 'https://platform.neuralspace.ai/api/file/upload'
    headers = {'Authorization': auth_key}
    files = {'files': (file_name, open(file_name, 'rb'))}
    response = requests.post(url, headers=headers, files=files)
    return response.json()['data']['fileId']


def transcribeId(fieldId):
    url = 'https://platform.neuralspace.ai/api/transcription/v1/file/transcribe'
    headers = {'Authorization': auth_key,
                  'Content-Type': 'application/json'
                  }

    data = {"fileId": fieldId,
                "language": "en",
                "domain": "general-v3-united_kingdom-default"
                }
    response = requests.post(url, headers=headers, json=data)
    return response.json()['data']['transcribeId']


def text_output(transcribeId):
    """feltch transcription"""
    url = 'https://platform.neuralspace.ai/api/transcription/v1/single/transcription'
    params = {'transcribeId': transcribeId}
    headers = {'Authorization': auth_key}
    while True:
        response = requests.get(url, params=params, headers=headers)
        data = response.json()
        if data['data']['transcriptionStatus'] == 'Completed':
            break
        else:
            time.sleep(5)

    return data['data']['transcripts']
