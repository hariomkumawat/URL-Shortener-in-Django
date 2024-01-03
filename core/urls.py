from django.urls import path
from core import views

urlpatterns = [
 path("", views.urlShort, name="urlShort"),
    path("<str:slugs>", views.urlRedirect, name="redirect")
]
