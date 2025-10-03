from modeltranslation.translator import register, TranslationOptions
from .models import Projects


@register(Projects)
class ProjectsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)







