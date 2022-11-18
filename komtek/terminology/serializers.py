from rest_framework import serializers

from komtek.terminology.models import Glossary, GlossaryElement


class GlossarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Glossary
        fields = [
            "id",
            "name",
            "short_name",
            "description",
            "version",
            "start_date",
        ]


class GlossaryElementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GlossaryElement
        fields = ["prarent_id", "code", "value"]
