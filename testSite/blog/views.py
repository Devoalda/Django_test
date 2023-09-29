import requests

from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response
from django.http import HttpResponse

from blog.models import Author, Post
from blog.serializers import AuthorSerializer, PostSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def list(self, request):
        # Send a request to localhost:8001/blog/api/authors/ as well and aggregate the results.
        queryset = Author.objects.all()

        # Convert the queryset to a list so that we can append to it.
        queryset = list(queryset)

        # Only send if current port is 8000
        if request.META['SERVER_PORT'] == '8000':
            try:
                results = requests.get("http://127.0.0.1:8001/blog/authors/").json()
            except:
                results = None
            if results:
                for result in results:
                    # Append "8001" to the body so that we can differentiate between the two.
                    result["name"] = result["name"] + " From Another instance running on port 8001"
                    queryset.append(result)
            else:
                queryset.append({"name": "No results from 8001, ensure that another instance is running"})

        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer