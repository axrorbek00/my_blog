from .models import PostModel
from modeltranslation.translator import TranslationOptions, register


@register(PostModel)
class PostmodelTranslation(TranslationOptions):
    fields = ['title', 'body']
