from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from .serializers import SnippetSerializer,CircleSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from restapi.models import User
from rest_framework import viewsets
from django.db.models import Q

from .models import Snippet,Circle



# Create your views here
class TestView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, format=None):
        username = request.query_params.get('username')
        response = dict()
        response["username"] = username
        print ("META", request.META['HTTP_COOKIE'])
        return Response(response)

    def post(self, request, format=None):
        username = request.data["testpstuser"]
        response = dict()
        response["testpstuser"] = username
        return Response(response)

class CustomAuth(BasicAuthentication):
    def authenticate(self, request):
        email = request.data["username"]
        password = request.data["password"]
        user = self.authenticate_credentials(email, password, request)
        print ("Custom Auth:")
        print (user)
        print(user[0])
        return user

#class CustomAuthSession(SessionAuthentication):
    #def enforce_csrf(self, request):
      #  return  # To not perform the csrf check previously happening

class CircleViewSet(viewsets.ViewSet):
    def list(self, request):
        #Entry.objects.extra(where=["foo='a' OR bar = 'a'", "baz = 'a'"])
        #Blog.objects.filter(pk__in=[1, 4, 7])
        group_access = request.query_params.get('groupAccess')
        on_demand_status = request.query_params.get("onDemandStatus")
        queryset = Circle.objects.get( Q(on_demand_status=on_demand_status),Q(group_access=group_access) | Q(group_access__isnull=True))
        serializer = CircleSerializer(queryset)
        return Response(serializer.data)

class TestAuthView(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    def post(self, request, format=None):
        #print("csrf_token",csrf_token)
        content = {
            'user': request.user.email,
            'auth': request.auth,  # None
        }
        #print (request.META)
        return Response(content)





@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
    