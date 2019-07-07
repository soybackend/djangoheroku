from django.contrib import admin
from .models import Persona


@admin.register(Persona)
class InscripcionAdmin(admin.ModelAdmin):
	pass