from django.urls import path
from . import views  


urlpatterns = [
    path("search/", views.search_for_user),
    path("conversations/<int:id>/", views.loading_conv),
    path("conversation/<int:id>/", views.conversation),
    path("conversations/", views.conversations)
]
