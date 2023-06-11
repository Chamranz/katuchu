from django.contrib import admin
from .models import Bag, colours, material, Status, BookInstance, Modification

#admin.site.register(Bag)
#admin.site.register(colours)
admin.site.register(material)
admin.site.register(Status)
admin.site.register(Modification)
#admin.site.register(BookInstance)
class coloursAdmin(admin.ModelAdmin):
    pass
admin.site.register(colours, coloursAdmin)

class BookInstanceInline (admin.TabularInline):
    model = BookInstance

@admin.register(Bag)
class BagAdmin(admin.ModelAdmin):
    list_display = ('title', 'colours', 'material','summary', 'Basket')
    list_filter = ("colours", 'material', 'Basket')
    inlines = [BookInstanceInline]






# Register your models here.
