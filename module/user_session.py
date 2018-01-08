from flask_login import LoginManager
class user_session(UserMixin):
    def __init__(self, email, id, active=True):
        self.email = email
        self.id = id
        self.active = active

    def is_active(self):
        # Here you should write whatever the code is
        # that checks the database if your user is active
        return self.active

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True