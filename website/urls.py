
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('blogs.html', views.blogs, name="blogs"),
    path('blog.html', views.blog, name="blog"),
    path('department.html', views.department, name="department"),
    path('doctor.html', views.doctor, name="doctor"),
    path('pricing.html', views.pricing, name="pricing"),
    path('appointment.html', views.appointment, name="appointment"),
]