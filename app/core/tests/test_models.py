from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        '''Test that a new user can be created with an e-mail'''
        email = 'test@samplecompany.com'
        password = 'TestPass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''Test that the email for a new user is normalized'''
        email = 'thiscrazy@eMaiLaDDreSS.cOm'
        user = get_user_model().objects.create_user(email, 'dumbpword')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''Test creating a user with an invalid password'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '123')

    def test_create_new_super_user(self):
        '''Test creating a new superuser'''
        user = get_user_model().objects.create_superuser(
            'test@samplecompany.com',
            'dummyPword'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
