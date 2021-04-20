from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_admin, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Email must be set') 
        email = self.normalize_email(email)
        user = self.model (
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_admin=is_admin,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, False **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, True **extra_fields)

