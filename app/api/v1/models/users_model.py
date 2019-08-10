import json
from werkzeug.security import generate_password_hash
from app.api.v1.models.database import Database


class UsersModel(Database):
    """Add a new user and retrieve User(s) by Username, or Email."""

    def __init__(self, firstname=None, lastname=None, phone=None, username=None, email=None, password=None):
        super().__init__()
        self.firstname = firstname
        self.lastname = lastname
        self.phone = phone
        self.username = username
        self.email = email
        if password:
            self.password = generate_password_hash(password)

    def save(self):
        """Save information of the new user."""
        self.curr.execute(
            ''' INSERT INTO users(firstname, lastname, phone, username, email, password)\
                VALUES('{}','{}','{}','{}','{}','{}') RETURNING firstname, lastname, phone, username, email, password''' \
                .format(self.firstname, self.lastname, self.phone,  self.username, self.email, self.password))
        user = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return json.dumps(user, default=str)

    def get_username(self, username):
        """Request a single user with specific Username."""
        self.curr.execute(""" SELECT * FROM users WHERE username=%s""", (username,))
        user = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return json.dumps(user, default=str)

    def get_email(self, email):
        """Request a single user with specific Email Address."""
        self.curr.execute(''' SELECT * FROM users WHERE email=%s''', (email,))
        user = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return json.dumps(user, default=str)

    def get_phone(self, phone):
        """Request a single user with specific Email Address."""
        self.curr.execute(''' SELECT * FROM users WHERE phone=%s''', (phone,))
        user = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return json.dumps(user, default=str)
