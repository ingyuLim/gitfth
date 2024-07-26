from django.contrib import admin
from .models import Burger
# Register your models here.

@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
	pass
	# list_display = ('name', 'price', 'topping', 'created_at', 'updated_at')
	# list_filter = ('name', 'price', 'topping', 'created_at', 'updated_at')
	# search_fields = ('name', 'price', 'topping', 'created_at', 'updated_at')
	# ordering = ('name', 'price', 'topping', 'created_at', 'updated_at')

# admin.site.register(Burger)
