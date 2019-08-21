import json
from werkzeug.security import generate_password_hash
from app.api.v1.models.database import Database
from datetime import datetime
import psycopg2


class HotelsModel(Database):
    """A registered user can book a hotel."""

    def __init__(self, name=None, location=None, lodges=None, conference_rooms=None, img_url=None, category=None):
        super().__init__()
        self.name = name
        self.location = location
        self.lodges = lodges
        self.conference_rooms = conference_rooms
        self.img_url = img_url
        self.category = category
        self.date = datetime.now()

    def save(self):
        """Save information of the hotel."""

        self.curr.execute(
            ''' INSERT INTO hotels(name, location, lodges, conference_rooms, img_url, category, date)\
                VALUES('{}','{}','{}','{}','{}','{}','{}') RETURNING name, location, lodges, conference_rooms, img_url, category, date''' \
                .format(self.name, self.location, self.lodges, self.conference_rooms, self.img_url, self.category, self.date))
        hotel = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return json.dumps(hotel, default=str)

    def get_hotels(self):
        """Fetch all hotels."""

        query = "SELECT * from hotels"
        hotels = Database().fetch(query)
        return json.dumps(hotels, default=str)

    def get_hotel(self, name):
        """Get a hotel with specific name."""

        self.curr.execute(''' SELECT * FROM hotels WHERE name=%s''', (name,))
        hotel = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return json.dumps(hotel, default=str)
