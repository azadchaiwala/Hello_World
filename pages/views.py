from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.
# def homeView(request):
#     message='Hello Husnain'


#     return HttpResponse(message)

class homeView(TemplateView):
    template='index.html'

# def aboutView(request):
#     message=('this is about section of our project')

#     return HttpResponse(message)

class aboutView(TemplateView):
    template_name='about.html'

# def contactView(request):
#     message=('this is contact section')

#     return HttpResponse(message)

class contactView(TemplateView):
    template_name='contact.html'

# def cartView(request):
#     message=('this is a cart section')

#     return HttpResponse(message)

class cartView(TemplateView):
    template_name='cart.html'
