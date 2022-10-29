from datetime import datetime
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime

from .models import Tweek

class TweekSerializer(serializers.ModelSerializer):
    tweeker_name = serializers.CharField(source='created_by')
    likes_count = serializers.IntegerField(source='likes.count')
    dislikes_count = serializers.IntegerField(source='dislikes.count')
    avatar_url = serializers.CharField(source='created_by.twikkerprofile.avatar.url')
    
    class Meta:
        model = Tweek
        fields = ('id', 'body', 'created_by', 'tweeker_name', 'likes_count', 'dislikes_count', 'avatar_url', 'formatted_time')