from django.forms import ModelForm
from .models import Protocol
from .models import ProtocolVersion
from .models import ProtocolVersionStep
from .models import Procedure

class NewProtocolForm(ModelForm):
    class Meta:
        model = Protocol
        fields = ['title']

class CreateProcedureForm(ModelForm):
    class Meta:
        model = Procedure
        fields = ['description']

class CreateProtocolForm(ModelForm):
    class Meta:
        model = ProtocolVersionStep
        fields = ['step']
