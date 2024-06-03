from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"

    def get(self,request):
        return render(request,self.template_name)
    


class DiscoverView(TemplateView):
    template_name = "discover.html"

    def get(self,request):
        return render(request,self.template_name)
