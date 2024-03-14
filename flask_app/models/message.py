from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Message:
    def __init__(self, data):
        self.id = data['id']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def post_msg(cls, data):
        query = "UPDATE messages \
            SET comment = %(comment)s \
                WHERE id = %(id)s;"

        connectToMySQL('music_maestro_schema').query_db(query, data)
