from django.contrib.auth.models import UserManager as Manager


class UserManager(Manager):
    def create_user(
            self, email=None, password=None, **extra_fields
    ):
        if not email:
            raise ValueError('Email must be provided')

        if not password:
            raise ValueError('Password must be provided')

        # email = self.normalize_email(email)
        # user = self.model(email=email, **extra_fields)
        # user.set_password(password)
        # user.save()
        # return user
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        print(f"In UserManager.create_user: Calling set_password for {email}")
        user.set_password(password)
        print(user.password)
        print(f"In UserManager.create_user: Password set. Now saving user.")
        user.save()
        print(f"User {email} saved.")
        return user

    def create_superuser(
            self, email=..., password=..., **extra_fields
    ):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields['is_active']:
            raise ValueError("Superuser must be active")
        if not extra_fields['is_staff']:
            raise ValueError("Superuser must be staff")

        if not extra_fields['is_superuser']:
            raise ValueError("Superuser must be superuser")

        user = self.create_user(email=email, password=password, **extra_fields)
        return user
