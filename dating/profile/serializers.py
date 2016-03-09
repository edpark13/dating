from rest_framework import serializers
from profile.models import Man, Woman, Profile
from django.contrib.auth.models import User

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Profile
        fields = ('user', 'friends', 'bio')
