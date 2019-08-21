import json
from werkzeug.security import generate_password_hash
from app.api.v1.models.database import Database
from datetime import datetime
import psycopg2


class LodgesModel(Database):
    """A registered user can book a new lodge."""

    def __init__(self, booked_by=None, hotel_name=None, lodge_no=None, status="Booked"):
        super().__init__()
        self.booked_by = booked_by
        self.hotel_name = hotel_name
        self.lodge_no = lodge_no
        self.status = status
        self.date = datetime.now()

    def save(self):
        """Save information of the lodge."""

        try:
            self.curr.execute(
                ''' INSERT INTO lodges(booked_by, hotel_name, lodge_no, status, date)\
                    VALUES('{}','{}',{},'{}','{}') RETURNING booked_by, hotel_name, lodge_no, status, date''' \
                    .format(self.booked_by, self.hotel_name, self.lodge_no, self.status, self.date))
            lodge = self.curr.fetchone()
            self.conn.commit()
            self.curr.close()
            return lodge


            query = """
					SELECT users.username, hotels.name FROM lodges\
					INNER JOIN users ON lodges.booked_by=users.user_id\
                    INNER JOIN hotels ON lodges.hotel_name=hotels.hotel_id;
					"""

            lodge = self.curr.fetchall()

            self.curr.execute(query)
            self.conn.commit()
            self.curr.close()

            return json.dumps(lodge, default=str)
        except psycopg2.IntegrityError:
            return "error"

    def get_lodges(self):
        """Fetch all lodges."""

        query = "SELECT * from lodges"
        lodges = Database().fetch(query)
        return json.dumps(lodges, default=str)

    def get_lodge(self, booked_by):
        """Get a lodge with specific username."""

        self.curr.execute(''' SELECT * FROM lodges WHERE booked_by=%s''', (booked_by,))
        lodge = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return json.dumps(lodge, default=str)

    def get_lodge_by_id(self, lodge_id):
        """Get a lodge with specific id."""

        self.curr.execute(''' SELECT * FROM lodges WHERE lodge_id=%s''', (lodge_id,))
        trip = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return trip

    def cancel(self, lodge_id):
        """ cancel a specific lodge."""
        self.curr.execute(
            """
        UPDATE lodges SET status=%s WHERE lodge_id=%s
        """, ('Cancelled', lodge_id))

        self.conn.commit()
        self.curr.close()

    def complete(self, lodge_id):
        """ complete a specific lodge."""
        self.curr.execute(
            """
        UPDATE lodges SET status=%s WHERE lodge_id=%s
        """, ('Completed', lodge_id))

        self.conn.commit()
        self.curr.close()

    def activate(self, lodge_id):
        """ activate a booked lodge."""
        self.curr.execute(
            """
        UPDATE lodges SET status=%s WHERE lodge_id=%s
        """, ('Active', lodge_id))

        self.conn.commit()
        self.curr.close()
