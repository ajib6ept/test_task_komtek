from django.db import models
from django.utils import timezone


class Glossary(models.Model):

    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    @property
    def version(self):
        return (
            self.versions.filter(initial_date__lte=timezone.now())
            .order_by("-initial_date")
            .first()
            .version
        )

    @property
    def start_date(self):
        return (
            self.versions.filter(initial_date__lte=timezone.now())
            .order_by("-initial_date")
            .first()
            .initial_date
        )


class GlossaryVersion(models.Model):
    version = models.CharField(max_length=200, blank=False, null=False)
    initial_date = models.DateField()
    glossary = models.ForeignKey(
        Glossary, on_delete=models.CASCADE, related_name="versions"
    )

    def __str__(self):
        return f"{self.version} | {self.glossary}"


class GlossaryElement(models.Model):

    prarent_id = models.ForeignKey(
        Glossary, on_delete=models.CASCADE, related_name="items"
    )
    code = models.CharField(max_length=50, blank=False, null=False)
    value = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return f"{self.code} | {self.prarent_id}"
