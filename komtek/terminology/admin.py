from django.contrib import admin

from komtek.terminology.models import Glossary, GlossaryElement


admin.site.register(Glossary)
admin.site.register(GlossaryElement)