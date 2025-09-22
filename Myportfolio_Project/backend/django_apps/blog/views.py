from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer
import feedparser
from rest_framework.response import Response
from rest_framework.views import APIView

class BlogListView(generics.ListAPIView):
    serializer_class = BlogSerializer

    def get_queryset(self):
        return Blog.objects.filter(status="published").order_by("-created_at")

class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.filter(status="published")  # 👈 only published
    serializer_class = BlogSerializer
    lookup_field = "slug"


# views.py

class ExternalBlogView(APIView):
    def get(self, request):
        feed = feedparser.parse("https://techcrunch.com/feed/")
        articles = []
        for entry in feed.entries[:10]:  # limit to 10
            articles.append({
                "title": entry.title,
                "link": entry.link,
                "published": entry.published,
                "summary": entry.summary,
            })
        return Response(articles)
