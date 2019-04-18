from django.urls import path

from . import views

urlpatterns = [
    path("", view=views.UserRedirectView.as_view(), name="redirect"),
    path("home/", view=views.HomePageView.as_view(), name="home"),
    path('home/diagnose/', views.DiagnoseView.as_view(), name='diagnose'),
]