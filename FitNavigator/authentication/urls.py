from django.urls import path, include
from . import views

urlpatterns = [
    path('signup', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    # path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signout', views.signout, name='signout'),
    path('account', views.account, name='account'),
]