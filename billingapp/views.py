from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from billingapp.serializers import UserSerializer, GroupSerializer
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .models import Bucketlist
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import BucketlistSerializer
from django.views.decorators.csrf import requires_csrf_token


class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer

class BucketListViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	# authentication_classes = (BasicAuthentication,)
 #    permission_classes = (IsAuthenticated,)
	queryset = Bucketlist.objects.all()
	serializer_class = BucketlistSerializer
	
	# def perform_create(self, serializer):
	# 	"""Save the post data when creating a new bucketlist."""
	# 	serializer.save()






class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our rest api."""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

# class UserDetail(generics.RetrieveAPIView):
#     """
#     A view that returns a templated HTML representation of a given user.
#     """
#     queryset = User.objects.all()
#     renderer_classes = (TemplateHTMLRenderer,)

#     def get(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return Response({'user': self.object}, template_name='user_detail.html')

def index(request): 
	return render(request,'billingapp/login.html')




# Create your views here.
def admin_home(request):
	if not request.user.is_superuser and not request.user.is_authenticated():
		return redirect('schoollogout')
	return render(request, 'billingapp/admin_home.html')

def login(request):

	if request.user.is_authenticated():
		#To redirect to different pages
		#print(request.user.is_superuser)
		return redirect('admin_home')

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = auth.authenticate(username=username, password=password)

		if user is not None:
			# correct username and password login the user
			auth.login(request, user)
			return redirect('admin_home')

		else:
			messages.error(request, 'Error wrong username/password')

	return render(request, 'billingapp/login.html')

def logout(request):
	auth.logout(request)
	return redirect('login')