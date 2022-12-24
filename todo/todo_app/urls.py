from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_task, name="create"),
    path("save/", views.save, name="save"),
    path("delete/<int:id>/", views.delete),
    path("update/<int:id>/", views.update),

]
