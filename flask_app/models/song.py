from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Song:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.artist = data['artist']
        self.release_date = data['release_date']
        self.genre = data['genre']
        self.cover_link = data['cover_link']
        self.track_link = data['track_link']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
