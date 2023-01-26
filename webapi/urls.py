from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('terms/', views.terms, name='terms'),
    path('terms/all/', GetTerm.as_view()),
    path('terms/create/', CreateTerm.as_view()),
    path('terms/mindmap/', views.mindmap, name='mindmap')
]