from django.test import TestCase
from django.contrib.auth.middleware import get_user
from django.contrib.auth.models import User
from django.urls import reverse

# class RegistrationTestCase(TestCase):
#     def test_user_accout_is_created(self):
#         self.client.post(
#             #"/users/register",
#             reverse("users:register"),
#             data={
#                 "username": 'Vohidjon',
#                 "first_name": 'Vohidjon',
#                 "last_name": 'Azimqulov',
#                 "email": 'admin@mail.ru',
#                 "password": '12345'
#             }
#         )
#         user = User.objects.get(username='Vohidjon')
#         self.assertEqual(user.username,'Vohidjon')
#         self.assertEqual(user.last_name,'Azimqulov')
#         self.assertEqual(user.email,'admin@mail.ru')
#         self.assertNotEqual(user.password, '12345')
#         self.assertTrue(user.check_password('12345'))

#     def test_required_fields(self):
#             response = self.client.post(
#                  reverse('users:register'),
#                  data= {
#                       "first_name": 'Vohidjon',
#                       "email": 'admin@mail.ru',
#                  }
#             )
#             user_count = User.objects.count()
#             self.assertEqual(user_count, 0)
#             self.assertFormError(response, 'form', 'username', 'This field is required.')
#             self.assertFormError(response, 'form', 'password', 'This field is required.')

#     def test_invalid_email(self):
#         response = self.client.post(
#             reverse('users:register'),
#             data={
#                 "username": 'Vohidjon',
#                 "first_name": 'Vohidjon',
#                 "last_name": 'Azimqulov',
#                 "email": 'invalid-email',
#                 "password": '12345'
#             }
#         )
#         user_count = User.objects.count()
#         self.assertEqual(user_count, 0)
#         self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')

#     def test_unique_username(self):
#          user =User.objects.create_user(username='Vohidjon')
#          user.set_password('12345')
#          user.save()
#          response = self.client.post(
#               reverse("users:register"),
#               data={
#                    "username": 'Vohidjon',
#                    "first_name": 'Vohidjon',
#                    "last_name": 'Azimqulov',
#                    "email": 'admin@mail.ru',
#                    "password": '12345'
#               }
#          )
#          user_count = User.objects.count()
#          self.assertEqual(user_count, 1)
#          self.assertFormError(response, 'form', 'username', 'A user with that username already exists.')

class LoginTestCase(TestCase):
     def test_successful_login(self):
        db_user = User.objects.create(username = 'Vohidjon', first_name = 'Vohidjon')
        db_user.set_password('12345')
        db_user.save()
        self.client.post(
            reverse('users:login'),
            data= {
                'username': 'Vohidjon',
                'password': '12345'
            }
        )
        user = get_user(self.client)
        self.assertTrue(user.is_authenticated) 

     def test_successful_login(self):
        db_user = User.objects.create(username = 'Vohidjon', first_name = 'Vohidjon')
        db_user.set_password('12345')
        db_user.save()
        self.client.post(
            reverse('users:login'),
            data= {
                'username': 'wrong-username',
                'password': '12345'
            }
        )
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated) 

        self.client.post(
            reverse('users:login'),
            data= {
                'username': 'Vohidjon',
                'password': 'wrong-password'
            }
        )
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated) 
