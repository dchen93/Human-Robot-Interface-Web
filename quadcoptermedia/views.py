from django.shortcuts import render
from django.views import generic
from django.http import Http404
from .models import User, File
from rest_framework import viewsets, views, status
from rest_framework.response import Response
from .serializers import FileSerializer

# Create your views here.

def index(request):
    user_list = User.objects.order_by('-username')
    context = {'user_list': user_list}
    return render(request, 'quadcoptermedia/index.html', context)

class DetailView(generic.DetailView):
	model = User
	template_name = 'quadcoptermedia/flight.html'

# class MediaView(generic.DetailView):
# 	model = File
# 	template_name = 'quadcoptermedia/media.html'

class FileViewSet(viewsets.ModelViewSet):
	queryset = File.objects.all()
	serializer_class = FileSerializer

class FileUpload(views.APIView):
#    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get(self, request, format=None):
        uploaded_file = File.objects.all()
        serializer = FileSerializer(uploaded_file, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
       serializer = FileSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def pre_save(self, obj):
    #     obj.user = self.request.user


class FileDetail(views.APIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def get_object(self, pk):
        try:
            return File.objects.get(pk=pk)
        except File.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        uploaded_file = self.get_object(pk)
        serializer = FileSerializer(uploaded_file)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        uploaded_file = self.get_object(pk)
        serializer = FileSerializer(uploaded_file, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        uploaded_file = self.get_object(pk)
        uploaded_file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def pre_save(self, obj):
    #     obj.user = self.request.user