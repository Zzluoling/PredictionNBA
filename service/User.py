from flask_login import LoginManager, UserMixin, login_user, login_required, current_user
from config import cursor

login_manager = LoginManager()


class User(UserMixin):
    def __init__(self, id="000", username="000", password="000"):
        self.id = id
        self.username = username
        self.password = password

    @staticmethod
    def getUserById(userid):
        sql = "SELECT * FROM user WHERE id = %s"
        cursor.execute(sql, userid)
        user = cursor.fetchone()
        if user is None:
            return None
        else:
            return User(user[0], user[1], user[2])

    @staticmethod
    def getUserByPassword(username, password):
        sql = "SELECT * FROM user WHERE username = %s AND password = %s"
        cursor.execute(sql, (username, password))
        user = cursor.fetchone()
        if user is None:
            return None
        else:
            return User(user[0], user[1], user[2])


@login_manager.user_loader
def load_user(user_id):
    return User.getUserById(user_id)
