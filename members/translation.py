from modeltranslation.translator import register, TranslationOptions
from .models import Member


@register(Member)
class ProjectsTranslationOptions(TranslationOptions):
    fields = ('full_name', 'workplace','bio',)



