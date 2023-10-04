import requests

from rest_framework import mixins, permissions, viewsets
from rest_framework.response import Response
from django.http import HttpResponse
from django.core.cache import cache

from blog.models import Author, Post
from blog.serializers import AuthorSerializer, PostSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def list(self, request):
        # Print Cache URL
        # Get the cached value if it exists
        cached_value = cache.get("authors")

        if cached_value:
            # Serialise and return the cached value
            serializer = AuthorSerializer(cached_value, many=True)
            return Response(serializer.data)

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
                    result["name"] = result["name"] + " From Another instance running on port 8000"
                    queryset.append(result)
            else:
                queryset.append({"name": "No results from 8000"})

        # Append "from cache" to the body so that we can differentiate between the two.
        queryset = list()
        for author in Author.objects.all():
            queryset.append({"name": author.name + " from cache"})

        # Cache in redis
        cache.set("authors", queryset, timeout=60)

        # Convert the list back to a queryset
        queryset = Author.objects.all()

        serializer = AuthorSerializer(queryset, many=True)
        return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer