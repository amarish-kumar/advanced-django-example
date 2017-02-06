from django.contrib import admin

# Register your models here.
from models import Categoria, Enlace, Agregador
from actions import export_as_csv_action

class EnlaceAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'enlace', 'categoria', 'imagen_voto', 'es_popular','imagen_post')
    list_filter = ('categoria', 'usuario',)
    search_fields = ('categoria__titulo','usuario__email',)
    list_editable = ('titulo', 'enlace', 'categoria',)
    list_display_links = ('es_popular',)
    actions = [export_as_csv_action]
    raw_id_fields = ('categoria', 'usuario',)

    def imagen_voto(self, obj):
        url = obj.mis_votos_en_imagen_rosada()
        tag = '<img src="%s">' % url
        return tag

    def imagen_post(self, obj):
        url = obj.imagen
        tag = '<img src="%s">' % url
        return tag

    imagen_voto.allow_tags = True
    # imagen_post.allow_tags = True
    imagen_voto.admin_order_field = 'votos'

class EnlaceInline(admin.StackedInline):
    model = Enlace
    raw_id_fields = ('usuario',)
    extra = 1

class CategoriaAdmin(admin.ModelAdmin):
    actions = [export_as_csv_action]
    inlines = [EnlaceInline]

class AgregadorAdmin(admin.ModelAdmin):
    filter_horizontal = ('enlaces',)

admin.site.register(Agregador, AgregadorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Enlace, EnlaceAdmin)
