from django.contrib import admin

from .models import UserProfile, Project, Task, Supervisor, Developer

# Register your models here.


admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Supervisor)
admin.site.register(Developer)

