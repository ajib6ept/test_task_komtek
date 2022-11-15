

from komtek.terminology.models import Glossary, GlossaryElement
from komtek.terminology.serializers import (GlossaryElementSerializer,
                                            GlossarySerializer)
from rest_framework import viewsets


class GlossaryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Glossary.objects.all()
    serializer_class = GlossarySerializer




class GlossaryElementViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GlossaryElement.objects.all()
    serializer_class = GlossaryElementSerializer
