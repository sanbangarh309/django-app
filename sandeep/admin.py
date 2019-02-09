from django.contrib import admin
from .models import User,Project,History

class UsersAdmin(admin.ModelAdmin):
    pass

class ProjectsAdmin(admin.ModelAdmin):
    pass

class HistoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UsersAdmin)
admin.site.register(Project, ProjectsAdmin)
admin.site.register(History, HistoryAdmin)
