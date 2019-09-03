from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, first_name, last_name, email, password=None):
        """
        Creates and saves a User with the given username, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email')
        user = self.model(first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given username and password.
        """
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True

        user.save(using=self._db)
        return user
