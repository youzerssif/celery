from django.contrib import admin
from django.contrib.postgres import fields
from django_json_widget.widgets import JSONEditorWidget
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin
from django.utils.safestring import mark_safe

from . import models
# Register your models here.

class CategorieAdmin(admin.ModelAdmin):
    list_display = (
        'nom',
        'statut',
        'date_add'
    )
    list_filter = (
        'statut',
        'date_add'
    )
    
    search_fields = ('nom',)
    date_hierarchy = ('date_add')
    actions = ('active', 'desactive')
    
    list_per_page = 10

    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, "La selection a été activé avec succés")

    active.short_description = "activer Les Categories selectionnées"

    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, "La selection a été desactivé avec succés")

    desactive.short_description = "desactivés Les Categories selectionnées"

class SousCategorieAdmin(admin.ModelAdmin):
    list_display = (
        'categorie',
        'nom',
        'statut',
        'date_add'
    )
    list_filter = (
        'statut',
        'date_add'
    )
    
    search_fields = ('nom',)
    date_hierarchy = ('date_add')
    actions = ('active', 'desactive')
    
    list_per_page = 10

    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, "La selection a été activé avec succés")

    active.short_description = "activer Les SousCategories selectionnées"

    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, "La selection a été desactivé avec succés")

    desactive.short_description = "desactivés Les SousCategories selectionnées"

class ProduitAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = (
        'sous_categorie_item',
        'nom',
        'statut',
        'date_add'
    )
    list_filter = (
        'statut',
        'date_add'
    )
    
    search_fields = ('nom',)
    date_hierarchy = ('date_add')
    actions = ('active', 'desactive')
    
    list_per_page = 30
    
    formfield_overrides = {
        fields.JSONField: {'widget': JSONEditorWidget},
    }

    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, "La selection a été activé avec succés")

    active.short_description = "activer Les Produits selectionnées"

    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, "La selection a été desactivé avec succés")

    desactive.short_description = "desactivés Les Produits selectionnées"
    
class CollectionAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = (
        'titre',
        'statut',
        'date_add'
    )
    list_filter = (
        'statut',
        'date_add'
    )
    
    search_fields = ('nom',)
    date_hierarchy = ('date_add')
    actions = ('active', 'desactive')
    
    filter_horizontal = (
        'article',
    )
    list_per_page = 30
    

    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, "La selection a été activé avec succés")

    active.short_description = "activer Les Collections selectionnées"

    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, "La selection a été desactivé avec succés")

    desactive.short_description = "desactivés Les Collections selectionnées"

class LookAdmin(admin.ModelAdmin, DynamicArrayMixin):
    list_display = (
        'nom_auteur',
        'statut',
        'date_add'
    )
    list_filter = (
        'statut',
        'date_add'
    )
    
    search_fields = ('nom_auteur',)
    date_hierarchy = ('date_add')
    actions = ('active', 'desactive')
    
    filter_horizontal = (
        'article'
    )
    list_per_page = 30

    def active(self, request, queryset):
        queryset.update(statut=True)
        self.message_user(request, "La selection a été activé avec succés")

    active.short_description = "activer Les Look selectionnées"

    def desactive(self, request, queryset):
        queryset.update(statut=False)
        self.message_user(request, "La selection a été desactivé avec succés")

    desactive.short_description = "desactivés Les Look selectionnées"