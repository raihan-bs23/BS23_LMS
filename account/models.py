from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils.html import mark_safe


class UserAdditionalInfo(models.Model):
    username = models.CharField(max_length=100, primary_key=True)
    user_full_name = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=100)
    profession = models.CharField(max_length=300)
    user_role = models.CharField(max_length=300)
    profile_picture = models.ImageField(upload_to="user_DP/", null=True, blank=True)
    social_link = models.CharField(max_length=200)

    def get_full_name(self):
        return f"{self.user_full_name.first_name} {self.user_full_name.last_name}"

    def __str__(self):
        return self.get_full_name()

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % self.profile_picture.url)

    class Meta:
        db_table = "UserAdditionalInfo"
