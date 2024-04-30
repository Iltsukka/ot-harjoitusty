import unittest
from repositories.user_repository import user_repository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_users()
        user_repository.create_user('test', 'mate')
    
    def test_user_creation(self):
        user_created = user_repository.create_user('username', 'password')
        self.assertTrue(user_created)
    
    def test_cannot_create_duplicate_user(self):
        user_created = user_repository.create_user('username', 'password')
        self.assertTrue(user_created)
        same_user_again = user_repository.create_user('username', 'password')
        self.assertFalse(same_user_again)
    
    def test_validate_login(self):
        user = user_repository.user_exists('test', 'mate')
        self.assertTrue(user)
        non_existant_user = user_repository.user_exists('non', 'user')
        self.assertFalse(non_existant_user)