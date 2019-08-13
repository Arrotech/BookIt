import json
from werkzeug.security import generate_password_hash
from app.api.v1.models.database import Database
import datetime
import psycopg2


class TripsModel(Database):
    """A registered user can book a new trip."""

    def __init__(self, booked_by=None, pickup=None, destination=None, means=None):
        super().__init__()
        self.booked_by = booked_by
        self.pickup = pickup
        self.destination = destination
        self.means = means

    def save(self):
        """Save information of the trip."""

        try:
            self.curr.execute(
                ''' INSERT INTO trips(booked_by, pickup, destination, means)\
                    VALUES('{}','{}','{}','{}') RETURNING booked_by, pickup, destination, means''' \
                    .format(self.booked_by, self.pickup, self.destination, self.means))
            trip = self.curr.fetchone()
            self.conn.commit()
            self.curr.close()
            return trip


            query = """
					SELECT users.username FROM trips\
					INNER JOIN users ON trips.booked_by=users.user_id;
					"""

            trip = self.curr.fetchall()

            self.curr.execute(query)
            self.conn.commit()
            self.curr.close()

            return json.dumps(trip, default=str)
        except psycopg2.IntegrityError:
            return "error"

    def get_trips(self):
        """Fetch all trips."""

        query = "SELECT * from trips"
        trips = Database().fetch(query)
        return json.dumps(trips, default=str)

    def get_trip(self, booked_by):
        """Get a trip with specific username."""

        self.curr.execute(''' SELECT * FROM trips WHERE booked_by=%s''', (booked_by,))
        trip = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return json.dumps(trip, default=str)
