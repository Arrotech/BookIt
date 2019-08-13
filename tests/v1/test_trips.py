import json

from utils.v1.dummy import new_account, new_trip, wrong_trips_keys, wrong_trip_booked_by_input,\
new_trip2

from .base_test import BaseTest


class TestTrips(BaseTest):
    """Testing that a registered can book a new trip."""
    def test_book_trip(self):
        """A user can book a new trip."""
        response1 = self.client.post(
            '/api/v1/auth/register', data=json.dumps(new_account), content_type='application/json',
            headers=self.get_token())
        response = self.client.post(
            '/api/v1/trips', data=json.dumps(new_trip), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'You have successfully booked the trip!')
        assert response.status_code == 201

    def test_book_trip_for_unexisting_user(self):
        """Test that unregistered user cannot book a trip."""

        response = self.client.post(
            '/api/v1/trips', data=json.dumps(new_trip2), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'Please check your input and try again!')
        assert response.status_code == 400

    def test_trips_keys(self):
        """Test book trips json keys."""

        response1 = self.client.post(
            '/api/v1/auth/register', data=json.dumps(new_account), content_type='application/json',
            headers=self.get_token())
        response = self.client.post(
            '/api/v1/trips', data=json.dumps(wrong_trips_keys), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'Invalid booked_by key')
        assert response.status_code == 400

    def test_trip_booked_by_input(self):
        """Test the format of the booked_by input"""

        response1 = self.client.post(
            '/api/v1/auth/register', data=json.dumps(new_account), content_type='application/json',
            headers=self.get_token())
        response = self.client.post(
            '/api/v1/trips', data=json.dumps(wrong_trip_booked_by_input), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'only positive integer is accepted')
        assert response.status_code == 400

    def test_get_trips(self):
        """Test fetching all trips that have been created."""

        response = self.client.post(
            '/api/v1/trips', data=json.dumps(new_trip), content_type='application/json',
            headers=self.get_token())
        response1 = self.client.get(
            '/api/v1/trips', content_type='application/json', headers=self.get_token())
        result = json.loads(response1.data.decode())
        self.assertEqual(result['message'],
                         "success")
        assert response1.status_code == 200

    def test_get_trip(self):
        """Test getting a trip by username."""

        response1 = self.client.post(
            '/api/v1/trips', data=json.dumps(new_trip), content_type='application/json',
            headers=self.get_token())
        response = self.client.get(
            '/api/v1/trips/1', content_type='application/json', headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'],
                         'success')
        assert response.status_code == 200

    def test_get_unexisting_trip(self):
        """Test getting an unexisting trip."""

        response = self.client.get(
            '/api/v1/trips/1', content_type='application/json', headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'],
                         'trip not found')
        assert response.status_code == 404
