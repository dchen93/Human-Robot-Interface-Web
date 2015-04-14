from django.shortcuts import render
from django.views import generic
from .models import UploadGroup, File

# Create your views here.

def index(request):
    upload_group_list = UploadGroup.objects.order_by('-upload_group')
    context = {'upload_group_list': upload_group_list}
    return render(request, 'quadcoptermedia/index.html', context)

class DetailView(generic.DetailView):
	model = UploadGroup
	template_name = 'quadcoptermedia/flight.html'

# class MediaView(generic.DetailView):
# 	model = File
# 	template_name = 'quadcoptermedia/media.html'