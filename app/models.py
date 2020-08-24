import uuid

from django.db import models
from django.apps import apps


class ActiveRevision(models.Model):
    """
    Contains revision of VersionContolModel
    """
    VERSION_MODEL = None

    uuid = models.UUIDField(
        primary_key=True
    )

    def add_version(self, data, *args, **kwargs):
        _models = apps.get_models()
        _model = [x for x in _models if x.__name__==self.VERSION_MODEL]
        if not _model:
            raise
        data['program_id'] = self.uuid
        _model[0].objects.create(**data)

    def update_version(self, *args, **kwargs):
        pass

    def activate_version(self, *args, **kwargs):
        pass

    def save(self, *args, **kwargs):
        if not self.uuid:
            self.uuid = uuid.uuid4().hex
        super().save(*args, **kwargs)

    class Meta:
        abstract = True


class VersionControlBaseModel(models.Model):
    """
    Base model for implementing versioning in django model
    """

    class Meta:
        abstract = True


"""
Program ID -> (multiple version IDs) -> (active version ID)
Supported queries:
- Add a new version to program
- Make changes to any version of the program
- Make any version active / deactive
- Program should have minimum one active version
"""

class Program(ActiveRevision):
    VERSION_MODEL = 'ProgramVersions'

    name = models.CharField(max_length=50)


class ProgramVersions(VersionControlBaseModel):
    field1 = models.CharField(max_length=50)
    field2 = models.IntegerField()
    field3 = models.IntegerField()
    is_active = models.BooleanField(
        default=False
    )
    program = models.ForeignKey(
        Program,
        on_delete=models.CASCADE,
    )
