from api.models import Api, Profile, ConnectLog
from api.serializers import ApiSerializer, ProfileSerializer, \
                            UserSerializer, ConnectLogSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User

from rest_framework import renderers

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'api': reverse('api-list', request=request, format=format),
        'profile': reverse('profile-list', request=request, format=format),
        'connectlog': reverse('connectlog-list',
                              request=request, format=format),
    })


class ApiHighlight(generics.GenericAPIView):
    queryset = Api.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        api = self.get_object()
        return Response(api.highlighted)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ApiList(generics.ListCreateAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Api.objects.all()
    serializer_class = ApiSerializer


class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Profile.objects.all()
        badgenum = self.request.query_params.get('badge', None)
        username = self.request.query_params.get('user', None)
        if badgenum is not None:
            queryset = queryset.filter(badge=badgenum)
        elif username is not None:
            queryset = queryset.filter(user__username=username)
        return queryset


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('badge')


class ConnectLogList(generics.ListCreateAPIView):
    queryset = ConnectLog.objects.all()
    serializer_class = ConnectLogSerializer


class ConnectLogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ConnectLog.objects.all()
    serializer_class = ConnectLogSerializer
