from flask import abort

class Post():
    LIST_POST = [
        {'id': 1, 'title': 'first post', 'content': 'this is my first post'},
        {'id': 2, 'title': 'second post', 'content': 'this is my second post'},
        {'id': 3, 'title': 'third post', 'content': 'this is my third post'},
        ]

    @classmethod
    def all(cls):
        return cls.LIST_POST

    @classmethod
    def find(cls, id):
        try:
            return cls.LIST_POST[int(id) -1]
        except IndexError:
            abort(404)


