from django.conf.urls import url, include
from billingapp import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView,BucketListViewSet
from django.views.generic import TemplateView


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'bucketlistapi', BucketListViewSet)



urlpatterns = [
	url(r'^api/', include(router.urls)),
    url(r'^schooladmin/$', views.admin_home, name='admin_home'),
      
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='schoollogout'),
    #url(r'^bucketlistapi/$', CreateView.as_view(), name="bucketlistsapi"),
    url(r'^$',TemplateView.as_view(template_name='index.html')),
]

