from django.db    import models


class Language(models.Model):
     name = models.CharField(max_length=50)
     class Meta:
         db_table = 'languages'


class Country(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        db_table = 'countries'


class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    profile_image_url = models.URLField(null=True)
    language = models.ForeignKey("Language", on_delete=models.PROTECT)
    country = models.ForeignKey("Country", on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
