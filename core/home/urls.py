from django.urls import path
from . import views
from .views import home,post_student

urlpatterns = [
    path('', home),
    path('student/',views.post_student),
]
