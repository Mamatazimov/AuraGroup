from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import Member


@admin.register(Member)
class MembersTranslationAdmin(TranslationAdmin):
    fields = ('full_name', 'workplace','bio',)




