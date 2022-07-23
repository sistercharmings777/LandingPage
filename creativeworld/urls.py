from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('subscription', views.subscription, name="subscription"),
    # path('success', views.successpage, name="success"),
]