import json

from utils.v1.dummy import new_account, new_hotel, wrong_hotels_keys

from .base_test import BaseTest


class TestHotels(BaseTest):
    """Testing that a registered user can book a hotel."""
    def test_add_hotel(self):
        """A user can book a hotel."""
        response1 = self.client.post(
            '/api/v1/auth/register', data=json.dumps(new_account), content_type='application/json',
            headers=self.get_token())
        response = self.client.post(
            '/api/v1/hotels', data=json.dumps(new_hotel), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'You have successfully booked the hotel!')
        assert response.status_code == 201

    def test_method_not_allowed(self):
        """Test method not allowed."""

        response = self.client.put(
            '/api/v1/hotels', data=json.dumps(new_hotel), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'method not allowed')
        assert response.status_code == 405

    def test_unexisting_hotelUrl(self):
        """Test when unexisting url is provided."""

        response = self.client.get(
            '/api/v1/hotel')
        result = json.loads(response.data.decode())
        assert response.status_code == 404
        assert result['message'] == "resource not found"

    def test_hotel_keys(self):
        """Test book hotel json keys."""

        response1 = self.client.post(
            '/api/v1/auth/register', data=json.dumps(new_account), content_type='application/json',
            headers=self.get_token())
        response = self.client.post(
            '/api/v1/hotels', data=json.dumps(wrong_hotels_keys), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'Invalid name key')
        assert response.status_code == 400

    def test_get_hotels(self):
        """Test fetching all hotels that have been booked."""

        response = self.client.post(
            '/api/v1/hotels', data=json.dumps(new_hotel), content_type='application/json',
            headers=self.get_token())
        response1 = self.client.get(
            '/api/v1/hotels', content_type='application/json', headers=self.get_token())
        result = json.loads(response1.data.decode())
        self.assertEqual(result['message'],
                         "success")
        assert response1.status_code == 200

    def test_get_hotel(self):
        """Test getting a hotel by username."""

        response1 = self.client.post(
            '/api/v1/hotels', data=json.dumps(new_hotel), content_type='application/json',
            headers=self.get_token())
        response = self.client.get(
            '/api/v1/hotels/savannah', content_type='application/json', headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'],
                         'success')
        assert response.status_code == 200

    def test_get_unexisting_hotel(self):
        """Test getting an unexisting hotel."""

        response = self.client.get(
            '/api/v1/hotels/savannah', content_type='application/json', headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'],
                         'hotel not found')
        assert response.status_code == 404
