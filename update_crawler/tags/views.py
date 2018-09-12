from rest_framework import generics, status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Tags, ProgrammingLanguage
from .serializers import TagsSerializer, UserSerializer, ProgrammingLanguagesSerializer
from .utils import process_request
from .permissions import IsOwnerOrReadOnly
from .programming_languages_script import run_script


class TagList(APIView):
    tags = Tags.objects.all()
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = TagsSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(self.tags, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(ip_address=process_request(request), owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,
                          IsOwnerOrReadOnly,)
    queryset = Tags.objects.all()
    serializer_class = TagsSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProgrammingLanguagesList(APIView):
    languages_all = ProgrammingLanguage.objects.all()
    serializer_class = ProgrammingLanguagesSerializer

    def post(self, request, format=None):
        data = run_script()
        ProgrammingLanguage.objects.bulk_create(data)
        serializer = self.serializer_class(self.languages_all, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


