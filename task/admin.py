from django.contrib import admin

from task.models import ContractPlan, Task, TaskComment

admin.site.register(ContractPlan)
admin.site.register(Task)
admin.site.register(TaskComment)
