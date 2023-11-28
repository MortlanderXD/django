from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def index(request):
#    if request.method == 'GET':
#     return render(request, 'index.html')
   
  template = loader.get_template('MnMs/index.html')
  return HttpResponse(template.render())