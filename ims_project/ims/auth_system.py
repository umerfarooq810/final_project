
# ims/auth_system.py

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def authenticate(self, password):
        return self.password == password
