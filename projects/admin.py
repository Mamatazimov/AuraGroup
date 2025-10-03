from .models import Projects, Images
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin




class ImagesPortfolioInline(admin.TabularInline):
    model = Images
    extra = 1
    fields = ('image',)


@admin.register(Projects)
class MembersTranslationAdmin(TranslationAdmin):
    fields = ('title', 'description',)
    inlines = [ImagesPortfolioInline]


