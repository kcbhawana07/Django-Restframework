from django.urls import path
from . import views
from .views import home,post_student,update_student,get_book,get_category

urlpatterns = [
    path('', home),
    path('student/',views.post_student),
    path('delete/',views.delete),
    path("update/<id>",views.update_student),
    path('get-book/',views.get_book),
    path('category/',views.get_category)
    
]


