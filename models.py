from mongoframes import *
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv('.env')
Frame._client = MongoClient(os.getenv('DATABASE_URI'))

class User(Frame):
    _fields = {
      'name',
      'email',
      'password',
      'registration_date',
      'songs',
      'playlist'
    }

class Song(SubFrame):
    _fields = {
        'artist',
        'song_title',
        'duration',
        'album',
        'release_date',
        'likes',
        'genre',
        'song_id'
    }

class Playlist(SubFrame):
    _fields = {
        'name',
        'genre',
        'availability',
        'songs',
        'likes',
        'fans'
    }