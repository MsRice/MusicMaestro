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

    @classmethod
    def game_of_10(cls):
        query = "SELECT * FROM songs ORDER BY  rand() LIMIT 10;"

        results = connectToMySQL('music_maestro_schema').query_db(query)

        return results

    @classmethod
    def question_fluff(cls, data):
        query = "SELECT * FROM songs WHERE NOT id = %(id)s ORDER BY  rand() LIMIT 3;"

        results = connectToMySQL('music_maestro_schema').query_db(query, data)

        return results

    @classmethod
    def get_leaderboard(cls):
        query = "SELECT users.id , first_name ,last_name ,score , messages.comment, messages.id as message_id FROM users \
            LEFT JOIN messages ON users.id = user_id;"

        results = connectToMySQL('music_maestro_schema').query_db(query)

        return results

    @classmethod
    def add_score(cls, data):
        query = "SELECT score FROM users WHERE id = %(id)s;"

        score = connectToMySQL('music_maestro_schema').query_db(query, data)

        x = data['score'] + score[0]['score']
        data['score'] = x

        query1 = "UPDATE users \
            SET score = %(score)s \
                WHERE id = %(id)s;"

        connectToMySQL('music_maestro_schema').query_db(query1, data)
