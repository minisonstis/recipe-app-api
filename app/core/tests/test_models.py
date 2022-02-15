import email
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user"""
        email = 'test@dev.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(email=email, password=password)

        assert user.email == email
        assert user.check_password(password) == True

    def test_new_user_email_normalized(self):
        """Test email normalized"""
        email = 'test@LONDONAPPDEV.com'
        user = get_user_model().objects.create_user(email, 'test123')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Raise error when invalid email adress is subitted"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating new superuser"""
        user = get_user_model().objects.create_superuser('test@dev.com', 'test123')

        assert user.is_superuser == True
        assert user.is_staff == True
