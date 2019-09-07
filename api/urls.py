from .views import ListCreateImagesView, ImagesDetailView
from django.urls import path

urlpatterns = [
    path('images/', ListCreateImagesView.as_view(), name="images-all"),
    path('images/<int:pk>', ImagesDetailView.as_view(), name="images-detail")
]
