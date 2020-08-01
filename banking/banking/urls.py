"""banking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from . import views
import debug_toolbar
# from personalbanking.models import Customer
#
# from rest_framework import routers, serializers, viewsets
#
# # Serializers define the API representation.
# class CustomerSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ['url', 'firstname', 'lastname']
# # ViewSets define the view behavior.
# class CustomerViewSet(viewsets.ModelViewSet):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer
#
# # Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', CustomerViewSet)
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login_page),
    path('login', views.login_user),
    path('logout', views.logout_user),
    path('home', views.home_user),
    path('personal/', include('personalbanking.urls')),#
    path('api/', include('api.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # <-- And here
    path('__debug__/', include(debug_toolbar.urls)),
    path('cust', views.customer_list),

]
