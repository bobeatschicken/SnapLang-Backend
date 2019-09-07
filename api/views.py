from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status

from .decorators import validate_request_data
from .models import Images
from .serializers import ImagesSerializer


class ListCreateImagesView(generics.ListCreateAPIView):
    """
    GET images/
    POST images/
    """
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

    @validate_request_data
    def post(self, request, *args, **kwargs):
        an_image = Images.objects.create(
            english_definition=request.data["english_definition"],
            foreign_definition=request.data["foreign_definition"],
            foreign_language=request.data["foreign_language"]
        )
        return Response(
            data=ImagesSerializer(an_image).data,
            status=status.HTTP_201_CREATED
        )


class ImagesDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET images/:id/
    PUT images/:id/
    DELETE images/:id/
    """
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer

    def get(self, request, *args, **kwargs):
        try:
            an_image = self.queryset.get(pk=kwargs["pk"])
            return Response(ImagesSerializer(an_image).data)
        except Images.DoesNotExist:
            return Response(
                data={
                    "message": "Image with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_request_data
    def put(self, request, *args, **kwargs):
        try:
            an_image = self.queryset.get(pk=kwargs["pk"])
            serializer = ImagesSerializer()
            updated_image = serializer.update(an_image, request.data)
            return Response(ImagesSerializer(updated_image).data)
        except Images.DoesNotExist:
            return Response(
                data={
                    "message": "Image with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            an_image = self.queryset.get(pk=kwargs["pk"])
            an_image.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Images.DoesNotExist:
            return Response(
                data={
                    "message": "Image with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
