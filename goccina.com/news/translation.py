from modeltranslation.translator import translator, TranslationOptions
from news.models import *

class MenuTranslationOption(TranslationOptions):
	fields = ('title',)


class NewsTranslationOption(TranslationOptions):
    fields = ('title', 'content')

class TeamsTranslationOption(TranslationOptions):
	fields = ('name','text')

class ContactTranslationOption(TranslationOptions):
	fields = ('address',)

class CategoryTranslationOption(TranslationOptions):
	fields = ('text',)

class ReferenceTranslationOption(TranslationOptions):
	fields = ('text',)

class CollectionTranslationOption(TranslationOptions):
	fields = ('text',)




translator.register(Menu, MenuTranslationOption)
translator.register(News, NewsTranslationOption)
translator.register(Teams, TeamsTranslationOption)
translator.register(Contact, ContactTranslationOption)
translator.register(Category, CategoryTranslationOption)
translator.register(Reference, ReferenceTranslationOption)
translator.register(Collection, CollectionTranslationOption)