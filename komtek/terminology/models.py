from django.db import models

class Glossary(models.Model):

    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class GlossaryVersion(models.Model):
    version = models.CharField(max_length=200, blank=False, null=False)
    initial_date = models.DateField()
    glossary = models.ForeignKey(Glossary, on_delete=models.CASCADE)

    def __str__(self):
        return self.version

class GlossaryElement(models.Model):

    prarent_id = models.ForeignKey(Glossary, on_delete=models.CASCADE)
    code = models.CharField(max_length=50, blank=False, null=False)
    value = models.CharField(max_length=150, blank=False, null=False)

    def __str__(self):
        return self.code
