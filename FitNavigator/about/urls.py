from django.urls import path, include
from . import views

urlpatterns = [

    path('about', views.about, name="about")

    # path('aboutsUs', views.aboutUs, name="aboutUs"),
    # path('about1', views.about1, name="about1"),
    # path('about2', views.about2, name="about2"),
    # path('about3', views.about3, name="about3"),
    # path('aboutContacts', views.aboutContacts, name="aboutContacts"),
]