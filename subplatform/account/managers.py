from django.contrib.auth.base_user import BaseUserManager

# For translational strings.
from django.utils.translation import gettext_lazy as _


# For managing custom user model.
class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError(_("The email must be set."))
        
        email = self.normalize_email(email)

        # Creating user object.
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:

            raise ValueError(_("The superuser must have is_staff=True."))
        
        if extra_fields.get("is_superuser") is not True:

            raise ValueError(_("The superuser must have is_superuser=True."))
        
        return self.create_user(email, password, **extra_fields)