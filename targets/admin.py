from django.contrib import admin
from .models import Target_model

# Register your models here.


class Target_modelAdmin(admin.ModelAdmin):
    # fields = ["args"]
    fieldsets = [
        ("Content", {"fields": ["label", "time_created"]}),
        ("Other", {"fields": ["target_id", "new_field"]}),
    ]


admin.site.register(Target_model, Target_modelAdmin)
