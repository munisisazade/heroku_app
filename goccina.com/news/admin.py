from django.contrib import admin
from .models import *
# Register your models here.
class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 3

class NewsAdmin(admin.ModelAdmin):
	inlines = [ NewsImageInline, ]
	fieldsets = [
		('Başlık', {
            'fields': ['title_tr', 'title_en','title_ru']
        }),
        ('Metni', {
            'fields': ['content_tr', 'content_en','content_ru']
        }),
        ('Arka plan resmi',{
            'fields': ['background']
        }),
    ]

class MenuAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Menu_adı',{
            'fields': ['title_tr', 'title_en','title_ru']
        }),
        ('Site_urli',{
            'fields': ['url']
        }),
    ]

class TeamsAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Adlari',{
            'fields': ['name_tr', 'name_en','name_ru']
        }),
        ('email', {
            'fields': ['email']
        }),
        ('Alintilar',{
            'fields': ['text_tr', 'text_en','text_ru']
        }),
        ('Şekli',{
            'fields': ['image']
        }),
        
    ]

class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
        ('adresi',{
            'fields': ['address_tr','address_en','address_ru']
        }),
        ('numara',{
            'fields': ['number']
        }),
        ('email',{
            'fields': ['email']
        }),
        ('social app', {
            'fields': ['facebook','twitter','google','instagram']
        }),
    ]     

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Kategory', {
            'fields': ['text_tr','text_en','text_ru']
        }),
    ]

class ReferenceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Referanslar', {
            'fields': ['text_tr','text_en','text_ru']
        }),
        ('Şekil', {
            'fields': ['image']
        }),
   
    ]


class CollectionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Koleksiyon', {
            'fields': ['text_tr','text_en','text_ru']
        }),
        ('Şekil', {
            'fields': ['image']
        }),
        ('Tipi', {
            'fields': ['types']
        }),


    ]


admin.site.register(Slider)
admin.site.register(Teams, TeamsAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Reference, ReferenceAdmin)
admin.site.register(Collection, CollectionAdmin)