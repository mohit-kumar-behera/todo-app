from django.contrib import admin
from .models import taskCreate,taskList

class taskListAdmin(admin.ModelAdmin):
	list_display = ('taskDescription','taskTime','isComplete')
	list_filter = ['taskTime','isComplete'] 

admin.site.register(taskCreate)
admin.site.register(taskList,taskListAdmin)

