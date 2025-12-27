from django.urls import path
from . import views
from .views import home,post_student,update_student,get_book,get_category,StudentAPI,RegisterUser,GenericView,GenericDelete
from rest_framework.authtoken import views

urlpatterns = [
    path('', home),
    # path('student/',views.post_student),
    # path('delete/',views.delete),
    # path("update/<id>",views.update_student),
    # path('get-book/',views.get_book),
    # path('category/',views.get_category),
    path('api-token-auth/', views.obtain_auth_token),
    path('register/',RegisterUser.as_view()),
    path('generic_views/',GenericView.as_view()),
    path("generic_views/<id>/",GenericDelete.as_view())
]


