from rest_framework import viewsets
from profile.models import Profile
from profile.serializers import ProfileSerializer
from rest_framework import viewsets

# Create your views here.
# class FriendsList(viewsets.ReadOnlyModelViewSet):
#   queryset = request.user.profile.friends.all()
#   serializer_class = UserSerializer


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
