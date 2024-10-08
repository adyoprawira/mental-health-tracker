from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from .models import MoodEntry

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_strong_mood_user(self):
        now = timezone.now()
        mood = MoodEntry.objects.create(
            mood="LUMAYAN SENANG",
            time = now,
            feelings = "senang sih, cuman tadi baju aku basah kena hujan :(",
            mood_intensity = 8,
        )
        self.assertTrue(mood.is_mood_strong)

    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='username', password='pass')

    def test_main_template_uses_correct_page_title(self):
        # Log in the client
        self.client.login(username='username', password='pass')

        self.client.cookies['last_login'] = '2024-09-20 10:00:00'

        # Now get the response
        response = self.client.get("/")
        html_response = response.content.decode("utf8")

        # Check if the title is present
        self.assertIn("PBD Mental Health Tracker", html_response)
    