from mongoframes import *
from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime
from tinytag import TinyTag
from PIL import Image
import os
import secrets
import lyricsgenius
import shutil
import io
import uuid

load_dotenv('.env')
Frame._client = MongoClient(os.getenv('DATABASE_URI'))
genius = lyricsgenius.Genius(os.getenv('LYRICSGENIUS_API_KEY'))

class User(Frame):
    _fields = {
      'name',
      'email',
      'password',
      'registration_date',
      'songs',
      'playlist'
    }

    def register(user):
        return User(**user).insert()

    def deactivate():
        pass

    def delete():
        pass

    def edit():
        pass



class Song(SubFrame):
    _fields = {
        'song_id',
        'artist',
        'song_title',
        'duration',
        'album',
        'release_date',
        'likes',
        'genre'
    }

    def add(user_id, song):
        pass
        #Song.get_cover_art(song)
        

    def get_cover_art(song):
        tag = TinyTag.get(f'uploads/songs/{song}', image=True)
        album_cover = tag.get_image()
        im = Image.open(io.BytesIO(album_cover))
        im.save(f'uploads/images/{song}.png')
        return tag

    def search():
        pass

    def get_lyrics():
        pass


    def delete():
        pass

    def edit():
        pass

    def retrieve_track():
        pass

    def retrieve_tracks():
        pass

class Playlist(SubFrame):
    _fields = {
        'playlist_id',
        'name',
        'genre',
        'availability',
        'songs',
        'likes',
        'fans'
    }
    def create():
        pass

    def delete():
        pass

    def edit():
        pass

    def retrieve_all():
        pass

    def retrieve():
        pass