from django.contrib import admin
from .models import Protocol, ProtocolVersion, Procedure, ProtocolVersionStep, Component, ProcedureComponent

# Register your models here.
admin.site.register(Protocol)
admin.site.register(ProtocolVersion)
admin.site.register(Procedure)
admin.site.register(ProtocolVersionStep)
admin.site.register(Component)
admin.site.register(ProcedureComponent)

