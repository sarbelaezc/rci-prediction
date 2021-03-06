from rest_framework.test import APIClient,APITestCase
from django.urls import reverse
from rest_framework import status

client = APIClient()

class TrainTest(APITestCase):
    """
    Test module for train model API
    """

    def test_get_prediction(self):
        response = client.get(
            reverse(
                'train-model'
            ),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)