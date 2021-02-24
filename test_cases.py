from django.test.testcases import TestCase

def create_user(data='test_user'):
    
    user = G(User, username=data, is_active=True)
    user.set_password(data)
    user.save()
    return user

class UsernameCaseInsensitiveTests(TestCase):

    def test_user_create(self):
        testuser = 'testuser'
        user = create_user(testuser)
        # Lowercase
        self.assertEqual(testuser, user.username)
        # Uppercase
        user.username = testuser.upper()
        user.save()
        self.assertEqual(testuser, user.username)

def test_username_eq(self):
    testuser = 'test_user'
    user = create_user(testuser)
    self.assertTrue(isinstance(user.username, iunicode))
    self.assertEqual(user.username, testuser)
    self.assertEqual(user.username, testuser.upper())
    self.assertTrue(user.username == testuser.upper())
    self.assertTrue(testuser.upper() == user.username)
    self.assertTrue(user.username == iunicode(testuser.upper()))