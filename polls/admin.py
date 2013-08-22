from polls.models import Poll
from django.contrib import admin
from polls.models import Choice

#admin.site.register(Poll)


class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 4 

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 		{'fields': ['question']}),
		('Date Information', {'fields' : ['pub_date'], 'classes' : ['collapse']}),
	]
	inlines = [ChoiceInline]

	list_display = ('question', 'pub_date')
	list_filter = ['pub_date']
	date_hierarchy = 'pub_date'
	

admin.site.register(Poll, PollAdmin)

#admin.site.register(Choice)
