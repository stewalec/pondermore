from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class UsernameOrEmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # Check if the input matches an email
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            try:
                # If not an email, check if it matches a username
                user = UserModel.objects.get(username=username)
            except UserModel.DoesNotExist:
                return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None