from rest_framework import serializers
from accounts.models import User
from user_activity.models import UserActivity


class UserActivitySerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format='%b %d %Y %I:%M%p')
    end_time = serializers.DateTimeField(format='%b %d %Y %I:%M%p')

    class Meta:
        model = UserActivity
        fields = ['start_time', 'end_time']


class UserSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    real_name = serializers.SerializerMethodField()
    activity_periods = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'real_name', 'tz', 'activity_periods']

    @staticmethod
    def get_id(user):
        return user.user_id

    @staticmethod
    def get_real_name(user):
        real_name = user.first_name + ' ' + user.last_name
        return real_name

    @staticmethod
    def get_activity_periods(instance):
        activities = instance.activity_periods.all().order_by('-start_time')
        return UserActivitySerializer(activities, many=True, read_only=True).data

