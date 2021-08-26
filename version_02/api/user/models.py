from django.db    import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User Must Have an Email Address")

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class Language(models.Model):
     name = models.CharField(max_length=50)
     class Meta:
         db_table = 'languages'


class Country(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'countries'


class User(AbstractBaseUser, PermissionsMixin):
    nickname = models.CharField(max_length=20)
    email = models.EmailField(
        verbose_name="Customer Email", 
        help_text="Required and Unique", 
        unique=True
    )
    
    password = models.CharField(
        verbose_name="Customer Password",
        help_text="Required and Secured",
        max_length=255
    )

    profile_image_url = models.URLField(null=True)
    language = models.ForeignKey("Language", on_delete=models.PROTECT)
    country = models.ForeignKey("Country", on_delete=models.PROTECT)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
