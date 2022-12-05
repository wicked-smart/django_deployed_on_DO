from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet")
]
