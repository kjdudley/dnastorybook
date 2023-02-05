from django.db import models
from django.contrib.auth.models import User
from note.models import Note

# Create your models here.
class Protocol(models.Model):
    title = models.CharField(max_length=250)
    note = models.ForeignKey(Note, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.title)

class ProtocolVersion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    version = models.CharField(max_length=10)
    created = models.DateField(auto_now_add=True)
    protocol = models.ForeignKey(Protocol, on_delete=models.CASCADE, related_name="version_protocol")
    note = models.ForeignKey(Note, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.protocol)+"_"+str(self.version)

class Procedure(models.Model):
    description = models.TextField()
    note = models.ForeignKey(Note, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.description)

class ProtocolVersionStep(models.Model):
    protocol_version = models.ForeignKey(ProtocolVersion, on_delete=models.CASCADE)
    step = models.IntegerField(default=0)
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.protocol_version)+"_"+str(self.step)

COMPONENT_TYPES = (
    ('Equipment', 'EQUIPMENT'),
    ('Reagent', 'REAGENT'),
    ('Chemical', 'CHEMICAL'),
    ('Consumable', 'CONSUMABLE'),
    ('Software', 'SOFTWARE'),
    ('Other', 'OTHER'),
)

class Component(models.Model):
    component_name = models.CharField(max_length=100)
    component_type = models.CharField(max_length=10, choices=COMPONENT_TYPES, default='Other')
    note = models.ForeignKey(Note, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.component_name)

AMOUNT_UNITS = (
    ('mL', 'MILILITRE'),
    ('uL', 'MICROLITRE'),
    ('L','LITRE'),
    ('g', 'GRAM'),
    ('mg', 'MILIGRAM'),
    ('ug', 'MICROGRAM'),
    ('Pellet', 'PELLET'),
    ('Other', 'OTHER'),
)
    
class ProcedureComponent(models.Model):
    procedure = models.ForeignKey(Procedure, on_delete=models.CASCADE)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    amount = models.CharField(max_length=20)
    amount_unit = models.CharField(max_length=10, choices=AMOUNT_UNITS, default='Other')

    def __str__(self):
        return str(self.amount)+"_"+str(self.amount_unit)+"_"+str(self.component)
