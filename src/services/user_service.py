from repositories.user_repository import user_repository

class UserService:
    def __init__(self, default_user_repository = user_repository):
        self.default_user_repository = default_user_repository

    def check_login_credentials(self, username, password):
        return self.default_user_repository.user_exists(username, password)

    def register_user(self, username, password):
        return self.default_user_repository.create_user(username, password)

user_service = UserService()
