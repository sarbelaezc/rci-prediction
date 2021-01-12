from rest_framework.test import APIClient,APITestCase
from django.urls import reverse
from rest_framework import status

client = APIClient()

class PredictionTest(APITestCase):
    """
    Test module for get prediction API
    """

    def test_get_prediction(self):
        response = client.get(
            reverse(
                'predict'
            ),
            content_type='application/json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)