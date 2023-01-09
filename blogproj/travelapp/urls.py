from travelapp import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),

#    path('booking',views.booking,name='booking'),

]
