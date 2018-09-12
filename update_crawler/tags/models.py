from django.db import models

# Create your models here.


class Tags(models.Model):
    owner = models.ForeignKey('auth.user', related_name='tags', on_delete=models.CASCADE)
    tag_name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag_code = models.CharField(max_length=255)
    created_by = models.CharField(max_length=42)
    ip_address = models.GenericIPAddressField(null=True)

    class Meta:
        ordering = ('tag_name',)


class ProgrammingLanguage(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('code',)
