import os

import psycopg2
from psycopg2.extras import RealDictCursor


class Database:
    """Initialization."""

    def __init__(self):
        self.db_name = os.getenv('DB_NAME')
        self.db_host = os.getenv('DB_HOST')
        self.db_user = os.getenv('DB_USER')
        self.db_password = os.getenv('DB_PASSWORD')
        self.conn = psycopg2.connect(database=self.db_name, host=self.db_host, user=self.db_user, password=self.db_password)
        self.curr = self.conn.cursor(cursor_factory=RealDictCursor)

    def create_table(self):
        """Create tables."""
        queries = [
            """
            CREATE TABLE IF NOT EXISTS users(
                user_id serial PRIMARY KEY,
                firstname varchar NOT NULL,
                lastname varchar NOT NULL,
                phone varchar NOT NULL,
                username varchar NOT NULL,
                email varchar NOT NULL,
                password varchar NOT NULL
            )""",
            """
            CREATE TABLE IF NOT EXISTS hotels(
                hotel_id serial UNIQUE,
                name varchar NOT NULL,
                location varchar NOT NULL,
                lodges varchar NOT NULL,
                conference_rooms varchar NOT NULL,
                img_url varchar NOT NULl,
                category varchar NOT NULL
            )""",
            """
            CREATE TABLE IF NOT EXISTS trips(
                trip_id serial UNIQUE,
                booked_by integer NOT NULl DEFAULT 0,
                pickup varchar NOT NULL,
                destination varchar NOT NULL,
                means varchar NOT NULL,
                status varchar NOT NULL, 
                CONSTRAINT booked_by_fk FOREIGN KEY(booked_by) REFERENCES users(user_id),
                CONSTRAINT trip_composite_key PRIMARY KEY(booked_by)
            )""",
            """
            CREATE TABLE IF NOT EXISTS lodges(
                lodge_id serial UNIQUE,
                booked_by integer NOT NULl DEFAULT 0,
                hotel_name integer NOT NULl DEFAULT 0,
                lodge_no integer NOT NULL,
                CONSTRAINT booked_by_fk FOREIGN KEY(booked_by) REFERENCES users(user_id),
                CONSTRAINT hotel_name_fk FOREIGN KEY(hotel_name) REFERENCES hotels(hotel_id),
                CONSTRAINT lodge_composite_key PRIMARY KEY(booked_by,hotel_name)
            )"""

        ]
        try:
            for query in queries:
                self.curr.execute(query)
            self.conn.commit()
            self.curr.close()
        except Exception as e:
            return e

    def fetch(self, query):
        """Manipulate query."""

        self.curr.execute(query)
        fetch_all = self.curr.fetchall()
        self.conn.commit()
        self.curr.close()
        return fetch_all

    def destroy_table(self):
        """Destroy tables"""
        users = "DROP TABLE IF EXISTS  users CASCADE"
        trips = "DROP TABLE IF EXISTS  trips CASCADE"
        lodges = "DROP TABLE IF EXISTS  lodges CASCADE"
        hotels = "DROP TABLE IF EXISTS  hotels CASCADE"
        queries = [users, trips, lodges, hotels]
        try:
            for query in queries:
                self.curr.execute(query)
            self.conn.commit()
            self.curr.close()
        except Exception as e:
            return e

if __name__ == '__main__':
    Database().destroy_table()
    Database().create_table()
