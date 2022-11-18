from django.urls import path

from komtek.terminology.views import GlossaryViewSet

urlpatterns = [
    path("glossary", GlossaryViewSet.as_view({"get": "list"})),
    # path("glossary/{glossary_id}/items", GlossaryViewSet.as_view({"get": "list"})),
]
