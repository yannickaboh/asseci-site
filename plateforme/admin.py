from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from . import models
from plateforme import models
from django.conf import settings

# Register your models here.


admin.site.register(models.Evenement, )
admin.site.register(models.Annonce, )
admin.site.register(models.ThemeForum, )
admin.site.register(models.SujetForum, )
admin.site.register(models.Commentaires, )


admin.site.register(models.Board, )
admin.site.register(models.Topic, )
