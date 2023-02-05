from django.shortcuts import render, redirect, get_object_or_404
from .models import Protocol, ProtocolVersion, Procedure, ProtocolVersionStep, Component, ProcedureComponent
from django.contrib.auth.decorators import login_required
from .forms import NewProtocolForm, CreateProtocolForm, CreateProcedureForm

#Create your views here.
def currentprotocols(request):
    protocols = Protocol.objects.all()
    return render(request, 'protocol/currentprotocols.html', {'protocols':protocols})

def selectedprotocol(request, prv_fk):
    prv = ProtocolVersion.objects.get(id=prv_fk)
    procedures = ProtocolVersionStep.objects.filter(protocol_version=prv_fk).order_by('step')
    return render(request, 'protocol/selectedprotocol.html', {'procedures':procedures, 'prv': prv})

@login_required
def newprotocol(request):
    if request.method == 'GET':
        return render(request, 'protocol/newprotocol.html', {'form':NewProtocolForm()})
    else:
        try:
            try:
                protocol_form = NewProtocolForm(request.POST)
                newprotocol = protocol_form.save(commit=False)
                newprotocol.user = request.user
                newprotocol.save()
                protocol_pk = Protocol.objects.latest('id')
                version = ProtocolVersion(user=request.user, version='1', protocol=protocol_pk)
                version.save()
                nextstep = 1
                print(nextstep)
                return render(request, 'protocol/newprotocol.html', {'step_form':CreateProtocolForm(), 'protocol_pk':protocol_pk,'prv_pk':ProtocolVersion.objects.latest('id'), 'nextstep':nextstep})
            except:
                procedure_form = CreateProcedureForm(request.POST)
                step_form = CreateProtocolForm(request.POST)
                newprocedure = procedure_form.save()
                newstep = step_form.save(commit=False)
                newstep.protocol_version = ProtocolVersion.objects.latest('id')
                newstep.procedure = Procedure.objects.latest('id')
                newstep.save()
                prv_pk = ProtocolVersion.objects.latest('id')
                procedures = ProtocolVersionStep.objects.filter(protocol_version=prv_pk).order_by('step')
                #print(ProtocolVersionStep.objects.filter(protocol_version=prv_pk).order_by('-step').values_list('step')[0][0])
                nextstep = 1
                nextstep += ProtocolVersionStep.objects.filter(protocol_version=prv_pk).order_by('-step').values_list('step')[0][0]
                print(nextstep)
                if "add" in request.POST:
                    return render(request, 'protocol/newprotocol.html', {'step_form':CreateProtocolForm(), 'procedure_form':CreateProcedureForm(), 'procedures':procedures, 'prv_pk':prv_pk, 'nextstep':nextstep})
                elif "save" in request.POST:
                    return redirect('currentprotocols')
        except ValueError:
            return render(request, 'protocol/newprotocol.html', {'protocol_form':NewProtocolForm(), 'error':'Bad data. Try again.'})

