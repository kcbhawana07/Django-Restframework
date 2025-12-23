from django.urls import path
from . import views
urlpatterns = [
    path("transaction",views.get_transaction),
]
