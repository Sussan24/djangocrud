from django.contrib import admin
from .models import Post

admin.site.register(Post)
# Register your models here.
# from django.db import models
# from django.contrib.auth import get_user_model
# from django.utils import timezone
# from django.urls import reverse
# from django.template.defaultfilters import slugify
# # Create your models here.


# class Post(models.Model):

#     STATUS_CHOICES = (
#         ("draft", "Draft"),
#         ("published", "Published")
#     )