from django.test import TestCase

# Create your tests here.

from django.contrib.auth import get_user_model

class TestModel(TestCase):
    """
      testing for creating user model .
    """
    def test_create_user_email_successfull(self):
         """
            testing for creating user model .
         """
         email='user@gmail.com'
         password="user123"
         user=get_user_model().objects.create_user(
                 email=email,password=password
         )
         self.assertEqual(user.email,email)
         self.assertTrue(user.check_password(password))
    def test_new_user_normalize(self):
         sample_users=[
               ['test1@GMAIL.com','test1@gmail.com'],
               ['test2@GMAIL.com','test2@gmail.com'],
               ['test3@GMAIL.com','test3@gmail.com'],
               ['test4@GMAIL.com','test4@gmail.com'],
         ]
         for email,excpected in sample_users:
              user= get_user_model().objects.create_user(
                   email,'test123'
              )
              self.assertEqual(user.email,excpected)
    def test_create_user_without_email_raise_valueError(self):
         """Test that creating new user without email rasises a ValueError ."""
         with self.assertRaises(ValueError):
               get_user_model().objects.create_user('','test123')
    def test_create_superuser(self):
         "Test creating super user ."
         email='mohmaed@gmail.com'
         password='mohamed123'
         user=get_user_model().objects.create_superuser(email=email,password=password)
         self.assertTrue(user.is_superuser)
         self.assertTrue(user.is_staff)
       