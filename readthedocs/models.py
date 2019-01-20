from django.db import models


class Project(models.Model):
    project_id = models.IntegerField()
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    programming_language = models.CharField(max_length=255)
    default_version = models.CharField(max_length=255)
    default_branch = models.CharField(max_length=255)
    repo_type = models.CharField(max_length=255)
    repo = models.CharField(max_length=255)
    description = models.TextField()
    language = models.CharField(max_length=255)
    documentation_type = models.CharField(max_length=255)
    canonical_url = models.CharField(max_length=255)
    actual_language = models.CharField(
        'detected language', max_length=255, blank=True, null=True)
    license = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class ScrapeResult(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    project = models.ForeignKey(
        Project, on_delete=models.SET_NULL, null=True, blank=True)
    success = models.BooleanField(default=False)
    folder = models.CharField(max_length=255)

    def __str__(self):
        return '{} {}'.format(self.project.name, folder)
