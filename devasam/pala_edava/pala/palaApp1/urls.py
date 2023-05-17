from django.urls import path
from . import views
app_name='palaApp1'

urlpatterns = [
    path('',views.index,name='index'),
    path('feeds/<int:feeds_id>/', views.details, name='details'),
    path('about/', views.about, name='about'),
    path('donate/', views.donate, name='donate'),
    path('enquiry/', views.enquiry, name='enquiry'),
    path('members/', views.members, name='members'),
    path('spcilepooja/', views.spcilepooja, name='spcilepooja'),
    path('notification/<int:notify_id>/', views.notification, name='notification'),
    path('todaypooja/', views.todaypooja, name='todaypooja'),
    path('login/', views.login, name='login'),
    path("logout/",views.logout,name='logout')

]
