from django.contrib import admin
from evento.models import Evento
from evento.models import Foto

#admin.site.register(Poll)


class FotoInline(admin.TabularInline):
	model = Foto
#	extra = 

class EventoAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 		{'fields': ['nombre', 'fecha', 'imagen', 'descripcion' ]}),
		#('Date Information', {'fields' : ['pub_date'], 'classes' : ['collapse']}),
	]
	inlines = [FotoInline]

#Muestra los eventos en linea.

	list_display = ('nombre', 'fecha')
#Filtra los eventos por fecha de publicacion

	list_filter = ['fecha']
	#date_hierarchy = 'pub_date'
	
    
admin.site.register(Evento, EventoAdmin)


#admin.site.register(Choice)
