from django.urls import path

from . import views

app_name = "documents"
urlpatterns = [
    path("", views.documents, name="all"),
    path("control/", views.documents_control, name="on_control"),
    path("document/<int:pk>/", views.document, name="document"),
    path("document/add/", views.add, name="add"),
]