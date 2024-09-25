from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
# def homeView(request):
#     message='Hello Husnain'


#     return HttpResponse(message)

class homeview(TemplateView):
    template='index.html'

def aboutView(request):
    message=('this is about section of our project')

    return HttpResponse(message)

def contactView(request):
    message=('this is contact section')

    return HttpResponse(message)

def cartView(request):
    message=('this is a cart section')

    return HttpResponse(message)


