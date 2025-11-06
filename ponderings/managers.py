from django.contrib.auth.base_user import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password, **extra_fields):
        """
        Create and save a user with the given email, username, and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        
        if not username:
            raise ValueError("Users must have a username")
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            username=username,
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
