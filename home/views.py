from django.shortcuts import render

from .models import DocInfos
from django.views.generic import CreateView, DetailView, ListView 

# Create your views here.

def list(request):
    all_DocInfos = DocInfos.objects.all()
    return render(request, 'home/info_list.html', {'DocInfos' : all_DocInfos})

class DocInfosCreateView(CreateView):
    model = DocInfos
    fields = ['input1', 'input2']
    success_url = "/docinfos"
    template_name = 'home/inputForm.html'