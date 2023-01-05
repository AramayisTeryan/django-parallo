from django.urls import path
from . import views

urlpatterns=[
    path('', views.HomeListView.as_view(), name='index'),
    path('about/', views.AboutListView.as_view(), name='about'),
    path('services/', views.ServicesListView.as_view(), name='services'),
    path('testimonials/', views.TestimonialsListView.as_view(), name='testimonials'),
    path('contact/', views.ContactListView.as_view(), name='contact')
]