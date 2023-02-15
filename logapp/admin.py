from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . import models

admin.site.register(models.User)#若要自己定义的模型类也能在/admin后台管理界面中显示和管理，需要将自己的类注册到后台管理界面.user为自己创建的模型类名