from django.contrib import admin
from .models import *


class LivingExpenseAdmin(admin.ModelAdmin):
    list_display = ['done_at', 'description', 'income']

admin.site.register(Source)
admin.site.register(Income)
admin.site.register(LivingExpense, LivingExpenseAdmin)
admin.site.register(InterpersonalCircle)
admin.site.register(ExtendKnowledge)
admin.site.register(Holiday)
admin.site.register(Saving)
