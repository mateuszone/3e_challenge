import json
from django.urls import reverse
from API.models import Users
from rest_framework.test import APITestCase
from rest_framework import status


class UsersViewSetTestCase(APITestCase):
    """
    Simple tests cases created for testing this simple API.
    """
    def setUp(self):
        self.user = Users.objects.create(name="Mateusz",
                                         age=27)
        self.data = {'name': 'Sebastian', 'age': 32}

    def test_user_create(self):
        response = self.client.post('/users/add/', json.dumps(self.data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(Users.objects.all()), 2)
        self.assertEqual(Users.objects.last().name, self.data['name'])
        self.assertEqual(Users.objects.last().age, self.data['age'])

    def test_category_list(self):
        response = self.client.get(reverse('users-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
