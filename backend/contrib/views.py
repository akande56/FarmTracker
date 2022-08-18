from django.http import JsonResponse
from rest_framework import generics
from .models import post
from .serializers import PostSerializer


def char_count(request):
    text = request.GET.get("text", "")

    return JsonResponse({"count": len(text)})


class PostView(generics.CreateAPIView):
    # queryset = post.objects.all()
    serializer_class = PostSerializer
