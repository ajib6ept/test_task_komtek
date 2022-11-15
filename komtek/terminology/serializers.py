from rest_framework import serializers

from komtek.terminology.models import Glossary, GlossaryElement

class GlossarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Glossary
        fields = ["name", 'short_name', 'description', 'version', 'initial_date']


class GlossaryElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GlossaryElement
        fields = ["prarent_id", 'code', 'value']


