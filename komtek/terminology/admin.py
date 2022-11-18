from django.contrib import admin

from komtek.terminology.models import (
    Glossary,
    GlossaryElement,
    GlossaryVersion,
)


admin.site.register(Glossary)
admin.site.register(GlossaryElement)
admin.site.register(GlossaryVersion)
