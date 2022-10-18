
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app import views
from rest_framework.authtoken.views import obtain_auth_token
# creating router obj
router=DefaultRouter()

# register studentviewset with router
router.register('MyApi',views.get_api,basename='studentApi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('gettoken/',obtain_auth_token)
]
