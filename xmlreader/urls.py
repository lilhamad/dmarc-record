from django.urls import path

from . import views

app_name = "xmlreader"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("charts/", views.charts, name="charts"),
    path("tables/", views.tables, name="tables"),
    path("results/<int:id>/", views.results, name="results"),
]
