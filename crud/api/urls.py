from django.urls import path
from expense import views
urlpatterns = [
    path("transaction",views.get_transaction),
]


