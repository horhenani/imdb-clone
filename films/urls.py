from django.urls import path


from . import views


app_name = "films"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("film/<int:pk>/", views.film_detail, name="film_detail"),
]
