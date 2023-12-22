from authentication.models import Profile
from authentication.serializers import ProfileSerializer
from rest_framework import viewsets


class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
