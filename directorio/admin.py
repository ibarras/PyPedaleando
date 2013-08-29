from django.contrib import admin
from directorio.models import Estado
from directorio.models import Ciudad
from directorio.models import GrupoCiclista

#admin.site.register(Poll)



#	inlines = [FotoInline]
#Muestra los eventos en linea.

#list_display = ('nombre')
#Filtra los eventos por fecha de publicacion

#	list_filter = ['fecha']
	#date_hierarchy = 'pub_date'
	
admin.site.register(Estado)
admin.site.register(Ciudad)
admin.site.register(GrupoCiclista)
