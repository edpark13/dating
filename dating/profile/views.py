from rest_framework import viewsets
from profile.models import Profile
from profile.serializers import ProfileSerializer
from rest_framework import viewsets


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
