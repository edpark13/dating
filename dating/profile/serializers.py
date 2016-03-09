from rest_framework import serializers
from profile.models import Man, Woman, Profile
from django.contrib.auth.models import User

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    friends = serializers.HyperlinkedIdentityField(many=False, view_name='profile-detail', lookup_field='slug', read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'friends', 'bio', 'slug')
