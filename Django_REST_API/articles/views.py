from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers, generics, viewsets, mixins
from rest_framework.response import Response
from articles.models import Article
from rest_framework.generics import ListCreateAPIView
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.viewsets import GenericViewSet

# Create your views here.

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('pk', 'title', 'content', 'user', 'updated_at', 'created_at')

# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

class ArticleViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer