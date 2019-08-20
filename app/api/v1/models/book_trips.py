import json
from werkzeug.security import generate_password_hash
from app.api.v1.models.database import Database
import datetime
import psycopg2


class TripsModel(Database):
    """A registered user can book a new trip."""

    def __init__(self, booked_by=None, pickup=None, destination=None, means=None, status="Booked"):
        super().__init__()
        self.booked_by = booked_by
        self.pickup = pickup
        self.destination = destination
        self.means = means
        self.status = status

    def save(self):
        """Save information of the trip."""

        try:
            self.curr.execute(
                ''' INSERT INTO trips(booked_by, pickup, destination, means, status)\
                    VALUES('{}','{}','{}','{}','{}') RETURNING booked_by, pickup, destination, means, status''' \
                    .format(self.booked_by, self.pickup, self.destination, self.means, self.status))
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

    def get_trip_by_id(self, trip_id):
        """Get a trip with specific id."""

        self.curr.execute(''' SELECT * FROM trips WHERE trip_id=%s''', (trip_id,))
        trip = self.curr.fetchone()
        self.conn.commit()
        self.curr.close()
        return trip

    def cancel(self, trip_id):
        """ cancel a specific trip."""
        self.curr.execute(
            """
        UPDATE trips SET status=%s WHERE trip_id=%s
        """, ('Cancelled', trip_id))

        self.conn.commit()
        self.curr.close()

    def complete(self, trip_id):
        """ complete a specific trip."""
        self.curr.execute(
            """
        UPDATE trips SET status=%s WHERE trip_id=%s
        """, ('Completed', trip_id))

        self.conn.commit()
        self.curr.close()

    def progress(self, trip_id):
        """ mark a specific trip in progress."""
        self.curr.execute(
            """
        UPDATE trips SET status=%s WHERE trip_id=%s
        """, ('In progress', trip_id))

        self.conn.commit()
        self.curr.close()
