from django.contrib import admin

# Register your models here.
from festalist.models import FestaListKeyword


@admin.register(FestaListKeyword)
class FestaListKeywordAdmin(admin.ModelAdmin):
    pass
