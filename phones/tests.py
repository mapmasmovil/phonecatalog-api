from django.test import TestCase
from django.urls import reverse


class QuestionModelTests(TestCase):

    def test_phones_index(self):
        response = self.client.get('/phones/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.json().keys()), ['page', 'before', 'after', 'phones'])
