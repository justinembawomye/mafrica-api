from django.shortcuts import render
from rest_framework import status, generics,permissions
from .models import Courses
from .serializers import CoursesSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# Create your views here.
class CoursesAPIView(APIView):
    """
    Registers a new Course.
    """
    permission_classes = [AllowAny]
    serializer_class = CoursesSerializer

    def post(self, request):
        """
        Creates a new course
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'title': serializer.data.get('title'),
                'Description': serializer.data.get('description'),
            },
            status=status.HTTP_201_CREATED,
        )



class CoursesListCreate(generics.ListCreateAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer