
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from rest_framework.utils import urls
 
from api import views
from rest_framework.routers import DefaultRouter
# create router object
router = DefaultRouter()



#register student viewset with router
router.register('studentapi',views.StudentViewSet,basename='student')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)), 

]
