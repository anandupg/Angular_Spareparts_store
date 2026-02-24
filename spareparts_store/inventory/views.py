from urllib import request
from rest_framework.views import APIView, Response
from rest_framework import status
from inventory.models import Category,Part
from .serializers import CategorySerializer,PartSerializer

class CategoryAPIView(APIView):

    def get(self, request):
        categories = Category.objects()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class CategoryDetailAPIView(APIView):

    def put(self, request, id):
        try:
            category = Category.objects.get(id=id)
        except:
            return Response(
                {"error": "Category not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CategorySerializer(category, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            category = Category.objects.get(id=id)
        except:
            return Response(
                {"error": "Category not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PartAPIView(APIView):

    def get(self, request):
        parts = Part.objects()
        serializer = PartSerializer(parts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PartSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PartDetailAPIView(APIView):

    def put(self, request, id):
        try:
            part = Part.objects.get(id=id)
        except:
            return Response(
                {"error": "Part not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = PartSerializer(part, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            part = Part.objects.get(id=id)
        except:
            return Response(
                {"error": "Part not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)