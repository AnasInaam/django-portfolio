from django.test import TestCase, Client
from django.urls import reverse
from .models import Project, Skill, Profile, Contact


class APITests(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile = Profile.objects.create(
            name='Test User', title='Developer', bio='Bio', email='test@example.com'
        )
        self.skill = Skill.objects.create(name='Python', proficiency=90, category='backend')
        self.project = Project.objects.create(
            title='Proj', description='Desc', short_description='Short desc', featured=True
        )
        self.project.technologies.add(self.skill)

    def test_projects_api(self):
        url = reverse('projects_api')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertTrue(data['success'])
        self.assertGreaterEqual(len(data['projects']), 1)

    def test_skills_api(self):
        url = reverse('skills_api')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertTrue(data['success'])
        self.assertEqual(len(data['skills']), 1)


class ContactFormTests(TestCase):
    def setUp(self):
        self.client = Client()
        Profile.objects.create(name='Test User', title='Dev', bio='Bio', email='test@example.com')

    def test_contact_form_valid(self):
        url = reverse('contact')
        resp = self.client.post(url, {
            'name': 'Alice', 'email': 'alice@example.com', 'subject': 'Hi', 'message': 'Test message',
            'website': '', 'timestamp': ''
        })
        self.assertEqual(resp.status_code, 302)  # redirect on success
        self.assertEqual(Contact.objects.count(), 1)

    def test_contact_form_honeypot(self):
        url = reverse('contact')
        resp = self.client.post(url, {
            'name': 'Bot', 'email': 'bot@example.com', 'subject': 'Spam', 'message': 'Spam',
            'website': 'filled', 'timestamp': ''
        })
        # Should not create message
        self.assertEqual(Contact.objects.count(), 0)
        self.assertEqual(resp.status_code, 200)
from django.test import TestCase

# Create your tests here.
