import json

from utils.v1.dummy import new_account, new_lodge, wrong_lodges_keys, wrong_lodge_booked_by_input,\
new_lodge2, new_hotel, wrong_lodge_hotel_name_input

from .base_test import BaseTest


class TestLodges(BaseTest):
    """Testing that a registered can book a new lodge."""
    def test_book_lodge(self):
        """A user can book a new lodge."""
        response1 = self.client.post(
            '/api/v1/auth/register', data=json.dumps(new_account), content_type='application/json',
            headers=self.get_token())
        response2 = self.client.post(
            '/api/v1/hotels', data=json.dumps(new_hotel), content_type='application/json',
            headers=self.get_token())
        response = self.client.post(
            '/api/v1/lodges', data=json.dumps(new_lodge), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'You have successfully booked the hotel!')
        assert response.status_code == 201

    def test_cancel_lodging(self):
        '''test cancelling an already booked lodge.'''

        response = self.client.post(
            '/api/v1/auth/register', data=json.dumps(new_account), content_type='application/json',
            headers=self.get_token())
        response3 = self.client.post(
            '/api/v1/hotels', data=json.dumps(new_hotel), content_type='application/json',
            headers=self.get_token())
        response1 = self.client.post(
            '/api/v1/lodges', data=json.dumps(new_lodge), content_type='application/json',
            headers=self.get_token())
        response2 = self.client.put(
            "/api/v1/lodges/cancel/1", content_type='application/json', headers=self.get_token())
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(json.loads(response2.data)['message'], "Lodging cancelled")

    def test_activate_lodging(self):
        '''test marking lodging active.'''

        response = self.client.post(
            '/api/v1/auth/register', data=json.dumps(new_account), content_type='application/json',
            headers=self.get_token())
        response3 = self.client.post(
            '/api/v1/hotels', data=json.dumps(new_hotel), content_type='application/json',
            headers=self.get_token())
        response1 = self.client.post(
            '/api/v1/lodges', data=json.dumps(new_lodge), content_type='application/json',
            headers=self.get_token())
        response2 = self.client.put(
            "/api/v1/lodges/activate/1", content_type='application/json', headers=self.get_token())
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(json.loads(response2.data)['message'], "Lodging is now activate")

    def test_complete_lodging(self):
        '''test completing lodging.'''

        response = self.client.post(
            '/api/v1/auth/register', data=json.dumps(new_account), content_type='application/json',
            headers=self.get_token())
        response3 = self.client.post(
            '/api/v1/hotels', data=json.dumps(new_hotel), content_type='application/json',
            headers=self.get_token())
        response1 = self.client.post(
            '/api/v1/lodges', data=json.dumps(new_lodge), content_type='application/json',
            headers=self.get_token())
        response2 = self.client.put(
            "/api/v1/lodges/complete/1", content_type='application/json', headers=self.get_token())
        self.assertEqual(response2.status_code, 200)
        self.assertEqual(json.loads(response2.data)['message'], "Lodging completed")

    def test_cancel_an_already_cancelled_lodging(self):
        '''test cancelling an already cancelled lodge.'''

        response = self.client.post(
            '/api/v1/auth/register', data=json.dumps(new_account), content_type='application/json',
            headers=self.get_token())
        response3 = self.client.post(
            '/api/v1/hotels', data=json.dumps(new_hotel), content_type='application/json',
            headers=self.get_token())
        response1 = self.client.post(
            '/api/v1/lodges', data=json.dumps(new_lodge), content_type='application/json',
            headers=self.get_token())
        response2 = self.client.put(
            "/api/v1/lodges/cancel/1", content_type='application/json', headers=self.get_token())
        response3 = self.client.put(
            "/api/v1/lodges/cancel/1", content_type='application/json', headers=self.get_token())
        self.assertEqual(response3.status_code, 400)
        self.assertEqual(json.loads(response3.data)['message'], "Lodging already Cancelled")

    def test_activating_lodging_that_is_already_active(self):
        '''test activating an already active lodging.'''

        response = self.client.post(
            '/api/v1/auth/register', data=json.dumps(new_account), content_type='application/json',
            headers=self.get_token())
        response3 = self.client.post(
            '/api/v1/hotels', data=json.dumps(new_hotel), content_type='application/json',
            headers=self.get_token())
        response1 = self.client.post(
            '/api/v1/lodges', data=json.dumps(new_lodge), content_type='application/json',
            headers=self.get_token())
        response2 = self.client.put(
            "/api/v1/lodges/activate/1", content_type='application/json', headers=self.get_token())
        response3 = self.client.put(
            "/api/v1/lodges/activate/1", content_type='application/json', headers=self.get_token())
        self.assertEqual(response3.status_code, 400)
        self.assertEqual(json.loads(response3.data)['message'], "Lodging already Active")

    def test_completing_an_already_completed_lodging(self):
        '''test completing an already completed lodging.'''

        response = self.client.post(
            '/api/v1/auth/register', data=json.dumps(new_account), content_type='application/json',
            headers=self.get_token())
        response3 = self.client.post(
            '/api/v1/hotels', data=json.dumps(new_hotel), content_type='application/json',
            headers=self.get_token())
        response1 = self.client.post(
            '/api/v1/lodges', data=json.dumps(new_lodge), content_type='application/json',
            headers=self.get_token())
        response2 = self.client.put(
            "/api/v1/lodges/complete/1", content_type='application/json', headers=self.get_token())
        response3 = self.client.put(
            "/api/v1/lodges/complete/1", content_type='application/json', headers=self.get_token())
        self.assertEqual(response3.status_code, 400)
        self.assertEqual(json.loads(response3.data)['message'], "Lodging already Completed")

    def test_cancel_unexisting_lodge(self):
        '''test cancelling unexisting lodge.'''

        response = self.client.post(
            '/api/v1/auth/register', data=json.dumps(new_account), content_type='application/json',
            headers=self.get_token())
        response3 = self.client.post(
            '/api/v1/hotels', data=json.dumps(new_hotel), content_type='application/json',
            headers=self.get_token())
        response3 = self.client.put(
            "/api/v1/lodges/cancel/1", content_type='application/json', headers=self.get_token())
        self.assertEqual(response3.status_code, 404)
        self.assertEqual(json.loads(response3.data)['message'], "Lodge not found")

    def test_completing_unexisting_lodge(self):
        '''test completing unexisting lodge.'''

        response = self.client.post(
            '/api/v1/auth/register', data=json.dumps(new_account), content_type='application/json',
            headers=self.get_token())
        response3 = self.client.post(
            '/api/v1/hotels', data=json.dumps(new_hotel), content_type='application/json',
            headers=self.get_token())
        response3 = self.client.put(
            "/api/v1/lodges/complete/1", content_type='application/json', headers=self.get_token())
        self.assertEqual(response3.status_code, 404)
        self.assertEqual(json.loads(response3.data)['message'], "Lodge not found")

    def test_activating_unexisting_lodge(self):
        '''test activating unexisting lodge.'''

        response = self.client.post(
            '/api/v1/auth/register', data=json.dumps(new_account), content_type='application/json',
            headers=self.get_token())
        response3 = self.client.post(
            '/api/v1/hotels', data=json.dumps(new_hotel), content_type='application/json',
            headers=self.get_token())
        response3 = self.client.put(
            "/api/v1/lodges/activate/1", content_type='application/json', headers=self.get_token())
        self.assertEqual(response3.status_code, 404)
        self.assertEqual(json.loads(response3.data)['message'], "Lodge not found")


    def test_lodges_keys(self):
        """Test book lodges json keys."""

        response1 = self.client.post(
            '/api/v1/auth/register', data=json.dumps(new_account), content_type='application/json',
            headers=self.get_token())
        response2 = self.client.post(
            '/api/v1/hotels', data=json.dumps(new_hotel), content_type='application/json',
            headers=self.get_token())
        response = self.client.post(
            '/api/v1/lodges', data=json.dumps(wrong_lodges_keys), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'Invalid booked_by key')
        assert response.status_code == 400

    def test_lodge_booked_by_input(self):
        """Test the format of the booked_by input"""

        response1 = self.client.post(
            '/api/v1/auth/register', data=json.dumps(new_account), content_type='application/json',
            headers=self.get_token())
        response2 = self.client.post(
            '/api/v1/hotels', data=json.dumps(new_hotel), content_type='application/json',
            headers=self.get_token())
        response = self.client.post(
            '/api/v1/lodges', data=json.dumps(wrong_lodge_booked_by_input), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'only positive integer is accepted')
        assert response.status_code == 400

    def test_lodge_hotel_name_input(self):
        """Test the format of the booked_by input"""

        response1 = self.client.post(
            '/api/v1/auth/register', data=json.dumps(new_account), content_type='application/json',
            headers=self.get_token())
        response2 = self.client.post(
            '/api/v1/hotels', data=json.dumps(new_hotel), content_type='application/json',
            headers=self.get_token())
        response = self.client.post(
            '/api/v1/lodges', data=json.dumps(wrong_lodge_hotel_name_input), content_type='application/json',
            headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'], 'only positive integer is accepted')
        assert response.status_code == 400

    def test_get_lodges(self):
        """Test fetching all lodges that have been booked."""

        response = self.client.post(
            '/api/v1/lodges', data=json.dumps(new_lodge), content_type='application/json',
            headers=self.get_token())
        response2 = self.client.post(
            '/api/v1/hotels', data=json.dumps(new_hotel), content_type='application/json',
            headers=self.get_token())
        response1 = self.client.get(
            '/api/v1/lodges', content_type='application/json', headers=self.get_token())
        result = json.loads(response1.data.decode())
        self.assertEqual(result['message'],
                         "success")
        assert response1.status_code == 200

    def test_get_lodge(self):
        """Test getting a lodge by username."""

        response2 = self.client.post(
            '/api/v1/hotels', data=json.dumps(new_hotel), content_type='application/json',
            headers=self.get_token())
        response1 = self.client.post(
            '/api/v1/lodges', data=json.dumps(new_lodge), content_type='application/json',
            headers=self.get_token())
        response = self.client.get(
            '/api/v1/lodges/1', content_type='application/json', headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'],
                         'success')
        assert response.status_code == 200

    def test_get_unexisting_lodge(self):
        """Test getting an unexisting lodge."""

        response = self.client.get(
            '/api/v1/lodges/1', content_type='application/json', headers=self.get_token())
        result = json.loads(response.data.decode())
        self.assertEqual(result['message'],
                         'lodge not found')
        assert response.status_code == 404
